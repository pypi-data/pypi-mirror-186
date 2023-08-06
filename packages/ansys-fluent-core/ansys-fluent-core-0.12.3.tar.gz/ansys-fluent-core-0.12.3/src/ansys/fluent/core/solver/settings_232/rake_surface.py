#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .rake_surface_child import rake_surface_child

class rake_surface(NamedObject[rake_surface_child], _CreatableNamedObjectMixin[rake_surface_child]):
    """
    'rake_surface' child.
    """

    fluent_name = "rake-surface"

    child_object_type: rake_surface_child = rake_surface_child
    """
    child_object_type of rake_surface.
    """
