#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/12/27 5:03 下午
# @Author  : Han Yu
# @File    : topology.py

from __future__ import annotations
from itertools import combinations

import json
import warnings
from typing import Any, Dict, List, Tuple


class LayoutEdge:
    """Implement a physical connection between physical qubits

    Attributes:
        u(int): Node u of edge
        v(int): Node v of edge
        directional(bool): Whether the layout is directional
        error_rate(float): Error_rate between u and v, default 1.0
    """

    @property
    def u(self) -> int:
        return self._u

    @u.setter
    def u(self, u):
        warnings.warn("In general, the LayoutEdge shouldn't be written.")
        self._u = u

    @property
    def v(self) -> int:
        return self._v

    @v.setter
    def v(self, v):
        warnings.warn("In general, the LayoutEdge shouldn't be written.")
        self._v = v

    @property
    def error_rate(self) -> float:
        return self._error_rate

    @error_rate.setter
    def error_rate(self, error_rate):
        self._error_rate = error_rate

    @property
    def directional(self):
        return self._directional

    @directional.setter
    def directional(self, value: bool):
        self._directional = value

    def to_dict(self) -> Dict[str, Any]:
        data = {}
        data["u"] = self._u
        data["v"] = self._v
        data["error_rate"] = self._error_rate
        data["directional"] = self._directional
        return data

    def __init__(self, u: int, v: int, directional: bool, error_rate: float):
        self._u = u
        self._v = v
        self._error_rate = error_rate
        self._directional = directional

    def __str__(self):
        dir = ' <-> ' if not self._directional else '-->'
        return f"{self._u} {dir} {self._v}, with error rate {self._error_rate}"


class Layout:
    """Implement a topology in a physical device

    Attributes:
        name(string): the name of the topology
        edge_list(list<LayoutEdge>): the edge in layout
        qubit_number(int): the number of qubits
    """

    DIRECTIONAL_DEFAULT = False
    ERROR_RATE_DEFAULT = 1.0

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def edge_list(self) -> List[LayoutEdge]:
        return list(self._edges.values())

    def __iter__(self):
        yield from self._edges.values()

    @property
    def qubit_number(self):
        return self._qubit_number

    def __init__(self, qubit_number: int, name: str = "unknown"):
        self._qubit_number = qubit_number
        self._name = name
        self._edges: Dict[Tuple[int, int], LayoutEdge] = {}
        self._directionalized = None

    def __str__(self):
        layout_str = f"{self._name} with {self._qubit_number} qubits."
        for edge in self.edge_list:
            layout_str += f"\n{edge}"

        return layout_str

    def out_edges(self, begin_point: int) -> List[LayoutEdge]:
        """edges begin from begin_point

        Args:
            begin_point(int): the index of begin node

        Return:
            list<LayoutEdge>: edges begin from begin_point
        """
        prior_list = []
        for edge in self.edge_list:
            if edge.u == begin_point:
                prior_list.append(edge)
        return prior_list

    @property
    def directionalized(self) -> Layout:
        """Return a copy of current layout with all un-directional edges
        replaced with 2 reversed directional edges.
        """
        layout = Layout(self._qubit_number, self._name)
        for edge in self:
            if edge.directional:
                layout.add_edge(edge)
            else:
                layout.add_edge(
                    u=edge.u, v=edge.v, directional=True, error_rate=edge.error_rate
                )
                layout.add_edge(
                    u=edge.v, v=edge.u, directional=True, error_rate=edge.error_rate
                )
        return layout

    def add_edge(
        self,
        u,
        v,
        directional=DIRECTIONAL_DEFAULT,
        error_rate=ERROR_RATE_DEFAULT,
    ):
        """add an edge in the layout

        Args:
            u(int): Edge endpoint u
            v(int): Edge endpoint v
            directional(bool): Whether the edge is directional
            error_rate(float): Error rate, default 1.0
        """
        assert u != v, "Endpoints cannot be the same"
        edge = LayoutEdge(u, v, directional, error_rate)
        key = (u, v) if directional or u < v else (v, u)
        self._edges[key] = edge
        # Reset cache
        self._directionalized = None

    def check_edge(self, u, v):
        """Check whether layout contain u->v

        Args:
            u(int): the edge endpoint u
            v(int): the edge endpoint v
        Return:
            bool: whether layout contain u->v
        """
        return ((u, v) in self._edges) or (
            (v, u) in self._edges and not self._edges[(v, u)].directional
        )

    def to_json(self) -> str:
        """Serialize current layout into json string."""
        data = {}
        data["name"] = self._name
        data["qubit_number"] = self._qubit_number
        edges = [edge.to_dict() for edge in self]
        data["edges"] = edges
        return json.dumps(data)

    def write_file(self, directory="./"):
        """Write layout into file.

        Args:
            directory(str): Directory to store layout file in, default "./"
        """
        with open(f"{directory}{self.name}.layout", "w") as f:
            f.write(self.to_json())

    @classmethod
    def from_json(cls, json_str: str) -> Layout:
        json_obj = json.loads(json_str)
        name = json_obj["name"]
        qubit_number = json_obj["qubit_number"]
        layout = Layout(qubit_number, name)
        edges = json_obj["edges"]
        for edge in edges:
            u = edge["u"]
            v = edge["v"]
            directional = (
                edge["directional"]
                if "directional" in edge
                else cls.DIRECTIONAL_DEFAULT
            )
            error_rate = (
                edge["error_rate"] if "error_rate" in edge else cls.ERROR_RATE_DEFAULT
            )
            layout.add_edge(u=u, v=v, directional=directional, error_rate=error_rate)
        return layout

    @classmethod
    def load_file(cls, file_path: str) -> Layout:
        """Load layout from file.
        Args:
            file_path(str): Path of layout file.
        Return:
            Layout: Layout parsed from file.
        """
        with open(file_path) as f:
            return cls.from_json(f.read())

    def get_sublayout_edges(self, qubits: list) -> list:
        connected_qubits = [qubits[0]]
        connected_edges = []
        for qubit in qubits:
            edges = self.out_edges(qubit)
            for edge in edges:
                if edge.v in qubits:
                    if edge.v not in connected_qubits:
                        connected_qubits.append(edge.v)

                    target_edge = set([edge.u, edge.v])
                    if target_edge not in connected_edges:
                        connected_edges.append(target_edge)

        if len(connected_qubits) == len(qubits):
            return connected_edges
        else:
            return []

    def sub_layout(self, qubits_number: int):
        """ Get partial layout. Only working for undirectional layout.

        Args:
            qubits_number (int): The number of qubits for sub-layout

        Returns:
            Layout: The sub-layout
        """
        assert qubits_number < self.qubit_number

        qubits_list = list(range(self.qubit_number))
        all_combined = list(combinations(qubits_list, qubits_number))
        num_edges_subl, edges_subl = [], []
        for q_comb in all_combined:
            edges_sl = self.get_sublayout_edges(q_comb)
            num_edges_subl.append(len(edges_sl))
            edges_subl.append(edges_sl)

        max_value = max(num_edges_subl)
        if max_value <= 0:
            raise ValueError("Failure to find sub-layout.")

        max_idx = num_edges_subl.index(max_value)
        sub_layout = self._get_layout(all_combined[max_idx], edges_subl[max_idx])

        return sub_layout

    def _get_layout(self, related_qubits: list, edges: list) -> Layout:
        sub_layout = Layout(len(related_qubits))
        index_mapping = {}
        for idx, q in enumerate(related_qubits):
            index_mapping[q] = idx

        for u, v in edges:
            sub_layout.add_edge(index_mapping[u], index_mapping[v], directional=False)

        return sub_layout
