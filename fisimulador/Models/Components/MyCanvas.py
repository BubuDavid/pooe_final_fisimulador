from tkinter import *
from tkinter import ttk

from fisimulador.Models.Scenarios.FreeFall import FreeFall

from ..Scenarios import *

class MyCanvas(Canvas):
	def __init__(
		self, 
		parent,
		simulation,
		bg = '#F3F1F5', 
		color = "#F0D9FF", 
		size = 2000,
		have_grid = True, 
		**options
	):
		super().__init__(
			parent,
			options,
			bg = bg, 
		)

		self.simulation = simulation
		self.parent = parent
		self.size = size
		self.color = color
		self.have_grid = have_grid
		self.validation_error = None
		self.scenario = None

		if self.have_grid:
			self.create_grid()

	def create_grid(self):
		# Horizontal lines
		for pos in range(0, self.size, 50):
			self.create_line(0, pos, self.size, pos, fill = self.color, width = 1)
			self.create_line(pos, 0, pos, self.size, fill = self.color, width = 1)

	def reset(self):
		self.delete('all')
		if self.have_grid:
			self.create_grid()

	def display_simulation(self):
		self.choose_simulation()
		self.create_param_frame(self.simulation.get('params', []))
		self.scenario.set_params(self.simulation, self.entries)
		try:
			if self.scenario.start_after:
				self.scenario.run()
		except:
			pass
		

	def choose_simulation(self):
		# Display simulation
		self.validation_error_destroy()
		name = self.simulation['name']
		if name == 'n-body':
			self.scenario = NBody(self)
		if name == 'collisions_pi':
			self.scenario = Collisions(self, self.parent)
		if name == 'free_fall':
			self.scenario = FreeFall(self.parent, self)

	def create_param_frame(self, params):
		self.param_frame = ttk.Frame(
			self,
			borderwidth = 1,
			relief = 'raised',
			width = 300,
			height = 300,
		)
		self.param_frame.pack()
		self.param_frame.pack_propagate(0)

		self.entries = {}
		for param in params:
			ttk.Label(
				self.param_frame,
				text = param['name'] + f" {param.get('limits', '')}",
				style = 'Param.TLabel',
				padding = 10,
				justify = 'center'
			).pack()

			limits = param.get('limits', False)
			dLimits = param.get('dLimits', False)
			options = param.get('options', False)
			if dLimits:
				self.entries[param['name']] = StringVar(value = param['default'])
				temp_entry = ttk.Entry(
					self.param_frame,
					textvariable = self.entries[param['name']],
					style = 'Param.TEntry',
				)
				temp_entry.pack()
			if limits:
				self.entries[param['name']] = StringVar(value = param['default'])
				temp_entry = ttk.Entry(
					self.param_frame,
					textvariable = self.entries[param['name']],
					style = 'Param.TEntry',
				)
				temp_entry.pack()

			if options:
				self.entries[param['name']] = StringVar(value = options[0])
				temp_option = OptionMenu(
					self.param_frame,
					self.entries[param['name']],
					*param['options'],
					command = lambda v: self.scenario.set_params(self.simulation, self.entries)
				)
				temp_option.pack()

		if self.scenario.have_buttons:
			buttom_frame = ttk.Frame(
				self.param_frame
			)
			buttom_frame.pack(side = 'bottom', pady = 16)
			self.run_text = StringVar(value = 'Correr')
			self.run_button = ttk.Button(
				buttom_frame,
				textvariable = self.run_text,
				command = self.wrapper_run
			)
			self.run_button.pack(side = 'left', padx = 16)
			ttk.Button(
				buttom_frame,
				text = "Reiniciar",
				command = lambda: self.scenario.set_params(self.simulation, self.entries)
			).pack(side = 'right', padx = 16)
		else:
			ttk.Button(
				self.param_frame,
				text = "Actualizar",
				command = lambda: self.scenario.set_params(self.simulation, self.entries)
			).pack(side = 'bottom', pady = 16)

		self.create_window(
			self.width - self.param_frame['width']/2 - 10,
			self.param_frame['width']/2 + 10,
			window = self.param_frame
		)

	def restart_simulation(self):
		self.reset()
		self.validation_error_destroy()
		self.display_simulation()

	def not_validation_error(self):
		if not self.validation_error:
			self.validation_error = ttk.Label(
				self.param_frame,
				text = 'Por favor, respeta los limites',
				style = 'Error.TLabel'
			)
			self.validation_error.pack(side = 'bottom')

	def validation_error_destroy(self):
		if self.validation_error:
			self.validation_error.destroy()
			self.validation_error = None

	def wrapper_pause(self):
		self.run_text.set('Correr')
		self.run_button['command'] = self.wrapper_run
		self.scenario.pause()

	def wrapper_run(self):
		if self.scenario.validate_params():
			self.validation_error_destroy()
			self.run_text.set('Pausa')
			self.run_button['command'] = self.wrapper_pause
			self.scenario.run()