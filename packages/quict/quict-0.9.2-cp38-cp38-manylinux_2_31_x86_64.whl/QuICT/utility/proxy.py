#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/5/27 下午4:23
# @Author  : Kaiqi Li
# @File    : proxy

import cupy as cp
import numpy as np
from cupy import cuda
from cupy.cuda import nccl

from typing import Union
from QuICT.utility.timeout import timeout


# Mapping between dtype and nccl dtype
# Modify for cupy>9.0.0

type_mapping = {
    "int8": np.int8,
    "uint8": np.uint8,
    "int32": np.int32,
    "uint32": np.uint32,
    "int64": np.int64,
    "uint64": np.uint64,
    "float16": np.float16,
    "float32": np.float32,
    "float64": np.float64,
    "complex64": np.complex64,
    "complex128": np.complex128
}


TIMEOUT = 300   # The timeout for receiving data


class Proxy:
    """ The proxy class of NCCL Communicators, which is used to transfer data between gpus.

    Args:
        ndevs(int): number of total GPU devices.
        uid(tuple): The unique ID, generate by cupy.cuda.nccl.get_unique_id().
        dev_id(int): The dev_id of GPU, between 0 and ndevs-1; represent the gpu device use in current process.
        timeout(int): The maximum waiting time for receiving data, default to 300 seconds.
    """
    def __init__(self, ndevs: int, uid: tuple, dev_id: int, timeout: int = 300):
        assert((dev_id < ndevs) and (ndevs <= cuda.runtime.getDeviceCount()))
        if dev_id != cuda.runtime.getDevice():
            target_device = cuda.Device(dev_id)
            target_device.use()

        self._ndevs = ndevs
        self._uid = uid
        self._dev_id = dev_id
        self._timeout = timeout
        self.peers = np.setdiff1d(np.arange(self._ndevs), self._dev_id)

        self.comm = nccl.NcclCommunicator(self._ndevs, self._uid, self._dev_id)

    def __exit__(self):
        self.comm.destroy()

    @staticmethod
    def allInit(devs: Union[int, list]):
        """ Initialize NCCL communicators for multiple devices in a single process. """
        return nccl.NcclCommunicator.initAll(devs)

    @property
    def ndevs(self):
        """ return the number of GPU devices. """
        return self._ndevs

    @property
    def uid(self):
        """ return the unique id of current communicator. """
        return self._uid

    @property
    def dev_id(self):
        """ return the dev_id of current communicator. """
        return self._dev_id

    def send(
        self,
        sendbuf: cp.ndarray,
        destination: int,
        stream: cuda.stream.Stream = cuda.Stream.null.ptr
    ):
        """
        Send data to destination.

        Args:
            sendbuf(cupy.ndarray): the sending data.
            destination(int): the dev_id of destination communicator.
            stream(Stream): the cupy stream.
        """
        assert(type(sendbuf) == cp.ndarray)
        pointer = sendbuf.data.ptr
        count = sendbuf.size
        nccl_datatype = type_mapping[str(sendbuf.dtype)]

        if sendbuf.dtype == cp.complex128:
            count *= 2

        self.comm.send(pointer, count, nccl_datatype, destination, stream)

    @timeout()
    def recv(
        self,
        recvbuf: cp.ndarray,
        source: int,
        stream: cuda.stream.Stream = cuda.Stream.null.ptr
    ):
        """
        Receive data from source and put it into recvbuf.

        Args:
            recvbuf(cupy.ndarray): the GPU array waitting for comming data.
            source(int): the dev_id of the source communicator.
            stream(Stream): the cupy stream.
        """
        count = recvbuf.size
        nccl_datatype = type_mapping[str(recvbuf.dtype)]

        if recvbuf.dtype == cp.complex128:
            count *= 2

        self.comm.recv(recvbuf.data.ptr, count, nccl_datatype, source, stream)

        return recvbuf

    def broadcast(
        self,
        databuf: cp.ndarray,
        root: int = 0,
        stream: cuda.stream.Stream = cuda.Stream.null.ptr
    ):
        """
        Send data to all communicators except root. The sending data is in sendbuf of root communicator.

        Args:
            databuf(cupy.ndarray): the sending data in root, and the received array for other communicators.
            root(int): the dev_id ID of root communicator.
            stream(Stream): the cupy stream.
        """
        pointer = databuf.data.ptr
        count = databuf.size
        nccl_datatype = type_mapping[str(databuf.dtype)]

        if databuf.dtype == cp.complex128:
            count *= 2

        self.comm.bcast(pointer, count, nccl_datatype, root, stream)

    def reduce(
        self,
        root: int,
        op: int,
        sendbuf: cp.ndarray = None,
        recvbuf: cp.ndarray = None,
        stream: cuda.stream.Stream = cuda.Stream.null.ptr
    ):
        """
        Compute the op with the data from other peers, and write the result in the root.

        Args:
            root(int): the dev_id ID of root communicator.
            op (int): The operation with one of
                NCCL_SUM = 0,
                NCCL_PROD = 1,
                NCCL_MAX = 2,
                NCCL_MIN = 3.
            sendbuf(cupy.ndarray): the sending data, not used in the root.
            recvbuf(cupy.ndarray): the array waitting for comming data, must be defined in the root.
            stream(Stream): the cupy stream.
        """
        if self._dev_id == root:
            assert(recvbuf is not None)
            sendbuf = cp.empty(1, dtype=recvbuf.dtype)
            pointer = recvbuf.data.ptr
            count = recvbuf.size
            nccl_datatype = type_mapping[str(recvbuf.dtype)]

            if recvbuf.dtype == cp.complex128:
                count *= 2

            self.comm.reduce(sendbuf.data.ptr, pointer, count, nccl_datatype, op, root, stream)
        else:
            assert(sendbuf is not None)
            recvbuf = cp.empty(1, dtype=sendbuf.dtype)
            pointer = sendbuf.data.ptr
            count = sendbuf.size
            nccl_datatype = type_mapping[str(sendbuf.dtype)]

            if sendbuf.dtype == cp.complex128:
                count *= 2

            self.comm.reduce(pointer, recvbuf.data.ptr, count, nccl_datatype, op, root, stream)

    def reducescatter(
        self,
        sendbuf: cp.ndarray,
        recvbuf: cp.ndarray,
        op: int,
        stream: cuda.stream.Stream = cuda.Stream.null.ptr
    ):
        """
        Compute the op with the data from all peers, and split the result into all peers.

        Args:
            sendbuf(cupy.ndarray): the sending data.
            recvbuf(cupy.ndarray): the array waitting for the result.
            op (int): The operation with one of
                NCCL_SUM = 0,
                NCCL_PROD = 1,
                NCCL_MAX = 2,
                NCCL_MIN = 3.
            stream(Stream): the cupy stream.
        """
        send_pointer = sendbuf.data.ptr
        recv_pointer = recvbuf.data.ptr
        count = recvbuf.size
        nccl_datatype = type_mapping[str(sendbuf.dtype)]

        if sendbuf.dtype == cp.complex128:
            count *= 2

        self.comm.reduceScatter(send_pointer, recv_pointer, count, nccl_datatype, op, stream)

    def allreduce(
        self,
        sendbuf: cp.ndarray,
        recvbuf: cp.ndarray,
        op: int,
        stream: cuda.stream.Stream = cuda.Stream.null.ptr
    ):
        """
        Compute the op with the data from all peers, and send the result to all peers.

        Args:
            sendbuf(cupy.ndarray): the sending data.
            recvbuf(cupy.ndarray): the array waitting for the result.
            op (int): The operation with one of
                NCCL_SUM = 0,
                NCCL_PROD = 1,
                NCCL_MAX = 2,
                NCCL_MIN = 3.
            stream(Stream): the cupy stream.
        """
        send_pointer = sendbuf.data.ptr
        recv_pointer = recvbuf.data.ptr
        count = sendbuf.size
        nccl_datatype = type_mapping[str(sendbuf.dtype)]

        if sendbuf.dtype == cp.complex128:
            count *= 2

        self.comm.allReduce(send_pointer, recv_pointer, count, nccl_datatype, op, stream)

    def scatter(
        self,
        sendbuf: cp.ndarray,
        targets: list,
        stream: cuda.stream.Stream = cuda.Stream.null.ptr
    ):
        """
        Split sending data, and send to all peers in targets.
        Note that target proxy should using proxy.recv to receive the piece of sending data.

        Args:
            sendbuf(cupy.ndarray): the sending data.
            targets(list): List of the communicators' dev_id ID which hope to receive.
            stream(Stream): the cupy stream.
        """
        # Divided data depending on the given rules
        dest_len = len(targets)
        data_interval = sendbuf.size // dest_len

        # Send data to each target
        for dest_idx, dest in enumerate(targets):
            self.send(sendbuf[dest_idx * data_interval:(dest_idx + 1) * data_interval], dest, stream)

    def gather(
        self,
        root: int,
        sendbuf: cp.ndarray = None,
        recvbuf: cp.ndarray = None,
        stream: cuda.stream.Stream = cuda.Stream.null.ptr
    ):
        """
        Collect all data from peers into the root.

        Args:
            root(int): the dev_id ID of the root communicator.
            sendbuf(cupy.ndarray): the sending data, not use in the root communicator.
            recvbuf(cupy.ndarray): the GPU array waitting for comming data, only use in the
            root communicator.
            stream(Stream): the cupy stream.
        """
        if self._dev_id == root:
            assert(recvbuf is not None)

            recv_count_per_dev = recvbuf.size // (self._ndevs - 1)
            for dest in self.peers:
                self.recv(recvbuf[(dest - 1) * recv_count_per_dev:dest * recv_count_per_dev], dest, stream)
        else:
            assert(sendbuf is not None)

            self.send(sendbuf, root, stream)

    def allgather(
        self,
        sendbuf: cp.ndarray,
        recvbuf: cp.ndarray,
        stream: cuda.stream.Stream = cuda.Stream.null.ptr
    ):
        """
        Collect all data from peers, and send the aggregation bact to each peer.

        Args:
            sendbuf(cupy.ndarray): the sending data.
            recvbuf(cupy.ndarray): the GPU array waitting for comming data.
            stream(Stream): the cupy stream.
        """
        send_pointer = sendbuf.data.ptr
        recv_pointer = recvbuf.data.ptr
        count = sendbuf.size
        nccl_datatype = type_mapping[str(sendbuf.dtype)]

        if sendbuf.dtype == cp.complex128:
            count *= 2

        self.comm.allGather(send_pointer, recv_pointer, count, nccl_datatype, stream)
