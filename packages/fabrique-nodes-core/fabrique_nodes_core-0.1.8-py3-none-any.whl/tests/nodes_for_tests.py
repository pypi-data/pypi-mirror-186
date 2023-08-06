from typing import List, Literal
from fabrique_nodes_core import BaseNode, NodeData, NodeConfig, Port, UIParams, UIPortGroupParams, port_type
from pydantic import BaseModel, Field
import jmespath


class A2E_Node(BaseNode):
    """node config"""
    type_ = 'ArrayToElement'
    category = 'StructOps'
    initial_config = NodeData(
        name='Array To Element',
        g_ports_in=[[Port(id_='array', name='array', type_=port_type[list])], []],
        g_ports_out=[[Port(id_='element', name='element', type_=port_type[None])], []],
        description='Array To Element ForEach iterator'
    )

    ui_params = UIParams(
        input_groups=[
            UIPortGroupParams(id_='required_i'),
            UIPortGroupParams(
                id_='custom_i',
                can_add=True,
                can_move=True,
                can_delete=True,
                can_set_type=True,
            )
        ],
        output_groups=[
            UIPortGroupParams(id_='required_o'),
            UIPortGroupParams(id_='custom_o', copy_from_group='custom_i')
        ]
    )

    def element_generator(self, array: list, *shared):
        """forEach inference function"""
        if shared:
            not_including = -len(shared)
        else:
            not_including = None
        iterat = 0
        for element in array:
            element_out = list()
            iterat += 1
            for out_port in self.cfg.ports_out[:not_including]:
                # DESTRUCTURER is only for element
                if not out_port.visible:
                    continue

                if out_port.code == "":
                    element_out.append(element)
                    continue

                if out_port.special:  # jmes
                    output = jmespath.search(out_port.code, element)
                    element_out.append(output)
                else:  # model port case
                    element_out.append(element[out_port.code])
                # SHARED PORTS JUST TRANSITED
            output = [*element_out, *shared]
            yield output


# if-else
class IfElseNode(BaseNode):
    """node config"""
    type_ = "If-Else"

    initial_config = NodeData(
        name="If-Else",
        g_ports_in=[
            [Port(id_="value", name="value", type=port_type[None])],
            [Port(id_="is_true", name="is_true", type=port_type[bool])]
        ],
        g_ports_out=[
            [Port(id_="value", name="value", type=port_type[None])],
            [Port(id_="value", name="value", type=port_type[None])]
        ],
        description='If-Else use "is_true" signal',
    )

    ui_params = UIParams(
        input_groups=[
            UIPortGroupParams(id_='custom_i', can_add=True, can_move=True, can_delete=True, can_set_type=True),
            UIPortGroupParams(id_='required_i', group_title='condition'),
        ],
        output_groups=[
            UIPortGroupParams(id_='is_conditon', copy_from_group='custom_i', cah_hide=True, group_title="is condition"),
            UIPortGroupParams(id_='is_not_conditon', copy_from_group='custom_i', cah_hide=True, group_title="else")
        ]
    )

    def __init__(self, cfg):
        super().__init__(cfg)
        self.out_indexes_true = list()
        self.out_indexes_false = list()

        middle = len(cfg.ports_out) / 2
        for num, port in enumerate(cfg.ports_out):
            if not port.visible:
                continue
            if num <= middle:
                self.out_indexes_true.append(num)
            else:
                self.out_indexes_false.append(num - middle)

    def process_conditional(self, *inputs):
        """inference func"""
        condition = inputs[-1]
        port_indexes = self.out_indexes_true if condition else self.out_indexes_false
        outputs = list()
        for num, element in enumerate(inputs[:-1]):
            if num in port_indexes:
                outputs.append(element)

        return (condition, outputs)


