import numpy as np
import cupy as cp

from QuICT.core.operator import DataSwitch, DataSwitchType


class DataSwitcher:
    """ A class of data switch functions using by multi-GPU simulator.

    Args:
        proxy (Proxy): The NCCL Communicator.
        qubits (int): The number of qubits.
    """
    @property
    def id(self):
        return self._id

    def __init__(self, proxy):
        self._proxy = proxy
        self._id = proxy.dev_id

    def __call__(self, op: DataSwitch, vector):
        destination = op.destination
        if op.type == DataSwitchType.all:
            self.all_switch(vector, destination)
        elif op.type == DataSwitchType.half:
            self.half_switch(vector, destination)
        elif op.type == DataSwitchType.ctarg:
            self.ctargs_switch(vector, destination, op.switch_condition)
        else:
            raise TypeError("unsupportted data switch type.")

    def _switch(self, vector, destination: int):
        """ Based data switch function, swithc the data between self and destination.

        Args:
            vector (cp.array): The data which will be sent to destination.
            destination (int): The communicator which switch the data with us.
            _0_1 (bool): Is the initiator or the follower about the switch behavior.

        Returns:
            np.array: the switched data from the destination.
        """
        is_initiator = self._id < destination
        recv_buf = cp.zeros(vector.size, dtype=vector.dtype)

        if is_initiator:
            self._proxy.send(vector, destination)
            self._proxy.recv(recv_buf, destination)
        else:
            self._proxy.recv(recv_buf, destination)
            self._proxy.send(vector, destination)

        return recv_buf

    def all_switch(self, vector, destination: int):
        """ Switch the whole data with the destination.

        Args:
            vector (cp.array): the switched data.
            destination (int): The communicator which switch the data with us.
        """
        vector[:] = self._switch(vector, destination)

    def half_switch(self, vector, destination: int):
        """ Switch the half data with the destination.

        Args:
            vector (cp.array): the switched data.
            destination (int): The communicator which switch the data with us.
        """
        _0_1 = self._id < destination
        sending_size = vector.size // 2

        if not _0_1:
            sending_data = vector[:sending_size]
            recv_buf = self._switch(sending_data, destination)
            vector[:sending_size] = recv_buf
        else:
            sending_data = vector[sending_size:]
            recv_buf = self._switch(sending_data, destination)
            vector[sending_size:] = recv_buf

    def quarter_switch(self, vector, destination: list):
        assert(len(destination) == 4)
        sending_size = vector.size // 4

        for idx, dest in enumerate(destination):
            if dest != self._id:
                sending_data = vector[idx * sending_size: (idx + 1) * sending_size]
                vector[idx * sending_size: (idx + 1) * sending_size] = self._switch(sending_data, dest)

    def ctargs_switch(self, vector, destination: int, condition: dict):
        """ Switch the data by the given condition.
            e.g. if condition = {3: 1}, switch the data which the third bit-indexes is 1 with the data
            from the destination.

        Args:
            vector (cp.array): the switched data.
            destination (int): The communicator which switch the data with us.
            condition (dict[index(int): 0/1]): Describe the indexes of the data will be switched.
        """
        target_idx = np.arange(vector.size, dtype=np.int64)
        for idx, _0_1 in condition.items():
            if isinstance(target_idx, tuple):
                target_idx = target_idx[0]

            if _0_1:
                target_idx = target_idx[np.where(target_idx & (1 << idx))]
            else:
                target_idx = target_idx[np.where((target_idx & (1 << idx)) == 0)]

        sending_data = vector[target_idx]
        recv_buf = self._switch(sending_data, destination)
        vector[target_idx] = recv_buf

    def add_prob(self, prob_result):
        recv_buf = cp.zeros_like(prob_result)

        self._proxy.allreduce(
            sendbuf=prob_result,
            recvbuf=recv_buf,
            op=0
        )

        return recv_buf
