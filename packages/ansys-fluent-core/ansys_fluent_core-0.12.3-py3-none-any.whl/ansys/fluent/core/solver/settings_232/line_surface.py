#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .line_surface_child import line_surface_child

class line_surface(NamedObject[line_surface_child], _CreatableNamedObjectMixin[line_surface_child]):
    """
    'line_surface' child.
    """

    fluent_name = "line-surface"

    child_object_type: line_surface_child = line_surface_child
    """
    child_object_type of line_surface.
    """
