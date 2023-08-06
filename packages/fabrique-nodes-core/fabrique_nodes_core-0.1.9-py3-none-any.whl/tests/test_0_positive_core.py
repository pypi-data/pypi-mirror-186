import os
import sys
import pickle
# noinspection PyPackageRequirements

cur_file_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = f'{cur_file_dir}/../fabrique_nodes_core'
sys.path.append(lib_dir)
os.chdir(cur_file_dir)

import tests.import_spoofer  # noqa: F401

from fabrique_nodes_core import BaseNode, UIParams, UIPortGroupParams, NodeData

expected_UIPortGroupParams = {
    'id_': '',
    'show_ports': True,
    'can_add': False,
    'can_delete': False,
    'can_move': False,
    'can_hide': False,
    'can_set_type': True,
    'has_code': False,
    'has_special': False,
    'has_required': False,
    'copy_name_from_code': True,
    'group_title': None,
    'special_title': None,
    'code_title': None,
    'copy_from_group': None,
    'code_validator_callback_name': None,
    'node_updater_callback_name': None,
    'valid_types': []
}


def test_def_ui():
    assert UIPortGroupParams().dict() == expected_UIPortGroupParams


def test_base_node():
    assert pickle.dumps(BaseNode.initial_config) == pickle.dumps(NodeData())
    assert hasattr(BaseNode, 'type_')
    assert BaseNode.ui_params == UIParams()
