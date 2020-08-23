from fastapi import APIRouter
from device import DEVICE
from api import get_filters_list

_root_router = APIRouter()

@_root_router.get("/", tags=["interface"])
def get_interface(
    _id: str = "", name: str = "", default_name: str = "", _type: str = "", mtu: str = "",
    actual_mtu: str = "", l2mtu: str = "", max_l2mtu: str = "", mac_address: str = "",
    last_link_up_time: str = "", link_downs: str = "", rx_byte: str = "", tx_byte: str = "",
    rx_packet: str = "", tx_packet: str = "", tx_queue_drop: str = "", fp_rx_byte: str = "",
    fp_tx_byte: str = "", fp_rx_packet: str = "", fp_tx_packet: str = "", running: str = "",
    disabled: str = ""
    ):

    try:

        filters_dict = {
            ".id": _id,
            "name": name,
            "default-name": default_name,
            "type": _type,
            "mtu": mtu,
            "actual-mtu": actual_mtu,
            "l2mtu": l2mtu,
            "max-l2mtu": max_l2mtu,
            "mac-address": mac_address,
            "last-link-up-time": last_link_up_time,
            "link-downs": link_downs,
            "rx-byte": rx_byte,
            "tx-byte": tx_byte,
            "rx-packet": rx_packet,
            "tx-packet": tx_packet,
            "tx-queue-drop": tx_queue_drop,
            "fp-rx-byte": fp_rx_byte,
            "fp-tx-byte": fp_tx_byte,
            "fp-rx-packet": fp_rx_packet,
            "fp-tx-packet": fp_tx_packet,
            "running": running,
            "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)
    
    except Exception as e:
        return {"error": e}