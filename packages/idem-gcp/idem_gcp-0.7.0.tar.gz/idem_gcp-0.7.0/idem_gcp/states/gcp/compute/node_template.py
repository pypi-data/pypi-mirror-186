"""State module for managing Node Templates."""
from dataclasses import field
from dataclasses import make_dataclass
from typing import Any
from typing import Dict
from typing import List


__contracts__ = ["resource"]


async def present(
    hub,
    ctx,
    name: str,
    resource_id: str = None,
    request_id: str = None,
    project: str = None,
    region: str = None,
    description: str = None,
    disks: List[
        make_dataclass(
            "LocalDisk",
            [
                ("disk_count", int, field(default=0)),
                ("disk_type", str, field(default=None)),
                ("disk_size_gb", int, field(default=0)),
            ],
        )
    ] = None,
    cpu_overcommit_type: str = None,
    server_binding: make_dataclass(
        "ServerBinding",
        [
            ("type", str, field(default=None)),
        ],
    ) = None,
    node_affinity_labels: Dict = None,
    node_type_flexibility: make_dataclass(
        "NodeTemplateNodeTypeFlexibility",
        [
            ("memory", str, field(default=None)),
            ("local_ssd", str, field(default=None)),
            ("cpus", str, field(default=None)),
        ],
    ) = None,
    accelerators: List[
        make_dataclass(
            "AcceleratorConfig",
            [
                ("acceleratorType", str, field(default=None)),
                ("acceleratorCount", int, field(default=0)),
            ],
        )
    ] = None,
    node_type: str = None,
) -> Dict[str, Any]:
    r"""Creates a network in the specified project using the data included in the request.

    Args:
        name(str):
            An Idem name of the resource.

        request_id(str, Optional):
            An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000). Defaults to None.

        project(str, Optional):
            Project ID for this request.

        region(str, Optional):
            The name of the region for this request.

        description(str, Optional):
            An optional description of this resource. Provide this field when you create the resource. Defaults to None.

        disks(List[LocalDisk], Optional):
            Local disk configurations.

        cpu_overcommit_type(str, Optional):
            CPU overcommit.

        server_binding(ServerBinding, Optional):
            Sets the binding properties for the physical server. Valid values include: - *[Default]* RESTART_NODE_ON_ANY_SERVER: Restarts VMs on any available physical server - RESTART_NODE_ON_MINIMAL_SERVER: Restarts VMs on the same physical server whenever possible See Sole-tenant node options for more information.

        node_affinity_labels({}, Optional):
            Labels to use for node affinity, which will be used in instance scheduling.

        node_type_flexibility(NodeTemplateNodeTypeFlexibility, Optional):
            The flexible properties of the desired node type. Node groups that use this node template will create nodes of a type that matches these properties. This field is mutually exclusive with the node_type property; you can only define one or the other, but not both.

        accelerators(List[AcceleratorConfig], Optional):
            A specification of the type and number of accelerator cards attached to the instance.

        node_type(str, Optional):
            The node type to use for nodes group that are created from this template.

        resource_id(str, Optional):
            An identifier of the resource in the provider. Defaults to None.

    Returns:
        Dict[str, Any]

    Examples:
        .. code-block:: sls

    """
    result = {
        "result": True,
        "old_state": None,
        "new_state": None,
        "name": name,
        "comment": [],
    }

    # TODO uncomment below line, when implementation is added
    # project = get_project_from_account(ctx, project)

    result["comment"].append(
        "No-op: There is no create/update function for gcp.compute.node_template"
    )

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

            delete-my-node-template:
              gcp.compute.node_template.absent:
                - resource_id: projects/project-name/regions/europe-west2/node_templates/node_template-123
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
            hub.tool.gcp.comment_utils.would_delete_comment(
                "gcp.compute.node_template", name
            )
        )
        return result

    if not ctx.get("rerun_data"):
        # First iteration; invoke instance's delete()
        delete_ret = await hub.exec.gcp_api.client.compute.node_template.delete(
            ctx, resource_id=resource_id
        )
        if delete_ret["ret"]:
            if "compute#operation" in delete_ret["ret"].get("kind"):
                result["result"] = False
                result["comment"] += delete_ret["comment"]
                result[
                    "rerun_data"
                ] = hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
                    delete_ret["ret"].get("selfLink"), "compute.region_operation"
                )
                return result

    else:
        # delete() has been called on some previous iteration
        handle_operation_ret = await hub.tool.gcp.operation_utils.handle_operation(
            ctx, ctx.get("rerun_data"), "compute.node_template"
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
                "gcp.compute.node_template", name
            )
        )

    result["comment"].append(
        hub.tool.gcp.comment_utils.delete_comment("gcp.compute.node_template", name)
    )
    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    r"""Describe the resource in a way that can be recreated/managed with the corresponding "present" function.

    Retrieves an aggregated list of node templates.

    Returns:
        Dict[str, Dict[str, Any]]

    Examples:
        .. code-block:: bash

            $ idem describe gcp.compute.node_template
    """
    result = {}

    # TODO: Pagination
    describe_ret = await hub.exec.gcp_api.client.compute.node_template.aggregatedList(
        ctx, project=ctx.acct.project_id
    )

    if not describe_ret["result"]:
        hub.log.debug(
            f"Could not describe gcp.compute.node_template {describe_ret['comment']}"
        )
        return {}

    for resource in describe_ret["ret"]["items"]:
        resource_id = resource.get("resource_id")

        result[resource_id] = {
            "gcp.compute.node_template.present": [
                {parameter_key: parameter_value}
                for parameter_key, parameter_value in resource.items()
            ]
        }

    return result
