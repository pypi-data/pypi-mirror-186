from abc import abstractmethod


class RemoteSimulator(object):
    """ The based class for remote simulator, currently support Qiskit and QCompute.

    Args:
        backend ([str]): The backend for the remote simulator.
        shots ([int]): The repeat times of running circuit, always be a positive integer.
    """
    def __init__(self, backend, shots):
        assert shots >= 1, "The shots must be a positive integer."
        self._backend = backend
        self._shots = shots

    @abstractmethod
    def run(self):
        pass

    def get_backend(self):
        return self.__BACKEND
