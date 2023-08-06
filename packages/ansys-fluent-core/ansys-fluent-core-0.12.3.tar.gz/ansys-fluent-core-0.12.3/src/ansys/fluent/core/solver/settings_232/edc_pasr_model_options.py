#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .edc_pasr_mixing_model import edc_pasr_mixing_model
from .mixing_constant import mixing_constant
from .fractal_dimension import fractal_dimension
class edc_pasr_model_options(Group):
    """
    'edc_pasr_model_options' child.
    """

    fluent_name = "edc-pasr-model-options"

    child_names = \
        ['edc_pasr_mixing_model', 'mixing_constant', 'fractal_dimension']

    edc_pasr_mixing_model: edc_pasr_mixing_model = edc_pasr_mixing_model
    """
    edc_pasr_mixing_model child of edc_pasr_model_options.
    """
    mixing_constant: mixing_constant = mixing_constant
    """
    mixing_constant child of edc_pasr_model_options.
    """
    fractal_dimension: fractal_dimension = fractal_dimension
    """
    fractal_dimension child of edc_pasr_model_options.
    """
