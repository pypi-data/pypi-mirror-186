import logging
import os
import time
from dataclasses import dataclass
from datetime import datetime
from functools import lru_cache
from typing import Optional

from neofs_testlib.hosting.config import ParsedAttributes
from neofs_testlib.hosting.interfaces import DiskInfo, Host
from neofs_testlib.shell import Shell, SSHShell
from neofs_testlib.shell.command_inspectors import SudoInspector
from neofs_testlib.shell.interfaces import CommandOptions

from neofs_testlib_plugin_sbercloud.sbercloud_client import SbercloudClient

logger = logging.getLogger("neofs.testlib.hosting")


@dataclass
class HostAttributes(ParsedAttributes):
    """Represents attributes of a virtual machine in Sbercloud.

    Attributes:
        sbercloud_access_key_id: Access key ID for Sbercloud API access.
        sbercloud_secret_key: Secret key for Sbercloud API access.
        sbercloud_ecs_endpoint: Endpoint for Sbercloud Elastic Compute Service API.
        sbercloud_project_id: ID of Sbercloud project the virtual machine belongs to.
        ssh_login: Login for SSH connection to the virtual machine.
        ssh_password: Password for SSH connection.
        ssh_private_key_path: Path to private key for SSH connection.
        ssh_private_key_passphrase: Passphrase for the private key.
        sudo_shell: Specifies whether shell commands should be auto-prefixed with sudo.
    """

    sbercloud_access_key_id: str
    sbercloud_secret_key: str
    sbercloud_ecs_endpoint: str
    sbercloud_project_id: str

    ssh_login: str
    ssh_password: Optional[str] = None
    ssh_private_key_path: Optional[str] = None
    ssh_private_key_passphrase: Optional[str] = None

    sudo_shell: bool = False


@dataclass
class ServiceAttributes(ParsedAttributes):
    """Represents attributes of service running as systemd service.

    Attributes:
        systemd_service_name: Name of systemd service.
        data_directory_path: Path to directory where storage node stores data.
        start_timeout: Timeout (in seconds) for service to start.
        stop_timeout: Timeout (in seconds) for service to stop.
    """

    systemd_service_name: str
    data_directory_path: Optional[str]
    start_timeout: int = 60
    stop_timeout: int = 60


