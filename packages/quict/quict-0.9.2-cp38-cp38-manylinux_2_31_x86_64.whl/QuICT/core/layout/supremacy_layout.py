from typing import DefaultDict
import numpy as np

from QuICT.core.layout import Layout


class SupremacyLayout(Layout):
    def __init__(self, qubits: int, name: str = "unknown"):
        assert(qubits >= 5)
        Layout.__init__(self, qubits, name)

        self._build_supremacy_layout()
        self._add_supremacy_edge()

    def _build_supremacy_layout(self):
        if self.qubit_number == 5:
            self.qubit_table = np.array(
                [[0, 1],
                 [2, -1],
                 [3, 4]], dtype=np.int32
            )
        else:
            full_size_width = int(np.ceil(np.sqrt(self.qubit_number)))

            self.qubit_table = np.zeros((full_size_width, full_size_width), dtype=np.int32)
            self.qubit_table -= 1

            for i in range(self.qubit_number):
                row = i // (full_size_width - 1)
                col = i % (full_size_width - 1)

                if row >= full_size_width:
                    self.qubit_table[i % full_size_width, full_size_width - 1] = i
                else:
                    self.qubit_table[row, col] = i

    def _add_supremacy_edge(self):
        row, col = self.qubit_table.shape
        self._pattern_edge = DefaultDict(list)

        for i in range(1, row, 2):
            for j in range(col):
                current_qubit = self.qubit_table[i, j]
                if current_qubit != -1:
                    # pattern "A"
                    if i + 1 < row:
                        qubit_a = self.qubit_table[i + 1, j]
                        if qubit_a != -1:
                            self._pattern_edge["A"].append([current_qubit, qubit_a])
                            self.add_edge(current_qubit, qubit_a)

                    # pattern "B"
                    if j + 1 < col:
                        qubit_b = self.qubit_table[i - 1, j + 1]
                        if qubit_b != -1:
                            self._pattern_edge["B"].append([current_qubit, qubit_b])
                            self.add_edge(current_qubit, qubit_b)

                    # pattern "C"
                    qubit_c = self.qubit_table[i - 1, j]
                    if qubit_c != -1:
                        self._pattern_edge["C"].append([current_qubit, qubit_c])
                        self.add_edge(current_qubit, qubit_c)

                    # pattern "D"
                    if i + 1 < row and j + 1 < col:
                        qubit_d = self.qubit_table[i + 1, j + 1]
                        if qubit_d != -1:
                            self._pattern_edge["D"].append([current_qubit, qubit_d])
                            self.add_edge(current_qubit, qubit_d)

    def get_edges_by_pattern(self, pattern: str):
        return self._pattern_edge[pattern]
