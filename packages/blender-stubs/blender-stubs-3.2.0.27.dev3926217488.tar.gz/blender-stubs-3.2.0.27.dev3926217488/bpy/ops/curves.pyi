"""


Curves Operators
****************

:func:`convert_from_particle_system`

:func:`convert_to_particle_system`

:func:`sculptmode_toggle`

:func:`select_all`

:func:`set_selection_domain`

:func:`snap_curves_to_surface`

:func:`surface_set`

"""

import typing

def convert_from_particle_system() -> None:

  """

  Add a new curves object based on the current state of the particle system

  """

  ...

def convert_to_particle_system() -> None:

  """

  Add a new or update an existing hair particle system on the surface object

  """

  ...

def sculptmode_toggle() -> None:

  """

  Enter/Exit sculpt mode for curves

  """

  ...

def select_all(action: str = 'TOGGLE') -> None:

  """

  (De)select all control points

  """

  ...

def set_selection_domain(domain: str = 'POINT') -> None:

  """

  Change the mode used for selection masking in curves sculpt mode

  """

  ...

def snap_curves_to_surface(attach_mode: str = 'NEAREST') -> None:

  """

  Move curves so that the first point is exactly on the surface mesh

  """

  ...

def surface_set() -> None:

  """

  Use the active object as surface for selected curves objects and set it as the parent

  """

  ...
