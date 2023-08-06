#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/9/11 08:06
# @Author  : Xiaoquan Xu
# @File    : moleculardata.py

import h5py


def get_from_file(item, molfile, set_type=None):
    """
    Args:
        item(str): the name of the target dataset
        molfile(dict): the read pointer of the molecular file
        set_type(str): the target type of data
    """
    try:
        data = molfile[item][...]
        if data.dtype.num == 0:
            data = None
        elif set_type is not None:
            data = data.astype(set_type)
    except Exception:
        data = None
        print("!! no " + item)
    return data


class MolecularData:
    """
    Attributes:
        molfile(str): the molecular file name with ".hdf5" suffix
        n_orbitals(integer): the number of the spatial orbitals
        n_electrons(integer): the number of the electrons in the molecule
        nuclear_repulsion(float): the energy from nuclei-nuclei interaction.
        one_body_integrals(ndarray): the one-electron integrals
            in the shape of (n_orbitals, n_orbitals)
        two_body_integrals(ndarray): the two-electron integrals
            in the shape of (n_orbitals, n_orbitals, n_orbitals, n_orbitals)
    """
    def __init__(self, molfile=""):
        """
        Args:
            molfile(str): the molecular file name
        """
        molfile = molfile.strip()
        if molfile[-5:] != ".hdf5":
            self.molfile = molfile + ".hdf5"
        else:
            self.molfile = molfile

        with h5py.File(self.molfile, "r") as f:
            self.n_orbitals = get_from_file("n_orbitals", f, 'int')
            self.n_electrons = get_from_file("n_electrons", f, 'int')
            self.nuclear_repulsion = get_from_file("nuclear_repulsion", f, 'float')
            self.one_body_integrals = get_from_file("one_body_integrals", f)
            self.two_body_integrals = get_from_file("two_body_integrals", f)

    def get_integrals(self):
        return self.one_body_integrals, self.two_body_integrals

    def save(self):
        with h5py.File("save_" + self.molfile, "w") as f:
            f.create_dataset("n_orbitals", data=str(self.n_orbitals))
            f.create_dataset("n_electrons", data=str(self.n_electrons))
            f.create_dataset("nuclear_repulsion", data=str(self.nuclear_repulsion))
            f.create_dataset("one_body_integrals", data=str(self.one_body_integrals))
            f.create_dataset("two_body_integrals", data=str(self.two_body_integrals))
