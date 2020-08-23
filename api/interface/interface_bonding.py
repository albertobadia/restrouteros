from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

interface_bonding_router = APIRouter()

@interface_bonding_router.get("/", tags=["interface"])
def get_interface_bonding(
    _id: str = "", name: str = "", mtu: str = "", mac_address: str = "", arp: str = "", arp_timeout: str = "",
    slaves: str = "", mode: str = "", primary: str = "", link_monitoring: str = "", arp_interval: str = "",
    arp_ip_targets: str = "", mii_interval: str = "", down_delay: str = "", up_delay: str = "",
    lacp_rate: str = "", transmit_hash_policy: str = "", min_links: str = "", running: str = "",
    disabled: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, "name": name, "mtu": mtu, "mac-address": mac_address, "arp": arp,
            "arp-timeout": arp_timeout, "slaves": slaves, "mode": mode, "primary": primary,
            "link-monitoring": link_monitoring, "arp-interval": arp_interval, "arp-ip-targets": arp_ip_targets,
            "mii-interval": mii_interval, "down-delay": down_delay, "up-delay": up_delay, "lacp-rate": lacp_rate,
            "transmit-hash-policy": transmit_hash_policy, "min-links": min_links, "running": running,
            "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "bonding")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}
