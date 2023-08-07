
from srsgui.task.task import Task
from srsgui.task.inputs import StringInput, IntegerInput, InstrumentInput

from srsinst.rga.plots.analogscanplot import AnalogScanPlot
from srsinst.rga.plots.timeplot import TimePlot

import numpy as np
from scipy.optimize import nnls
from srsinst.rga import get_rga


class CompositionAnalysisTask(Task):
    """
Task to run analog scans and analyze composition with a list of gas name \
from a gas library file.
    """
    InstrumentName = 'instrument to control'
    StartMass = 'start mass'
    StopMass = 'stop mass'
    ScanSpeed = 'scan speed'
    StepSize = 'step per AMU'
    GasList = 'gas list'

    CompPlot = 'composition_plot'
    DerivedPvsTPlot = 'derived_pvst'

    # input_parameters values can be changed interactively from GUI
    input_parameters = {
        InstrumentName: InstrumentInput(),
        StartMass: IntegerInput(2, " AMU", 0, 319, 1),
        StopMass: IntegerInput(50, " AMU", 1, 320, 1),
        ScanSpeed: IntegerInput(3, " ", 0, 9, 1),
        StepSize: IntegerInput(20, " steps per AMU", 10, 80, 1),
        GasList: StringInput('water, nitrogen, oxygen, hydrogen, argon, carbon dioxide'),
    }

    additional_figure_names = [CompPlot, DerivedPvsTPlot]
    
    def setup(self):
        # Get values to use for task  from input_parameters in GUI
        self.params = self.get_all_input_parameters()
        gas_list = self.params[self.GasList].split(',')
        self.gas_list = [gas.strip().lower() for gas in gas_list]
        print(self.gas_list)
        # Get logger to use
        self.logger = self.get_logger(__name__)

        self.init_scan()

        self.lib = self.read_gas_library()
        self.mat = self.build_coeff_matrix(self.lib, self.params[self.StartMass], 
                                           self.params[self.StopMass], self.gas_list)

        # Set up an derived P vs T plot
        self.ax_pvst = self.get_figure(self.DerivedPvsTPlot).add_subplot(111)
        key_list = self.gas_list
        self.pvst_plot = TimePlot(self, self.ax_pvst, 'PP vs T', key_list)
        self.pvst_plot.ax.set_yscale('log')

        # Set up a log plot for the last full analog scan
        self.ax_comp = self.get_figure(self.CompPlot).add_subplot(111)
        self.plot_comp = AnalogScanPlot(self, self.ax_comp, self.rga.scan, 'Composition Fit')
        self.rga.scan.set_callbacks(None, None, None)  # use no callbacks for self.plot_comp

        self.bar_x = np.arange(self.params[self.StartMass], self.params[self.StopMass] + 1)
        self.bar_y = np.zeros_like(self.bar_x)

        self.rect_dict = {}
        for gas in self.gas_list:
            self.rect_dict[gas] = self.ax_comp.bar(self.bar_x, self.bar_y, label=gas)

        self.ax_comp.legend()

        # Set up an analog scan plot for the test
        self.ax = self.get_figure().add_subplot(111)
        self.plot = AnalogScanPlot(self, self.ax, self.rga.scan, 'Analog Scan')

        self.conversion_factor = self.rga.pressure.get_partial_pressure_sensitivity_in_torr()
        self.plot.set_conversion_factor(self.conversion_factor, 'Torr')
        self.plot_comp.set_conversion_factor(self.conversion_factor, 'Torr')
        self.pvst_plot.set_conversion_factor(1.0, 'Torr')

    def init_scan(self):
        # Get the instrument to use
        self.rga = get_rga(self, self.params[self.InstrumentName])
        self.id_string = self.rga.status.id_string
        emission_current = self.rga.ionizer.emission_current
        cem_voltage = self.rga.cem.voltage

        self.logger.info('Emission current: {:.2f} mA CEM HV: {} V'.format(emission_current, cem_voltage))
        self.rga.scan.set_parameters(self.params[self.StartMass],
                                     self.params[self.StopMass],
                                     self.params[self.ScanSpeed],
                                     self.params[self.StepSize])

    def test(self):
        self.set_task_passed(True)
        self.add_details('{}'.format(self.id_string), key='ID')

        while True:
            if not self.is_running():
                break

            try:
                self.rga.scan.get_analog_scan()
            except Exception as e:
                self.set_task_passed(False)
                self.logger.error('{}: {}'.format(e.__class__.__name__, e))
                if not self.rga.is_connected():
                    self.logger.error('"{}" is disconnected'.format(self.params[self.InstrumentName]))
                    break

            # manually update self.plot_comp
            
            self.plot_comp.line.set_xdata(self.plot_comp.x_axis)
            self.plot_comp.line.set_ydata(self.plot_comp.scan.spectrum * self.conversion_factor)
            
            ys = np.array([self.rga.scan.get_peak_intensity_from_analog_scan_spectrum(mass) 
                          * self.conversion_factor for mass in self.bar_x]) 
            
            c = nnls(self.mat, ys)[0]
            
            self.display_result('', True)
            for n, pp in zip(self.gas_list, c): 
                self.display_result(f'{n}: {pp:.3e} ')    
            self.display_result(f'Offset: {c[-1]:.3e}')
            
            self.pvst_plot.add_data(c[:-1], True)
            
            # Update stacked bar graph
            bottom = np.zeros_like(self.bar_x, dtype=np.float64)
            for i, gas in enumerate(self.gas_list):
                ys = self.mat[:, i] * c[i]
                for k, y in enumerate(ys):
                    self.rect_dict[gas][k].set_height(y)
                    self.rect_dict[gas][k].set_y(bottom[k])
                bottom += ys
            self.request_figure_update(self.plot_comp.ax.figure)

    def cleanup(self):
        self.logger.info('Task finished')
        self.plot.cleanup() # Detach callback functions

    def read_gas_library(self, file_name='gaslib.dat'):
        """
        Read gaslib.dat file as a dict
        """
        d = {}
        with open(file_name, 'rt') as f:
            number_of_gas = int(f.readline())
            count = 0
            for line in f:
                if line.startswith('#'):
                    continue
                rem = count % 3
                if rem == 0:
                    first = line.split('"')
                    name = first[1].lower()
                    sens = first[2].split()
                    sensitivity = float(sens[0])
                    reduction_factor = float(sens[1])
                elif rem == 1:
                    mass = line.split()
                else:
                    inten = line.split()
                    if len(mass) != len(inten):
                        raise IndexError(f'{name} has mal-formatted peak(s).')
                    peaks = [(int(m), float(f)) for m, f in zip(mass, inten)]
                    d[name] = (sensitivity, reduction_factor, peaks)
                count += 1
        if number_of_gas != count //3:
            self.logger.error('Number of gas not matched. Claimed: {} Read-in: {}'
                              .format(number_of_gas, count//3))
        return d

    def build_coeff_matrix(self, gas_library, start_mass=1, stop_mass=50, 
                           gas_name_list=('Water', 'Nitrogen', 'Oxygen', 'Carbon dioxide')):
        """
        Build a least square fit coefficient matrix based on mass range  and 
        refeence gas hsitogram spectra.
        """
        mat = np.array([np.zeros(stop_mass - start_mass + 1)])
        for gas in gas_name_list:
            gas_vector = np.array([np.zeros(stop_mass - start_mass + 1)])
            first_sens = gas_library[gas][0]
            second_sens = gas_library[gas][1] / 100.0
            total_sens = first_sens * second_sens
            for peak in gas_library[gas][2]:
                if start_mass <= peak[0] <= stop_mass:
                    gas_vector[0][peak[0] - start_mass] = total_sens * peak[1]
            mat = np.append(mat, gas_vector, axis=0)
        ones = np.ones_like(mat[1])
        A = np.vstack ([mat[1:], ones]).T
        return A
 