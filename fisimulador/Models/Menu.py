from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from PIL import Image, ImageTk

from .Simulation import Simulation
from .Styles import Styles


class Menu:
	def __init__(self, simulations):
		self.config()
		self.simulations = simulations
		self.create_menu()
		self.root.mainloop()

	def config(self):
		self.root = Tk()
		window = {
			"width": 1024,
			"height": 812,
			"posx": 400,
			"posy": 100,
		}
		self.root.geometry(f'{window["width"]}x{window["height"]}+{window["posx"]}+{window["posy"]}')
		# root.geometry(f'+{window["posx"]}+{window["posy"]}')

	def create_menu(self):
		self.create_components()
		self.position_components()
		Styles()

	def create_components(self):
		self.main_frame = ttk.Frame(
			self.root,
			borderwidth = 1, 
			relief = 'raised',
			padding = 12,
		)

		# Logo
		logo = Image.open("./fisimulador/assets/images/logo.png")
		resized_logo = logo.resize((70, 50), Image.ANTIALIAS)
		new_logo = ImageTk.PhotoImage(resized_logo)

		self.title_label = ttk.Label(
			self.main_frame,
			text = "FISIMULACIONES",
			image = new_logo,
			compound = "left",
			style = 'Title.TLabel'
		)
		self.title_label.image = new_logo


		# Simulatino Frames
		self.simulation_frames = []
		for index, simulation in enumerate(self.simulations):
			# Get the images
			temp_frame = ttk.Frame(
				self.main_frame,
				cursor = 'center_ptr'
			)
			if not simulation.get("image", False):
				temp_image = (Image.open("./fisimulador/assets/images/default.png"))
			else:
				temp_image = (Image.open(f"./fisimulador/assets/images/{simulation['image']}"))

			# Resize the images
			resized = temp_image.resize((200, 200), Image.ANTIALIAS)
			new_image = ImageTk.PhotoImage(resized)
			# Create the images
			temp_label_image = ttk.Label(
				temp_frame,
				image = new_image,
				text = simulation['display_name'],
				compound = 'top',
				justify = 'center',
			)
			temp_label_image.image = new_image
			temp_label_image.pack(pady = 30)

			# Add interaction
			temp_frame.focus_set()
			self.simulation_frames.append(temp_frame)
			self.addHoverEffect(temp_frame)

	
	def position_components(self):
		padding = 15

		# Positioning
		## Main Frame
		self.main_frame.grid(
			column = 0,
			row = 0,
			sticky = (N, S, E, W),
		)
		## Title
		self.title_label.grid(
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
				sticky = (N, S, E, W),
			)

		# Resizing Config
		# Main Frame
		self.main_frame.columnconfigure((0,1), weight = 1)
		self.main_frame.rowconfigure((0,1,2), weight = 1)
		self.main_frame.pack(expand = 1, fill = 'both')


	def addHoverEffect(self, frame):
		def enter(frame):
			frame['relief'] = 'raised'
			frame['borderwidth'] = 1

		def leave(frame):
			frame['relief'] = 'flat'
			frame['borderwidth'] = 0

		def open_simulation(widget):
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
				
			Simulation({
					"name": simulation_name, 
					"display_name": simulation_display_name
				})
		
		for child in frame.winfo_children():
			child.bind("<Button-1>", lambda e: open_simulation(child))	
		
		frame.bind("<Enter>", lambda e: enter(frame))
		frame.bind("<Leave>", lambda e: leave(frame))
		frame.bind("<Button-1>", lambda e: open_simulation(frame))
