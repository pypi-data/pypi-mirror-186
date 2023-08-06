import os
import numpy as np


class Result:
    """ Data structure class for simulator result

    Args:
        mode (str): The simulator mode, usually be {device-backend}.
        shots (int): The running times; must be a positive integer.
        options (dict): Optional parameters for the simulator.
    """
    def __init__(
        self,
        device: str,
        backend: str,
        precision: str,
        circuit_record: bool,
        amplitude_record: bool,
        options: dict,
        output_path: str = None
    ):
        self.device = device
        self.backend = backend
        self.precision = precision
        self._circuit_record = circuit_record
        self._amplitude_record = amplitude_record
        self.options = options

        self.counts = {}
        self.state_vector = None
        self.density_matrix = None

        # prepare output path
        self._dump_folder = True if self._amplitude_record or self._circuit_record else False
        if self._dump_folder:
            self._output_path = self._prepare_output_file(output_path)

    def __str__(self):
        return f"Device: {self.device}\nBackend: {self.backend}\n" + \
            f"Options: {self.options}\nResults: {self.counts}"

    def __dict__(self):
        return {
            "id": self.id,
            "shots": self.shots,
            "backend_info": {
                "device": self.device,
                "backend": self.backend,
                "options": self.options
            },
            "data": {
                "counts": self.counts,
                "state_vector": self.state_vector,
                "density_matrix": self.density_matrix
            }
        }

    def _prepare_output_file(self, output_path):
        """ Prepare output path. """
        if output_path is None:
            curr_path = os.getcwd()
            output_path = os.path.join(curr_path, "output")

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        return output_path

    def record_sample(self, result: list):
        """ Record circuit's result

        Args:
            result (list): The sample of measured result from given circuit.
        """
        self.shots = sum(result)
        for i in range(len(result)):
            bit_idx = "{0:0b}".format(i)
            bit_idx = bit_idx.zfill(int(np.log2(len(result))))
            self.counts[bit_idx] = result[i]

        if self._dump_folder:
            with open(f"{self._output_path}/result_{self.id}.log", "w") as of:
                of.write(str(self.__dict__()))

    def record_circuit(self, circuit):
        """ dump the circuit. """
        self.id = circuit.name
        if self._circuit_record:
            with open(f"{self._output_path}/circuit_{self.id}.qasm", "w") as of:
                of.write(circuit.qasm())

    def record_amplitude(self, amplitude):
        """ dump the circuit. """
        if self.device == "GPU":
            amplitude = amplitude.get()

        if self._amplitude_record:
            np.savetxt(f"{self._output_path}/amp_{self.id}.txt", amplitude)

        if self.backend == "density_matrix":
            self.density_matrix = amplitude.copy()
        else:
            self.state_vector = amplitude.copy()
