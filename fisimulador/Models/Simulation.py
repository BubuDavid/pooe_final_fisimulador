from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from .Styles import Styles
from .Grid import Grid
from .Scenarios import *

class Simulation:
	def __init__(self, simulation_names):
		self.simulation_name = simulation_names['name']
		self.display_simulation = False
		self.simulation_display_name = simulation_names['display_name']
		self.config()
		self.create_simulation()
		self.window.mainloop()

	def config(self):
		self.window = Toplevel()
		window_props = {
			"width": 1024,
			"height": 812,
			"posx": 400,
			"posy": 100,
		}
		self.window.attributes('-zoomed', True)
		# self.window.geometry(f'{window_props["width"]}x{window_props["height"]}+{window_props["posx"]}+{window_props["posy"]}')

	def create_simulation(self):
		self.create_components()
		self.position_components()
		Styles()

		self.build_scenario()

	def create_components(self):
		# ========== Main Frame ========== #
		self.simulation_frame = ttk.Frame(
			self.window,
			borderwidth = 1, 
			relief = 'raised',
		)

		# ========== Logo ========== #
		logo = Image.open("./fisimulador/assets/images/logo.png")
		resized_logo = logo.resize((70, 50), Image.ANTIALIAS)
		new_logo = ImageTk.PhotoImage(resized_logo)

		self.logo_label = ttk.Label(
			self.simulation_frame,
			text = self.simulation_display_name.replace('\n', ""),
			image = new_logo,
			compound = "left",
			style = 'Title.TLabel'
		)
		self.logo_label.image = new_logo

		# ========== Buttons ========== #
		# Back Button
		self.back_button = ttk.Button(
			self.simulation_frame,
			text = "Regresar",
		)
		# Run Simulation
		self.run_text = StringVar(value = "Reproducir")
		self.run_simulation = ttk.Button(
			self.simulation_frame,
			textvariable = self.run_text
		)

		# ========== Parameters ========== #
		self.param_frame = ttk.Frame(
			self.window,
			borderwidth = 1, 
			relief = 'raised'
		)

		# ========== Canvas ========== #
		self.canvas = Grid(
			self.window,
			self.simulation_frame,
		)

	def position_components(self):
		padding = 15

		# Positioning
		## Main Frame
		self.simulation_frame.grid(
			column = 0,
			row = 0,
			sticky = (N, S, E, W),
		)
		## Logo
		self.logo_label.grid(
			column = 0,
			row = 0,
			columnspan = 3,
			padx = 50,
		)
		
		if True:
			## Buttons
			### Back Button
			self.back_button.grid(
				column = 0,
				row = 0,
				padx = padding,
				sticky = (W)
			)
			### Run Button
			self.run_simulation.grid(
				column = 2,
				row = 0,
				padx = padding,
				sticky = (E)
			)

			self.canvas.grid(
				column = 0,
				row = 2,
				columnspan = 3,
				sticky = (N, S, E, W),
			)
		else:
			self.simulation_frame.grid(
				column = 0,
				row = 1,
				columnspan = 3,
				sticky = (N, S, E, W)
			)

		# Resizing
		self.simulation_frame.columnconfigure((0,1,2), weight = 1)
		self.simulation_frame.rowconfigure(2, weight = 1)
		self.simulation_frame.pack(expand = 1, fill = 'both')

	
	def build_scenario(self):
		if self.simulation_name == "collisions_pi":
			scenario = Collisions(self.canvas, self.window)
		if self.simulation_name == "free_fall":
			scenario = FreeFall(self.canvas, self.window)
		if self.simulation_name == "simple_gas":
			scenario = SimpleGas(self.canvas, self.window)
		if self.simulation_name == "launch":
			scenario = Launch(self.canvas, self.window)

		def pause_wrapper():
			self.run_text.set("Reproducir")
			self.run_simulation['command'] = run_wrapper
			scenario.pause()

		def run_wrapper():
			self.run_text.set("Pausar")
			self.run_simulation['command'] = pause_wrapper
			scenario.run()


		self.run_simulation['command'] = run_wrapper
		self.back_button['command'] = scenario.close
		self.window.protocol("WM_DELETE_WINDOW", scenario.close)