import os
import yaml
from typing import Union, Dict

from QuICT.core.layout import Layout
from QuICT.tools.interface import OPENQASMInterface


class JobValidation:
    _SIMULATION_PARAMETERS = {
        "precision": ["single", "double"],
        "backend": ["state_vector", "density_matrix", "unitary"],
        "device": ["CPU", "GPU"]
    }

    _BASED_METHODS = ["GateTransform", "Clifford", "CliffordRz", "Commutative", "SymbolicClifford", "Template", "CNOT"]

    _QCDA_PARAMETERS = {
        "instruction_set": ["USTC", "Google", "IBMQ", "IonQ", "Nam", "Origin"],
        "auto_mode": ["light", "heavy"]
    }

    def __init__(self):
        self._job_template_path = os.path.join(
            os.path.dirname(__file__),
            "../template"
        )

    @staticmethod
    def get_circuit_info(qasm_file: str) -> dict:
        """ whether the given qasm file is valid or not. If not valid, raise ValueError. """
        try:
            circuit = OPENQASMInterface.load_file(qasm_file).circuit
        except:
            raise ValueError(f"Failure to load circuit from given file. {qasm_file}.")

        return {
            "width": str(circuit.width()),
            "size": str(circuit.size()),
            "depth": str(circuit.depth())
        }

    @staticmethod
    def load_yaml_file(file_path: str) -> dict:
        with open(os.path.abspath(file_path), encoding='utf-8') as yml:
            job_info = yaml.load(yml)

        return job_info

    @classmethod
    def based_info_validate(self, job_dict):
        # Necessary feature
        name = job_dict["job_name"]
        assert isinstance(name, str), f"Job's name shoule be a string, not {type(name)}."
        assert job_dict["device"] in self._SIMULATION_PARAMETERS['device'], \
            "Job's resource device should be one of [CPU, GPU]."

        # circuit's qasm file validation
        circuit_info = JobValidation.get_circuit_info(job_dict["circuit"])
        job_dict['circuit_info'] = circuit_info

    @classmethod
    def simulation_validation(self, simulation_dict: dict):
        # validation job's simulation
        assert simulation_dict["shots"] >= 1, "The number of shots >= 1."
        assert simulation_dict["precision"] in self._SIMULATION_PARAMETERS['precision'], \
            "precesion should be one of [single, double]."
        assert simulation_dict["backend"] in self._SIMULATION_PARAMETERS['backend'], \
            "backend should be one of [state_vector, density_matrix, unitary]."

    @classmethod
    def qcda_validation(self, qcda_dict: dict):
        # QCDA methods validation
        methods = qcda_dict["methods"]
        for method in methods:
            assert method in self._BASED_METHODS, \
                f"Unrecognized QCDA method, please use one of {self._BASED_METHODS}."

        # Extra Args Validation
        if "GateTransform" in methods:
            assert qcda_dict["instruction_set"] in self._QCDA_PARAMETERS["instruction_set"], \
                "Wrong Instruction Set."

        if "Auto" in methods:
            assert qcda_dict["auto_mode"] in self._QCDA_PARAMETERS["auto_mode"], \
                "auto_mode should be one of [light, heavy]."

        if "Commutative" in methods:
            assert isinstance(qcda_dict["para"], bool) and isinstance(qcda_dict["depara"], bool), \
                "The para and depara should be bool."

        if "Template" in methods:
            template_dict = qcda_dict["templates"]
            temp_args = [template_dict["max_width"], template_dict["max_size"], template_dict["max_depth"]]
            for arg in temp_args:
                assert isinstance(arg, int)

            qcda_dict["templates"] = "+".join([str(targ) for targ in temp_args])
        else:
            qcda_dict["templates"] = ""

        # Validate qcda mapping args
        if qcda_dict["mapping"]["enable"]:
            try:
                _ = Layout(1).load_file(qcda_dict["mapping"]["layout_path"])
            except Exception as e:
                raise KeyError(f"Failure to load layout from file as {e}.")

            # Update qcda dict
            qcda_dict["layout_path"] = qcda_dict["mapping"]["layout_path"]

        # adjust un-used options
        del qcda_dict["mapping"]
        qcda_dict["methods"] = "+".join(methods)

    def job_complement(self, info: dict, job_type: str):
        default_job_path = os.path.join(self._job_template_path, "quict_job.yml")
        default_job_dict = JobValidation.load_yaml_file(default_job_path)
        core_part = default_job_dict[job_type]

        for key, value in info.items():
            if key in list(core_part.keys()):
                core_part[key] = value

        return core_part

    def job_validation(self, job_file_path: Union[str, Dict]) -> Dict:
        """ Validate the given job's yaml file, and generate the regularized job's file.
        regularized_job_dict = {
            job_name(str),
            type(str): one of [qcda, simulation],
            circuit(str): circuit's qasm file path,
            output_path(str): The output path for store result
            circuit_info:
                qasm(str): circuit's qasm,
                width(int): the number of qubits in circuit,
                size(int): the number of qubits in circuit,
                depth(int): the number of qubits in circuit,

            ### only for simulation
            simulation:
                shots(int),
                precision(str), one of [single, double],
                backend(str), one of [state_vector, density_matrix, unitary]
                device(str), one of [CPU, GPU]

            ### only for qcda
            qcda:
                methods(list): []       # The methods for QCDA
                **extra_args:           # The arguments for QCDA methods

        Args:
            job_file_path (str): The file path for job's yaml file.

        Returns:
            regularized_job_dict(dict): The regularized job's dict
        """
        # Step 1: Load yaml file from given file path
        if isinstance(job_file_path, str):
            job_info = JobValidation.load_yaml_file(job_file_path)
        else:
            job_info = job_file_path

        # Step 2: check based information of job_yaml
        self.based_info_validate(job_info)

        # Step 3: complement and validate job's simulation/qcda information
        if "simulation" in job_info.keys():
            required_info = self.job_complement(job_info["simulation"], "simulation")
            self.simulation_validation(required_info)
            job_info["simulation"] = required_info

        if "qcda" in job_info.keys():
            required_info = self.job_complement(job_info["qcda"], "qcda")
            self.qcda_validation(required_info)
            job_info["qcda"] = required_info

        # Step 4: Prepare output path
        job_info["output_path"] = os.path.join(job_info["output_path"], job_info["job_name"])

        return job_info
