from tkinter import *
from tkinter import ttk

from .MyFrame import MyFrame

class Simulation(MyFrame):
	def __init__(self, parent, simulation_names, **args):
		super().__init__(parent, **args)

		self.parent = parent
		self.simulation_name = simulation_names['name']
		self.simulation_display_name = simulation_names['display_name']

		self.initial_configuration((0,1,2), (2))
		self.display()

	def display(self):
		self.create_components()
		self.position_components()

	def create_components(self):
		pass

	def position_components(self):
		pass