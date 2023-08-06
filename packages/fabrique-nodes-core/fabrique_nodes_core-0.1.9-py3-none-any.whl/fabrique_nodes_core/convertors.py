from fabrique_nodes_core import model_generators, jspath_parser, NodeData, NodeConfig
import json


# from nodes_lib.function.src.node import NodeMethods as FunctionNodeMethods
jsons2model = model_generators.jsons2model
schema2model = model_generators.schema2model
model2schema = model_generators.model2schema
field2schema = model_generators.field2schema
model2ports = model_generators.model2ports
is_valid_jspath = jspath_parser.is_valid_code
upd_jspath_output = jspath_parser.upd_output


def convert_node_data_to_config(node_data: NodeData, id_: int = None) -> NodeConfig:
    """converts NodeData to NodeConfig

    :param node_data: node data from API or tests
    :type node_data: NodeData
    :param id_: Node id, defaults to None
    :type id_: int, optional
    :param ConfigModelClass: UI form config class, defaults to None
    :type ConfigModelClass: BaseModel, optional
    :return: node cfg
    :rtype: NodeConfig
    """
    node_data_dict = node_data.__dict__
    hash_id = hash(json.dumps(node_data.__dict__, default=str))
    node_data_dict['id_'] = str(id_ if id_ else hash_id)
    cfg = NodeConfig(**node_data_dict)
    cfg.ports_in = [p for ports in cfg.g_ports_in for p in ports]
    cfg.ports_out = [p for ports in cfg.g_ports_out for p in ports]
    return cfg
