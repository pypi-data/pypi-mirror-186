import os

class TransitionDatabase(object):
    def __init__(self):
        self._db = {}
        self._load()

    def _load(self):
        converter = {
            0: str,  # Element name
            1: lambda x: int(x) if x != '' else 0,  # mass number
            3: float,  # Theory
            5: float,  # Exp. Direct
            7: float,  # Exp. Combined
            9: float,  # Exp. Vapor
        }


        file = os.path.join(os.path.dirname(__file__), "nist-energy-database.dat")
        with open(file, 'r') as fobj:
            for line in fobj:
                line = line.strip("\n")
                if line.startswith('#'):
                    continue

                data = line.split("\t")


                for key in converter.keys():
                    try:
                        data[key] = converter[key](data[key])
                    except:
                        pass

                if data[1] == 0:
                    name = data[0]
                else:
                    name = data[0] + "-" + str(data[1])

                if not name in self._db:
                    self._db[name] = {}

                values = {
                    'theory': 0, 'experimental': 0
                }

                # this selects first theoretical energy
                # then the exp. vapor energy, which will be overwritten by exp. combined if it exists
                # and so on...
                for idx, key in zip([3, 9, 7, 5], ['theory'] + 3*['experimental']):
                    try:
                        if data[idx] > 0:
                            values[key] = data[idx]
                    except:
                        pass

                self._db[name][data[2]] = values

    def get_elements(self):
        return self._db.keys()

    def get_all_transitions(self, element, filter=''):
        if filter == '':
            return self._db[element]
        else:
            res = {}

            if not element in self._db.keys():
                return []

            for transition in self._db[element].keys():
                if transition.startswith(filter):
                    res[transition] = self._db[element][transition]
        return res

    def find_all(self, name):
        if name == '':
            return []

        elements = self._db.keys()
        result = []
        for element in elements:
            if element.startswith(name):
                result.append(element)

        return result