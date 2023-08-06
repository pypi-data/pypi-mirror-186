"""Exec module for managing Subnetworks."""
__func_alias__ = {"list_": "list"}

from idem_gcp.tool.gcp.utils import get_project_from_account


async def list_(
    hub,
    ctx,
    project: str = None,
    region: str = None,
    filter: str = None,
    order_by: str = None,
):
    r"""Retrieves a list of subnetworks available to the specified project.

    Args:
        project(str, Optional):
            Project ID for this request.

        region(str, Optional):
            Name of the region scoping this request.

        filter(str, Optional):
            A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal AIP-160.

        order_by(str, Optional):
            Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.

    Examples:
        random-name:
          exec.run:
          - path: gcp.compute.subnetwork.list
          - kwargs:
              project: project-name
              region: region-name
    """
    result = {
        "comment": [],
        "ret": None,
        "result": True,
    }

    project = get_project_from_account(ctx, project)

    if region:
        list_result = await hub.exec.gcp_api.client.compute.subnetwork.list(
            ctx,
            project=project,
            region=region,
            filter=filter,
            orderBy=order_by,
        )
    else:
        list_result = await hub.exec.gcp_api.client.compute.subnetwork.aggregatedList(
            ctx,
            project=project,
            filter=filter,
            orderBy=order_by,
        )

    result["comment"] += list_result["comment"]
    if not list_result["result"]:
        result["result"] = False
        return result

    items_list = None
    if list_result and list_result.get("ret"):
        items_list = list_result["ret"].get("items")

    result["ret"] = items_list
    return result


async def get(
    hub,
    ctx,
    project: str = None,
    region: str = None,
    name: str = None,
    resource_id: str = None,
):
    r"""Returns the specified subnetwork. Gets a list of available subnetworks list() request.

    Args:
        project(str, Optional):
            Project ID for this request. Defaults to None.

        region(str, Optional):
            Name of the region scoping this request. Defaults to None.

        name(str, Optional):
            Name of the Subnetwork resource to return. Defaults to None.

        resource_id(str, Optional):
            An identifier of the resource in the provider. Defaults to None.

    Examples:
        random-name:
          exec.run:
          - path: gcp.compute.subnetwork.get
          - kwargs:
              project: project-name
              region: region-name
              name: subnetwork-name
    """
    result = {
        "comment": [],
        "ret": None,
        "result": True,
    }

    project = get_project_from_account(ctx, project)

    if resource_id:
        ret = await hub.exec.gcp_api.client.compute.subnetwork.get(
            ctx,
            resource_id=resource_id,
        )
    elif project and region and name:
        ret = await hub.exec.gcp_api.client.compute.subnetwork.get(
            ctx, project=project, region=region, subnetwork=name, name=name
        )
    else:
        result["result"] = False
        result["comment"] = [
            f"gcp.compute.subnetwork {name} either resource_id or project, region and name"
            f" should be specified."
        ]
        return result

    result["comment"] += ret["comment"]
    if not ret["result"]:
        result["result"] = False
        return result

    result["ret"] = ret["ret"]
    return result
