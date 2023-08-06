import os
import sys
import pytest
# noinspection PyPackageRequirements

cur_file_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = f'{cur_file_dir}/../fabrique_nodes_core'
sys.path.append(lib_dir)
os.chdir(cur_file_dir)

import tests.import_spoofer as import_spoofer  # noqa: F401

import tests.nodes_for_tests as nt
from fabrique_nodes_core.validators import (validate_node, NodeConfigException, UIParamsCallbackException,
                                            UIParamsPortGroupsException)


def test_positive_validations():
    validate_node(nt.BaseNode)
    validate_node(nt.A2E_Node)
    validate_node(nt.FilterNode)
    validate_node(nt.IfElseNode)
    validate_node(nt.FunctionNode)


def test_negative_validations():
    with pytest.raises(NodeConfigException, match='must have same length'):
        validate_node(nt.IfElseWithMismatchPorts)

    with pytest.raises(UIParamsPortGroupsException, match='non unique'):
        validate_node(nt.FunctionWithNonUniquePortGroupIds)

    with pytest.raises(UIParamsPortGroupsException, match='only one group'):
        validate_node(nt.FunctionWithDoubledCanAdd)
    with pytest.raises(UIParamsPortGroupsException, match='if you are able to add a port to'):
        validate_node(nt.FunctionWithCanAddCantDelete)
    with pytest.raises(UIParamsCallbackException, match='not found callback'):
        validate_node(nt.FunctionWithInvalidCbName)
    with pytest.raises(UIParamsCallbackException, match='unsuported callback'):
        validate_node(nt.FunctionWithNotClassmethodCB)
