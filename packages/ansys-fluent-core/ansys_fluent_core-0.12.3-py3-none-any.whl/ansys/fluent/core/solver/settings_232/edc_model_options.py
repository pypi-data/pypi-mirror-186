#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .edc_choice import edc_choice
from .edc_constant_coefficient_options import edc_constant_coefficient_options
from .edc_pasr_model_options import edc_pasr_model_options
from .user_defined_edc_scales import user_defined_edc_scales
class edc_model_options(Group):
    """
    'edc_model_options' child.
    """

    fluent_name = "edc-model-options"

    child_names = \
        ['edc_choice', 'edc_constant_coefficient_options',
         'edc_pasr_model_options', 'user_defined_edc_scales']

    edc_choice: edc_choice = edc_choice
    """
    edc_choice child of edc_model_options.
    """
    edc_constant_coefficient_options: edc_constant_coefficient_options = edc_constant_coefficient_options
    """
    edc_constant_coefficient_options child of edc_model_options.
    """
    edc_pasr_model_options: edc_pasr_model_options = edc_pasr_model_options
    """
    edc_pasr_model_options child of edc_model_options.
    """
    user_defined_edc_scales: user_defined_edc_scales = user_defined_edc_scales
    """
    user_defined_edc_scales child of edc_model_options.
    """
