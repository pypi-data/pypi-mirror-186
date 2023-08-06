#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .p0 import p0
from .p1 import p1
from .number_of_points import number_of_points
class rake_surface_child(Group):
    """
    'child_object_type' of rake_surface.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['p0', 'p1', 'number_of_points']

    p0: p0 = p0
    """
    p0 child of rake_surface_child.
    """
    p1: p1 = p1
    """
    p1 child of rake_surface_child.
    """
    number_of_points: number_of_points = number_of_points
    """
    number_of_points child of rake_surface_child.
    """
