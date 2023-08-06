""" Defines the configuration values of the module.
    Values in the ProStore are saved and loaded during application startup/shutdown automatically
Copyright Nanosurf AG 2021
License - MIT
"""

import enum
import nanosurf
import nanosurf.lib.datatypes.sci_val as sci_val
import nanosurf.lib.datatypes.prop_val as prop_val
import nanosurf.lib.spm.workflow.frequency_sweep as freq_sweep

class SweepSettings(prop_val.PropStore):
    """ settings defined here as PropVal are stored persistently in a ini-file
        settings with a '_' as first char are not stored
    """
    def __init__(self):
        self.cantilever = Cantilever()
        self.bandwidth = prop_val.PropVal(int(freq_sweep.Bandwidths.Hz_360))
        self.input_source = prop_val.PropVal(int(freq_sweep.InputSource.Deflection))
        self.output_source = prop_val.PropVal(int(freq_sweep.FrequencySweepOutput.Normal_Excitation))
        self.center_frequency = prop_val.PropVal(sci_val.SciVal(5000, "Hz"))
        self.frequency_range = prop_val.PropVal(sci_val.SciVal(200, "Hz"))
        self.frequency_steps = prop_val.PropVal(sci_val.SciVal(10, "Hz"))
        self.excitation_amplitude = prop_val.PropVal(sci_val.SciVal(0.2, "V"))
        self.deflection_setpoint = prop_val.PropVal(sci_val.SciVal(0, "V"))

        self.plot_style_id = prop_val.PropVal(int(PlotStyleID.Linear))
        self.excitation_method = prop_val.PropVal(int(ExcitationMethodID.CleanDrive))

class SweepResults():
    """ This class saves the worker task result (e.g be read by gui elements or saved to file """
    def __init__(self):
        self.resonance_frequency = 0.0
        self.q_factor = 0.0
        self.spring_constant = 0.0

class PlotStyleID(enum.IntEnum):
    Linear = 0,
    Logarithmic = 1,

class ExcitationMethodID(enum.IntEnum):
    CleanDrive = 0,
    PiezoDrive = 1,

class Cantilever():
    def __init__(self):
        self.index = 0
        self.name = ""
        self.length = prop_val.PropVal(sci_val.SciVal(0, "m"))
        self.width = prop_val.PropVal(sci_val.SciVal(0, "m"))
        self.spring_constant = prop_val.PropVal(sci_val.SciVal(0, "N/m"))
        self.resonance_frequency_air = prop_val.PropVal(sci_val.SciVal(0, "Hz"))
        self.q_factor_air = prop_val.PropVal(sci_val.SciVal(0, ""))
        self.resonance_frequency_liquid = prop_val.PropVal(sci_val.SciVal(0, "Hz"))
        self.q_factor_liquid = prop_val.PropVal(sci_val.SciVal(0, ""))
        self.shape = ""
        self.tip_half_angle = prop_val.PropVal(sci_val.SciVal(0, "deg"))
        self.tip_radius = prop_val.PropVal(sci_val.SciVal(0, "m"))