import numpy as np

from collections import defaultdict


class UnitCell:
    def __init__(self):
        self._atoms = defaultdict(list)

    def add_atom(self, element, pos):
        element = element.lower()
        pos = np.array(pos)

        if self._exists(element, pos):
            return

        if all(pos >= 0) and all(pos < 1):
            self._atoms[element].append(pos)

    def _exists(self, element, pos):
        if element in self._atoms:
            for base in self._atoms[element]:
                if all(base == pos):
                    return True

        return False

    def get_atoms(self):
        return list(map(lambda x: x.capitalize(), self._atoms.keys()))

    def get_positions(self, element):
        element = element.lower()
        return self._atoms[element]