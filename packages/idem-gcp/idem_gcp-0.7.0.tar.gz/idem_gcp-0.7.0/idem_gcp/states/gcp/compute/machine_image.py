"""State module for managing Machine Images."""
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
    project: str = None,
    resource_id: str = None,
    source_instance: str = None,
    storage_locations: List[str] = None,
    source_disk_encryption_keys: List[
        make_dataclass(
            "SourceDiskEncryptionKey",
            [
                ("sourceDisk", str, field(default=None)),
                ("diskEncryptionKey", {}, field(default=None)),
            ],
        )
    ] = None,
    description: str = None,
    saved_disks: List[
        make_dataclass(
            "SavedDisk",
            [
                ("kind", str, field(default="compute#savedDisk")),
                ("storageBytesStatus", str, field(default=None)),
                ("architecture", str, field(default=None)),
                ("storageBytes", str, field(default=None)),
                ("sourceDisk", str, field(default=None)),
            ],
        )
    ] = None,
    guest_flush: bool = None,
    machine_image_encryption_key: make_dataclass(
        "CustomerEncryptionKey",
        [
            ("kmsKeyServiceAccount", str, field(default=None)),
            ("rsaEncryptedKey", str, field(default=None)),
            ("rawKey", str, field(default=None)),
            ("kmsKeyName", str, field(default=None)),
        ],
    ) = None,
) -> Dict[str, Any]:
    r"""Creates a machine image in the specified project using the data that is included in the request. If you are creating a new machine image to update an existing instance, your new machine image should use the same network or, if applicable, the same subnetwork as the original instance.

    Args:

        name(str):
            An Idem name of the resource.

        project(str, Optional):
            Project ID for this request.

        resource_id(str, Optional):
            An identifier of the resource in the provider. Defaults to None.

        source_instance(str, Optional):
            The source instance used to create the machine image. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance . Defaults to None.

        storage_locations(list[str], Optional):
            The regional or multi-regional Cloud Storage bucket location where the machine image is stored. Defaults to None.

        source_disk_encryption_keys(list[Dict[str, Any]], Optional):
            [Input Only] The customer-supplied encryption key of the disks attached to the source instance. Required if the source disk is protected by a customer-supplied encryption key. Defaults to None.
            * properties (Dict[str, Dict[str, Any]], optional): None
                * sourceDisk (str, optional): URL of the disk attached to the source instance. This can be a full or valid partial URL. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /disks/disk - projects/project/zones/zone/disks/disk - zones/zone/disks/disk
                * diskEncryptionKey ({}, optional): The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.

        description(str, Optional):
            An optional description of this resource. Provide this property when you create the resource. Defaults to None.

        saved_disks(list[Dict[str, Any]], Optional):
            An array of Machine Image specific properties for disks attached to the source instance. Defaults to None.
            * properties (Dict[str, Dict[str, Any]], optional): An instance-attached disk resource.
                * kind (str, optional): [Output Only] Type of the resource. Always compute#savedDisk for attached disks.
                * storageBytesStatus (str, optional): [Output Only] An indicator whether storageBytes is in a stable state or it is being adjusted as a result of shared storage reallocation. This status can either be UPDATING, meaning the size of the snapshot is being updated, or UP_TO_DATE, meaning the size of the snapshot is up-to-date.
                * architecture (str, optional): [Output Only] The architecture of the attached disk.
                * storageBytes (str, optional): [Output Only] Size of the individual disk snapshot used by this machine image.
                * sourceDisk (str, optional): Specifies a URL of the disk attached to the source instance.

        guest_flush(bool, Optional):
            [Input Only] Whether to attempt an application consistent machine image by informing the OS to prepare for the snapshot process. Defaults to None.

        machine_image_encryption_key({}, Optional):
            Encrypts the machine image using a customer-supplied encryption key. After you encrypt a machine image using a customer-supplied key, you must provide the same key if you use the machine image later. For example, you must provide the encryption key when you create an instance from the encrypted machine image in a future request. Customer-supplied encryption keys do not protect access to metadata of the machine image. If you do not provide an encryption key when creating the machine image, then the machine image will be encrypted using an automatically generated key and you do not need to provide a key to use the machine image later. Defaults to None.

    Returns:
        Dict[str, Any]

    Examples:
        .. code-block:: sls

            example_resource_name:
                gcp.compute.machine_image.present:
                  - project: project-name
                  - source_instance: https://www.googleapis.com/compute/v1/projects/project-name/zones/zone-name/instances/instance-name
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
            "compute.machine_image", {**locals(), "machineImage": name}
        )
    old = None

    # TODO: Handle operation result state
    if ctx.get("rerun_data"):
        handle_operation_ret = await hub.tool.gcp.operation_utils.handle_operation(
            ctx, ctx.get("rerun_data"), "compute.machine_image"
        )

        if not handle_operation_ret["result"]:
            result["result"] = False
            result["comment"] += handle_operation_ret["comment"]
            result["rerun_data"] = handle_operation_ret["rerun_data"]
            return result

        resource_id = handle_operation_ret["resource_id"]

    if resource_id:
        old_get_ret = await hub.exec.gcp_api.client.compute.machine_image.get(
            ctx, resource_id=resource_id
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

            # If rerun_data is set at this point this means that there has been a completed create or update operation
            # so there is no need to run the code for create or update below again and we stop here
            if ctx.get("rerun_data"):
                result["new_state"] = result["old_state"]
                return result

    # TODO: Check if body contains the same parameters as old
    # to be autogenerated by pop-create based on insert/update props in properties.yaml
    resource_body = {
        "storage_locations": storage_locations,
        "guest_flush": guest_flush,
        "source_instance": source_instance,
        "description": description,
        "name": name,
        "saved_disks": saved_disks,
        "machine_image_encryption_key": machine_image_encryption_key,
        "source_disk_encryption_keys": source_disk_encryption_keys,
    }

    # TODO: How to handle query params which are not returned in the response body of get
    plan_state = {
        # "project": project,
        # "predefined_acl": predefined_acl,
        # "predefined_default_object_acl": predefined_default_object_acl,
        "resource_id": resource_id,
        **resource_body,
    }

    plan_state = {k: v for (k, v) in plan_state.items() if v is not None}
    operation = None
    if old:
        changes = hub.tool.gcp.utils.compare_states(
            old, plan_state, "compute.machine_image"
        )
        if not changes:
            result["result"] = True
            result["comment"].append(
                hub.tool.gcp.comment_utils.already_exists_comment(
                    "gcp.compute.machine_image", name
                )
            )
            result["new_state"] = result["old_state"]
            return result

        result["comment"].append(
            "No-op: There is no update function for gcp.compute.machine_image"
        )

    else:
        if ctx["test"]:
            result["comment"].append(
                hub.tool.gcp.comment_utils.would_create_comment(
                    "gcp.compute.machine_image", name
                )
            )
            result["new_state"] = plan_state
            return result

        # Create
        create_ret = await hub.exec.gcp_api.client.compute.machine_image.insert(
            ctx, project=project, body=resource_body
        )
        if not create_ret["result"]:
            result["result"] = False
            result["comment"] += create_ret["comment"]
            return result
        result["comment"].append(
            hub.tool.gcp.comment_utils.create_comment("gcp.compute.machine_image", name)
        )
        result["old_state"] = {}
        resource_id = create_ret["ret"].get("resource_id")
        if "compute#operation" in create_ret["ret"].get("kind"):
            operation = create_ret["ret"]

    if operation:
        operation_id = hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
            operation.get("selfLink"), "compute.global_operation"
        )
        handle_operation_ret = await hub.tool.gcp.operation_utils.handle_operation(
            ctx, operation_id, "compute.machine_image"
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
    get_ret = await hub.exec.gcp_api.client.compute.machine_image.get(
        ctx, resource_id=resource_id
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
    name: str,
    resource_id: str = None,
    request_id: str = None,
) -> Dict[str, Any]:
    r"""Deletes the specified machine image. Deleting a machine image is permanent and cannot be undone.

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

            resource_is_absent:
              gcp.compute.machine_image.absent:
                - name: value
                - project: value
                - machine_image: value
    """
    result = {
        "comment": [],
        "old_state": ctx.get("old_state"),
        "new_state": None,
        "name": name,
        "result": True,
    }

    if not resource_id:
        resource_id = (ctx.get("old_state") or {}).get("resource_id")

    if ctx.test:
        result["comment"].append(
            hub.tool.gcp.comment_utils.would_delete_comment(
                "gcp.compute.machine_image", name
            )
        )
        return result

    if not ctx.get("rerun_data"):
        # First iteration; invoke machine image's delete()
        delete_ret = await hub.exec.gcp_api.client.compute.machine_image.delete(
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
            ctx, ctx.get("rerun_data"), "compute.machine_image"
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
                "gcp.compute.machine_image", name
            )
        )
        return result

    result["comment"].append(
        hub.tool.gcp.comment_utils.delete_comment("gcp.compute.machine_image", name)
    )
    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    r"""Describe the resource in a way that can be recreated/managed with the corresponding "present" function.

    Retrieves a list of machine images that are contained within the specified project.

    Returns:
        Dict[str, Any]

    Examples:
        .. code-block:: bash

            $ idem describe gcp.compute.machine_image
    """
    result = {}

    describe_ret = await hub.exec.gcp_api.client.compute.machine_image.list(
        ctx, project=ctx.acct.project_id
    )

    if not describe_ret["result"]:
        hub.log.debug(
            f"Could not describe gcp.compute.machine_image {describe_ret['comment']}"
        )
        return {}

    for resource in describe_ret["ret"]["items"]:
        resource_id = resource.get("resource_id")
        result[resource_id] = {
            "gcp.compute.machine_image.present": [
                {parameter_key: parameter_value}
                for parameter_key, parameter_value in resource.items()
            ]
        }
    return result
