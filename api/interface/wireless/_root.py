from fastapi import APIRouter
from device import DEVICE
from api import get_filters_list

_root_router = APIRouter()

@_root_router.get("/", tags=["wireless"])
def get_interface_wireless(
    _id: str = "", default_name: str = "", name: str = "", mtu: str = "", l2mtu: str = "", mac_address: str = "",
    arp: str = "", arp_timeout: str = "", disable_running_check: str = "", interface_type: str = "",
    radio_name: str = "", mode: str = "", ssid: str = "", area: str = "", frequency_mode: str = "",
    country: str = "", installation: str = "", antenna_gain: str = "", frequency: str = "", band: str = "",
    channel_width: str = "", secondary_channel: str = "", scan_list: str = "", wireless_protocol: str = "",
    rate_set: str = "", supported_rates_ag: str = "", max_station_count: str = "", distance: str = "",
    tx_power_mode: str = "", noise_floor_threshold: str = "", nv2_noise_floor_offset: str = "",
    vlan_mode: str = "", vlan_id: str = "", wds_mode: str = "", wds_default_bridge: str = "",
    wds_default_cost: str = "", wds_cost_range: str = "", wds_ignore_ssid: str = "",
    update_stats_interval: str = "", bridge_mode: str = "", default_authentication: str = "",
    default_forwarding: str = "", default_ap_tx_limit: str = "", default_client_tx_limit: str = "",
    wmm_support: str = "", hide_ssid: str = "", security_profile: str = "", interworking_profile: str = "",
    wps_mode: str = "", station_roaming: str = "", disconnect_timeout: str = "", on_fail_retry_time: str = "",
    preamble_mode: str = "", compression: str = "", allow_sharedkey: str = "", station_bridge_clone_mac: str = "",
    ampdu_priorities: str = "", guard_interval: str = "", ht_supported_mcs: str = "", ht_basic_mcs: str = "",
    tx_chains: str = "", rx_chains: str = "", amsdu_limit: str = "", amsdu_threshold: str = "",
    tdma_period_size: str = "", nv2_queue_count: str = "", nv2_qos: str = "", nv2_cell_radius: str = "",
    nv2_security: str = "", nv2_preshared_key: str = "", nv2_mode: str = "", nv2_downlink_ratio: str = "",
    nv2_sync_secret: str = "", hw_retries: str = "", frame_lifetime: str = "", adaptive_noise_immunity: str = "",
    hw_fragmentation_threshold: str = "", hw_protection_mode: str = "", hw_protection_threshold: str = "",
    frequency_offset: str = "", rate_selection: str = "", multicast_helper: str = "", multicast_buffering: str = "",
    keepalive_frames: str = "", skip_dfs_channels: str = "", running: str = "", disabled: str = ""    
    ):
    try:
        filters_dict = {
            ".id": _id, "default-name": default_name, "name": name, "mtu": mtu, "l2mtu": l2mtu,
            "mac-address": mac_address, "arp": arp, "arp-timeout": arp_timeout,
            "disable-running-check": disable_running_check, "interface-type": interface_type,
            "radio-name": radio_name, "mode": mode, "ssid": ssid, "frequency-mode": frequency_mode,
            "country": country, "installation": installation, "antenna-gain": antenna_gain, "frequency": frequency,
            "band": band, "channel-width": channel_width, "secondary-channel": secondary_channel,
            "scan-list": scan_list, "wireless-protocol": wireless_protocol, "rate-set": rate_set,
            "supported-rates-a/g": supported_rates_ag, "max-station-count": max_station_count,
            "distance": distance, "tx-power-mode": tx_power_mode, "noise-floor-threshold": noise_floor_threshold,
            "nv2-noise-floor-offset": nv2_noise_floor_offset, "vlan-mode": vlan_mode, "vlan-id": vlan_id,
            "wds-mode": wds_mode, "wds-default-bridge": wds_default_bridge, "wds-default-cost": wds_default_cost,
            "wds-cost-range": wds_cost_range, "wds-ignore-ssid": wds_ignore_ssid,
            "update-stats-interval": update_stats_interval, "bridge-mode": bridge_mode,
            "default-authentication": default_authentication, "default-forwarding": default_forwarding,
            "default-ap-tx-limit": default_ap_tx_limit, "default-client-tx-limit": default_client_tx_limit,
            "wmm-support": wmm_support, "hide-ssid": hide_ssid, "security-profile": security_profile,
            "interworking-profile": interworking_profile, "wps-mode": wps_mode, "station-roaming": station_roaming,
            "disconnect-timeout": disconnect_timeout, "on-fail-retry-time": on_fail_retry_time,
            "preamble-mode": preamble_mode, "compression": compression, "allow-sharedkey": allow_sharedkey,
            "station-bridge-clone-mac": station_bridge_clone_mac, "ampdu-priorities": ampdu_priorities,
            "guard-interval": guard_interval, "ht-supported-mcs": ht_supported_mcs, "ht-basic-mcs": ht_basic_mcs,
            "tx-chains": tx_chains, "rx-chains": rx_chains, "amsdu-limit": amsdu_limit, "amsdu-threshold": amsdu_threshold,
            "tdma-period-size": tdma_period_size, "nv2-queue-count": nv2_queue_count, "nv2-qos": nv2_qos,
            "nv2-cell-radius": nv2_cell_radius, "nv2-security": nv2_security, "nv2-preshared-key": nv2_preshared_key,
            "nv2-mode": nv2_mode, "nv2-downlink-ratio": nv2_downlink_ratio, "nv2-sync-secret": nv2_sync_secret,
            "hw-retries": hw_retries, "frame-lifetime": frame_lifetime, "adaptive-noise-immunity": adaptive_noise_immunity,
            "hw-fragentation-threshold": hw_fragmentation_threshold, "hw-protection-mode": hw_protection_mode,
            "hw-protection-threshold": hw_protection_threshold, "frequency-offset": frequency_offset,
            "rate-selection": rate_selection, "multicast-helper": multicast_helper, "multicast-buffering": multicast_buffering,
            "keepalive-frames": keepalive_frames, "skip-dfs-channels": skip_dfs_channels, "running": running,
            "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "wireless")
        #data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}