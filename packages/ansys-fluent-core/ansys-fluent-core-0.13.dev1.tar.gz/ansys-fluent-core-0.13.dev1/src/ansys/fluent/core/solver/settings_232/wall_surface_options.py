#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .heat_of_surface_reactions import heat_of_surface_reactions
from .mass_deposition_source import mass_deposition_source
from .reaction_diffusion_balance import reaction_diffusion_balance
from .surface_reaction_aggresiveness_factor import surface_reaction_aggresiveness_factor
from .surface_reaction_rate_temperature_factor import surface_reaction_rate_temperature_factor
from .surface_reaction_solid_fraction import surface_reaction_solid_fraction
class wall_surface_options(Group):
    """
    'wall_surface_options' child.
    """

    fluent_name = "wall-surface-options"

    child_names = \
        ['heat_of_surface_reactions', 'mass_deposition_source',
         'reaction_diffusion_balance',
         'surface_reaction_aggresiveness_factor',
         'surface_reaction_rate_temperature_factor',
         'surface_reaction_solid_fraction']

    heat_of_surface_reactions: heat_of_surface_reactions = heat_of_surface_reactions
    """
    heat_of_surface_reactions child of wall_surface_options.
    """
    mass_deposition_source: mass_deposition_source = mass_deposition_source
    """
    mass_deposition_source child of wall_surface_options.
    """
    reaction_diffusion_balance: reaction_diffusion_balance = reaction_diffusion_balance
    """
    reaction_diffusion_balance child of wall_surface_options.
    """
    surface_reaction_aggresiveness_factor: surface_reaction_aggresiveness_factor = surface_reaction_aggresiveness_factor
    """
    surface_reaction_aggresiveness_factor child of wall_surface_options.
    """
    surface_reaction_rate_temperature_factor: surface_reaction_rate_temperature_factor = surface_reaction_rate_temperature_factor
    """
    surface_reaction_rate_temperature_factor child of wall_surface_options.
    """
    surface_reaction_solid_fraction: surface_reaction_solid_fraction = surface_reaction_solid_fraction
    """
    surface_reaction_solid_fraction child of wall_surface_options.
    """
