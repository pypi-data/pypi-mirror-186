def create_comment(hub, resource_type: str, name: str) -> str:
    return f"Created {resource_type} '{name}'"


def would_create_comment(hub, resource_type: str, name: str) -> str:
    return f"Would create {resource_type} '{name}'"


def update_comment(hub, resource_type: str, name: str) -> str:
    return f"Updated {resource_type} '{name}'"


def would_update_comment(hub, resource_type: str, name: str) -> str:
    return f"Would update {resource_type} '{name}'"


def no_resource_delete_comment(hub, resource_type: str) -> str:
    return f"Delete operation for resource type {resource_type} is not supported."


def no_resource_create_update_comment(hub, resource_type: str) -> str:
    return f"Create and update operations for resource type {resource_type} are not supported."


def delete_comment(hub, resource_type: str, name: str) -> str:
    return f"Deleted {resource_type} '{name}'"


def would_delete_comment(hub, resource_type: str, name: str) -> str:
    return f"Would delete {resource_type} '{name}'"


def already_absent_comment(hub, resource_type: str, name: str) -> str:
    return f"{resource_type} '{name}' already absent"


def already_exists_comment(hub, resource_type: str, name: str) -> str:
    return f"{resource_type} '{name}' already exists."


def update_tags_comment(hub, tags_to_remove, tags_to_add) -> str:
    return f"Update tags: Add keys {tags_to_add.keys()} Remove keys {tags_to_remove.keys()}"


def would_update_tags_comment(hub, tags_to_remove, tags_to_add) -> str:
    return f"Would update tags: Add keys {tags_to_add.keys()} Remove keys {tags_to_remove.keys()}"


def get_empty_comment(hub, resource_type: str, name: str) -> str:
    return f"Get {resource_type} '{name}' result is empty"


def list_empty_comment(hub, resource_type: str, name: str) -> str:
    return f"List {resource_type} '{name}' result is empty"


def find_more_than_one(hub, resource_type: str, resource_id: str) -> str:
    return (
        f"More than one {resource_type} resource was found. Use resource {resource_id}"
    )


def non_updatable_properties_comment(
    hub, resource_type: str, name: str, non_updatable_properties: set
) -> str:
    sorted_props = list(non_updatable_properties)
    sorted_props.sort()
    return f"Forbidden modification of non-updatable properties: {str(sorted_props)} for {resource_type} '{name}'"


def no_resource_update_comment(hub, resource_type: str, resource_id: str) -> str:
    return f"Update operation for resource type {resource_type} is not supported for {resource_id}."


def ill_formed_resource_id_comment(
    hub, resource_type: str, resource_id: str, reason: str
) -> str:
    return f"Ill-formed {resource_type} resource ID '{resource_id}': {reason}"
