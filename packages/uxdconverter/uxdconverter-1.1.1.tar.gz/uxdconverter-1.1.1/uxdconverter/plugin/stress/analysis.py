import numpy as np
import pylab

from uxdconverter.ui.controller import Controller
from uxdconverter.plugin.stress.fit import CorrelatedTwoPeakFit
from uxdconverter.plugin.stress.psi_fit import LinearPsiFit
from uxdconverter.measurement import Measurements
from uxdconverter.operation import MultiMerger, MeasurementMerger, ErrorCalculation

from collections import defaultdict
from skipi.function import Function, NullFunction

NAME = 'stress'

class StressAnalysis(object):
    def __init__(self, controller: Controller):
        self._c = controller
        self._fitters = {}

    def group_measurements_by_psi(self, measurements):

        mss = measurements.get_measurements()

        grouped = defaultdict(list)

        for ms in mss:
            grouped[round(ms.get_psi(), 2)].append(ms)

        return grouped

    def merge_group(self, group):
        multi_merge = MultiMerger(MeasurementMerger())
        merged = {}
        for psi, mss in group.items():
            merge = multi_merge.merge(mss)
            merge = ErrorCalculation().manipulate(merge, self._c._settings_controller.get_measurement_context())
            theta, dtheta, counts, dcounts = zip(*merge.get_data())
            theta = np.array(theta)
            dx = Function.to_function(theta, dtheta)
            dy = Function.to_function(theta, dcounts)
            merged[psi] = Function.to_function(theta, counts, dx=dx, dy=dy)

        return merged

    def analyze(self):
        measurements = self._c.measurements # type: uxdconverter.measurement.Measurements
        psi_measurement_dict = self.merge_group(self.group_measurements_by_psi(measurements))

        wavelength_k1 = 0.70931724
        wavelength_k2 = 0.71360728


        psis = []
        thetas = []

        for psi, fctn in psi_measurement_dict.items():
            if not( psi in self._fitters.keys()):
                self._fitters[psi] = CorrelatedTwoPeakFit(fctn, wavelength_k1, wavelength_k2)

            fitter = self._fitters[psi]

            fit = fitter.get_fit()
            fitter.plot()
            print(fit.fit_report(show_correl=False))
            if fit.redchi > 1000:
                continue

            psis.append(psi)
            thetas.append(fitter.get_peak_position())

        pylab.show()
        pylab.figure()
        pylab.xlabel("$sin^2(\psi)$")
        pylab.ylabel("lattice spacing $[\AA]$")

        f = Function.to_function(psis, np.array(thetas))
        trafo_to_lattice = lambda psi, theta: wavelength_k1 / (2 * np.sin(np.deg2rad(theta)))
        dy_traf = lambda psi, theta: np.abs(trafo_to_lattice(psi, theta) / np.tan(np.deg2rad(theta)))
        dy_scale = f.transform(dy_traf)
        dy_traf = lambda psi, dtheta: dtheta * dy_scale(psi)

        f = f.transform(trafo_to_lattice, trafo_dy=dy_traf)

        if f.get_dom().min() < 0:
            fneg = self._to_sin_sqr(f.vremesh((None, 0)))
        else:
            fneg = NullFunction(f.get_dom())

        if f.get_dom().max() > 0:
            fpos = self._to_sin_sqr(f.vremesh((0, None), dstart=-1))
        else:
            fpos = NullFunction(f.get_dom())

        fpos.plot(label='$\psi \geq 0$')
        fneg.plot(label='$\psi < 0$')

        self.analyze_psi(fpos)
        self.analyze_psi(fneg)

        pylab.show()

        return f

    def _to_sin_sqr(self, fctn):
        psi = fctn.get_domain()
        theta = fctn.eval()
        sinsqrd = np.fromiter(map(lambda x: np.sin(np.deg2rad(x)) ** 2, psi), float)
        dy = fctn.dy
        if not dy.is_null():
            dy = Function.to_function(sinsqrd, dy.eval())

        return Function.to_function(sinsqrd, theta, dy=dy)

    def plot_lin_fit(self, fit, function):
        comps = fit.eval_components(x=function.get_domain())
        pylab.plot(function.get_domain(), comps['Lin_'])

    def analyze_psi(self, f):
        if f.is_null():
            return

        fit = LinearPsiFit(f).get_fit()
        print(fit.fit_report(show_correl=False))
        self.plot_lin_fit(fit, f)
