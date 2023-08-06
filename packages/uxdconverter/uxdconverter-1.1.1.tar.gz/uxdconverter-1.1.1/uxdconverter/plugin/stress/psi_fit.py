import lmfit
import numpy as np

from skipi.function import Function
from lmfit.models import LinearModel


class LinearPsiFit():
    def __init__(self, psi_vs_d: Function):
        self._f = psi_vs_d
        self._fit = None
        self._model = None
        self._params = None

    def _setup_model(self):
        lin = LinearModel(prefix='Lin_')

        model = lin

        psi_min, psi_max = self._f.get_domain()[0], self._f.get_domain()[-1]
        slope = (self._f(psi_max) - self._f(psi_min)) / (psi_max - psi_min)

        lin.set_param_hint('intercept', value=self._f(0))
        lin.set_param_hint('slope', value=slope)

        params = lin.make_params()

        return model, params

    def get_model(self):
        if self._model is None:
            self._model, self._params = self._setup_model()
        return self._model, self._params

    def fit(self):
        model, params = self.get_model()

        f = self._f

        sin_psi = f.get_domain()
        lattice = f.eval()

        weights = None
        if not f.dy.is_null():
            weights = 1 / f.dy.eval()
        #idx = np.isfinite(weights)
        idx = np.isfinite(lattice)
        weights=None
        #idx = np.logical_and(np.logical_and(np.isfinite(sin_psi), np.isfinite(lattice)), np.isfinite(weights))

        return model.fit(lattice[idx], params, x=sin_psi[idx])

    def clear(self):
        self._fit, self._model, self._params = None, None, None

    def get_fit(self):
        if self._fit is None:
            self._fit = self.fit()

        return self._fit
