from enum import Enum

class DataNormalizationMethod(Enum):
    FLANK = 'flank'
    MAX = 'max'
    FACTOR = 'factor'