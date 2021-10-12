import energyNode
import Misc.defs

class EnergyConsumerNode(energyNode.EnergyNode):
    def __init__(self, consumerType):
        print("Making energy source node")
        self.consumerType = consumerType