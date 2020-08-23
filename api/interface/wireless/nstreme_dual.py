from fastapi import APIRouter
from device import DEVICE
from api import get_filters_list

nstreme_dual_router = APIRouter()

@nstreme_dual_router.get("/")
def get_interface_wireless_nstreme_dual(
    dead: str = "", _id: str = "", nextid: str = "", arp: str = "", arp_timeout: str = "", comment: str = "",
    disable_csma: str = "", disable_running_check: str = "", disabled: str = "", framer_limit: str = "",
    framer_policy: str = "", ht_channel_width: str = "", ht_guard_interval: str = "", ht_rates: str = "",
    ht_streams: str = "", l2mtu: str = "", mac_address: str = "", mtu: str = "", name: str = "", rates_ag: str = "",
    rates_b: str = "", remote_mac: str = "", running: str = "", rx_band: str = "", rx_channel_width: str = "",
    rx_frequency: str = "", rx_radio: str = "", tx_band: str = "", tx_channel_width: str = "", tx_frequency: str = "",
    tx_radio: str = ""
    ):
    try:
        filters_dict = {
            ".dead": dead, ".id": _id, ".nextid": nextid, "arp": arp, "arp-timeout": arp_timeout, "comment": comment,
            "disable-csma": disable_csma, "disable-running-check": disable_running_check, "disabled": disabled,
            "framer-limit": framer_limit, "framer-policy": framer_policy, "ht-channel-width": ht_channel_width,
            "ht-guard-interval": ht_guard_interval, "ht-rates": ht_rates, "ht-streams": ht_streams, "l2mtu": l2mtu,
            "mac-address": mac_address, "mtu": mtu, "name": name, "rates-a/g": rates_ag, "rates-b": rates_b,
            "remote-mac": remote_mac, "running": running, "rx-band": rx_band, "rx-channel-width": rx_channel_width,
            "rx-frequency": rx_frequency, "rx-radio": rx_radio, "tx-band": tx_band, "tx-channel-width": tx_channel_width,
            "tx-frequency": tx_frequency, "tx-radio": tx_radio
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "wireless", "nstreme-dual")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}