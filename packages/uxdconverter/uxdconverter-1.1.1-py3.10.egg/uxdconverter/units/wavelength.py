from periodictable.xsf import xray_wavelength
from uxdconverter.transition_energy.database import TransitionDatabase
from uxdconverter.units.si import SI

EMISSON_LINES = {
    'Ka1': 'KL3',
    'Ka2': 'KL2',
    'Kb': 'KM3',
    # Ka has to be the last element, as we iterate through it and it conflicts with Ka1
    'Ka': 'KL3',
}


class WavelengthError(Exception):
    pass


class Wavelength:
    @staticmethod
    def from_string(text, xray_database: TransitionDatabase):
        """
        Returns a wavelength parsed from a text in units of Angstrom
        :param text:
        :param xray_database:
        :return:
        """
        if any([emisson_line in text for emisson_line in EMISSON_LINES.keys()]):
            for emisson_line in EMISSON_LINES.keys():
                if not emisson_line in text:
                    continue

                element = text.replace(emisson_line, '').strip()
                transitions = xray_database.get_all_transitions(element, EMISSON_LINES[emisson_line])
                if len(transitions) != 1:
                    raise WavelengthError(f"Unknown transition line for '{text}'")
                # transition db returns in eV, xray-wavelength expects keV
                return xray_wavelength(transitions[EMISSON_LINES[emisson_line]]['experimental'] * 1e-3)

        try:
            if 'AA' in text or 'Ang' in text:
                wavelength = float(text.replace('AA', '').replace('Ang', ''))
            elif 'eV' in text:
                wavelength = SI.extract_number(text, 'eV')
            else:
                # Now we assume there is no unit, which means it should be Angstrom
                wavelength = float(text)

        except ValueError:
            raise WavelengthError(f"Input '{text}' could not be identified as an wavelength")

        if wavelength <= 0:
            raise WavelengthError("Wavelength has to be positive")

        return wavelength


