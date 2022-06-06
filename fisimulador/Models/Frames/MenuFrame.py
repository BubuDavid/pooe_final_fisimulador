from tkinter import *
from tkinter import ttk

from .MyFrame import MyFrame

from ..Config.MyImage import MyImage
from .Simulation import Simulation

class MenuFrame(MyFrame):
	def __init__(self, parent, simulations, **args):
		super().__init__(parent, **args)
		self.parent = parent
		self.simulations = simulations
		self.initial_configuration((0, 1), (0,1,2))
		self.display()

	def display(self):
		self.create_components()
		self.position_components()

	def create_components(self):
		# Title
		img = MyImage("./fisimulador/assets/images/logo.png", 70, 50)
		self.logo = img.get_image()
		self.title = ttk.Label(
			self,
			text = "FISIMULACIONES",
			image = self.logo,
			compound = "left",
			style = 'Title.TLabel'
		)

		# Simulatino Frames
		self.simulation_frames = []
		for simulation in self.simulations:
			if not simulation.get("image", False):
				# Get the image
				temp_image = MyImage(
					"./fisimulador/assets/images/default.png",
					200, 200
				).get_image()
			else:
				temp_image = MyImage(
					f"./fisimulador/assets/images/{simulation['image']}",
					200, 200
				).get_image()

			# Create the frame
			temp_frame = ttk.Frame(self, cursor = 'center_ptr')
			# Create labels inside frames
			temp_label_image = ttk.Label(
				temp_frame,
				image = temp_image,
				text = simulation['display_name'],
				compound = 'top',
				justify = 'center',
			)
			temp_label_image.image = temp_image
			temp_label_image.pack(pady = 30)

			# Add interaction
			temp_frame.focus_set()
			self.simulation_frames.append(temp_frame)
			self.add_interaction(temp_frame)

	def position_components(self):
		padding = 15

		# Positioning
		## Title
		self.title.grid(
			column = 0,
			row = 0,
			columnspan = 2,
			padx = 50,
			pady = padding
		)

		## Simulation Frames
		for index, simulation in enumerate(self.simulation_frames):
			simulation.grid(
				column = index % 2,
				row = index // 2 + 1,
				padx = padding,
				pady = padding,
				sticky = "NSEW",
			)


	def add_interaction(self, frame):
		def enter(frame):
			frame['relief'] = 'raised'
			frame['borderwidth'] = 1

		def leave(frame):
			frame['relief'] = 'flat'
			frame['borderwidth'] = 0

		for child in frame.winfo_children():
			child.bind("<Button-1>", lambda e: self.open_simulation(child))	
		frame.bind("<Button-1>", lambda e: self.open_simulation(frame))
		
		frame.bind("<Enter>", lambda e: enter(frame))
		frame.bind("<Leave>", lambda e: leave(frame))

	def open_simulation(self, widget):
		simulation_name = ""
		simulation_display_name = ""
		if "frame" in widget.winfo_name():
			index = widget.winfo_name()[-1]
			if index == 'e':
				simulation_name = self.simulations[0]['name']
				simulation_display_name = self.simulations[0]['display_name']
			else:
				simulation_name = self.simulations[int(index) - 1]['name']
				simulation_display_name = self.simulations[int(index) - 1]['display_name']
		else: 
			for simulation in self.simulations:
				if simulation['display_name'] == widget['text']:
					simulation_name = simulation['name']
					simulation_display_name = simulation['display_name']
					break

		self.parent.switch_frames(
			Simulation,
			simulation_names = {
				'name': simulation_name,
				'display_name': simulation_display_name
			},
			borderwidth = 1,
			relief = 'raised',
			padding = 16
		)