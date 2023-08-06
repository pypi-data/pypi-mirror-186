import numpy as np
import scipy.optimize as opt


def gauss(x, p):
    return 1.0 / (p[1] * np.sqrt(2 * np.pi)) * np.exp(-(x - p[0]) ** 2 / (2 * p[1] ** 2))


def fit_gaussian(x, y, mu=0, sigma=1):
    assert len(x) == len(y)

    xmin, xmax = np.min(x), np.max(x)
    n = len(x)

    y /= ((xmax - xmin) / n) * sum(y)

    p0 = [mu, sigma]

    f = lambda p, x, y: gauss(x, p) - y
    p1, suc = opt.leastsq(f, p0[:], args=(x, y))

    mu, sigma = p1

    return mu, sigma


def sigma2fwhm(sigma):
    return np.sqrt(8 * np.log(2)) * sigma


def fwhm2sigma(fwhm):
    return 1 / np.sqrt(8 * np.log(2)) * fwhm


def load_file(file):
    "/mnt/hektor/measure/Dünnschicht/01_X-ray_Messdaten/01_Alex/Detector_Scan_deltaTheta.raw"
    from uxdconverter.parser.general import GeneralParser
    measurements = GeneralParser().parse(file, None)
    data = measurements.get_measurement(0).get_data()
    x, y = data.T[0], data.T[2]
    return x, y


def find_fwhm(file):
    x, y = load_file(file)

    mu, sigma = fit_gaussian(x, y)
    return sigma2fwhm(sigma)


def plot_fwhm(x, y):
    import pylab

    norm = (np.max(x) - np.min(x)) / len(x) * sum(y)

    pylab.plot(x, y / norm)
    x_space = np.linspace(np.min(x), np.max(x), len(x))

    mu, sigma = fit_gaussian(x, y)
    fit_y = gauss(x_space, [mu, sigma])
    pylab.plot(x_space, fit_y)
    fwhm = sigma2fwhm(sigma)
    pylab.axvspan(mu - fwhm / 2, mu + fwhm / 2, facecolor='g', alpha=0.5)
    pylab.show()
