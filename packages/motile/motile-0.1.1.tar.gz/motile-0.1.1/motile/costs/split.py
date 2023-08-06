from ..variables import NodeSplit
from .costs import Costs


class Split(Costs):

    def __init__(self, constant):

        self.constant = constant

    def apply(self, solver):

        split_indicators = solver.get_variables(NodeSplit)

        for index in split_indicators.values():
            solver.add_variable_cost(index, self.constant)
