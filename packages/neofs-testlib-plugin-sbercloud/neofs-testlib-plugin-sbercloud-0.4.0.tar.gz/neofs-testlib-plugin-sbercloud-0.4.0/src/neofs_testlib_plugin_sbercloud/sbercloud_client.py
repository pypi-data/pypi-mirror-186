from typing import Any, Optional

from neofs_testlib_plugin_sbercloud.sbercloud_auth_requests import SbercloudAuthRequests


class SbercloudClient:
    """Manages resources in Sbercloud via API.

    API reference:
    https://docs.sbercloud.ru/terraform/ug/topics/quickstart.html
    https://support.hc.sbercloud.ru/en-us/api/ecs/en-us_topic_0020212668.html
    """

    def __init__(
        self,
        access_key_id: str,
        secret_key: str,
        ecs_endpoint: str,
        project_id: str,
    ) -> None:
        self.ecs_requests = SbercloudAuthRequests(
            endpoint=ecs_endpoint,
            base_path=f"/v1/{project_id}/cloudservers",
            access_key_id=access_key_id,
            secret_key=secret_key,
        )
        self.ecs_node_by_ip = {}

    def find_volume_id_by_pci_address(self, node_id: str, pci_address: str) -> str:
        """
        Find volume id by it's pci_address.

        Due to letter of disk in system and from sbercloud API can be different
        we need to find the volume info by it's PCI address.

        For details refer to:
            https://support.hc.sbercloud.ru/en-us/api/ecs/en-us_topic_0122107473.html

        Args:
            node_id: sbercloud server id.
            pci_address: address string without prefix "pci-" (i.e. 0000:02:06.0).

        Returns:
            volume id string.
        """

        response = self.ecs_requests.get(f"/{node_id}/block_device")
        response_json = response.json()
        if "volumeAttachments" not in response_json:
            raise RuntimeError(f"volumeAttachments not found in response: {response_json}")
        volumes = response_json["volumeAttachments"]

        queried_volume = [volume for volume in volumes if volume["pciAddress"] == pci_address]

        if not queried_volume:
            raise RuntimeError(f"Device with {pci_address} not found in volumes list: {volumes}")

        if "volumeId" not in queried_volume[0]:
            raise RuntimeError(f"Device with {pci_address} have no volume id: {queried_volume}")

        return queried_volume[0]["volumeId"]

    def detach_volume(self, node_id: str, volume_id: str):
        self.ecs_requests.delete(f"/{node_id}/detachvolume/{volume_id}")

    def attach_volume(self, node_id: str, device: str, volume_id: str):
        data = {
            "volumeAttachment": {
                "volumeId": volume_id,
                "device": device,
            },
            "dry_run": False,
        }

        self.ecs_requests.post(f"/{node_id}/attachvolume", data=data)

    def find_ecs_node_by_ip(self, ip: str) -> str:
        if ip not in self.ecs_node_by_ip:
            self.ecs_node_by_ip[ip] = self.get_ecs_node_id(ip)
        assert ip in self.ecs_node_by_ip
        return self.ecs_node_by_ip[ip]

    def get_ecs_node_id(self, ip: str) -> str:
        response = self.ecs_requests.get("/detail", {"ip": ip}).json()

        # Search server by exact IP match
        desired_server = [server for server in response["servers"] if self._has_address(server, ip)]

        if not desired_server:
            raise RuntimeError(f"Cannot find server with ip {ip}: {response}")

        return desired_server[0]["id"]

    def start_node(self, node_id: Optional[str] = None, node_ip: Optional[str] = None) -> None:
        data = {"os-start": {"servers": [{"id": node_id or self.find_ecs_node_by_ip(node_ip)}]}}
        self.ecs_requests.post("/action", data=data)

    def stop_node(
        self, node_id: Optional[str] = None, node_ip: Optional[str] = None, hard: bool = False
    ) -> None:
        data = {
            "os-stop": {
                "type": "HARD" if hard else "SOFT",
                "servers": [{"id": node_id or self.find_ecs_node_by_ip(node_ip)}],
            }
        }
        self.ecs_requests.post("/action", data=data)

    def _has_address(self, server: dict[str, Any], ip: str) -> bool:
        return any(
            address
            for address_set in server["addresses"].values()
            for address in address_set
            if address["addr"] == ip
        )
