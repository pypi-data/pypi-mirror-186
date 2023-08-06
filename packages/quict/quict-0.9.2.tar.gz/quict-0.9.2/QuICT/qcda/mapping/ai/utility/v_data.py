#!/usr/bin/env python3

"""This file generates some random circuits used for validation of trained RL agent.
"""

import os
import os.path as osp

from QuICT.core import *
from QuICT.core.layout.layout import Layout
from QuICT.core.utils import GateType
from QuICT.tools.logger import Logger

logger = Logger("rl-v-data")

data_dir = osp.dirname(os.getcwd())
data_dir = osp.join(data_dir, os.pardir)
data_dir = osp.join(data_dir, "data")
data_dir = osp.join(data_dir, "v_data")

if not osp.exists(data_dir):
    os.makedirs(data_dir)


def prepare_v_data(
    topo_names=("grid_4x4", "grid_3x3", "grid_4x5", "ibmq_lima"),
    circ_num_each_topo=10,
):
    for topo_name in topo_names:
        logger.info(f"Starting processing {topo_name}...")
        topo_dir = osp.dirname(osp.abspath(__file__))
        topo_dir = osp.join(topo_dir, os.pardir)
        topo_dir = osp.join(topo_dir, "data")
        topo_dir = osp.join(topo_dir, "topo")
        topo_path = osp.join(topo_dir, f"{topo_name}.json")
        topo = Layout.load_file(topo_path)
        q = topo.qubit_number
        for i in range(circ_num_each_topo):
            logger.info(".", end="")
            circ = Circuit(q)
            g = 10 * (i + 1)
            circ.random_append(rand_size=g, typelist=[GateType.crz], random_params=True)
            qasm = circ.qasm()
            qasm_path = osp.join(data_dir, f"{topo_name}_{i}.qasm")
            with open(qasm_path, "w") as f:
                f.write(qasm)

        logger.info()
