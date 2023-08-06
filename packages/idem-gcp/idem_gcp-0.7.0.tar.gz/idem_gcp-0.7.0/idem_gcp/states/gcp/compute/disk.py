"""State module for managing Disks."""
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
    name: str = None,
    project: str = None,
    zone: str = None,
    resource_id: str = None,
    request_id: str = None,
    source_image: str = None,
    size_gb: str = None,
    source_snapshot: str = None,
    source_storage_object: str = None,
    options: str = None,
    type: str = None,
    licenses: List[str] = None,
    guest_os_features: List[
        make_dataclass("GuestOsFeature", [("type", str, field(default=None))])
    ] = None,
    disk_encryption_key: make_dataclass(
        "CustomerEncryptionKey",
        [
            ("raw_key", str, field(default=None)),
            ("rsa_encrypted_key", str, field(default=None)),
            ("kms_key_name", str, field(default=None)),
            ("kms_key_service_account", str, field(default=None)),
        ],
    ) = None,
    source_image_encryption_key: make_dataclass(
        "CustomerEncryptionKey",
        [
            ("raw_key", str, field(default=None)),
            ("rsa_encrypted_key", str, field(default=None)),
            ("kms_key_name", str, field(default=None)),
            ("kms_key_service_account", str, field(default=None)),
        ],
    ) = None,
    source_snapshot_encryption_key: make_dataclass(
        "CustomerEncryptionKey",
        [
            ("raw_key", str, field(default=None)),
            ("rsa_encrypted_key", str, field(default=None)),
            ("kms_key_name", str, field(default=None)),
            ("kms_key_service_account", str, field(default=None)),
        ],
    ) = None,
    labels: Dict[str, str] = None,
    label_fingerprint: str = None,
    replica_zones: List[str] = None,
    license_codes: List[str] = None,
    physical_block_size_bytes: str = None,
    resource_policies: List[str] = None,
    source_disk: str = None,
    provisioned_iops: str = None,
    location_hint: str = None,
    architecture: str = None,
    params: make_dataclass(
        "DiskParams",
        [
            ("resource_manager_tags", Dict[str, str], field(default=None)),
        ],
    ) = None,
    description: str = None,
) -> Dict[str, Any]:
    r"""Creates or updates a persistent disk in the specified project using the data in the request.

    You can create a disk from a source (sourceImage, sourceSnapshot, or sourceDisk) or create an empty 500 GB data disk by omitting all properties.
    You can also create a disk that is larger than the default size by specifying the sizeGb property.

    Args:
        name(str):
            An Idem name of the resource.

        zone(str):
            The name of the zone for this request.

        project(str, Optional):
            Project ID for this request.

        resource_id(str, Optional):
            An identifier of the resource in the provider.
            Defaults to None.

        request_id(str, Optional):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must retry your request,
            the server will know to ignore the request if it has already been completed.
            For example, consider a situation where you make an initial request and the request times out.
            If you make the request again with the same request ID,
            the server can check if original operation with the same request ID was received, and if so,
            will ignore the second request. This prevents clients from accidentally creating duplicate commitments.
            The request ID must be a valid UUID with the exception that
            zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
            Defaults to None.

        source_image(str, Optional):
            The source image used to create this disk. If the source image is deleted, this field will not be set.
            To create a disk with one of the public operating system images, specify the image by its family name.
            For example, specify family/debian-9 to use the latest Debian 9 image:
            projects/debian-cloud/global/images/family/debian-9
            Alternatively, use a specific version of a public operating system image:
            projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD
            To create a disk with a custom image that you created, specify the image name in the following format:
            global/images/my-custom-image You can also specify a custom image by its image family,
            which returns the latest version of the image in that family.
            Replace the image name with family/family-name: global/images/family/my-image-family .
            Defaults to None.

        size_gb(str, Optional):
            Size, in GB, of the persistent disk.
            You can specify this field when creating a persistent disk using the sourceImage, sourceSnapshot,
            or sourceDisk parameter, or specify it alone to create an empty persistent disk.
            If you specify this field along with a source, the value of sizeGb must not
            be less than the size of the source. Acceptable values are 1 to 65536, inclusive.
            Defaults to None.

        source_snapshot(str, Optional):
            The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource.
            For example, the following are valid values:
                - https://www.googleapis.com/compute/v1/projects/project /global/snapshots/snapshot
                - projects/project/global/snapshots/snapshot
                - global/snapshots/snapshot
            Defaults to None.

        source_storage_object(str, Optional):
            The full Google Cloud Storage URI where the disk image is stored.
            This file must be a gzip-compressed tarball whose name ends in .tar.gz or virtual machine disk
            whose name ends in vmdk. Valid URIs may start with gs:// or https://storage.googleapis.com/.
            This flag is not optimized for creating multiple disks from a source storage object.
            To create many disks from a source storage object, use gcloud compute images import instead.
            Defaults to None.

        options(str, Optional):
            Internal use only.
            Defaults to None.

        type(str, Optional):
            URL of the disk type resource describing which disk type to use to create the disk.
            Provide this when creating the disk. For example: projects/project /zones/zone/diskTypes/pd-ssd.
            See Persistent disk types.
            Defaults to None.

        licenses(List[str], Optional):
            A list of publicly visible licenses. Reserved for Google's use.
            Defaults to None.

        guest_os_features(List[Dict[str, Any]], Optional):
            A list of features to enable on the guest operating system. Applicable only for bootable images.
            Read Enabling guest operating system features to see a list of available options.
            Defaults to None.

                * type (str, Optional):
                    The ID of a supported feature. To add multiple values,
                    use commas to separate values. Set to one or more of the following values:
                        - VIRTIO_SCSI_MULTIQUEUE
                        - WINDOWS
                        - MULTI_IP_SUBNET
                        - UEFI_COMPATIBLE
                        - GVNIC
                        - SEV_CAPABLE
                        - SUSPEND_RESUME_COMPATIBLE
                        - SEV_SNP_CAPABLE
                    For more information, see Enabling guest operating system features.

        disk_encryption_key(Dict[str, Any], Optional):
            Encrypts the disk using a customer-supplied encryption key or a customer-managed encryption key.
            Encryption keys do not protect access to metadata of the disk. After you encrypt a disk with a
            customer-supplied key, you must provide the same key if you use the disk later. For example,
            to create a disk snapshot, to create a disk image, to create a machine image, or to attach the disk to a
            virtual machine. After you encrypt a disk with a customer-managed key, the diskEncryptionKey.kmsKeyName
            is set to a key *version* name once the disk is created. The disk is encrypted with this version of the key.
            In the response, diskEncryptionKey.kmsKeyName appears in the following format:
            "diskEncryptionKey.kmsKeyName":
            "projects/kms_project_id/locations/region/keyRings/ key_region/cryptoKeys/key /cryptoKeysVersions/version"
            If you do not provide an encryption key when creating the disk, then the disk is encrypted using an
            automatically generated key and you don't need to provide a key to use the disk later.
            Defaults to None.

                * raw_key(str, Optional):
                    Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt
                    or decrypt this resource. You can provide either the rawKey or the rsaEncryptedKey.
                    For example: \"raw_key\": \"SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0=\"

                * rsa_encrypted_key(str, Optional):
                    Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit customer-supplied encryption key to
                    either encrypt or decrypt this resource. You can provide either the rawKey or the rsaEncryptedKey.
                    For example:
                        \"rsa_encrypted_key\":
                        \"ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/
                        NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEM
                        MoNUXMCZEIpg9Vtp9x2oe==\"
                    The key must meet the following requirements before you can provide it to Compute Engine:
                        1. The key is wrapped using a RSA public key certificate provided by Google.
                        2. After being wrapped, the key must be encoded in RFC 4648 base64 encoding.
                    Gets the RSA public key certificate provided by Google at:
                    https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem

                * kms_key_name(str, Optional):
                    The name of the encryption key that is stored in Google Cloud KMS.
                    For example:
                        \"kms_key_name\":
                        \"projects/kms_project_id/locations/region/keyRings/ key_region/cryptoKeys/key

                * kms_key_service_account(str, Optional):
                    The service account being used for the encryption request for the given KMS key. If absent,
                    the Compute Engine default service account is used. For example:
                        \"kms_key_service_account\":
                        \"name@project_id.iam.gserviceaccount.com/


        source_image_encryption_key(Dict[str, Any], Optional):
            The customer-supplied encryption key of the source image.
            Required if the source image is protected by a customer-supplied encryption key.
            Defaults to None.

                * raw_key(str, Optional)
                * rsa_encrypted_key(str, Optional)
                * kms_key_name(str, Optional)
                * kms_key_service_account(str, Optional)

        source_snapshot_encryption_key(Dict[str, Any], Optional):
            The customer-supplied encryption key of the source snapshot.
            Required if the source snapshot is protected by a customer-supplied encryption key.
            Defaults to None.

                * raw_key(str, Optional)
                * rsa_encrypted_key(str, Optional)
                * kms_key_name(str, Optional)
                * kms_key_service_account(str, Optional)

        labels(Dict[str, Dict[str, str]], Optional):
            Labels to apply to this disk. These can be later modified by the setLabels method.
            Defaults to None.

        label_fingerprint(str, Optional):
            A fingerprint for the labels being applied to this disk,
            which is essentially a hash of the labels set used for optimistic locking.
            The fingerprint is initially generated by Compute Engine and
            changes after every request to modify or update labels.
            You must always provide an up-to-date fingerprint hash in order to update or change labels,
            otherwise the request will fail with error 412 conditionNotMet.
            To see the latest fingerprint, make a get() request to retrieve a disk.
            Defaults to None.

        replica_zones(List[str], Optional):
            URLs of the zones where the disk should be replicated to. Only applicable for regional resources.
            Defaults to None.

        license_codes(List[str], Optional):
            Integer license codes indicating which licenses are attached to this disk.
            Defaults to None.

        physical_block_size_bytes(str, Optional):
            Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used.
            The currently supported size is 4096, other sizes may be added in the future.
            If an unsupported value is requested,
            the error message will list the supported values for the caller's project.
            Defaults to None.

        resource_policies(List[str], Optional):
            Resource policies applied to this disk for automatic snapshot creations.
            Defaults to None.

        source_disk(str, Optional):
            The source disk used to create this disk. You can provide this as a partial or full URL to the resource.
            For example, the following are valid values:
                - https://www.googleapis.com/compute/v1/projects/project/zones/zone /disks/disk
                - https://www.googleapis.com/compute/v1/projects/project/regions/region /disks/disk
                - projects/project/zones/zone/disks/disk
                - projects/project/regions/region/disks/disk
                - zones/zone/disks/disk
                - regions/region/disks/disk
                Defaults to None.

        provisioned_iops(str, Optional):
            Indicates how many IOPS to provision for the disk.
            This sets the number of I/O operations per second that the disk can handle.
            Values must be between 10,000 and 120,000. For more details, see the Extreme persistent disk documentation.
            Defaults to None.

        location_hint(str, Optional):
            An opaque location hint used to place the disk close to other resources.
            This field is for use by internal tools that use the public API.
            Defaults to None.

        architecture(str, Optional):
            The architecture of the disk. Valid values are ARM64 or X86_64.
            Defaults to None.

        params(Dict[str, Dict[str, str]], Optional):
            Input only. [Input Only] Additional params passed with the request,
            but not persisted as part of resource payload.
            Defaults to None.

                * resourceManagerTags(Dict[str, str], Optional):
                    Resource manager tags to be bound to the disk. Tag keys and values have the same definition as
                    resource manager tags. Keys must be in the format `tagKeys/{tag_key_id}`, and values are in the format
                    `tagValues/456`. The field is ignored (both PUT & PATCH) when empty.

        description(str, Optional):
            An optional description of this resource.
            Defaults to None.

    Returns:
        Dict[str, Any]

    Examples:
        .. code-block:: sls

            example_resource_name:
              gcp.compute.disk.present:
                - project: project-name
                - zone: us-central1-a
                - description: Description for example_resource_name
                - type: projects/project-name/zones/us-central1-a/diskTypes/pd-balanced
                - size_gb: 10
                - resource_policies:
                    - projects/project-name/regions/us-central1/resourcePolicies/default-schedule-1
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
        resource_id = (ctx.old_state or {}).get(
            "resource_id"
        ) or hub.tool.gcp.resource_prop_utils.construct_resource_id(
            "compute.disk", {**locals(), "disk": name}
        )

    if ctx.get("rerun_data"):
        handle_operation_ret = await hub.tool.gcp.operation_utils.handle_operation(
            ctx, ctx.get("rerun_data"), "compute.disk"
        )

        if not handle_operation_ret["result"]:
            result["result"] = False
            result["comment"] += handle_operation_ret["comment"]
            result["rerun_data"] = handle_operation_ret["rerun_data"]
            return result

        resource_id = handle_operation_ret["resource_id"]

    if resource_id:
        old_get_ret = await hub.exec.gcp.compute.disk.get(
            ctx, name=name, resource_id=resource_id
        )

        if not old_get_ret["result"]:
            # error other than non-existing resource
            result["result"] = False
            result["comment"] += old_get_ret["comment"]
            return result
        if old_get_ret["ret"]:
            # copy.copy(old_get_ret['ret']) is needed to convert any objects of type NamespaceDict to dict
            # in old_get_ret['ret']. This is done so that comparisons with the plan_state which has
            # objects of type dict works properly
            result["old_state"] = copy.deepcopy(copy.copy(old_get_ret["ret"]))
            zone = hub.tool.gcp.resource_prop_utils.parse_link_to_zone(
                result["old_state"]["zone"]
            )
            result["old_state"]["zone"] = zone

            # If rerun_data is set at this point this means that there has been a completed create or update operation
            # so there is no need to run the code for create or update below again, and we stop here
            if ctx.get("rerun_data"):
                result["new_state"] = result["old_state"]
                return result

    # to be autogenerated by pop-create based on insert/update props in properties.yaml
    resource_body = {
        "type": type,
        "name": name,
        "source_image": source_image,
        "label_fingerprint": label_fingerprint,
        "architecture": architecture,
        "guest_os_features": guest_os_features,
        "source_disk": source_disk,
        "resource_policies": resource_policies,
        "options": options,
        "source_storage_object": source_storage_object,
        "licenses": licenses,
        "size_gb": size_gb,
        "license_codes": license_codes,
        "source_snapshot_encryption_key": source_snapshot_encryption_key,
        "zone": zone,
        "source_image_encryption_key": source_image_encryption_key,
        "physical_block_size_bytes": physical_block_size_bytes,
        "source_snapshot": source_snapshot,
        "description": description,
        "labels": labels,
        "params": params,
        "replica_zones": replica_zones,
        "location_hint": location_hint,
        "disk_encryption_key": disk_encryption_key,
        "provisioned_iops": provisioned_iops,
    }

    # TODO: How to handle query params which are not returned in the response body of get
    plan_state = {"resource_id": resource_id, **resource_body}

    plan_state = {k: v for (k, v) in plan_state.items() if v is not None}
    operation = None
    if result["old_state"]:
        # Resize
        size_gb_updated = False
        if size_gb is not None and str(result["old_state"]["size_gb"]) != str(size_gb):
            if not ctx.get("test"):
                resize_body = {"size_gb": size_gb}
                update_ret = await hub.exec.gcp_api.client.compute.disk.resize(
                    ctx,
                    resource_id=resource_id,
                    body=resize_body,
                    request_id=request_id,
                )

                if not update_ret["result"]:
                    result["result"] = False
                    result["comment"] += update_ret["comment"]
                    return result

                if "compute#operation" in update_ret["ret"].get("kind"):
                    operation = update_ret["ret"]
                    operation_id = (
                        hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
                            operation.get("selfLink"), "compute.zone_operation"
                        )
                    )
                    op_ret = await hub.tool.gcp.operation_utils.handle_operation(
                        ctx, operation_id, "compute.disk", True
                    )
                    if not op_ret["result"]:
                        result["result"] = False
                        result["comment"] += op_ret["comment"]
                        result["rerun_data"] = op_ret["rerun_data"]
                        return result

            size_gb_updated = True

        # Update labels
        labels_updated = False
        if (
            labels is not None
            and not (labels == {} and result["old_state"].get("labels") is None)
            and result["old_state"].get("labels") != labels
        ):
            if not ctx.get("test"):
                set_labels_body = {
                    "labels": labels,
                    "label_fingerprint": label_fingerprint,
                }
                update_ret = await hub.exec.gcp_api.client.compute.disk.setLabels(
                    ctx,
                    project=project,
                    zone=zone,
                    resource=name,
                    body=set_labels_body,
                    request_id=request_id,
                )

                if not update_ret["result"]:
                    result["result"] = False
                    result["comment"] += update_ret["comment"]
                    return result

                if "compute#operation" in update_ret["ret"].get("kind"):
                    operation = update_ret["ret"]
                    operation_id = (
                        hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
                            operation.get("selfLink"), "compute.zone_operation"
                        )
                    )
                    op_ret = await hub.tool.gcp.operation_utils.handle_operation(
                        ctx, operation_id, "compute.disk", True
                    )
                    if not op_ret["result"]:
                        result["result"] = False
                        result["comment"] += op_ret["comment"]
                        result["rerun_data"] = op_ret["rerun_data"]
                        return result

            labels_updated = True

        # Update resource policies
        resource_policies_updated = False
        if not hub.tool.gcp.state_comparison_utils.are_lists_identical(
            result["old_state"].get("resource_policies"), resource_policies
        ):
            # If (some) resource policies are links, parse them to resource policy resource ids
            new_resource_policies = [
                hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
                    policy, "compute.resource_policy"
                )
                for policy in (
                    resource_policies if resource_policies is not None else []
                )
            ]
            current_resource_policies = [
                hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
                    policy, "compute.resource_policy"
                )
                for policy in result["old_state"].get("resource_policies", [])
            ]

            resource_policies_to_remove = [
                policy
                for policy in current_resource_policies
                if policy not in new_resource_policies
            ]
            resource_policies_to_add = [
                policy
                for policy in new_resource_policies
                if policy not in current_resource_policies
            ]

            if (
                len(resource_policies_to_remove) > 0
                or len(resource_policies_to_add) > 0
            ):
                if not ctx.get("test"):
                    add_request_body = None
                    if len(resource_policies_to_add) > 0:
                        add_request_body = {
                            "resource_policies": resource_policies_to_add
                        }
                    remove_request_body = None
                    if len(resource_policies_to_remove) > 0:
                        remove_request_body = {
                            "resource_policies": resource_policies_to_remove
                        }

                    remove_ret = None
                    if remove_request_body is not None:
                        remove_ret = await hub.exec.gcp_api.client.compute.disk.removeResourcePolicies(
                            ctx,
                            resource_id=resource_id,
                            body=remove_request_body,
                            request_id=request_id,
                        )

                        if not remove_ret["result"]:
                            result["result"] = False
                            result["comment"] += remove_ret["comment"]
                            return result

                        if "compute#operation" in remove_ret["ret"].get("kind"):
                            operation = remove_ret["ret"]
                            operation_id = hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
                                operation.get("selfLink"), "compute.zone_operation"
                            )
                            op_ret = (
                                await hub.tool.gcp.operation_utils.handle_operation(
                                    ctx, operation_id, "compute.disk", True
                                )
                            )
                            if not op_ret["result"]:
                                result["result"] = False
                                result["comment"] += op_ret["comment"]
                                result["rerun_data"] = op_ret["rerun_data"]
                                return result

                    if (
                        remove_ret is None or remove_ret["result"]
                    ) and add_request_body is not None:
                        add_ret = await hub.exec.gcp_api.client.compute.disk.addResourcePolicies(
                            ctx,
                            resource_id=resource_id,
                            body=add_request_body,
                            request_id=request_id,
                        )

                        if not add_ret["result"]:
                            result["result"] = False
                            result["comment"] += add_ret["comment"]
                            return result

                        if "compute#operation" in add_ret["ret"].get("kind"):
                            operation = add_ret["ret"]
                            operation_id = hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
                                operation.get("selfLink"), "compute.zone_operation"
                            )
                            op_ret = (
                                await hub.tool.gcp.operation_utils.handle_operation(
                                    ctx, operation_id, "compute.disk", True
                                )
                            )
                            if not op_ret["result"]:
                                result["result"] = False
                                result["comment"] += op_ret["comment"]
                                result["rerun_data"] = op_ret["rerun_data"]
                                return result

                resource_policies_updated = True

        # Reset the operation because we don't need it
        # since we are waiting for the operations to finish in order to proceed
        operation = None
        resource_updated = (
            size_gb_updated or labels_updated or resource_policies_updated
        )
        if resource_updated:
            if ctx.get("test", False):
                result["comment"].append(
                    hub.tool.gcp.comment_utils.would_update_comment(
                        "gcp.compute.disk", name
                    )
                )
            else:
                result["comment"].append(
                    hub.tool.gcp.comment_utils.update_comment("gcp.compute.disk", name)
                )
        else:
            result["comment"].append(
                hub.tool.gcp.comment_utils.already_exists_comment(
                    "gcp.compute.disk", name
                )
            )
    else:
        if ctx["test"]:
            result["comment"].append(
                hub.tool.gcp.comment_utils.would_create_comment(
                    "gcp.compute.disk", name
                )
            )
            result["new_state"] = plan_state
            result["new_state"]["resource_id"] = resource_id
            return result

        # Create
        create_ret = await hub.exec.gcp_api.client.compute.disk.insert(
            ctx, name=name, project=project, zone=zone, body=resource_body
        )
        if not create_ret["result"]:
            result["result"] = False
            result["comment"] += create_ret["comment"]
        else:
            result["comment"].append(
                hub.tool.gcp.comment_utils.create_comment("gcp.compute.disk", name)
            )
            resource_id = create_ret["ret"].get("resource_id")
        if create_ret["ret"] is not None:
            if "compute#operation" in create_ret["ret"].get("kind"):
                operation = create_ret["ret"]

    if operation:
        operation_id = hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
            operation.get("selfLink"), "compute.zone_operation"
        )
        handle_operation_ret = await hub.tool.gcp.operation_utils.handle_operation(
            ctx, operation_id, "compute.disk"
        )

        if not handle_operation_ret["result"]:
            result["result"] = False
            result["comment"] += handle_operation_ret["comment"]
            result["rerun_data"] = handle_operation_ret["rerun_data"]
            return result

        resource_id = handle_operation_ret["resource_id"]

    # Try getting the resource again
    # TODO: Check if this can be removed because insert and update may also return the necessary data on success
    get_ret = await hub.exec.gcp.compute.disk.get(
        ctx, name=name, resource_id=resource_id
    )

    if not get_ret["result"] or not get_ret["ret"]:
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
    r"""Deletes the specified persistent disk.

    Deleting a disk removes its data permanently and is irreversible.
    However, deleting a disk does not delete any snapshots previously made from the disk.
    You must separately delete snapshots.

    Args:
        name(str):
            An Idem name of the resource.

        resource_id(str, Optional):
            An identifier of the resource in the provider.
            Defaults to None.

        request_id(str, Optional):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must retry your request,
            the server will know to ignore the request if it has already been completed.
            For example, consider a situation where you make an initial request and the request times out.
            If you make the request again with the same request ID,
            the server can check if original operation with the same request ID was received, and if so,
            will ignore the second request. This prevents clients from accidentally creating duplicate commitments.
            The request ID must be a valid UUID with the exception that zero UUID is not supported
            ( 00000000-0000-0000-0000-000000000000).
            Defaults to None.

    Returns:
        Dict[str, Any]

    Examples:
        .. code-block:: sls

            resource_is_absent:
              gcp.compute.disk.absent:
                - resource_id: resource_id
    """
    result = {
        "result": True,
        "old_state": ctx.get("old_state"),
        "new_state": None,
        "name": name,
        "comment": [],
    }

    resource_id = resource_id or (ctx.old_state or {}).get("resource_id")
    if not resource_id:
        result["comment"].append(
            hub.tool.gcp.comment_utils.already_absent_comment("gcp.compute.disk", name)
        )
        return result

    if not ctx.get("rerun_data"):
        get_ret = await hub.exec.gcp.compute.disk.get(ctx, resource_id=resource_id)

        if not get_ret["result"]:
            result["result"] = False
            result["comment"] += get_ret["comment"]
            return result

        if not get_ret["ret"]:
            result["comment"].append(
                hub.tool.gcp.comment_utils.already_absent_comment(
                    "gcp.compute.disk", name
                )
            )
            return result

        result["old_state"] = get_ret["ret"]

    if ctx["test"]:
        result["comment"].append(
            hub.tool.gcp.comment_utils.would_delete_comment("gcp.compute.disk", name)
        )
        return result

    if not ctx.get("rerun_data"):
        # First iteration; invoke disk's delete()
        delete_ret = await hub.exec.gcp_api.client.compute.disk.delete(
            ctx, resource_id=resource_id
        )
        if delete_ret["ret"]:
            if "compute#operation" in delete_ret["ret"].get("kind"):
                result["result"] = False
                result["comment"] += delete_ret["comment"]
                result[
                    "rerun_data"
                ] = hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
                    delete_ret["ret"].get("selfLink"), "compute.zone_operation"
                )
                return result
    else:
        # delete() has been called on some previous iteration
        handle_operation_ret = await hub.tool.gcp.operation_utils.handle_operation(
            ctx, ctx.get("rerun_data"), "compute.disk"
        )
        if not handle_operation_ret["result"]:
            result["result"] = False
            result["comment"] += handle_operation_ret["comment"]
            result["rerun_data"] = handle_operation_ret["rerun_data"]
            return result

    result["comment"].append(
        hub.tool.gcp.comment_utils.delete_comment("gcp.compute.disk", name)
    )
    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    r"""Describe the resource in a way that can be recreated/managed with the corresponding "present" function.

    Retrieves a list of persistent disks contained within the specified zone.

    Returns:
        Dict[str, Any]

    Examples:
        .. code-block:: bash

            $ idem describe gcp.compute.disk
    """
    result = {}

    describe_ret = await hub.exec.gcp.compute.disk.list(
        ctx, project=ctx.acct.project_id
    )

    if not describe_ret["result"]:
        hub.log.debug(f"Could not describe disks {describe_ret['comment']}")
        return {}

    for resource in describe_ret["ret"]:
        resource_id = resource.get("resource_id")
        result[resource_id] = {
            "gcp.compute.disk.present": [
                {parameter_key: parameter_value}
                for parameter_key, parameter_value in resource.items()
            ]
        }

    return result