class FilterNode(BaseNode):
    """node config"""
    type_ = 'Filter'
    initial_config = NodeData(
        name='Filter',
        g_ports_in=[
            [Port(id_='value', name='value', type_=port_type[None])],
            [Port(id_='is_true', name='is_true', type_=port_type[bool])]
        ],
        g_ports_out=[[Port(id_='value', name='value', type_=port_type[None])]],
        description='Filters by "is_true" signal'
    )
    ui_params = UIParams(
        input_groups=[
            UIPortGroupParams(id_='custom_i', can_add=True, can_move=True, can_delete=True, can_set_type=True),
            UIPortGroupParams(id_='required_i', group_title='condition'),
        ],
        output_groups=[
            UIPortGroupParams(id_='is_conditon', copy_from_group='custom_i')
        ]
    )

    def process(self, *values):
        '''inference func'''
        len_ports = len(self.cfg.ports_in)
        len_values = len(values)
        assert len_values == len_ports, f'must be {len_ports} params, not {len_values}'
        if values[-1]:  # last port is boolean
            return values[:-1]


# Function
is_valid_code_cbs = lambda x: True


def output2input_codes(codes_lst: List[str]):
    assert codes_lst == ['A + B', 'B - C']
    return ['A', 'B', 'C']


compute_formula = lambda x: x

initial_config = NodeData(
    name='Function',
    g_ports_in=[[], []],
    description=''
)


class FunctionNode(BaseNode):
    """node config"""
    type_ = 'Function'
    ui_params = UIParams(
        input_groups=[
            UIPortGroupParams(
                id_='auto',
                can_move=True
            ),
            UIPortGroupParams(
                id_='custom',
                can_add=True,
                can_delete=True,
                can_move=True,
                has_code=True
            )
        ],
        output_groups=[UIPortGroupParams(
            id_='outputs',
            can_add=True,
            can_delete=True,
            can_move=True,
            has_code=True,
            node_updater_callback_name='upd_inputs_from_outputs_cb',
            code_validator_callback_name='is_valid_code_cb'
        )]
    )
    initial_config = initial_config

    def __init__(self, cfg: NodeConfig):
        self.cfg = cfg

        self.indexes = []
        input_codes = [p.code for p in self.cfg.ports_in]
        for port in self.cfg.ports_out:
            arg_codes = output2input_codes([port.code, ])
            self.indexes.append([i for c in arg_codes for i, code in enumerate(input_codes) if code == c])

    @classmethod
    def is_valid_code_cb(cls, code: str) -> str:
        return {'is_valid': is_valid_code_cbs([code, ])}

    @classmethod
    def upd_inputs_from_outputs_cb(cls, cfg: NodeConfig) -> NodeConfig:
        output_codes = [p.code for p in cfg.g_ports_out[0]]  # port group id = = "outputs"
        input_codes = output2input_codes(output_codes)
        ports_in = [Port(id_=code, name=code, code=code) for code in input_codes]
        cfg.g_ports_in[0] = ports_in  # port group id = "auto"
        return cfg

    def process(self, *inputs):
        '''inference func'''
        outputs = []
        for i, port in enumerate(self.cfg.ports_out):
            indexes = self.indexes[i]
            args = [inputs[k] for k in indexes]
            outputs.append(compute_formula(port.code, args))

        return outputs


class IfElseWithMismatchPorts(IfElseNode):
    ui_params = UIParams(
        input_groups=[
            UIPortGroupParams(
                id_='auto',
                can_move=True
            )
        ],
        output_groups=IfElseNode.ui_params.output_groups
    )


class FunctionWithDoubledCanAdd(FunctionNode):
    ui_params = UIParams(
        input_groups=[
            UIPortGroupParams(
                id_='auto',
                can_add=True,
                can_delete=True,
                can_move=True,
            ),
            UIPortGroupParams(
                id_='custom',
                can_add=True,
                can_delete=True,
                can_move=True,
                has_code=True
            )
        ],
        output_groups=FunctionNode.ui_params.output_groups
    )


