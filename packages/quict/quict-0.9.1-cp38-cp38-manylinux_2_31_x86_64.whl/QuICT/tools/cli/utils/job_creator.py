import os
import yaml


class JobCreator:
    def __init__(self, name: str, circuit_path: str, device: str = "CPU", output_path: str = None):
        self._job_dict = {
            "job_name": name,
            "device": device,
            "circuit": circuit_path,
            "output_path": os.path.abspath('.') if output_path is None else output_path
        }

    def set_simulation_spec(self, shots: int = 100, precision: str = "double", backend: str = "state_vector"):
        simulation_dict = {
            "shots": shots,
            "precision": precision,
            "backend": backend
        }
        self._job_dict["simulation"] = simulation_dict

    def set_qcda_spec(
        self,
        methods: list,
        instruction_set: str = "Google",
        auto_mode: str = "light",
        para: bool = True,
        depara: bool = False,
        templates: dict = None,
        layout_path: str = None
    ):
        qcda_dict = {
            "methods": methods,
            "instruction_set": instruction_set,
            "auto_mode": auto_mode,
            "para": para,
            "depara": depara
        }
        if templates is not None:
            qcda_dict["templates"] = templates

        if layout_path is not None:
            qcda_dict["mapping"] = {"enable": True, "layout_path": layout_path}

        self._job_dict["qcda"] = qcda_dict

    @property
    def job_dict(self):
        return self._job_dict

    def to_yaml(self, output_path: str = None):
        if output_path is None:
            job_name = self._job_dict['job_name']
            output_path = os.path.join(os.path.abspath('.'), f"{job_name}.yml")

        with open(output_path, 'w') as save_file:
            save_file.write(yaml.dump(self._job_dict, allow_unicode=True))
