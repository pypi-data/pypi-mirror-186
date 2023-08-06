import codecs
import datetime
import yaml
import os

from uxdconverter.measurement import Measurement
from uxdconverter.measurement import MeasurementContext
from uxdconverter import __version__


class AbstractExportAlgorithm(object):
    def __init__(self, measurement: Measurement, ctx: MeasurementContext):
        self._ms = measurement
        self._ctx = ctx

    def export(self) -> str:
        raise NotImplementedError()


class FileExporter(object):
    def __init__(self, output_file, export_algorithm: AbstractExportAlgorithm):
        self._file = output_file
        self._alg = export_algorithm

    def do_export(self):
        fp = codecs.open(self._file, 'w')
        fp.write(self._alg.export())
        fp.close()


class ParrattExportAlgorithm(AbstractExportAlgorithm):

    def export(self):

        measurement = self._ms
        ctx = self._ctx

        if not ctx.qz_conversion:
            header = {
                'column 1': 'Theta / deg',
                'column 2': 'sigma Theta / deg , standard deviation',
                'column 3': 'R(Theta)',
                'column 4': 'sigma R(Theta), standard deviation'
            }
        else:
            header = {
                'column 1': 'Qz / Aa^-1',
                'column 2': 'sigma Qz / Aa^-1, standard deviation',
                'column 3': 'R(Qz)',
                'column 4': 'sigma R(Theta), standard deviation'
            }

        data_line = 999 * [""]

        data = measurement.get_data()

        header = "# " + yaml.dump(header).replace('\n', '\n# ') + "\n"
        # write out at most 1000 lines. Parratt cannot handle more than that...
        for idx in range(min(len(data), 999)):
            x = "{:.4E}".format(data[idx][0])
            err_x = "{:.4E}".format(data[idx][1])
            y = "{:.4E}".format(data[idx][2])
            err_y = "{:.4E}".format(data[idx][3])

            data_line[idx] = "\t".join([x, err_x, y, err_y])

        return header + "\n".join(data_line).strip()


class ORSOExportAlgorithm(AbstractExportAlgorithm):
    def export(self):
        header = self._create_headers()
        d_to_str = lambda d: "\t".join(map(lambda v: "{:.4E}".format(v), d))
        data = "\n".join([d_to_str(d) for d in self._ms.get_data()]).strip()

        h = "# " + yaml.dump(header).replace('\n', '\n# ')
        return h + "\n" + data

    def _file(self, file):
        try:
            created = datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime("%Y/%m/%d/%H:%M:%S")
        except:
            created = 'Unknown'

        return {
            'file': file,
            'created': created
        }


    def set_used_data_files(self, files):
        self._data_files = [
            self._file(file) for file in files
        ]

    def set_used_background_files(self, files):
        self._bkgrd_files = [
            self._file(file) for file in files
        ]

    @classmethod
    def as_list(cls, ls):
        s = ", ".join(map(str, ls))
        return "["+s+"]"

    def _create_headers(self):

        if not self._ctx.qz_conversion:
            data = {
                'column 1': 'Theta # deg',
                'column 2': 'sigma Theta # deg , standard deviation',
                'column 3': 'R(Theta)',
                'column 4': 'sigma R(Theta), standard deviation'
            }
        else:
            data = {
                'column 1': 'Qz # Aa^-1',
                'column 2': 'sigma Qz # Aa^-1, standard deviation',
                'column 3': 'R(Qz)',
                'column 4': 'sigma R(Theta), standard deviation'

            }
        data['separator'] = "\t"

        headers = {
            'reflectivity data file': 'orso file format 0.0',
            'creator': {
                'creator': 'Alexander Book',
                'affiliation': 'TUM',
                'time': datetime.datetime.now().strftime("%Y/%m/%d/%H:%M:%S")
            },
            'data source': {
                'origin': {
                    'owner': 'Alexander Book, TUM',
                    'facility': 'Technische Universitaet Muenchen, E21',
                },
                'experiment': {
                    'instrument': 'X-Ray Reflectometer D5000',
                    'probe': 'x-rays',
                    'measurement': {
                        'angular range': self.as_list(self._ctx.qz_range) + " # deg" if self._ctx.qz_conversion is False else '',
                        'scheme': 'angle-dispersive',
                        'wavelength': self._ctx.get_wavelength(),
                        'wavelength unit': 'Aa',
                    },
                    'sample': {
                        'name': '', # TODO,
                    }
                }
            },
            'reduction': {
                'software': {
                    'programm': 'UXDConverter',
                    'version': __version__,
                    'call': 'via gui',
                    'corrections': {
                        'footprint': not self._ctx.knife_edge,
                    }
                },
                'parameters': {
                    'wavelength': str(self._ctx.get_wavelength()) + " # Aa",
                    'error wavelength': str(self._ctx.wavelength_error) + ' # Aa, standard deviation',
                    'error theta': str(self._ctx.theta_error) + ' # deg, standard deviation',
                    'sample length': str(self._ctx.sample_length) + ' # mm',
                    'beam width': str(self._ctx.xray_width) + ' # mm',
                    'data range': self.as_list(self._ctx.qz_range) + (" # Aa" if self._ctx.qz_conversion else " # deg")
                },
                'input files': {
                    'background': self._bkgrd_files,
                    'data': self._data_files,
                }
            },
            'data': data
        }

        return headers
