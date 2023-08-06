import pylab
import numpy as np

from uxdconverter.util import UXDFileLoader
from uxdconverter.plugin.stress.fit import CorrelatedTwoPeakFit
from skipi.function import Function, FunctionFileLoader, Derivative

data = []
dmax = []

wavelength_k1 = 0.70931724
wavelength_k2 = 0.71360728

for psi in range(-8, 10):
    f = UXDFileLoader("data/psi_{}.xrdml.dat".format(psi)).from_file()

    fitter = CorrelatedTwoPeakFit(f, wavelength_k1, wavelength_k2)
    # fitter.set_parameter_hint_function(hint_function)
    model, params = fitter.get_model()

    fit = fitter.get_fit()
    #fig, gs = fitter.plot()

    data.append((psi, fitter.get_peak_position()))
    dmax.append((psi, f.argmax()))

    print(fit.fit_report(show_correl=False))
pylab.show()


def function_to_sin(fctn: Function):
    psi = fctn.get_domain()
    theta = fctn.eval()
    sinsqrd = np.fromiter(map(lambda x: np.sin(np.deg2rad(x)) ** 2, psi), float)
    dy = fctn.dy
    if dy is not None:
        dy = Function.to_function(sinsqrd, dy.eval())

    return Function.to_function(sinsqrd, theta, dy=dy)

def function_to_d(fctn: Function):
    return fctn.transform(lambda sin, theta: wavelength_k1 / (2*np.sin(np.deg2rad(theta))))

# data = dmax
psi, theta = zip(*data)
psi = np.array(psi)
f = Function.to_function(psi, theta)
fpos = function_to_d(function_to_sin(f.vremesh((0, None), dstart=-1)))
fneg = function_to_d(function_to_sin(f.vremesh((None, 0))))

pylab.xlabel(xlabel="$\sin^2 \psi")

fpos.plot(label='$\psi > 0$')
fneg.plot(show=True, label='$\psi < 0$', )
