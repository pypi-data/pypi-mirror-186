"""
Class for customizing the whole process of synthesis, optimization and mapping
"""


from QuICT.qcda.synthesis import GateTransform
from QuICT.qcda.optimization import CommutativeOptimization, CliffordRzOptimization
from QuICT.qcda.mapping import MCTSMapping, SABREMapping
from QuICT.tools import Logger


logger = Logger("QCDA")


class QCDA(object):
    """ Customize the process of synthesis, optimization and mapping

    In this class, we meant to provide the users with a direct path to design the
    process by which they could transform a unitary matrix to a quantum circuit
    and/or optimize a quantum circuit.
    """

    def __init__(self, process=None):
        """ Initialize a QCDA process

        A QCDA process is defined by a list of synthesis, optimization and mapping.
        Experienced users could customize the process for certain purposes.

        Args:
            instruction(InstructionSet, optional): InstructionSet for default process
            layout(Layout, optional): Layout for default process
            process(list, optional): A customized list of Synthesis, Optimization and Mapping
        """
        self.process = []
        if process is not None:
            self.process = process

    def add_method(self, method=None):
        """ Adding a specific method to the process

        Args:
            method: Some QCDA method
        """
        self.process.append(method)

    def add_gate_transform(self, target_instruction=None):
        """ Add GateTransform for some target InstructionSet

        GateTransform would transform the gates in the original Circuit/CompositeGate to a certain InstructionSet.

        Args:
            instruction(InstructionSet): The target InstructionSet
        """
        assert target_instruction is not None, ValueError('No InstructionSet provided for Synthesis')
        self.add_method(GateTransform(target_instruction))

    def add_default_optimization(self, level='light'):
        """ Generate the default optimization process

        The default optimization process contains the CommutativeOptimization.

        Args:
            level(str): Optimizing level. Support `light`, `heavy` level.
        """

        self.add_method(CommutativeOptimization())
        self.add_method(CliffordRzOptimization(level=level))

    def add_mapping(self, layout=None, method='sabre'):
        """ Generate the default mapping process

        The default mapping process contains the Mapping

        Args:
            layout(Layout): Topology of the target physical device
            method(str, optional): used mapping method in ['mcts', 'sabre']
        """
        assert layout is not None, ValueError('No Layout provided for Mapping')
        assert method in ['mcts', 'sabre'], ValueError('Invalid mapping method')
        mapping_dict = {
            'mcts': MCTSMapping(layout=layout),
            'sabre': SABREMapping(layout=layout)
        }
        self.add_method(mapping_dict[method])

    def compile(self, circuit):
        """ Compile the circuit with the given process

        Args:
            circuit(CompositeGate/Circuit): the target CompositeGate or Circuit

        Returns:
            CompositeGate/Circuit: the resulting CompositeGate or Circuit
        """
        logger.info("QCDA Now processing GateDecomposition.")
        circuit.gate_decomposition()
        for process in self.process:
            logger.info(f"QCDA Now processing {process.__class__.__name__}.")
            circuit = process.execute(circuit)

        return circuit
