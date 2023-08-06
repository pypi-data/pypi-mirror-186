import copy
import re
from typing import Any
from typing import Dict
from typing import List
from typing import Set

import yaml
from deepdiff import DeepDiff
from importlib_resources import files


def __init__(hub):
    file_text = (
        files("idem_gcp.resources")
        .joinpath("properties.yaml")
        .read_text(encoding="utf-8")
    )

    # TODO: Maybe convert the properties names in hub.tool.gcp.RESOURCE_PROPS
    #  to snake case here so that we do not have to do conversion
    #  very often anywhere these snake case properties names are needed.
    #  Check if hub.tool.gcp.RESOURCE_PROPS are always convert to snake case

    hub.tool.gcp.RESOURCE_PROPS = yaml.safe_load(file_text)


def get_create_properties(hub, resource_type: str, convert_to_present=True) -> Set:
    resource_methods_properties = hub.tool.gcp.RESOURCE_PROPS[resource_type]
    raw_props = set(
        resource_methods_properties.get("insert", {})
        or resource_methods_properties.get("create", {})
    )
    if raw_props and convert_to_present:
        return hub.tool.gcp.conversion_utils.convert_raw_properties_to_present(
            raw_props
        )
    return raw_props


def get_update_properties(hub, resource_type: str, convert_to_present=True) -> Set:
    raw_props = set(hub.tool.gcp.RESOURCE_PROPS[resource_type].get("update", {}))
    if convert_to_present:
        return hub.tool.gcp.conversion_utils.convert_raw_properties_to_present(
            raw_props
        )
    return raw_props


def get_fields_of_enum_type(hub, resource_type: str, convert_to_present=True) -> Set:
    raw_props = set(
        hub.tool.gcp.RESOURCE_PROPS[resource_type].get("fields_enum_type", {})
    )
    if convert_to_present:
        return hub.tool.gcp.conversion_utils.convert_raw_properties_to_present(
            raw_props
        )
    return raw_props


def get_get_properties(hub, resource_type: str, convert_to_present=True) -> Set:
    raw_props = set(hub.tool.gcp.RESOURCE_PROPS[resource_type].get("get", {}))
    if convert_to_present:
        return hub.tool.gcp.conversion_utils.convert_raw_properties_to_present(
            raw_props
        )
    return raw_props


def get_delete_properties(hub, resource_type: str, convert_to_present=True) -> Set:
    raw_props = set(hub.tool.gcp.RESOURCE_PROPS[resource_type].get("delete", {}))
    if convert_to_present:
        return hub.tool.gcp.conversion_utils.convert_raw_properties_to_present(
            raw_props
        )
    return raw_props


def get_non_updatable_properties(hub, resource_type: str) -> Set:
    raw_nested_non_updatable_properties = hub.tool.gcp.RESOURCE_PROPS[
        resource_type
    ].get("nested_non_updatable_properties", [])

    non_updatable_properties = set(
        hub.tool.gcp.conversion_utils.convert_raw_properties_to_present(
            raw_nested_non_updatable_properties
        )
    )

    non_updatable_properties.update(
        hub.tool.gcp.resource_prop_utils.get_create_properties(resource_type)
        - hub.tool.gcp.resource_prop_utils.get_update_properties(resource_type)
    )
    return non_updatable_properties


def get_changed_non_updatable_properties(
    hub, resource_type: str, changes: DeepDiff
) -> Set:
    non_updatable_properties = (
        hub.tool.gcp.resource_prop_utils.get_non_updatable_properties(resource_type)
    )

    changed_non_updatable_properties = set()
    for changed_property_full_path in changes.affected_paths:
        # This formats changed_property_full_path from e.g. "root['network_interfaces'][0]['alias_ip_ranges']"
        # to "network_interfaces[].alias_ip_ranges"
        changed_property_path_elements = re.findall(
            r"(?<=\[).*?(?=\])", changed_property_full_path
        )
        formatted_path_elements = []
        for i in range(len(changed_property_path_elements)):
            if changed_property_path_elements[i].isdigit():
                formatted_path_elements.append("[]")
            else:
                if i > 0:
                    formatted_path_elements.append(".")
                formatted_path_elements.append(
                    changed_property_path_elements[i].strip("'")
                )
        formatted_property_path = "".join(formatted_path_elements)
        for non_updatable_property_path in non_updatable_properties:
            if non_updatable_property_path in formatted_property_path:
                changed_non_updatable_properties.add(non_updatable_property_path)
                break

    return changed_non_updatable_properties


