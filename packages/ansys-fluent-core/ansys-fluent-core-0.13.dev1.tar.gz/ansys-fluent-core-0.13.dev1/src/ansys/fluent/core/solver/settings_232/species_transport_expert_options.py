#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .linearize_convection_source import linearize_convection_source
from .linearize_diffusion_source import linearize_diffusion_source
from .blending import blending
from .minimum_cell_quality_threshold import minimum_cell_quality_threshold
class species_transport_expert_options(Group):
    """
    'species_transport_expert_options' child.
    """

    fluent_name = "species-transport-expert-options"

    child_names = \
        ['linearize_convection_source', 'linearize_diffusion_source',
         'blending', 'minimum_cell_quality_threshold']

    linearize_convection_source: linearize_convection_source = linearize_convection_source
    """
    linearize_convection_source child of species_transport_expert_options.
    """
    linearize_diffusion_source: linearize_diffusion_source = linearize_diffusion_source
    """
    linearize_diffusion_source child of species_transport_expert_options.
    """
    blending: blending = blending
    """
    blending child of species_transport_expert_options.
    """
    minimum_cell_quality_threshold: minimum_cell_quality_threshold = minimum_cell_quality_threshold
    """
    minimum_cell_quality_threshold child of species_transport_expert_options.
    """
