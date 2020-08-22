from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

interface_bridge_port_router = APIRouter()

@interface_bridge_port_router.get("/")
def get_interface_bridge_port(
    _id: str = "", nextid: str = "", interface: str = "", bridge: str = "", priority: str = "",
    path_cost: str = "", internal_path_cost: str = "", edge: str = "", point_to_point: str = "", learn: str = "",
    horizon: str = "", auto_isolate: str = "", restricted_role: str = "", restricted_tcn: str = "", pvid: str = "",
    frame_types: str = "", ingress_filtering: str = "", unknown_unicast_flood: str = "",
    unknown_multicast_flood: str = "", broadcast_flood: str = "", tag_stacking: str = "", bpdu_guard: str = "",
    trusted: str = "", multicast_router: str = "", fast_leave: str = "", status: str = "", port_number: str = "",
    role: str = "", edge_port: str = "", edge_port_discovery: str = "", point_to_point_port: str = "",
    external_fdb_status: str = "", sending_rstp: str = "", learning: str = "", forwarding: str = "",
    debug_info: str = "", inactive: str = "", dynamic: str = "", disabled: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, ".nextid": nextid, "interface": interface, "bridge": bridge, "priority": priority,
            "path-cost": path_cost, "internal-path-cost": internal_path_cost, "edge": edge,
            "point-to-point": point_to_point, "learn": learn, "frame-types": frame_types,
            "ingress-filtering": ingress_filtering, "unknown-unicast-flood": unknown_unicast_flood,
            "unknown-multicast-flood": unknown_multicast_flood, "broadcast-flood": broadcast_flood,
            "tag-stacking": tag_stacking, "bpdu-guard": bpdu_guard, "trusted": trusted, 
            "multicast-router": multicast_router, "fast-leave": fast_leave, "status": status,
            "port-number": port_number, "role": role, "edge-port": edge_port,
            "edge-port-discovery": edge_port_discovery, "point-to-point-port": point_to_point_port,
            "external-fdb-status": external_fdb_status, "sending-rstp": sending_rstp, "learning": learning,
            "forwarding": forwarding, "debug-info": debug_info, "inactive": inactive, "dynamic": dynamic,
            "disabled": disabled
        }
        
        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "bridge", "port")
        data = data.select(*filters_dict.keys()).where(*filters_list)


        return tuple(data)

    except Exception as e:
        return {"error": e}