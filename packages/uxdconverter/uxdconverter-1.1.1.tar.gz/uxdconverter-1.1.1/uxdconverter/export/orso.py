HEADERS = [
    lambda ctx: f'# # ORSO reflectivity data file | 1.0 standard | YAML encoding | https://www.reflectometry.org/',
    lambda ctx: f'# # {ctx.get_title()} | {ctx.get_meta().get_date()} | {ctx.get_meta().get_sample_name()} | {ctx.get_meta().get_what()}'
]

class ORSOItem:
    pass

class ORSOEntry:
    def __init__(self, key, value):
        self.key = key,
        self.value = value,

    def get

class Optional(ORSOEntry):
    def __init__(self, entry_value):
        self.val = entry_value

    def get(self):
        pass


class MetaInformation:
    def __init__(self):
        pass

    def get_title(self):
        pass

    def get_date(self):
        pass

    def get_sample_name(self):
        pass

    def get_what(self):
        pass

class OwnerInformation(ORSOItem):

    def __init__(self):
        self.name = "Alexander Book"
        self.affiliation = "Technische Universität München; Heinz-Mair-Leibniz Zentrum (MLZ)"
        self.contact = "alexander.book@frm2.tum.de"

    def get(self):
        return {
            'name': self.name,
            'affiliation': self.affiliation,
            'contact': self.contact,
        }

class ExperimentInformation(ORSOItem):
    def __init__(self):
        pass

    def get(self):
        return {
            'title': self.title,
            'instrument': self.instrument,
            'start_date': self.date,
            'probe': self.probe,
            'facility': self.facility,
            'proposalID': self.proposalID,
            'doi': self.doi,
        }

class SampleInformation(ORSOItem):
    def __init__(self):
        pass

    def get(self):
        return {
            'name': self.name,
            'category': f'{self.category_front}/{self.category_back}',
            'composition': Optional(self.composition),
            'description': self.description,
            'environment': self.environment,
            'sample_parameters': self.sample_params,
        }


class DataSourceInformation:
    def __init__(self):
        pass

    def get_owner(self):
        pass

    def set_owner(self, name, affiliation, contact):
        pass