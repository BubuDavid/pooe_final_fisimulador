from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from .Styles import Styles
from .Grid import Grid
from .Scenarios import *

class Simulation:
	def __init__(self, simulation_names):
		self.simulation_name = simulation_names['name']
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

		self.window.geometry(f'{window_props["width"]}x{window_props["height"]}+{window_props["posx"]}+{window_props["posy"]}')

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
			command = self.close_window
		)
		# Run Simulation
		self.run_simulation = ttk.Button(
			self.simulation_frame,
			text = "¡Empezar!"
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

		# Resizing
		self.simulation_frame.columnconfigure((0,1,2), weight = 1)
		self.simulation_frame.rowconfigure(2, weight = 1)
		self.simulation_frame.pack(expand = 1, fill = 'both')

	
	def build_scenario(self):
		if self.simulation_name == "collisions_pi":
			Collisions(self.canvas)
		if self.simulation_name == "free_fall":
			FreeFall(self.canvas)
		if self.simulation_name == "simple_gas":
			SimpleGas(self.canvas)
		if self.simulation_name == "launch":
			Launch(self.canvas)

	def close_window(self):
		self.window.destroy()