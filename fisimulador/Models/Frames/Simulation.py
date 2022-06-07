from tkinter import *
from tkinter import ttk

from ..Components.MyImage import MyImage
from .MyFrame import MyFrame
from ..Components.MyCanvas import MyCanvas

class Simulation(MyFrame):
	def __init__(self, parent, simulation, **args):
		super().__init__(parent, **args)

		self.parent = parent
		self.simulation = simulation

		self.initial_configuration((0,1,2), 1)
		self.display()

	def display(self):
		self.create_components()
		self.position_components()
		self.parent.update_idletasks()
		self.canvas.width = self.canvas.winfo_width()
		self.canvas.height = self.canvas.winfo_height()
		
		self.canvas.display_simulation()

	def create_components(self):
		img = MyImage("./fisimulador/assets/images/logo.png", 70, 50)
		self.logo = img.get_image()
		self.title = ttk.Label(
			self,
			text = self.simulation['display_name'],
			image = self.logo,
			compound = "left",
			style = 'Title.TLabel'
		)
		
		# Back Button
		self.back_button = ttk.Button(
			self,
			text = 'Regresar',
			command = self.parent.switch_to_menu
		)

		# Canvas
		self.canvas = MyCanvas(self, self.simulation)
		

	def position_components(self):
		padding = 15
		
		# Buttons
		self.back_button.grid(
			column = 0,
			row = 0,
			sticky = 'W',
			pady = padding
		)
		# Title
		self.title.grid(
			column = 0,
			row = 0,
			columnspan = 2,
			padx = 50,
			pady = padding
		)
		# Canvas
		self.canvas.grid(
			column = 0,
			row = 1,
			columnspan = 3,
			sticky = "NSEW"
		)