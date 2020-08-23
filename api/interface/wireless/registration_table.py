from fastapi import APIRouter
from device import DEVICE
from api import get_filters_list

registration_table_router = APIRouter()

@registration_table_router.get("/", tags=["wireless"])
def get_interface_wireless_registration_table(
    _id: str = "", interface: str = "", radio_name: str = "", mac_address: str = "", ap: str = "", wds: str = "",
    bridge: str = "", rx_rate: str = "", tx_rate: str = "", packets: str = "", bytes: str = "", frames: str = "",
    frame_bytes: str = "", hw_frames: str = "", hw_frame_bytes: str = "", tx_frames_timed_out: str = "",
    uptime: str = "", last_activity: str = "", signal_strength: str = "", signal_to_noise: str = "",
    signal_strength_ch0: str = "", signal_strength_ch1: str = "", tx_signal_strength_ch0: str = "",
    tx_signal_strength_ch1: str = "", strength_at_rates: str = "", tx_signal_strength: str = "", tx_ccq: str = "",
    rx_ccq: str = "", p_throughput: str = "", nstreme: str = "", framing_mode: str = "", routeros_version: str = "",
    last_ip: str = "", ap_tx_limit: str = "", client_tx_limit: str = "", _802_1x_port_enabled: str = "",
    authentication_type: str = "", encryption: str = "", group_encryption: str = "", management_protection: str = "",
    compression: str = "", wmm_enabled: str = "", tx_rate_set: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, "interface": interface, "radio-name": radio_name, "mac-address": mac_address, "ap": ap, "wds": wds,
            "bridge": bridge, "rx-rate": rx_rate, "tx-rate": tx_rate, "packets": packets, "bytes": bytes, "frames": frames,
            "frame-bytes": frame_bytes, "hw-frames": hw_frames, "hw-frame-bytes": hw_frame_bytes,
            "tx-frames-timed-out": tx_frames_timed_out, "uptime": uptime, "last-activity": last_activity,
            "signal-strength": signal_strength, "signal-to-noise": signal_to_noise,
            "signal-strength-ch0": signal_strength_ch0, "signal-strength-ch1": signal_strength_ch1,
            "tx-signal-strength-ch0": tx_signal_strength_ch0, "tx-signal-strength-ch1": tx_signal_strength_ch1,
            "strength-at-rates": strength_at_rates, "tx-signal-strength": tx_signal_strength,
            "tx-ccq": tx_ccq, "rx-ccq": rx_ccq, "p-throughput": p_throughput, "nstreme": nstreme, "framing-mode": framing_mode,
            "routeros-version": routeros_version, "last-ip": last_ip, "ap-tx-limit": ap_tx_limit,
            "client-tx-limit": client_tx_limit, "802.1x-port-enabled": _802_1x_port_enabled,
            "authentication-type": authentication_type, "encryption": encryption, "group-encryption": group_encryption,
            "management-protection": management_protection, "compression": compression, "wmm-enabled": wmm_enabled,
            "tx-rate-set": tx_rate_set
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "wireless", "registration-table")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}