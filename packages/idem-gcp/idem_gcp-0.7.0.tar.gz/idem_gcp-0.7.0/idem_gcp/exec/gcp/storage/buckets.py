"""Exec module for managing Buckets."""
from typing import Any
from typing import Dict

from idem_gcp.tool.gcp.utils import get_project_from_account

__func_alias__ = {"list_": "list"}


async def list_(
    hub,
    ctx,
    project: str = None,
    prefix: str = None,
    projection: str = None,
):
    r"""Retrieves a list of buckets for a given project, ordered in the list lexicographically by name.

    Args:
        project(str, Optional):
            Project ID for this request.

        prefix(str, Optional):
            Filter results to buckets whose names begin with this prefix.

        projection(str, Optional):
            Set of properties to return. Defaults to noAcl.

            Acceptable values are:
               full: Include all properties.
               noAcl: Omit owner, acl, and defaultObjectAcl properties.

    Examples:
        .. code-block: sls

            random-name:
              exec.run:
              - path: gcp.storage.buckets.list
              - kwargs:
                  project: project-name
                  prefix: bucket-name-prefix
    """
    result = {
        "comment": [],
        "ret": None,
        "result": True,
    }

    project = get_project_from_account(ctx, project)

    ret = await hub.exec.gcp_api.client.storage.buckets.list(
        ctx,
        project=project,
        prefix=prefix,
        projection=projection,
    )

    if not ret["result"]:
        result["comment"] += ret["comment"]
        result["result"] = False
        return result

    result["ret"] = ret["ret"]["items"]
    return result


async def get(
    hub,
    ctx,
    name: str,
    projection: str = None,
) -> Dict[str, Any]:
    r"""Returns the specified bucket.

    Args:
        name(str):
            Name of the bucket.

        projection(str, Optional):
            Set of properties to return. Defaults to noAcl.

            Acceptable values are:
                full: Include all properties.
                noAcl: Omit owner, acl, and defaultObjectAcl properties.

    Examples:
        .. code-block: sls

            random-name:
              exec.run:
              - path: gcp.storage.buckets.get
              - kwargs:
                  name: bucket-name
    """
    result = {
        "comment": [],
        "ret": None,
        "result": True,
    }

    ret = await hub.exec.gcp_api.client.storage.buckets.get(
        ctx,
        bucket=name,
        projection=projection,
    )

    if not ret["result"]:
        result["comment"] += ret["comment"]
        result["result"] = False
        return result

    result["ret"] = ret["ret"]
    return result
