from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch_geometric.nn as gnn


class GnnBlock(nn.Module):
    def __init__(
        self,
        qubit_num: int,
        max_gate_num: int,
        feat_dim: int,
        pool: bool,
    ) -> None:
        super().__init__()

        self._max_qubit_num = qubit_num
        self._max_gate_num = max_gate_num
        self._feat_dim = feat_dim
        self._pool = pool

        self._gc_grp = nn.ModuleList(
            [
                gnn.SAGEConv(
                    in_channels=feat_dim,
                    out_channels=feat_dim,
                    normalize=False,
                ),
                gnn.SAGEConv(
                    in_channels=feat_dim,
                    out_channels=feat_dim,
                    normalize=False,
                ),
            ]
        )

        if pool:
            # TopKPooling is returning (x, edge_index, edge_attr, batch, perm, score[perm])
            self._pool = gnn.TopKPooling(in_channels=feat_dim)

    def forward(
        self,
        x: torch.Tensor,
        edge_index: torch.Tensor,
        batch: Optional[torch.Tensor],
    ):
        for conv in self._gc_grp:
            x = F.leaky_relu(conv(x, edge_index)) + x
        if self._pool:
            x, edge_index, _, batch, _, _ = self._pool(x, edge_index, None, batch, None)
        return x, edge_index, batch


class CircuitGnn(nn.Module):
    def __init__(
        self,
        qubit_num: int,
        max_gate_num: int,
        feat_dim: int,
    ) -> None:
        super().__init__()

        self._max_qubit_num = qubit_num
        self._max_gate_num = max_gate_num
        self._feat_dim = feat_dim

        self._gc_grp = nn.ModuleList(
            [
                GnnBlock(
                    qubit_num=qubit_num,
                    max_gate_num=max_gate_num,
                    feat_dim=feat_dim,
                    pool=False,
                ),
                GnnBlock(
                    qubit_num=qubit_num,
                    max_gate_num=max_gate_num,
                    feat_dim=feat_dim,
                    pool=False,
                ),
                GnnBlock(
                    qubit_num=qubit_num,
                    max_gate_num=max_gate_num,
                    feat_dim=feat_dim,
                    pool=False,
                ),
                GnnBlock(
                    qubit_num=qubit_num,
                    max_gate_num=max_gate_num,
                    feat_dim=feat_dim,
                    pool=False,
                ),
                GnnBlock(
                    qubit_num=qubit_num,
                    max_gate_num=max_gate_num,
                    feat_dim=feat_dim,
                    pool=False,
                ),
            ]
        )

        self._aggr = gnn.aggr.SoftmaxAggregation(learn=False)

    def forward(
        self,
        x: torch.Tensor,
        edge_index: torch.Tensor,
        batch: Optional[torch.Tensor] = None,
    ):
        f = self._feat_dim

        for conv_block in self._gc_grp:
            x, edge_index, batch = conv_block(x, edge_index, batch)

        x = self._aggr(x, batch)  # [b, f]
        x = x.view(-1, f)  # [b, f]
        return x


class GnnMapping(nn.Module):
    def __init__(
        self,
        qubit_num: int,
        max_gate_num: int,
        feat_dim: int,
        action_num: int,
        device: str,
    ) -> None:
        super().__init__()

        self._max_qubit_num = qubit_num
        self._max_gate_num = max_gate_num
        self._feat_dim = feat_dim
        self._action_num = action_num
        self._device = device

        # All gate nodes and virtual node feature embedding.
        self._x_trans = nn.Embedding(
            num_embeddings=qubit_num + 1,
            embedding_dim=feat_dim,
            padding_idx=0,
        )

        self._circ_gnn = CircuitGnn(
            qubit_num=qubit_num,
            max_gate_num=max_gate_num,
            feat_dim=feat_dim * 2,
        )

        f_start = feat_dim * 2
        self._mlp_1 = nn.Sequential(
            nn.Linear(f_start, f_start),
            nn.LeakyReLU(),
            nn.Linear(f_start, f_start // 2),
            nn.LeakyReLU(),
            nn.Linear(f_start // 2, self._action_num),
        )

    def forward(self, x: torch.Tensor, edge_index: torch.Tensor, batch: torch.Tensor):
        f = self._feat_dim
        a = self._action_num

        circ_x = self._x_trans(x).view(-1, 2 * f)
        circ_feat = self._circ_gnn(circ_x, edge_index, batch)  # [b, f]

        x = self._mlp_1(circ_feat).view(-1, a)  # [b, a]
        return x


NnMapping = GnnMapping
