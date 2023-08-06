import os
import json


def options_validation(options: dict, device: str, backend: str = None):
    """ Validation the given options is related simulator's parameters.

    Args:
        options (dict): The given simulator's parameters.
        device (str): The device of the simulator. One of [CPU, GPU]
        backend (str): The backend for the simulator. One of [unitary, state_vector, density_matrix]
    """
    # Load simulator's options dict
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "simulator_parameters.json")
    with open(data_path, "r") as f:
        simulator_options = json.load(f)

    assert device in ["CPU", "GPU"], "Device should be one of [CPU, GPU]."
    simulator_options = simulator_options[device]
    # Select target simulator's option by input
    simulator_options_keys = []
    if backend is not None:
        assert backend in ["unitary", "state_vector", "density_matrix"], \
            "backend should be one of [unitary, state_vector, density_matrix]."

        simulator_options_keys.append(set(simulator_options[backend].keys()))
    else:
        for backend, parameters in simulator_options.items():
            simulator_options_keys.append(set(parameters.keys()))

    # Validation the input options
    input_option_keys = set(options.keys())
    for parameters_set in simulator_options_keys:
        union_params = input_option_keys & parameters_set
        if len(union_params) == len(input_option_keys):
            return True

    return False
