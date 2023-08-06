#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .model import model
from .options_2 import options
from .reactions import reactions
from .wall_surface_options import wall_surface_options
from .turb_chem_interaction_model import turb_chem_interaction_model
from .turb_chem_interaction_model_options import turb_chem_interaction_model_options
from .species_transport_expert_options import species_transport_expert_options
from .edc_model_options import edc_model_options
from .tfm_model_options import tfm_model_options
from .chemistry_solver import chemistry_solver
from .integration_parameters import integration_parameters
class species(Group):
    """
    'species' child.
    """

    fluent_name = "species"

    child_names = \
        ['model', 'options', 'reactions', 'wall_surface_options',
         'turb_chem_interaction_model', 'turb_chem_interaction_model_options',
         'species_transport_expert_options', 'edc_model_options',
         'tfm_model_options', 'chemistry_solver', 'integration_parameters']

    model: model = model
    """
    model child of species.
    """
    options: options = options
    """
    options child of species.
    """
    reactions: reactions = reactions
    """
    reactions child of species.
    """
    wall_surface_options: wall_surface_options = wall_surface_options
    """
    wall_surface_options child of species.
    """
    turb_chem_interaction_model: turb_chem_interaction_model = turb_chem_interaction_model
    """
    turb_chem_interaction_model child of species.
    """
    turb_chem_interaction_model_options: turb_chem_interaction_model_options = turb_chem_interaction_model_options
    """
    turb_chem_interaction_model_options child of species.
    """
    species_transport_expert_options: species_transport_expert_options = species_transport_expert_options
    """
    species_transport_expert_options child of species.
    """
    edc_model_options: edc_model_options = edc_model_options
    """
    edc_model_options child of species.
    """
    tfm_model_options: tfm_model_options = tfm_model_options
    """
    tfm_model_options child of species.
    """
    chemistry_solver: chemistry_solver = chemistry_solver
    """
    chemistry_solver child of species.
    """
    integration_parameters: integration_parameters = integration_parameters
    """
    integration_parameters child of species.
    """
