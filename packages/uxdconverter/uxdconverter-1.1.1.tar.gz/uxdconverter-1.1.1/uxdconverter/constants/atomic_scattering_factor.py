import os
import numpy as np

FILE_PATH = os.path.join(os.path.dirname(__file__), "data/atomic_form_factor_approximation.dat")

class AtomicScatteringFactor(object):
    def __init__(self):
        self._d = self._load_data()

    def _load_data(self):
        keys = map(lambda x: x.lower(), np.loadtxt(FILE_PATH, usecols=[0], dtype=np.str))
        d = np.loadtxt(FILE_PATH, usecols=range(1, 10))

        return dict(zip(keys, d))

    def by_element(self, element):
        constants = self._d.get(element.lower(), None)

        if constants is None:
            raise RuntimeError(f"Unknown element {element}")

        a_s = constants[slice(0, 8, 2)]
        b_s = constants[slice(1, 9, 2)]
        c = constants[8]

        # f(q) = sum_i a_i * exp(-b * (q/4pi)^2) + c
        return lambda q: np.dot(a_s, np.exp(np.outer(-b_s, (q/4/np.pi)**2))) + c

    def get_factor(self, element, q):
        fs = self.by_element(element)(q)

        if isinstance(q, float) or isinstance(q, int):
            return fs[0]
        return fs
