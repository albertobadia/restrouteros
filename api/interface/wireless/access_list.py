from fastapi import APIRouter
from device import DEVICE
from api import get_filters_list

access_list_router = APIRouter()

@access_list_router.get("/")
def get_interface_wireless_access_list(
    _id: str = "", mac_address: str = "", interface: str = "", signal_range: str = "", allow_signal_out_of_range: str = "",
    authentication: str = "", forwarding: str = "", ap_tx_limit: str = "", client_tx_limit: str = "", private_algo: str = "",
    private_key: str = "", private_pre_shared_key: str = "", management_protection_key: str = "", vlan_mode: str = "",
    vlan_id: str = "", disabled: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, "mac-address": mac_address, "interface": interface, "signal-range": signal_range,
            "allow-signal-out-of-range": allow_signal_out_of_range, "authentication": authentication, "forwarding": forwarding,
            "ap-tx-limit": ap_tx_limit, "client-tx-limit": client_tx_limit, "private-algo": private_algo,
            "private-key": private_key, "private-pre-shared-key": private_pre_shared_key,
            "management-protection-key": management_protection_key, "vlan-mode": vlan_mode, "vlan-id": vlan_id,
            "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "wireless", "access-list")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}