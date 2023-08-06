#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .isat_error_tolerance import isat_error_tolerance
from .isat_table_size import isat_table_size
from .isat_verbosity import isat_verbosity
from .clear_isat_table import clear_isat_table
class isat_options(Group):
    """
    'isat_options' child.
    """

    fluent_name = "isat-options"

    child_names = \
        ['isat_error_tolerance', 'isat_table_size', 'isat_verbosity']

    isat_error_tolerance: isat_error_tolerance = isat_error_tolerance
    """
    isat_error_tolerance child of isat_options.
    """
    isat_table_size: isat_table_size = isat_table_size
    """
    isat_table_size child of isat_options.
    """
    isat_verbosity: isat_verbosity = isat_verbosity
    """
    isat_verbosity child of isat_options.
    """
    command_names = \
        ['clear_isat_table']

    clear_isat_table: clear_isat_table = clear_isat_table
    """
    clear_isat_table command of isat_options.
    """
