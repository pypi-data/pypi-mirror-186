import time
from typing import Any
from typing import Dict


async def handle_operation(
    hub, ctx, operation_id: str, resource_type: str, wait_until_done: bool = False
) -> Dict[str, Any]:
    result = {
        "comment": [],
        "result": True,
        "rerun_data": None,
        "resource_id": None,
    }

    operation_type = hub.tool.gcp.operation_utils.get_operation_type(operation_id)

    if operation_type is None:
        result["result"] = False
        result["comment"].append(
            f"Cannot determine operation scope (zonal/regional/global) {operation_id}"
        )
        return result

    if operation_type == "compute.zone_operation":
        get_ret = await hub.exec.gcp_api.client.compute.zone_operation.get(
            ctx, resource_id=operation_id
        )
    elif operation_type == "compute.region_operation":
        get_ret = await hub.exec.gcp_api.client.compute.region_operation.get(
            ctx, resource_id=operation_id
        )
    elif operation_type == "compute.global_operation":
        get_ret = await hub.exec.gcp_api.client.compute.global_operation.get(
            ctx, resource_id=operation_id
        )

    if not get_ret["result"] or not get_ret["ret"]:
        result["result"] = False
        result["comment"] = get_ret["comment"]
        return result

    operation = get_ret["ret"]
    if operation["status"] != "DONE":
        if wait_until_done:
            operation = await hub.tool.gcp.operation_utils.wait_for_operation(
                ctx, operation, operation_type
            )
        else:
            result["result"] = False
            result[
                "rerun_data"
            ] = hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
                operation.get("selfLink"), operation_type
            )
            result["comment"] += get_ret["comment"]
            return result

    if operation.get("error"):
        result["result"] = False
        result["comment"] += str(operation.get("error", {}))
        return result

    result["resource_id"] = hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
        operation.get("targetLink"), resource_type
    )

    return result


async def wait_for_operation(hub, ctx, operation, operation_type: str) -> Dict:
    while True:
        if operation_type == "compute.zone_operation":
            op_ret = await hub.exec.gcp_api.client.compute.zone_operation.wait(
                ctx, resource_id=operation["selfLink"]
            )
        elif operation_type == "compute.region_operation":
            op_ret = await hub.exec.gcp_api.client.compute.region_operation.wait(
                ctx, resource_id=operation["selfLink"]
            )
        elif operation_type == "compute.global_operation":
            op_ret = await hub.exec.gcp_api.client.compute.global_operation.wait(
                ctx, resource_id=operation["selfLink"]
            )

        operation = op_ret["ret"]
        if operation["status"] == "DONE" or "error" in operation:
            break

        time.sleep(1)

    return operation


def get_operation_type(hub, operation_id) -> str:
    if "/zones/" in operation_id:
        return "compute.zone_operation"
    elif "/regions/" in operation_id:
        return "compute.region_operation"
    elif "/global/" in operation_id:
        return "compute.global_operation"
    else:
        return None


async def await_operation_completion(
    hub, ctx, api_call_ret: Dict[str, Any], resource_type: str, operation_type: str
) -> Dict[str, Any]:
    result = {"result": False, "comment": []}

    if not api_call_ret["result"] and not api_call_ret["ret"]:
        result["comment"] += api_call_ret["comment"]
        return result

    if "compute#operation" in api_call_ret["ret"].get("kind"):
        operation = api_call_ret["ret"]

        operation_id = hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
            operation.get("selfLink"), operation_type
        )
        handle_operation_ret = await hub.tool.gcp.operation_utils.handle_operation(
            ctx, operation_id, resource_type, True
        )

        if not handle_operation_ret["result"]:
            result["comment"] += handle_operation_ret["comment"]
            return result

    result["result"] = True
    return result
