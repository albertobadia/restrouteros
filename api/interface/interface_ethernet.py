from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

interface_ethernet_router = APIRouter()

@interface_ethernet_router.get("/", tags=["interface"])
def get_interface_ethernet(
    _id: str = "", name: str = "", default_name: str = "", mtu: str = "", l2mtu: str = "",
    mac_address: str = "", orig_mac_address: str = "", arp: str = "", arp_timeout: str = "",
    loop_protect: str = "", loop_protect_status: str = "", loop_protect_send_interval: str = "",
    loop_protect_disable_time: str = "", auto_negotiation: str = "", advertise: str = "",
    full_duplex: str = "", tx_flow_control: str = "", rx_flow_control: str = "", speed: str = "",
    bandwidth: str = "", switch: str = "", driver_rx_byte: str = "", driver_rx_packet: str = "",
    driver_tx_byte: str = "", driver_tx_packet: str = "", rx_bytes: str = "", rx_packet: str = "",
    rx_too_short: str = "", rx_64: str = "", rx_65_127: str = "", rx_128_255: str = "", rx_256_511: str = "",
    rx_512_1023: str = "", rx_1024_1518: str = "", rx_too_long: str = "", rx_broadcast: str = "",
    rx_pause: str = "", rx_multicast: str = "", rx_fcs_error: str = "", rx_align_error: str = "",
    rx_fragment: str = "", rx_jabber: str = "", rx_drop: str = "", tx_bytes: str = "", tx_packet: str = "",
    tx_64: str = "", tx_65_127: str = "", tx_128_255: str = "", tx_256_511: str = "", tx_512_1023: str = "",
    tx_1024_1518: str = "", tx_broadcast: str = "", tx_pause: str = "", tx_multicast: str = "",
    tx_collision: str = "", tx_excessive_collision: str = "", tx_multiple_collision: str = "",
    tx_single_collision: str = "", tx_deferred: str = "", tx_late_collision: str = "", tx_drop: str = "",
    tx_fcs_error: str = "", running: str = "", disabled: str = ""
    ):
    try:
        
        filters_dict = {
            ".id": _id, "name": name, "default-name": default_name, "mtu": mtu, "l2mtu": l2mtu,
            "mac-address": mac_address, "orig-mac-address": orig_mac_address, "arp": arp,
            "arp-timeout": arp_timeout, "loop-protect": loop_protect, "loop-protect-status": loop_protect_status,
            "loop-protect-send-interval": loop_protect_send_interval,
            "loop-protect-disable-time": loop_protect_disable_time, "auto-negotiation": auto_negotiation,
            "advertise": advertise, "full-duplex": full_duplex, "tx-flow-control": tx_flow_control,
            "rx-flow-control": rx_flow_control, "speed": speed, "bandwidth": bandwidth, "switch": switch,
            "driver-rx-byte": driver_rx_byte, "driver-rx-packet": driver_rx_packet,
            "driver-tx-byte": driver_tx_byte, "driver-tx-packet": driver_tx_packet, "rx-bytes": rx_bytes,
            "rx-packet": rx_packet, "rx-too-short": rx_too_short, "rx-64": rx_64, "rx-65-127": rx_65_127,
            "rx-128-255": rx_128_255, "rx-256-511": rx_256_511, "rx-512-1023": rx_512_1023,
            "rx-1024-1518": rx_128_255, "rx-too-long": rx_too_long, "rx-broadcast": rx_broadcast,
            "rx-pause": rx_pause, "rx-multicast": rx_multicast, "rx-fcs-error": rx_fcs_error,
            "rx-align-error": rx_align_error, "rx-fragment": rx_fragment, "rx-jabber": rx_jabber,
            "rx-drop": rx_drop, "tx-bytes": tx_bytes, "tx-packet": tx_packet, "tx-64": tx_64,
            "tx-65-127": tx_65_127, "tx-128-255": tx_128_255, "tx-256-511": tx_256_511,
            "tx-512-1023": tx_512_1023, "tx-1024-1518": tx_1024_1518, "tx-broadcast": tx_broadcast,
            "tx-pause": tx_pause, "tx-multicast": tx_multicast, "tx-collision": tx_collision,
            "tx-excessive-collision": tx_excessive_collision, "tx-multiple-collision": tx_multiple_collision,
            "tx-single-collision": tx_single_collision, "tx-deferred": tx_deferred,
            "tx-late-collision": tx_late_collision, "tx-drop": tx_drop, "tx-fcs-error": tx_fcs_error,
            "running": running, "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "ethernet")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}