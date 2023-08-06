# TODO: How to handle corner cases like abcXYZ ?
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Set


# TODO: make this work with the JSON schemas so that we can handles cases such as abcXYZ
def convert_raw_resource_to_present(
    hub,
    raw_resource: Dict[str, Any],
    resource_type_name: str = None,
    exclude_properties_from_transformation: List[str] = None,
) -> Dict[str, Any]:
    return _convert_resource(
        raw_resource,
        hub.tool.gcp.case.snake,
        resource_type_name,
        exclude_properties_from_transformation,
    )


def convert_present_resource_to_raw(
    hub,
    present_resource: Dict[str, Any],
    resource_type_name: str = None,
    exclude_properties_from_transformation: List[str] = None,
) -> Dict[str, Any]:
    return _convert_resource(
        present_resource,
        hub.tool.gcp.case.camel,
        resource_type_name,
        exclude_properties_from_transformation,
    )


def _convert_resource(
    resource,
    key_transformer: Callable[[Any], Any],
    resource_type_name: str = None,
    exclude_properties_from_transformation: List[str] = None,
):
    if resource is None:
        return None

    if exclude_properties_from_transformation is None:
        exclude_properties_from_transformation = []

    if isinstance(resource, list):
        return list(
            _convert_resource(
                v,
                key_transformer,
                resource_type_name,
                exclude_properties_from_transformation,
            )
            for v in resource
        )
    elif isinstance(resource, set):
        return {
            _convert_resource(
                v,
                key_transformer,
                resource_type_name,
                exclude_properties_from_transformation,
            )
            for v in resource
        }
    elif isinstance(resource, dict):
        return {
            k
            if k in exclude_properties_from_transformation
            else key_transformer(k): _convert_resource(
                v,
                key_transformer,
                resource_type_name,
                exclude_properties_from_transformation,
            )
            for k, v in resource.items()
        }
    else:
        return resource


def convert_raw_properties_to_present(
    hub, raw_properties: Set, resource_type_name: str = None
) -> Set:
    if not raw_properties:
        return set()

    properties_translated = set()

    for value in raw_properties:
        properties_translated.add(hub.tool.gcp.case.snake(value))

    return properties_translated


def convert_present_properties_to_raw(
    hub, present_properties: Set, resource_type_name: str = None
) -> Set:
    if not present_properties:
        return set()

    properties_translated = set()

    for value in present_properties:
        properties_translated.add(hub.tool.gcp.case.camel(value))

    return properties_translated
