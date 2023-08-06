"""Utilities for Google Cloud Platform APIs.

Copyright (c) 2021-2022 VMware, Inc.
SPDX-License-Identifier: Apache-2.0
"""
import copy
import logging
from copy import deepcopy
from typing import Any
from typing import Dict

from deepdiff import DeepDiff

# Import plugin helpers

log = logging.getLogger(__name__)


def _is_empty(o) -> bool:
    return not isinstance(o, bool) and not o


def _is_within_dict(parent, o, ignore: set):
    """Determine of an object is within a parent dict object.

    :param parent: The object in which o hopefully exists.
    :param o: The object to find in parent.
    :param ignore: A set of keys to ignore in parent.
    return: True if o is within parent somewhere. False otherwise.
    """
    ret = True
    for k, v in o.items():
        if k in ignore:
            break
        elif k not in parent:
            # TODO: Handle pure default value cases.
            # Need to handle cases where the state spec provides a key
            # the value of which containes purely default values. Google APIs
            # responses do not present keys filled with default values.
            if not _is_empty(o[k]):
                ret = False
                break
        elif not _is_empty(o[k]) and _is_empty(parent[k]):
            ret = False
            break
        elif not _is_within(parent[k], v, ignore):
            ret = False
            break
    return ret


def _is_within_list(parent, o, ignore: set):
    """Determine of an object is within a parent list object.

    :param parent: The object in which o hopefully exists.
    :param o: The object to find in parent.
    :param ignore: A set of keys to ignore in parent.
    return: True if o is within parent somewhere. False otherwise.
    """
    ret = True
    plen = len(parent)

    if len(o) > len(parent):
        ret = False
    else:
        for oidx in range(len(o)):
            inner_ret = False
            for pidx in range(plen):
                if _is_within(parent[pidx], o[oidx], ignore):
                    inner_ret = True
                    break
            if not inner_ret:
                ret = inner_ret
                break

    return ret


def _is_within_set(parent, o, ignore: set):
    """Determine of an object is within a parent set object.

    :param parent: The object in which o hopefully exists.
    :param o: The object to find in parent.
    :param ignore: A set of keys to ignore in parent.
    return: True if o is within parent somewhere. False otherwise.
    """
    return _is_within_list(list(parent), list(o), ignore)


def _is_within(parent, o, ignore: set):
    """Determine of an object is within a parent object.

    :param parent: The object in which o hopefully exists.
    :param o: The object to find in parent.
    :param ignore: A set of keys to ignore in parent.
    return: True if o is within parent somewhere. False otherwise.
    """
    if not isinstance(parent, type(o)):
        return False
    elif isinstance(o, dict):
        return _is_within_dict(parent, o, ignore)
    elif isinstance(o, list):
        return _is_within_list(parent, o, ignore)
    elif isinstance(o, set):
        return _is_within_set(parent, o, ignore)
    elif isinstance(o, tuple):
        return _is_within_list(parent, o, ignore)
    elif isinstance(o, str):
        return o in parent
    else:
        return parent == o


def is_within(hub, parent, o, ignore: set = {}):
    """Returns True if the object (o) is contained within parent (top level) object.

    :param hub: The redistributed pop central hub. This is required in
    Idem, so while not used, must appear.
    :param parent: The object to check if contains o.
    :param o: An object to check if is within the parent object.
    :return: False if parent and o are different types or do not compare,
    otherwise True.

    For example:

    The subset:

    { name: "my_object" }

    exists within

    { something_else: "some other thing", name: "my_object" },
    """
    return _is_within(parent, o, ignore)


# TODO: Cover the merge logic with tests
def _merge_dicts(target: Dict, source: Dict) -> Dict:
    if not source:
        return target
    new_target: Dict = {}
    for key in source:
        if key not in target or not isinstance(target[key], dict):
            new_target[key] = deepcopy(source[key])
        else:
            new_target[key] = _merge_dicts(target[key], source[key])
    return new_target


def merge_dicts(hub, target: dict, source: dict) -> dict:
    """Returns the dict resulting from overwriting values within a source dict into a target dict, recursively.

    All values within a key from the source
    will overwrite the same within the target. For example, consider the
    following merged result:

       source = { 'text': ["this", "is", "my_object"] }
       target = { 'text': ["not', "this" "time"], 'place': "elsewhere" }

       merged = { 'text': ["this", "is", "my_object" ], 'place': "elsewhere" }

    :param hub: The redistributed pop central hub. This is required in
    Idem, so while not used, must appear.
    :param target: The dict into which to merge the source.
    :param source: The dict from which to merge into the target.
    :return: dict as merged.
    """
    result = copy.deepcopy(target)
    return _merge_dicts(result, source)


def compare_states(
    hub, old_state: Dict, plan_state: Dict, resource_type: str = None
) -> Dict:
    exclude_paths = []

    for key in old_state.keys():
        if key not in plan_state:
            exclude_paths.append(f"root['{key}']")

    if resource_type:
        paths = hub.tool.gcp.resource_prop_utils.get_exclude_paths(resource_type)
        for path in paths:
            s = "root"
            for part in path.split("."):
                if part.endswith("[]"):
                    s += f"\\['{part[:-2]}'\\]\\[\\d+\\]"
                else:
                    s += f"\\['{part}'\\]"
            exclude_paths.append(s)

    changes = DeepDiff(old_state, plan_state, exclude_regex_paths=exclude_paths)

    # If an item is in old_state but not in plan_state, i.e. changes.get("dictionary_item_removed") is not None,
    # we can ignore this change

    # TODO: changes.get("dictionary_item_removed") also includes nested items, which means deleted nested items
    #  are ignored. Ignore only root items and read-only nested items
    if (
        not changes.get("dictionary_item_added")
        and not changes.get("iterable_item_added")
        and not changes.get("iterable_item_removed")
        and not changes.get("values_changed")
    ):
        return {}

    return changes


def get_project_from_account(ctx: dict, project: str) -> str:
    """If project is explicitly passed by the user, this project will be returned.
    If project is empty, this method will return gcp account default project
    :param ctx: A dict with the keys/values for the execution of the Idem run
    located in `hub.idem.RUNS[ctx['run_name']]`.
    :param project: A string explicitly passed by the user.
    :return: the correct project
    """
    if not project:
        project = ctx.acct.project_id
    return project


# TODO: Enhance this method to work for multi dictionary layers as opposed to now working with only the top one.
def create_dict_body_on_top_of_old(
    hub, ctx, old: Dict[str, Any], new: Dict[str, Any]
) -> Dict[str, Any]:
    result = copy.deepcopy(old)
    for key, value in new.items():
        if value is not None and value != old.get(key):
            result[key] = value

    return result
