"""State module for managing Networks."""
import copy
from dataclasses import field
from dataclasses import make_dataclass
from typing import Any
from typing import Dict
from typing import List

from idem_gcp.tool.gcp.utils import get_project_from_account

__contracts__ = ["resource"]


async def present(
    hub,
    ctx,
    name: str,
    resource_id: str = None,
    request_id: str = None,
    project: str = None,
    auto_create_subnetworks: bool = None,
    description: str = None,
    enable_ula_internal_ipv6: bool = None,
    internal_ipv6_range: str = None,
    i_pv4_range: str = None,
    mtu: int = None,
    network_firewall_policy_enforcement_order: str = None,
    routing_config: make_dataclass(
        "NetworkRoutingConfig",
        [
            ("routing_mode", str, field(default=None)),
        ],
    ) = None,
    peerings: List[
        make_dataclass(
            "NetworkPeering",
            [
                ("export_custom_routes", bool, field(default=None)),
                ("auto_create_routes", bool, field(default=None)),
                ("network", str, field(default=None)),
                ("name", str, field(default=None)),
                ("state", str, field(default=None)),
                ("peer_mtu", int, field(default=None)),
                ("import_subnet_routes_with_public_ip", bool, field(default=None)),
                ("import_custom_routes", bool, field(default=None)),
                ("state_details", str, field(default=None)),
                ("export_subnet_routes_with_public_ip", bool, field(default=None)),
                ("exchange_subnet_routes", bool, field(default=None)),
                ("stack_type", str, field(default=None)),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""Creates a network in the specified project using the data included in the request.

    Args:
        name(str):
            An Idem name of the resource.

        request_id(str, Optional):
            An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000). Defaults to None.

        project(str, Optional):
            Project ID for this request.

        routing_config(NetworkRoutingConfig, Optional):
            The network-level routing configuration for this network. Used by Cloud Router to determine what type of network-wide routing behavior to enforce. Defaults to None.

        description(str, Optional):
            An optional description of this resource. Provide this field when you create the resource. Defaults to None.

        auto_create_subnetworks(bool, Optional):
            Must be set to create a VPC network. If not set, a legacy network is created. When set to true, the VPC network is created in auto mode. When set to false, the VPC network is created in custom mode. An auto mode VPC network starts with one subnet per region. Each subnet has a predetermined range as described in Auto mode VPC network IP ranges. For custom mode VPC networks, you can add subnets using the subnetworks insert method. Defaults to None.

        internal_ipv6_range(str, Optional):
            When enabling ula internal ipv6, caller optionally can specify the /48 range they want from the google defined ULA prefix fd20::/20. The input must be a valid /48 ULA IPv6 address and must be within the fd20::/20. Operation will fail if the speficied /48 is already in used by another resource. If the field is not speficied, then a /48 range will be randomly allocated from fd20::/20 and returned via this field. . Defaults to None.

        network_firewall_policy_enforcement_order(str, Optional):
            The network firewall policy enforcement order. Can be either AFTER_CLASSIC_FIREWALL or BEFORE_CLASSIC_FIREWALL. Defaults to AFTER_CLASSIC_FIREWALL if the field is not specified. Defaults to None.

        enable_ula_internal_ipv6(bool, Optional):
            Enable ULA internal ipv6 on this network. Enabling this feature will assign a /48 from google defined ULA prefix fd20::/20. . Defaults to None.

        i_pv4_range(str, Optional):
            Deprecated in favor of subnet mode networks. The range of internal addresses that are legal on this network. This range is a CIDR specification, for example: 192.168.0.0/16. Provided by the client when the network is created. Defaults to None.

        mtu(int, Optional):
            Maximum Transmission Unit in bytes. The minimum value for this field is 1300 and the maximum value is 8896. The suggested value is 1500, which is the default MTU used on the Internet, or 8896 if you want to use Jumbo frames. If unspecified, the value defaults to 1460. Defaults to None.

        resource_id(str, Optional):
            An identifier of the resource in the provider. Defaults to None.

        peerings(List[Dict[str, Any]], Optional): [Output Only] A list of network peerings for the resource. Defaults to None.
            * export_custom_routes(bool, Optional):
                Whether to export the custom routes to peer network. The default value is false.
            * auto_create_routes(bool, Optional):
                This field will be deprecated soon. Use the exchange_subnet_routes field instead. Indicates whether full mesh connectivity is created and managed automatically between peered networks. Currently this field should always be true since Google Compute Engine will automatically create and manage subnetwork routes between two networks when peering state is ACTIVE.
            * network(str, Optional):
                The URL of the peer network. It can be either full URL or partial URL. The peer network may belong to a different project. If the partial URL does not contain project, it is assumed that the peer network is in the same project as the current network.
            * name(str, Optional):
                Name of this peering. Provided by the client when the peering is created. The name must comply with RFC1035. Specifically, the name must be 1-63 characters long and match regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all the following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
            * state(str, Optional):
                [Output Only] State for the peering, either `ACTIVE` or `INACTIVE`. The peering is `ACTIVE` when there's a matching configuration in the peer network.
                Enum type. Allowed values:
                "ACTIVE" - Matching configuration exists on the peer.
                "INACTIVE" - There is no matching configuration on the peer, including the case when peer does not exist.
            * peer_mtu(int, Optional):
                Maximum Transmission Unit in bytes.
            * import_subnet_routes_with_public_ip(bool, Optional):
                Whether subnet routes with public IP range are imported. The default value is false. IPv4 special-use ranges are always imported from peers and are not controlled by this field.
            * import_custom_routes(bool, Optional):
                Whether to import the custom routes from peer network. The default value is false.
            * state_details(str, Optional):
                [Output Only] Details about the current state of the peering.
            * export_subnet_routes_with_public_ip(bool, Optional):
                Whether subnet routes with public IP range are exported. The default value is true, all subnet routes are exported. IPv4 special-use ranges are always exported to peers and are not controlled by this field.
            * exchange_subnet_routes(bool, Optional):
                Indicates whether full mesh connectivity is created and managed automatically between peered networks. Currently this field should always be true since Google Compute Engine will automatically create and manage subnetwork routes between two networks when peering state is ACTIVE.
            * stack_type(str, Optional):
                Which IP version(s) of traffic and routes are allowed to be imported or exported between peer networks. The default value is IPV4_ONLY.
                Enum type. Allowed values:
                "IPV4_IPV6" - This Peering will allow IPv4 traffic and routes to be exchanged. Additionally if the matching peering is IPV4_IPV6, IPv6 traffic and routes will be exchanged as well.
                "IPV4_ONLY" - This Peering will only allow IPv4 traffic and routes to be exchanged, even if the matching peering is IPV4_IPV6.

    Returns:
        Dict[str, Any]

    Examples:
        .. code-block:: sls

            example_resource_name:
              gcp.compute.network.present:
                - project: project-name
                - auto_create_subnetworks: false
    """
    result = {
        "result": True,
        "old_state": None,
        "new_state": None,
        "name": name,
        "comment": [],
    }

    project = get_project_from_account(ctx, project)

    # Get the resource_id from ESM
    if not resource_id:
        resource_id = (ctx.get("old_state") or {}).get(
            "resource_id"
        ) or hub.tool.gcp.resource_prop_utils.construct_resource_id(
            "compute.network", {**locals(), "network": name}
        )

    old = None

    if ctx.get("rerun_data"):
        handle_operation_ret = await hub.tool.gcp.operation_utils.handle_operation(
            ctx, ctx.get("rerun_data"), "compute.network"
        )

        if not handle_operation_ret["result"]:
            result["result"] = False
            result["comment"] += handle_operation_ret["comment"]
            result["rerun_data"] = handle_operation_ret["rerun_data"]
            return result

        resource_id = handle_operation_ret["resource_id"]

    if resource_id:
        old_get_ret = await hub.exec.gcp_api.client.compute.network.get(
            ctx, name=name, resource_id=resource_id
        )

        if not old_get_ret["result"]:
            # error other than non-existing resource
            result["result"] = False
            result["comment"] += old_get_ret["comment"]
            return result

        if old_get_ret["ret"]:
            # resource already exists

            # copy.copy(old_get_ret['ret']) is needed to convert any objects of type NamespaceDict to dict
            # in old_get_ret['ret']. This is done so that comparisons with the plan_state which has
            # objects of type dict works properly
            old = copy.deepcopy(copy.copy(old_get_ret["ret"]))
            result["old_state"] = old

        # do not return here even after fetching network post operation return,
        # as there are further update operations below which might need to run

    request_body = {
        "name": name,
        "description": description,
        "auto_create_subnetworks": auto_create_subnetworks,
        "enable_ula_internal_ipv6": enable_ula_internal_ipv6,
        "internal_ipv6_range": internal_ipv6_range,
        "i_pv4_range": i_pv4_range,
        "mtu": mtu,
        "network_firewall_policy_enforcement_order": network_firewall_policy_enforcement_order,
        "routing_config": routing_config,
        "peerings": peerings,
    }

    request_body = {k: v for (k, v) in request_body.items() if v is not None}
    operation = None
    if old:
        new_state_for_whole_resource_comparison = {
            "resource_id": resource_id,
            **request_body,
        }
        if hasattr(old, "peerings"):
            new_state_for_whole_resource_comparison["peerings"] = old.get("peerings")
        else:
            new_state_for_whole_resource_comparison.pop("peerings", None)

        changes = hub.tool.gcp.utils.compare_states(
            old, new_state_for_whole_resource_comparison, "compute.network"
        )
        are_peerings_changed = (
            not hub.tool.gcp.state_comparison_utils.are_lists_identical(
                old.get("peerings"), peerings
            )
        )

        if not changes and not are_peerings_changed:
            result["result"] = True
            result["comment"].append(
                hub.tool.gcp.comment_utils.already_exists_comment(
                    "gcp.compute.network", name
                )
            )
            result["new_state"] = result["old_state"]
            return result

        if ctx["test"]:
            result["comment"].append(
                hub.tool.gcp.comment_utils.would_update_comment(
                    "gcp.compute.network", name
                )
            )
            result["new_state"] = request_body
            result["new_state"]["resource_id"] = resource_id
            return result

        if are_peerings_changed:
            update_peerings_ret = await hub.tool.gcp.compute.network.update_peerings(
                ctx, resource_id, old.get("peerings"), peerings
            )
            if not update_peerings_ret["result"]:
                result["result"] = False
                result["comment"].append(update_peerings_ret["comment"])
                return result

        if changes:
            if are_peerings_changed:
                get_ret = await hub.exec.gcp.compute.network.get(
                    ctx, resource_id=resource_id
                )
                if not get_ret["result"] and not get_ret["ret"]:
                    result["result"] = False
                    result["comment"] += get_ret["comment"]
                    return result

                # The network interfaces should be the same so update does not happen there
                request_body["peerings"] = get_ret["ret"].get("peerings")

            patch_ret = await hub.exec.gcp_api.client.compute.network.patch(
                ctx, resource_id=resource_id, body=request_body
            )

            if not patch_ret["result"]:
                result["result"] = False
                result["comment"].append(patch_ret["comment"])
                return result
            if patch_ret["ret"] is not None:
                if "compute#operation" in patch_ret["ret"].get("kind"):
                    operation = patch_ret["ret"]

        result["comment"].append(
            hub.tool.gcp.comment_utils.update_comment("gcp.compute.network", name)
        )
    else:
        if ctx["test"]:
            result["comment"].append(
                hub.tool.gcp.comment_utils.would_create_comment(
                    "gcp.compute.network", name
                )
            )
            result["new_state"] = request_body
            result["new_state"]["resource_id"] = resource_id
            return result

        # Create
        create_ret = await hub.exec.gcp_api.client.compute.network.insert(
            ctx, name=name, project=project, body=request_body
        )
        if not create_ret["result"]:
            result["result"] = False
            result["comment"] += create_ret["comment"]
            return result

        result["old_state"] = {}
        resource_id = create_ret["ret"].get("resource_id")
        if "compute#operation" in create_ret["ret"].get("kind"):
            operation = create_ret["ret"]

    if operation:
        operation_id = hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
            operation.get("selfLink"), "compute.global_operation"
        )
        handle_operation_ret = await hub.tool.gcp.operation_utils.handle_operation(
            ctx, operation_id, "compute.network"
        )

        if not handle_operation_ret["result"]:
            result["result"] = False
            result["comment"] += handle_operation_ret["comment"]
            result["rerun_data"] = handle_operation_ret["rerun_data"]
            return result

        resource_id = handle_operation_ret["resource_id"]

    # Try getting the resource again
    # TODO: Reconciliation or waiter loop?
    # TODO: Check if this can be removed because insert and update may also return the necessary data on success
    get_ret = await hub.exec.gcp_api.client.compute.network.get(
        ctx, name=name, resource_id=resource_id
    )
    if not get_ret["result"] and not get_ret["ret"]:
        result["result"] = False
        result["comment"] += get_ret["comment"]
        return result
    result["new_state"] = get_ret["ret"]

    # Handle the peerings addition when new network is created
    if not result["new_state"].get("peerings") and peerings:
        add_peerings_ret = await hub.tool.gcp.compute.network.add_peerings(
            ctx, resource_id, peerings
        )
        if not add_peerings_ret["result"]:
            result["result"] = False
            result["comment"] += add_peerings_ret["comment"]
            return result

    # Make a new get request containing the peerings in their form in gcp api
    get_ret = await hub.exec.gcp_api.client.compute.network.get(
        ctx, name=name, resource_id=resource_id
    )
    if not get_ret["result"] and not get_ret["ret"]:
        result["result"] = False
        result["comment"] += get_ret["comment"]
        return result
    result["new_state"] = get_ret["ret"]
    return result


async def absent(
    hub,
    ctx,
    name: str = None,
    resource_id: str = None,
    request_id: str = None,
) -> Dict[str, Any]:
    r"""Deletes the specified network.

    Args:
        name(str):
            An Idem name of the resource.

        resource_id(str, Optional):
            An identifier of the resource in the provider. Defaults to None.

        request_id(str, Optional):
            An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000). Defaults to None.

    Returns:
        Dict[str, Any]

    Examples:
        .. code-block:: sls

            my-network:
              gcp.compute.network.absent:
                - resource_id: projects/project-name/global/networks/my-network

    """
    result = {
        "comment": [],
        "old_state": ctx.get("old_state"),
        "new_state": None,
        "name": name,
        "result": True,
    }

    if not resource_id:
        resource_id = (ctx.old_state or {}).get("resource_id")

    if ctx.test:
        result["comment"].append(
            hub.tool.gcp.comment_utils.would_delete_comment("gcp.compute.network", name)
        )
        return result

    if not ctx.get("rerun_data"):
        # First iteration; invoke instance's delete()
        delete_ret = await hub.exec.gcp_api.client.compute.network.delete(
            ctx, resource_id=resource_id
        )
        if delete_ret["ret"]:
            if "compute#operation" in delete_ret["ret"].get("kind"):
                result["result"] = False
                result["comment"] += delete_ret["comment"]
                result[
                    "rerun_data"
                ] = hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
                    delete_ret["ret"].get("selfLink"), "compute.global_operation"
                )
                return result

    else:
        # delete() has been called on some previous iteration
        handle_operation_ret = await hub.tool.gcp.operation_utils.handle_operation(
            ctx, ctx.get("rerun_data"), "compute.network"
        )
        if not handle_operation_ret["result"]:
            result["result"] = False
            result["comment"] += handle_operation_ret["comment"]
            result["rerun_data"] = handle_operation_ret["rerun_data"]
            return result

        resource_id = handle_operation_ret["resource_id"]

    if not resource_id:
        result["comment"].append(
            hub.tool.gcp.comment_utils.already_absent_comment(
                "gcp.compute.network", name
            )
        )

    result["comment"].append(
        hub.tool.gcp.comment_utils.delete_comment("gcp.compute.network", name)
    )
    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    r"""Describe the resource in a way that can be recreated/managed with the corresponding "present" function.

    Retrieves the list of networks available to the specified project.

    Returns:
        Dict[str, Dict[str, Any]]

    Examples:
        .. code-block:: bash

            $ idem describe gcp.compute.network

    """
    result = {}

    # TODO: Pagination
    describe_ret = await hub.exec.gcp_api.client.compute.network.list(
        ctx, project=ctx.acct.project_id
    )

    if not describe_ret["result"]:
        hub.log.debug(
            f"Could not describe gcp.compute.network {describe_ret['comment']}"
        )
        return {}

    for resource in describe_ret["ret"]["items"]:
        resource_id = resource.get("resource_id")

        result[resource_id] = {
            "gcp.compute.network.present": [
                {parameter_key: parameter_value}
                for parameter_key, parameter_value in resource.items()
            ]
        }

    return result
