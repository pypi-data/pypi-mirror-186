#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .multi_component_diffusion_mf_child import multi_component_diffusion_mf_child

class extrapolate_eqn_vars(NamedObject[multi_component_diffusion_mf_child], _NonCreatableNamedObjectMixin[multi_component_diffusion_mf_child]):
    """
    Enter the extrapolation menu.
    """

    fluent_name = "extrapolate-eqn-vars"

    child_object_type: multi_component_diffusion_mf_child = multi_component_diffusion_mf_child
    """
    child_object_type of extrapolate_eqn_vars.
    """
