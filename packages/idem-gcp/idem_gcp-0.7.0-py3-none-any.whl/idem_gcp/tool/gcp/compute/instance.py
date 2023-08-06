import copy
from typing import Any
from typing import Dict
from typing import List


async def update_network_interfaces(
    hub,
    ctx,
    current_instance: Dict[str, Any],
    new_network_interfaces: List[Dict[str, Any]],
) -> Dict[str, Any]:
    # Update the updatable network interface properties and the access configs
    result = {"result": False, "comment": []}

    existing_network_interfaces = copy.deepcopy(
        current_instance.get("network_interfaces", [])
    )
    for net_intf in new_network_interfaces:
        existing_net_intf = next(
            (
                existing_network_interfaces[idx]
                for idx in range(len(existing_network_interfaces))
                if existing_network_interfaces[idx].get("name") == net_intf.get("name")
            ),
            None,
        )
        if not existing_net_intf:
            break

        # According to documentation, only one access config per instance is supported.

        existing_access_configs = existing_net_intf.get("access_configs", [])
        desired_access_configs = net_intf.get("access_configs", [])

        existing_ac = (
            existing_access_configs[0] if len(existing_access_configs) > 0 else None
        )
        desired_ac = (
            desired_access_configs[0] if len(desired_access_configs) > 0 else None
        )

        if not existing_ac and not desired_ac:
            continue

        elif existing_ac and not desired_ac:
            op_ret = await hub.exec.gcp_api.client.compute.instance.deleteAccessConfig(
                ctx,
                resource_id=current_instance.get("resource_id"),
                access_config=existing_ac.get("name"),
                network_interface=net_intf.get("name"),
            )

            r = await hub.tool.gcp.operation_utils.await_operation_completion(
                ctx, op_ret, "compute.instance", "compute.zone_operation"
            )
            if not r["result"]:
                result["comment"] += r["comment"]
                return result

        elif desired_ac and not existing_ac:
            op_ret = await hub.exec.gcp_api.client.compute.instance.addAccessConfig(
                ctx,
                resource_id=current_instance.get("resource_id"),
                network_interface=net_intf.get("name"),
                body=desired_ac,
            )

            r = await hub.tool.gcp.operation_utils.await_operation_completion(
                ctx, op_ret, "compute.instance", "compute.zone_operation"
            )
            if not r["result"]:
                result["comment"] += r["comment"]
                return result

        # existing_ac and desired_ac
        elif next(
            (
                key
                for key in desired_ac.keys()
                if desired_ac.get(key) != existing_ac.get(key)
            ),
            None,
        ):
            op_ret = await hub.exec.gcp_api.client.compute.instance.updateAccessConfig(
                ctx,
                resource_id=current_instance.get("resource_id"),
                network_interface=net_intf.get("name"),
                body=desired_ac,
            )

            r = await hub.tool.gcp.operation_utils.await_operation_completion(
                ctx, op_ret, "compute.instance", "compute.zone_operation"
            )
            if not r["result"]:
                result["comment"] += r["comment"]
                return result

        # Network interface update
        # Cannot update access config through network interface update function - must be a separate call
        body = hub.tool.gcp.utils.create_dict_body_on_top_of_old(
            ctx, existing_net_intf, net_intf
        )

        # We want to exclude access configs from update nic operation because it is not supported and
        # it is handled separately.
        body.pop("access_configs", None)
        existing_net_intf.pop("access_configs", None)

        if body != existing_net_intf:
            op_ret = (
                await hub.exec.gcp_api.client.compute.instance.updateNetworkInterface(
                    ctx,
                    resource_id=current_instance.get("resource_id"),
                    network_interface=existing_net_intf.get("name"),
                    body=body,
                )
            )

            ret = await hub.tool.gcp.operation_utils.await_operation_completion(
                ctx, op_ret, "compute.instance", "compute.zone_operation"
            )
            if not ret["result"]:
                result["comment"] += ret["comment"]
                return result

    result["result"] = True
    return result