def get_present_properties(hub, resource_type: str) -> Set:
    return (
        hub.tool.gcp.resource_prop_utils.get_create_properties(resource_type, False)
        .union(
            hub.tool.gcp.resource_prop_utils.get_update_properties(resource_type, False)
        )
        .union(
            hub.tool.gcp.resource_prop_utils.get_fields_of_enum_type(
                resource_type, False
            )
        )
    )


def get_exclude_paths(hub, resource_type: str) -> Set:
    raw_props_names = hub.tool.gcp.RESOURCE_PROPS[resource_type].get(
        "exclude_paths", []
    )
    return set(
        hub.tool.gcp.conversion_utils.convert_raw_properties_to_present(raw_props_names)
    )


def get_exclude_properties_from_transformation(
    hub, resource_type: str, convert_to_present=True
) -> Set:
    resource_methods_properties = hub.tool.gcp.RESOURCE_PROPS[resource_type]
    raw_props = set(
        resource_methods_properties.get("exclude_properties_from_transformation", {})
    )
    if raw_props and convert_to_present:
        return hub.tool.gcp.conversion_utils.convert_raw_properties_to_present(
            raw_props
        )
    return raw_props


def get_exclude_keys_from_transformation(
    hub, resource_body: Dict[str, Any], resource_type: str = None
) -> List[str]:
    # Get the properties whose keys should be excluded from transformation
    exclude_properties_from_transformation = (
        hub.tool.gcp.resource_prop_utils.get_exclude_properties_from_transformation(
            resource_type
        )
    )

    # Create a list, which has lists per each property and have the properties' keys as items
    list_of_properties_key_lists = [
        list(resource_body[item].keys()) if resource_body.get(item, False) else []
        for item in exclude_properties_from_transformation
    ]

    # Map the list_of_properties_key_lists to a list containing only the keys to be excluded
    exclude_keys_from_transformation = []
    for _list in list_of_properties_key_lists:
        exclude_keys_from_transformation += _list

    return exclude_keys_from_transformation


def extract_resource_id(hub, input_props: Dict, resource_type: str) -> Dict:
    if "selfLink" in input_props:
        return hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
            input_props.get("selfLink"), resource_type
        )

    if "resource_id" in hub.tool.gcp.RESOURCE_PROPS[resource_type]:
        resource_id_fields = hub.tool.gcp.RESOURCE_PROPS[resource_type]["resource_id"]
        for resource_id_field in resource_id_fields:
            if resource_id_field in input_props:
                return input_props[resource_id_field]


def get_resource_path(hub, resource_type: str) -> str:
    resource_path = resource_type.split(".")
    hub_ref = hub.metadata.gcp
    for resource_path_segment in resource_path:
        hub_ref = hub_ref[resource_path_segment]

    return hub_ref["PATH"]


def get_resource_id_property_name(hub, resource_type: str, method_name: str) -> str:
    resource_id_props = hub.tool.gcp.RESOURCE_PROPS[resource_type]["resource_id"]
    method_properties = {}
    if method_name == "get":
        method_properties = hub.tool.gcp.resource_prop_utils.get_get_properties(
            resource_type
        )
    elif method_name == "insert" or method_name == "create":
        method_properties = hub.tool.gcp.resource_prop_utils.get_create_properties(
            resource_type
        )
    elif method_name == "update":
        method_properties = hub.tool.gcp.resource_prop_utils.get_update_properties(
            resource_type
        )
    elif method_name == "delete":
        method_properties = hub.tool.gcp.resource_prop_utils.get_delete_properties(
            resource_type
        )

    for resource_id_prop in resource_id_props:
        if resource_id_prop in method_properties:
            return resource_id_prop

    return ""


