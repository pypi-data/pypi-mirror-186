#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .integration_method import integration_method
from .integration_options import integration_options
from .isat_options import isat_options
from .chemistry_agglomeration import chemistry_agglomeration
from .chemistry_agglomeration_options import chemistry_agglomeration_options
from .dynamic_mechanism_reduction import dynamic_mechanism_reduction
from .dynamic_mechanism_reduction_options import dynamic_mechanism_reduction_options
from .dimension_reduction import dimension_reduction
from .dimension_reduction_mixture_options import dimension_reduction_mixture_options
class integration_parameters(Group):
    """
    'integration_parameters' child.
    """

    fluent_name = "integration-parameters"

    child_names = \
        ['integration_method', 'integration_options', 'isat_options',
         'chemistry_agglomeration', 'chemistry_agglomeration_options',
         'dynamic_mechanism_reduction', 'dynamic_mechanism_reduction_options',
         'dimension_reduction', 'dimension_reduction_mixture_options']

    integration_method: integration_method = integration_method
    """
    integration_method child of integration_parameters.
    """
    integration_options: integration_options = integration_options
    """
    integration_options child of integration_parameters.
    """
    isat_options: isat_options = isat_options
    """
    isat_options child of integration_parameters.
    """
    chemistry_agglomeration: chemistry_agglomeration = chemistry_agglomeration
    """
    chemistry_agglomeration child of integration_parameters.
    """
    chemistry_agglomeration_options: chemistry_agglomeration_options = chemistry_agglomeration_options
    """
    chemistry_agglomeration_options child of integration_parameters.
    """
    dynamic_mechanism_reduction: dynamic_mechanism_reduction = dynamic_mechanism_reduction
    """
    dynamic_mechanism_reduction child of integration_parameters.
    """
    dynamic_mechanism_reduction_options: dynamic_mechanism_reduction_options = dynamic_mechanism_reduction_options
    """
    dynamic_mechanism_reduction_options child of integration_parameters.
    """
    dimension_reduction: dimension_reduction = dimension_reduction
    """
    dimension_reduction child of integration_parameters.
    """
    dimension_reduction_mixture_options: dimension_reduction_mixture_options = dimension_reduction_mixture_options
    """
    dimension_reduction_mixture_options child of integration_parameters.
    """
