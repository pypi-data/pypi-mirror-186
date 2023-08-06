#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .inlet_diffusion_1 import inlet_diffusion
from .thermal_diffusion import thermal_diffusion
from .thickened_flame_model import thickened_flame_model
from .diffusion_energy_source import diffusion_energy_source
from .multi_component_diffusion_mf import multi_component_diffusion_mf
from .multi_component_diffusion import multi_component_diffusion
from .liquid_energy_diffusion import liquid_energy_diffusion
from .save_gradients import save_gradients
from .species_migration import species_migration
from .species_transport_expert import species_transport_expert
class options(Group):
    """
    'options' child.
    """

    fluent_name = "options"

    child_names = \
        ['inlet_diffusion', 'thermal_diffusion', 'thickened_flame_model',
         'diffusion_energy_source', 'multi_component_diffusion_mf',
         'multi_component_diffusion', 'liquid_energy_diffusion',
         'save_gradients', 'species_migration', 'species_transport_expert']

    inlet_diffusion: inlet_diffusion = inlet_diffusion
    """
    inlet_diffusion child of options.
    """
    thermal_diffusion: thermal_diffusion = thermal_diffusion
    """
    thermal_diffusion child of options.
    """
    thickened_flame_model: thickened_flame_model = thickened_flame_model
    """
    thickened_flame_model child of options.
    """
    diffusion_energy_source: diffusion_energy_source = diffusion_energy_source
    """
    diffusion_energy_source child of options.
    """
    multi_component_diffusion_mf: multi_component_diffusion_mf = multi_component_diffusion_mf
    """
    multi_component_diffusion_mf child of options.
    """
    multi_component_diffusion: multi_component_diffusion = multi_component_diffusion
    """
    multi_component_diffusion child of options.
    """
    liquid_energy_diffusion: liquid_energy_diffusion = liquid_energy_diffusion
    """
    liquid_energy_diffusion child of options.
    """
    save_gradients: save_gradients = save_gradients
    """
    save_gradients child of options.
    """
    species_migration: species_migration = species_migration
    """
    species_migration child of options.
    """
    species_transport_expert: species_transport_expert = species_transport_expert
    """
    species_transport_expert child of options.
    """
