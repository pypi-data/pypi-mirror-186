import inspect
from collections import Counter
from fabrique_nodes_core.core import BaseNode  # noqa: F401


class NodeConfigException(Exception):
    pass


class UIParamsPortGroupsException(Exception):
    pass


class UIParamsCallbackException(Exception):
    pass


def validate_node(node: BaseNode) -> None:
    """Validate user defined node

    :param node: Your custom node
    :type node: BaseNode
    :raises NodeConfigException: error in config structure
    :raises UIParamsPortGroupsException: error in port groups
    :raises UIParamsCallbackException: error in UIParams
    """

    # validate portgroups length
    ui_ig = node.ui_params.input_groups
    ic_ig = node.initial_config.g_ports_in
    ui_og = node.ui_params.output_groups
    ic_og = node.initial_config.g_ports_out

    group_dict = {group_params.id_: group_params for groups in [ui_ig, ui_og] for group_params in groups}

    if len(ui_ig) != len(ic_ig):
        raise NodeConfigException('ui_params.input_groups and initial_config.g_ports_in must have same length')
    if len(ui_og) != len(ic_og):
        raise NodeConfigException('ui_params.output_groups and initial_config.g_ports_out must have same length')

    # validate uniqness of portgroup ids
    counts_pgroups = Counter(group_params.id_ for groups in [ui_ig, ui_og] for group_params in groups)
    most_common_id = counts_pgroups.most_common(1)[0]
    if most_common_id[1] > 1:
        raise UIParamsPortGroupsException(f'non unique "{most_common_id[0]}" group id!')

    # validate can_add cases
    addable_input_groups = sum(group_params.can_add for group_params in ui_ig)
    addable_output_groups = sum(group_params.can_add for group_params in ui_og)
    if addable_input_groups > 1:
        raise UIParamsPortGroupsException(f'only one group in inputs can add new ports, have {addable_input_groups}')
    if addable_output_groups > 1:
        raise UIParamsPortGroupsException(f'only one group in outputs can add new ports, have {addable_output_groups}')

    for id_, group_params in group_dict.items():
        if group_params.can_add and not group_params.can_delete:
            raise UIParamsPortGroupsException(
                f'if you are able to add a port to "{id_}", you should be able to delete it!'
            )

    # validate autocopy copy_from_group
    for cur_id_, group_params in group_dict.items():
        copy_from_id = group_params.copy_from_group
        if not copy_from_id:
            continue
        if copy_from_id not in group_dict:
            raise UIParamsPortGroupsException(
                f'can\'t copy ports from group "{copy_from_id}", no such id_ in port groups!'
            )
        if copy_from_id == cur_id_:
            raise UIParamsPortGroupsException(f'can\'t copy ports same group "{copy_from_id}"!')

    # validate callback presence
    for cur_id_, group_params in group_dict.items():
        copy_from_id = group_params.copy_from_group
        if not copy_from_id:
            continue
        if copy_from_id not in group_dict:
            raise UIParamsPortGroupsException(
                f'can\'t copy ports from group "{copy_from_id}", no such id_ in port groups!'
            )
        if copy_from_id == cur_id_:
            raise UIParamsPortGroupsException(f'can\'t copy ports same group "{cur_id_}"!')

    for cur_id_, group_params in group_dict.items():
        for cb_name in [group_params.code_validator_callback_name, group_params.node_updater_callback_name]:
            if not cb_name:
                continue
            if not hasattr(node, cb_name):
                raise UIParamsCallbackException(f'not found callback "{cb_name}" in "{cur_id_}"!')
            method = getattr(node, cb_name)
            if inspect.ismethod(method) and method.__self__ is node:
                continue
            raise UIParamsCallbackException(f'unsuported callback "{cb_name}", must be classmethod!')