class SbercloudHost(Host):
    """Manages services hosted on virtual machines at Sbercloud."""

    def get_shell(self) -> Shell:
        host_attributes = HostAttributes.parse(self._config.attributes)

        command_inspectors = []
        if host_attributes.sudo_shell:
            command_inspectors.append(SudoInspector())

        return SSHShell(
            host=self._config.address,
            login=host_attributes.ssh_login,
            password=host_attributes.ssh_password,
            private_key_path=host_attributes.ssh_private_key_path,
            private_key_passphrase=host_attributes.ssh_private_key_passphrase,
            command_inspectors=command_inspectors,
        )

    def start_host(self) -> None:
        sbercloud_client = self._get_sbercloud_client()
        sbercloud_client.start_node(node_ip=self._config.address)

    def stop_host(self, mode: str) -> None:
        hard_mode = mode == "hard"

        sbercloud_client = self._get_sbercloud_client()
        sbercloud_client.stop_node(node_ip=self._config.address, hard=hard_mode)

    def start_service(self, service_name: str) -> None:
        service_attributes = self._get_service_attributes(service_name)

        shell = self.get_shell()
        output = shell.exec(f"sudo systemctl start {service_attributes.systemd_service_name}")
        logger.info(f"Start command output: {output.stdout}")

        self._wait_for_service_to_be_in_state(
            service_attributes.systemd_service_name,
            "active (running)",
            service_attributes.start_timeout,
        )

    def stop_service(self, service_name: str) -> None:
        service_attributes = self._get_service_attributes(service_name)

        shell = self.get_shell()
        output = shell.exec(f"sudo systemctl stop {service_attributes.systemd_service_name}")
        logger.info(f"Start command output: {output.stdout}")

        self._wait_for_service_to_be_in_state(
            service_attributes.systemd_service_name,
            "inactive",
            service_attributes.start_timeout,
        )

    def delete_storage_node_data(self, service_name: str, cache_only: bool = False) -> None:
        service_attributes = self._get_service_attributes(service_name)

        shell = self.get_shell()
        meta_clean_cmd = f"sudo rm -rf {service_attributes.data_directory_path}/meta*/*"
        data_clean_cmd = (
            f"; sudo rm -rf {service_attributes.data_directory_path}/data*/*"
            if not cache_only
            else ""
        )
        cmd = f"{meta_clean_cmd}{data_clean_cmd}"
        shell.exec(cmd)

    def _get_volume_pci_address(self, device: str) -> str:
        shell = self.get_shell()
        # Drive letters in Sbercloud have weird behavior
        # let's say we have drives [vda, vdb, vdc]
        # If we detach vd*b* and attach it again, the new drive letter
        # MAY change and new set of drives will be [vda, vdc, vde]
        # or MAY NOT change and new set of drives will be [vda, vdb, vdc] as before
        # However, sbercloud API will still have it as vd*b*
        # Due to letter of a drive may change we need to find volume by pci address.
        cmd = f"sudo udevadm info -n {device} | egrep \"S:.*path/pci\" | awk '{{print $2}}'"
        pci_address = os.path.basename(shell.exec(cmd).stdout.strip())
        return pci_address

    def _get_volume_label(self, device: str) -> str:
        shell = self.get_shell()
        # PCI address of a drive may also change, so
        # we need to find volume label to check if volume is detached/attached.
        cmd = f"sudo udevadm info -n {device} | egrep \"S:.*label\" | awk '{{print $2}}'"
        pci_address = os.path.basename(shell.exec(cmd).stdout.strip())
        return pci_address

    def detach_disk(self, device: str) -> DiskInfo:
        sbercloud_client = self._get_sbercloud_client()
        node_id = sbercloud_client.find_ecs_node_by_ip(self._config.address)

        pci_address = self._get_volume_pci_address(device)
        volume_label = self._get_volume_label(device)
        volume_id = sbercloud_client.find_volume_id_by_pci_address(
            node_id, pci_address.replace("pci-", "")
        )

        sbercloud_client.detach_volume(node_id, volume_id)

        return DiskInfo({"volume_id": volume_id, "volume_label": volume_label})

    def is_disk_attached(self, device: str, disk_info: DiskInfo) -> bool:
        label = disk_info["volume_label"]
        shell = self.get_shell()
        cmd = f"ls /dev/disk/by-label | grep ^{label}"
        return shell.exec(cmd, options=CommandOptions(check=False)).stdout.strip() != ""

    def attach_disk(self, device: str, disk_info: DiskInfo) -> None:
        sbercloud_client = self._get_sbercloud_client()
        node_id = sbercloud_client.find_ecs_node_by_ip(self._config.address)

        if "volume_id" not in disk_info:
            raise RuntimeError(f"Volume_id must present in service_info for sbercloud: {disk_info}")

        volume_id = disk_info["volume_id"]

        sbercloud_client.attach_volume(node_id, device, volume_id)

    def dump_logs(
        self,
        directory_path: str,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
    ) -> None:
        # We do not filter out logs of neofs services, because system logs might contain
        # information that is useful for troubleshooting
        filters = " ".join(
            [
                f"--since '{since:%Y-%m-%d %H:%M:%S}'" if since else "",
                f"--until '{until:%Y-%m-%d %H:%M:%S}'" if until else "",
            ]
        )

        shell = self.get_shell()
        options = CommandOptions(no_log=True)
        result = shell.exec(f"journalctl --no-pager {filters}", options)
        logs = result.stdout

        # Dump logs to the directory
        file_path = os.path.join(directory_path, f"{self._config.address}-log.txt")
        with open(file_path, "w") as file:
            file.write(logs)

    def _get_service_attributes(self, service_name) -> ServiceAttributes:
        service_config = self.get_service_config(service_name)
        return ServiceAttributes.parse(service_config.attributes)

    def _wait_for_service_to_be_in_state(
        self, systemd_service_name: str, expected_state: str, timeout: int
    ) -> None:
        iterations = 10
        iteration_wait_time = timeout / iterations

        shell = self.get_shell()
        for _ in range(iterations):
            # Run command to get service status (set --lines=0 to suppress logs output). Also we
            # don't verify return code, because for an inactive service return code will be 3
            command = f"sudo systemctl status {systemd_service_name} --lines=0"
            output = shell.exec(command, CommandOptions(check=False))
            if expected_state in output.stdout:
                return
            time.sleep(iteration_wait_time)

        raise RuntimeError(f"Service {systemd_service_name} is not in {expected_state} state")

    @lru_cache
    def _get_sbercloud_client(self) -> SbercloudClient:
        host_attributes = HostAttributes.parse(self._config.attributes)
        return SbercloudClient(
            access_key_id=host_attributes.sbercloud_access_key_id,
            secret_key=host_attributes.sbercloud_secret_key,
            ecs_endpoint=host_attributes.sbercloud_ecs_endpoint,
            project_id=host_attributes.sbercloud_project_id,
        )
