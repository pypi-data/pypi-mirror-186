from ..variables import NodeAppear
from .costs import Costs


class Appear(Costs):

    def __init__(self, constant):

        self.constant = constant

    def apply(self, solver):

        appear_indicators = solver.get_variables(NodeAppear)

        for index in appear_indicators.values():
            solver.add_variable_cost(index, self.constant)
