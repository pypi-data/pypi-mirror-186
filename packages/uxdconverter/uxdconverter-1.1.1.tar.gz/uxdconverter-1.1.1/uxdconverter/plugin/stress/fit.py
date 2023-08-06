import lmfit
import numpy as np

from uxdconverter.measurement import Measurement
from skipi.function import Function
from lmfit.models import GaussianModel, ConstantModel, LinearModel, VoigtModel, PseudoVoigtModel, \
    LorentzianModel, SkewedVoigtModel, SkewedGaussianModel

from uncertainties import ufloat


class AbstractFit(object):
    def fit(self):
        pass

    def plot(self):
        pass

    def get_peak_position(self):
        pass


class CorrelatedTwoPeakFit(AbstractFit):
    def __init__(self, xrd_measurement: Function, wavelength_Kalpha1, wavelength_Kalpha2):
        self._f = xrd_measurement
        self._l1 = wavelength_Kalpha1
        self._l2 = wavelength_Kalpha2
        self._fit = None
        self._model = None
        self._params = None
        self._peaks = [PseudoVoigtModel, GaussianModel]
        self._hint_fctn = None

    def plot(self):
        fit = self.get_fit()
        fig, ax = fit.plot(data_kws={'linestyle': '-', 'marker': '1'})
        axis = fig.get_axes()[1]

        p1 = fit.result.params['Peak_KAlpha1_center']
        p2 = fit.result.params['Peak_KAlpha2_center']

        axis.axvline(p1.value)
        axis.axvline(p2.value)

        try:
            axis.axvspan(p1.value - p1.stderr, p1.value + p1.stderr, color='red', alpha=0.5)
            axis.axvspan(p1.value - 2 * p1.stderr, p1.value + 2 * p1.stderr, color='red', alpha=0.25)
            axis.axvspan(p2.value - p2.stderr, p2.value + p2.stderr, color='red', alpha=0.5)
            axis.axvspan(p2.value - 2 * p2.stderr, p2.value + 2 * p2.stderr, color='red', alpha=0.25)
        except:
            pass

        comps = fit.eval_components(x=self._f.get_domain())
        axis.plot(self._f.get_domain(), comps['Peak_KAlpha1_'])
        axis.plot(self._f.get_domain(), comps['Peak_KAlpha2_'])
        axis.plot(self._f.get_domain(), comps['Background_'])
        # axis.axhline(comps['Background_intercept'])

        fig.show()
        return fig, ax

    def set_peak_model(self, peak_id, model):
        self._model[peak_id] = model

    def set_parameter_hint_function(self, fctn):
        self._hint_fctn = fctn

    def apply_parameter_hints(self, model):
        peak_k1 = model.components[0]
        peak_k2 = model.components[1]
        bkgrd = model.components[2]
        # bkgrd_2 = model.components[3]

        peak_k1.set_param_hint('center', value=self._f.argmax(), vary=True, min=self._f.get_dom().min(),
                               max=self._f.get_dom().max())
        peak_k1.set_param_hint('amplitude', value=self._f.max(), min=0)
        peak_k1.set_param_hint('gamma', value=0, vary=False)
        peak_k1.set_param_hint('sigma', value=0.04)

        # This is the correlation function between the K alpha1 peak and K alpha2 peak
        #
        # theta_2 = arcsin( lambda_2 / lambda_1 * sin(theta_1) )
        #
        # where the wavelength lambda_i is for K alpha_i radiation and theta_1 is the peak position
        # for the K alpha_1 radiation
        # The 180/pi is included for transforming from deg to rad.
        peak_correlation_expr = 'arcsin({}*sin(Peak_KAlpha1_center/180*pi))*180/pi'.format(
            self._l2 / self._l1)
        peak_2_center = np.rad2deg(np.arcsin(self._l2 / self._l1 * np.deg2rad(self._f.argmax())))
        peak_k2.set_param_hint('center', vary=False, expr=peak_correlation_expr)

        peak_k2.set_param_hint('amplitude', value=self._f.max() / 2, min=0)
        peak_k2.set_param_hint('sigma', value=0.04)

        bkgrd.set_param_hint('intercept', value=self._f.min(), min=0)
        bkgrd.set_param_hint('slope', value=0)
        # return
        # bkgrd_2.set_param_hint('center', value=self._f.argmax(), vary=True)
        # bkgrd_2.set_param_hint('height', value=self._f.min(), min=0)
        # bkgrd.set_param_hint('sigma', value=5)

    def get_model(self):
        if self._model is None:
            self._model, self._params = self._setup_model()
            if self._hint_fctn is not None:
                self._hint_fctn(self._params)

        return self._model, self._params

    def _setup_model(self):
        peak_k1 = self._peaks[0](prefix='Peak_KAlpha1_')
        peak_k2 = self._peaks[1](prefix='Peak_KAlpha2_')
        bkgrd = LinearModel(prefix='Background_')
        # bkgrd_2 = GaussianModel(prefix='Background_Gauss_')

        model = peak_k1 + peak_k2 + bkgrd  # + bkgrd_2

        self.apply_parameter_hints(model)

        params = bkgrd.make_params()
        # params = peak_k1.make_params()
        params.update(peak_k1.make_params())
        params.update(peak_k2.make_params())
        # params.update(bkgrd_2.make_params())

        return model, params

    def fit(self):
        model, params = self.get_model()

        f = self._f

        if False:
            dx = self._f.get_dom().dx()

            p1 = self._f.argmax()
            p2 = np.rad2deg(np.arcsin(self._l2 / self._l1 * np.deg2rad(self._f.argmax())))
            n = 6
            f = self._f.vremesh((p1 - n * dx, p2 + n * dx))

        theta = f.get_domain()
        intensity = f.eval()

        weights = None
        if not f.dy.is_null():
            weights = 1 / f.dy.eval()

        return model.fit(intensity, params, x=theta, weights=weights)

    def clear(self):
        self._fit, self._model, self._params = None, None, None

    def get_fit(self):
        if self._fit is None:
            self._fit = self.fit()

        return self._fit

    def get_peak_position(self):
        fit = self.get_fit()
        nom, err = 0, 0

        try:
            nom = fit.result.params['Peak_KAlpha1_center'].value
            err = fit.result.params['Peak_KAlpha1_center'].stderr
        except:
            return ufloat(0, 0)

        if err is None:
            err = 0

        return ufloat(nom, err)
