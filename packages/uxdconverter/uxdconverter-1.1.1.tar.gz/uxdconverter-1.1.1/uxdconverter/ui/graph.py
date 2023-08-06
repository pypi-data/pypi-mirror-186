import matplotlib.pyplot as plt

from typing import List
from uxdconverter.measurement import Measurement, MeasurementContext


class Plotting(object):
    def plot(self, measurement: List[Measurement], context: MeasurementContext, names=None, counts=False):
        """
        Plots the measurement.

        If measurement is of type list, each measurement in the list is plotted in the same graph.

        :param Measurement measurement: Single measurement or a list if measurements.
        :param MeasurementContext context: Measurement context (conditions). required for plotting eg. the x-axis as
                    q (wavevector transfer) or in Theta (incidence angle)
        :param names: List of names (str) for the measurement
        :param counts: Bool, plot the reflectivity in counts (not recommended)
        :return: None
        """

        if names is not None and not len(names) == len(measurement):
            raise ValueError("Given names must have the same length as measurements")

        handles = []
        for ms in measurement:
            data = ms.get_data()
            x = [x[0] for x in data]
            x_err = [x[1] for x in data]
            y = [x[2] for x in data]
            y_err = [x[3] for x in data]

            handles.append(plt.errorbar(x, y, xerr=x_err, yerr=y_err, markeredgewidth=1, capsize=2))

        if names is not None:
            plt.legend(handles, names)

        if context.qz_conversion:
            plt.xlabel(r'$q_z$ $[A^{-1}]$')
        else:
            plt.xlabel(r'$\theta$ [deg]')

        if context.y_log_scale:
            prefix = '$log$'
        else:
            prefix = ''

        if not counts:
            suffix = "Reflectivity [1]"
        else:
            suffix = "Counts $[1]$"

        label = '{} {}'.format(prefix, suffix)

        plt.ylabel(label)

        if context.y_log_scale:
            plt.yscale('log')

        plt.show()

    def interactive_plot(self, measurement: Measurement, signal=None):
        data = measurement.get_data()

        x = [x[0] for x in data]
        y = [x[2] for x in data]
        global picked, norm
        picked = []
        norm = None

        plt.plot(x, y)
        plt.yscale('log')

        # plt.show()

        def on_click(event):
            global picked, norm
            if event.button == 1:
                if event.inaxes:
                    print('Picked coords %f %f' % (event.xdata, event.ydata))
                    picked.append((event.xdata, event.ydata))

            if event.dblclick:
                norm = [event.xdata, event.ydata]
                if not signal is None:
                    signal.sig.emit(norm)

        def on_keyboard(event):
            global picked, norm
            if event.key == 'x' and len(picked) > 0:
                norm = picked[-1]
                picked = []

        plt.gcf().canvas.mpl_connect('button_press_event', on_click)
        plt.gcf().canvas.mpl_connect('key_press_event', on_keyboard)
        plt.show()

        return norm
