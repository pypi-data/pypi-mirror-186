from uxdconverter.constants.atomic_scattering_factor import AtomicScatteringFactor
from uxdconverter.diffraction.crystal import CubicSpacing, BraggCondition, DiffractionContext
from uxdconverter.diffraction.unitcell import UnitCell
from uxdconverter.diffraction.structurefactor import StructureFactor
import numpy as np
from CifFile import ReadCif

#cif = ReadCif('9013014.cif')
cif = ReadCif('1000041.cif')

cif_data = cif[cif.keys()[0]]

symmetries = cif_data['_symmetry_equiv_pos_as_xyz']

cell = UnitCell()
if '_atom_type_symbol' in cif_data:
    atoms = cif_data['_atom_type_symbol']
elif '_atom_site_type_symbol' in cif_data:
    atoms = cif_data['_atom_site_type_symbol']
elif '_atom_site_label' in cif_data:
    atoms = cif_data['_atom_site_label']

for idx, atom in enumerate(atoms):
    x, y, z = float(cif_data['_atom_site_fract_x'][idx]), float(cif_data['_atom_site_fract_y'][idx]), float(cif_data['_atom_site_fract_z'][idx])
    for sym in symmetries:
        _x, _y, _z = eval(sym)
        cell.add_atom(atom, [_x, _y, _z])

af = AtomicScatteringFactor()

ctx = DiffractionContext()
bragg = BraggCondition(ctx, CubicSpacing({CubicSpacing.PARAMETER_A: 5.6393}))
sf = StructureFactor(cell, bragg, af)
