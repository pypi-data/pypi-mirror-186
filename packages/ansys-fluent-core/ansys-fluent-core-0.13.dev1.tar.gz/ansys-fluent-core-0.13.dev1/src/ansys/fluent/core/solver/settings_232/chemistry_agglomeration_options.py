#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .chemistry_agglomeration_error_tolerance import chemistry_agglomeration_error_tolerance
from .chemistry_agglomeration_temperature_bin import chemistry_agglomeration_temperature_bin
class chemistry_agglomeration_options(Group):
    """
    'chemistry_agglomeration_options' child.
    """

    fluent_name = "chemistry-agglomeration-options"

    child_names = \
        ['chemistry_agglomeration_error_tolerance',
         'chemistry_agglomeration_temperature_bin']

    chemistry_agglomeration_error_tolerance: chemistry_agglomeration_error_tolerance = chemistry_agglomeration_error_tolerance
    """
    chemistry_agglomeration_error_tolerance child of chemistry_agglomeration_options.
    """
    chemistry_agglomeration_temperature_bin: chemistry_agglomeration_temperature_bin = chemistry_agglomeration_temperature_bin
    """
    chemistry_agglomeration_temperature_bin child of chemistry_agglomeration_options.
    """
