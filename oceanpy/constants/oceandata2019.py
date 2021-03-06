# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Oceanography constants in SI units.  See :mod:`oceanpy.constants`
for a complete listing of constants defined in Oceanpy.
"""
import numpy as np

import unyt

# May generate a Unit Registry some day

# Earth day
T_earth = 86164 * unyt.s
unyt.define_unit('T_earth', T_earth)

# Rotation rate of the Earth
Omega_earth = 2*np.pi/T_earth
unyt.define_unit('Omega_earth', Omega_earth)

# Density of water -- T=25 deg C, S=35 g/kg, P = 1 atm
density_seawater = 1023.6 * unyt.kg / unyt.m**3
unyt.define_unit('density_seawater', density_seawater)
