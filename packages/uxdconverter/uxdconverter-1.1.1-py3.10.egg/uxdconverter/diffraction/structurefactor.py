import numpy as np


from .unitcell import UnitCell
from .crystal import BraggCondition
from uxdconverter.constants.atomic_scattering_factor import AtomicScatteringFactor


class StructureFactor:
    def __init__(self, unitcell: UnitCell, bragg: BraggCondition, atomicfactor: AtomicScatteringFactor):
        self._cell = unitcell
        self._bragg = bragg
        self._af = atomicfactor

    def get_sf(self, h, k, l):
        return self.get_structurefactor(h, k, l)

    def get_structurefactor(self, h, k, l):
        sf = 0
        q = self._bragg.get_q(h, k, l)
        for element in self._cell.get_atoms():
            f = self._af.by_element(element)
            for pos in self._cell.get_positions(element):
                sf += f(q) * np.exp(-1j * 2 * np.pi * np.dot([h, k, l], pos))

        return sf[0]

    def get(self, h, k, l):
        return np.abs(self.get_structurefactor(h, k, l))