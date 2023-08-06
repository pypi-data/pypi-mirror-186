#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .point_surface import point_surface
from .line_surface import line_surface
from .rake_surface import rake_surface
from .plane_surface import plane_surface
class surfaces(Group):
    """
    'surfaces' child.
    """

    fluent_name = "surfaces"

    child_names = \
        ['point_surface', 'line_surface', 'rake_surface', 'plane_surface']

    point_surface: point_surface = point_surface
    """
    point_surface child of surfaces.
    """
    line_surface: line_surface = line_surface
    """
    line_surface child of surfaces.
    """
    rake_surface: rake_surface = rake_surface
    """
    rake_surface child of surfaces.
    """
    plane_surface: plane_surface = plane_surface
    """
    plane_surface child of surfaces.
    """
