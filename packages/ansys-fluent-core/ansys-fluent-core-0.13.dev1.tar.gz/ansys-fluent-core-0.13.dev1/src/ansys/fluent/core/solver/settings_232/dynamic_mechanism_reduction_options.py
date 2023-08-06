#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .dynamic_mechanism_reduction_tolerance import dynamic_mechanism_reduction_tolerance
from .dynamic_mechanism_reduction_expert import dynamic_mechanism_reduction_expert
from .dynamic_mechanism_reduction_min_target import dynamic_mechanism_reduction_min_target
from .dynamic_mechanism_reduction_targets import dynamic_mechanism_reduction_targets
class dynamic_mechanism_reduction_options(Group):
    """
    'dynamic_mechanism_reduction_options' child.
    """

    fluent_name = "dynamic-mechanism-reduction-options"

    child_names = \
        ['dynamic_mechanism_reduction_tolerance',
         'dynamic_mechanism_reduction_expert',
         'dynamic_mechanism_reduction_min_target',
         'dynamic_mechanism_reduction_targets']

    dynamic_mechanism_reduction_tolerance: dynamic_mechanism_reduction_tolerance = dynamic_mechanism_reduction_tolerance
    """
    dynamic_mechanism_reduction_tolerance child of dynamic_mechanism_reduction_options.
    """
    dynamic_mechanism_reduction_expert: dynamic_mechanism_reduction_expert = dynamic_mechanism_reduction_expert
    """
    dynamic_mechanism_reduction_expert child of dynamic_mechanism_reduction_options.
    """
    dynamic_mechanism_reduction_min_target: dynamic_mechanism_reduction_min_target = dynamic_mechanism_reduction_min_target
    """
    dynamic_mechanism_reduction_min_target child of dynamic_mechanism_reduction_options.
    """
    dynamic_mechanism_reduction_targets: dynamic_mechanism_reduction_targets = dynamic_mechanism_reduction_targets
    """
    dynamic_mechanism_reduction_targets child of dynamic_mechanism_reduction_options.
    """
