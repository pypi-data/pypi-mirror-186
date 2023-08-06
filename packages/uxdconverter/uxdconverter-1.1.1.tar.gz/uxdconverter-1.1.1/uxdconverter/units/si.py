SI_PREFIX = {
    'P': 1e15,
    'T': 1e12,
    'G': 1e9,
    'M': 1e6,
    'k': 1e3,
    'd': 1e-1,
    'c': 1e-2,
    'm': 1e-3,
    'µ': 1e-6,
    'n': 1e-9,
    'p': 1e-12,
    'f': 1e-15,
    '': 1e0
}

class SIError(Exception):
    pass


class SI(object):

    @staticmethod
    def extract_number(text, unit):
        if not unit in text:
            raise SIError(f"Text '{text}' does not contain the unit '{unit}'")

        for prefix, factor in SI_PREFIX.items():
            fullunit = f"{prefix}{unit}"
            if fullunit in text:
                number = float(text.replace(fullunit, ''))
                return number * factor

        raise SIError(f"Could not extract from '{text}' a number with unit '{unit}'")