class FunctionWithCanAddCantDelete(FunctionNode):
    ui_params = UIParams(
        input_groups=[
            UIPortGroupParams(
                id_='auto'
            ),
            UIPortGroupParams(
                id_='custom',
                can_add=True,
                can_move=True,
                has_code=True
            )
        ],
        output_groups=FunctionNode.ui_params.output_groups
    )


class FunctionWithInvalidCbName(FunctionNode):
    ui_params = UIParams(
        input_groups=FunctionNode.ui_params.input_groups,
        output_groups=[UIPortGroupParams(
            id_='outputs',
            can_add=True,
            can_delete=True,
            can_move=True,
            has_code=True,
            node_updater_callback_name='upd_inputs_from_outputs_cb',
            code_validator_callback_name='not_implemented_is_valid_code_cb'
        )]
    )


class FunctionWithNotClassmethodCB(FunctionNode):
    def is_valid_code_cb(self, code: str) -> str:
        return {'is_valid': is_valid_code_cbs([code, ])}


class FunctionWithNonUniquePortGroupIds(FunctionNode):
    ui_params = UIParams(
        input_groups=[
            UIPortGroupParams(
                id_='auto',
            ),
            UIPortGroupParams(
                id_='auto',
                has_code=True
            )
        ],
        output_groups=FunctionNode.ui_params.output_groups
    )


# UIConfig nodes!


class UIConfig(BaseModel):
    global_collection_name: str = Field('', title='Collection name', description='Collection name in store')
    step: int = Field(5.0, title='Step size', description='Step size', ge=0.0, le=172800.0)
    size: int = Field(5.0, title='Window size', description='Window size', ge=0.0, le=172800.0)
    expiration_time: float = Field(172800.0, title='Expiration Time', description='Message Expiration Time',
                                   ge=0.0, le=172800.0)
    aggregator: Literal['SUM', 'MEAN', 'MAX', 'MIN'] = Field('SUM', title='Aggregator', description='Aggregator method')


initial_config = NodeData(
    name="WindowWrite",
    g_ports_in=[
        [Port(id_="ts", name="ts", type_=port_type[float])],
        [Port(id_="key", name="key", type_=port_type[str]), Port(id_="value", name="value", type_=port_type[float])]
    ],
    description="",
    ui_config=UIConfig()
)

ui_params = UIParams(
    input_groups=[UIPortGroupParams(id_='required_i'), UIPortGroupParams(id_='optional_i', can_hide=True)],
    ui_config_schema=UIConfig.schema_json()
)


class FakeStore:
    def __init__(self, store_config):
        self.store_config = store_config


class DumbWindow(BaseNode):
    type_ = "WindowWrite"
    initial_config = initial_config
    ui_params = ui_params

    def __init__(self, cfg: NodeConfig, shared_store: dict = None):
        super().__init__(cfg)
        self.ui_config = UIConfig(**cfg.ui_config)
        self.store = FakeStore(self.ui_config)

    def process(self, *inputs):
        """inference func"""
        pass


class DumbWindowWithoutUIconfig(DumbWindow):
    initial_config = NodeData(
        name="WindowWrite",
        g_ports_in=[
            [Port(id_="ts", name="ts", type_=port_type[float])],
            [Port(id_="key", name="key", type_=port_type[str]), Port(id_="value", name="value", type_=port_type[float])]
        ],
        description=""
    )


class DumbWindowWithoutUIconfigSchema(DumbWindow):
    ui_params = UIParams(
        input_groups=[UIPortGroupParams(id_='required_i'), UIPortGroupParams(id_='optional_i', can_hide=True)]
    )


class DumbWindowWithMismatchUIConfAndSchema(DumbWindow):
    initial_config = NodeData(
        name="WindowWrite",
        g_ports_in=[
            [Port(id_="ts", name="ts", type_=port_type[float])],
            [Port(id_="key", name="key", type_=port_type[str]), Port(id_="value", name="value", type_=port_type[float])]
        ],
        description="",
        ui_config={'key': 'value'}
    )