def get_elements_from_resource_id(hub, resource_type: str, resource_id: str) -> Dict:
    resource_path = hub.tool.gcp.resource_prop_utils.get_resource_path(resource_type)
    src = resource_path.split("/")
    act = resource_id.split("/")
    result = {}

    if len(act) < len(src):
        hub.log.warning(
            hub.tool.gcp.comment_utils.ill_formed_resource_id_comment(
                resource_type, resource_id, "insufficient number of segments."
            )
        )
        return {}

    idx = -1
    for s in reversed(src):
        val = act[idx]
        if s.startswith("{") and s.endswith("}"):
            key = s[1:-1]
            result[key] = val
        elif val != s:
            hub.log.warning(
                hub.tool.gcp.comment_utils.ill_formed_resource_id_comment(
                    resource_type, resource_id, "segment names do not match."
                )
            )
            return {}
        idx -= 1

    return result


def parse_link_to_resource_id(hub, link, resource_type: str):
    resource_path = hub.tool.gcp.resource_prop_utils.get_resource_path(resource_type)
    result = copy.deepcopy(resource_path)
    src = result.split("/")
    act = link.split("/")

    if len(act) < len(src):
        return None

    idx = -1
    for s in reversed(src):
        val = act[idx]
        if s.startswith("{") and s.endswith("}"):
            result = result.replace(s, val)
        elif val != s:
            hub.log.warning(
                f"Resource selfLink differs from the actual path for resource type: {resource_type}"
                f"\nselfLink: {link}, PATH: {resource_path}"
            )
            return None
        idx -= 1

    return result


def construct_resource_id(hub, resource_type: str, input_props: Dict[str, Any]) -> str:
    if input_props is not None and input_props.get("name") is not None:
        # handle case where "name" contains full resource id
        name = input_props.get("name")
        if (
            hub.tool.gcp.resource_prop_utils.parse_link_to_resource_id(
                name, resource_type
            )
            is not None
        ):
            return name

    resource_path = hub.tool.gcp.resource_prop_utils.get_resource_path(resource_type)
    try:
        filtered_without_none_properties = {
            k: v for k, v in input_props.items() if v is not None
        }
        return resource_path.format(**filtered_without_none_properties)
    except:
        # a required input prop is missing or input_props is invalid format
        return None


def parse_link_to_zone(hub, link: str) -> str:
    return link.split("/")[-1]


def get_path_parameters(hub, resource_type):
    resource_path = hub.tool.gcp.resource_prop_utils.get_resource_path(resource_type)
    src = resource_path.split("/")
    result = set()

    for s in src:
        if s.startswith("{") and s.endswith("}"):
            result.add(s[1:-1])

    return result


def format_path_params(hub, resource, resource_type):
    resource_copy = copy.deepcopy(resource)
    path_params = hub.tool.gcp.resource_prop_utils.get_path_parameters(resource_type)
    for path_el in path_params:
        if resource_copy.get(path_el):
            resource_copy[path_el] = resource_copy[path_el].split("/")[-1]

    return resource_copy


# TODO: Remove this logic once we have all the nested properties defined for a method
def are_properties_allowed_for_update(hub, resource_type, request_body):
    can_update = True
    if resource_type == "compute.instance":
        for disk in request_body.get("disks" or {}):
            if disk.get("initialize_params"):
                can_update = False

    return can_update


def resource_type_matches(hub, resource_id: str, resource_type: str) -> bool:
    resource_path = hub.tool.gcp.resource_prop_utils.get_resource_path(resource_type)
    rpath = resource_path.split("/")
    rid = resource_id.split("/")

    if len(rid) < len(rpath):
        return False

    idx = -1
    for s in reversed(rpath):
        if not (s.startswith("{") and s.endswith("}")) and rid[idx] != s:
            return False
        idx -= 1

    return True
