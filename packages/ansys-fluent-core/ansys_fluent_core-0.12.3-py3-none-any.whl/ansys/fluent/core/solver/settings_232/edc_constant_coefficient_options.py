#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .volume_fraction_constant import volume_fraction_constant
from .time_scale_constant_1 import time_scale_constant
class edc_constant_coefficient_options(Group):
    """
    'edc_constant_coefficient_options' child.
    """

    fluent_name = "edc-constant-coefficient-options"

    child_names = \
        ['volume_fraction_constant', 'time_scale_constant']

    volume_fraction_constant: volume_fraction_constant = volume_fraction_constant
    """
    volume_fraction_constant child of edc_constant_coefficient_options.
    """
    time_scale_constant: time_scale_constant = time_scale_constant
    """
    time_scale_constant child of edc_constant_coefficient_options.
    """
