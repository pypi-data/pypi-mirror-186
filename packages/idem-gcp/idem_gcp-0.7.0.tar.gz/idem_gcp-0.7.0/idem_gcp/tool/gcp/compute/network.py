from typing import Any
from typing import Dict
from typing import List


async def update_peerings(
    hub,
    ctx,
    resource_id: str,
    current_peerings: List[Dict[str, Any]],
    new_peerings: List[Dict[str, Any]],
) -> Dict[str, Any]:
    result = {"result": False, "comment": []}

    current_peerings = current_peerings if current_peerings is not None else []
    new_peerings = new_peerings if new_peerings is not None else current_peerings

    peerings_map = {peering.get("name"): peering for peering in current_peerings}
    peerings_to_add = []
    peerings_to_update = []

    for peering in new_peerings:
        if peering.get("name") not in peerings_map:
            peerings_to_add.append(peering)
        else:
            element = peerings_map.pop(peering.get("name"))
            needs_update: bool = (
                element.get("exchange_subnet_routes")
                != peering.get("exchange_subnet_routes")
                or element.get("export_custom_routes")
                != peering.get("export_custom_routes")
                or element.get("export_subnet_routes_with_public_ip")
                != peering.get("export_subnet_routes_with_public_ip")
                or element.get("import_custom_routes")
                != peering.get("import_custom_routes")
                or element.get("import_subnet_routes_with_public_ip")
                != peering.get("import_subnet_routes_with_public_ip")
                or element.get("name") != peering.get("name")
                or element.get("network") != peering.get("network")
                or element.get("peer_mtu") != peering.get("peer_mtu")
                or element.get("stack_type") != peering.get("stack_type")
            )

            if needs_update:
                peerings_to_update.append(peering)

    for peering in peerings_map.values():
        remove_peering_request_body = {"name": peering.get("name")}

        remove_ret = await hub.exec.gcp_api.client.compute.network.removePeering(
            ctx, resource_id=resource_id, body=remove_peering_request_body
        )

        r = await hub.tool.gcp.operation_utils.await_operation_completion(
            ctx, remove_ret, "compute.network", "compute.global_operation"
        )
        if not r["result"]:
            result["comment"] += r["comment"]
            return result

    for peering in peerings_to_update:
        update_peering_request_body = build_peering_request_body(peering)

        update_ret = await hub.exec.gcp_api.client.compute.network.updatePeering(
            ctx, resource_id=resource_id, body=update_peering_request_body
        )

        r = await hub.tool.gcp.operation_utils.await_operation_completion(
            ctx, update_ret, "compute.network", "compute.global_operation"
        )
        if not r["result"]:
            result["comment"] += r["comment"]
            return result

    r = await hub.tool.gcp.compute.network.add_peerings(
        ctx, resource_id, peerings_to_add
    )

    if not r["result"]:
        result["comment"] += r["comment"]
        return result

    result["result"] = True
    return result


async def add_peerings(
    hub, ctx, resource_id: str, peerings_to_add: Dict[str, Any]
) -> Dict[str, Any]:
    result = {"result": False, "comment": []}

    for peering in peerings_to_add:
        add_peering_request_body = build_peering_request_body(peering)

        add_ret = await hub.exec.gcp_api.client.compute.network.addPeering(
            ctx, resource_id=resource_id, body=add_peering_request_body
        )

        r = await hub.tool.gcp.operation_utils.await_operation_completion(
            ctx, add_ret, "compute.network", "compute.global_operation"
        )
        if not r["result"]:
            result["comment"] += r["comment"]
            return result

    result["result"] = True
    return result


def build_peering_request_body(
    peering: Dict[str, Dict[str, Any]]
) -> Dict[str, Dict[str, Any]]:
    return {
        "network_peering": {
            "exchange_subnet_routes": peering.get("exchange_subnet_routes"),
            "export_custom_routes": peering.get("export_custom_routes"),
            "export_subnet_routes_with_public_ip": peering.get(
                "export_subnet_routes_with_public_ip"
            ),
            "import_custom_routes": peering.get("import_custom_routes"),
            "import_subnet_routes_with_public_ip": peering.get(
                "import_subnet_routes_with_public_ip"
            ),
            "name": peering.get("name"),
            "network": peering.get("network"),
            "peer_mtu": peering.get("peer_mtu"),
            "stack_type": peering.get("stack_type"),
        }
    }
