from tkinter import *
from tkinter import ttk
import numpy as np

from .Scenario import Scenario

from ..Components.Block import Block
from ..Components.Limit import Limit

class Collisions(Scenario):
	def __init__(self, canvas, window):
		self.have_buttons = True
		self.running = False
		self.canvas = canvas
		self.window = window
		self.collision_counter = 0
		self.block1, self.block2 = None, None
		self.display_background()

	def destroy_blocks(self):
		if self.block1:
			self.canvas.delete(self.block1.canvas_object)
		if self.block2:
			self.canvas.delete(self.block2.canvas_object)

	def display_blocks(self):
		self.destroy_blocks()
		if not self.validate_params():
			self.canvas.not_validation_error()
			return
		# Create blocks
		self.block1 = Block(
			self.window,
			self.canvas,
			100, 
			600, 
			200, 
			697,
			vx = 0,
			vy = 0,
			color = '#A760FF',
			m = 1
		)
		self.block2 = Block(
			self.window,
			self.canvas,
			400,
			300,
			800,
			697,
			vx = -1,
			vy = 0,
			color = '#7C3E66',
			m = self.block1.m * 100 ** (self.digits - 1)
		)
		if self.digits >= 4:
			new_velocity = -1/(10**(self.digits - 3))
			self.block2.velocity[0] = new_velocity
			coords1 = [
				np.array([50, 600], dtype = np.float64), 
				np.array([150, 600], dtype = np.float64), 
				np.array([150, 697], dtype = np.float64),
				np.array([50, 697], dtype = np.float64),
			]
			coords2 = [
				np.array([155, 300], dtype = np.float64), 
				np.array([555, 300], dtype = np.float64), 
				np.array([555, 697], dtype = np.float64),
				np.array([155, 697], dtype = np.float64),
			]
			self.block1.coords = coords1
			self.block2.coords = coords2

		self.block1.show(self.canvas)
		self.block2.show(self.canvas)

		self.create_labels()

	def create_labels(self):
		self.counter_text = StringVar(value = f"Pi ~ {self.collision_counter}")
		self.counter_label = ttk.Label(
			self.canvas,
			textvariable = self.counter_text,
			style = "CanvasLabel.TLabel"
		)
		self.canvas.create_window(
			500, 100,
			anchor = "nw",
			window = self.counter_label
		)

	def display_background(self):
		fx1 = 0
		fx2 = 2000
		fy = 700
		self.floor = Limit(fx1, fy, fx2, fy)
		self.floor.show(self.canvas)

		wx = 50
		wy1 = 0
		wy2 = 2000
		self.wall = Limit(wx, wy1, wx, wy2)
		self.wall.show(self.canvas)
	
	def pause(self):
		self.running = False
	
	def run(self):
		self.running = True
		while self.running and self.validate_params():
			for _ in range(1):
				if self.block1.collide(self.block2):
					self.collision_counter += 1
					new_velocity1 = self.block1.bounce(self.block2)
					new_velocity2 = self.block2.bounce(self.block1)
					self.block1.velocity = np.array([new_velocity1, 0])
					self.block2.velocity = np.array([new_velocity2, 0])
					
					# self.block2.snap_back(self.block1, 'l')

				if self.block1.collide(self.wall):
					self.collision_counter += 1
					self.block1.velocity = -self.block1.velocity
					# self.block1.snap_back(self.wall, 'l')

				self.counter_text.set(f"PI ~ {self.collision_counter}")
				self.block1.update(0)
				self.block2.update(0)
			self.window.update()

	def close(self):
		if not self.running:
			self.window.destroy()
			
		self.running = False

		self.window.destroy()


	def set_params(self, simulation, params):
		self.simulation = simulation
		self.params = params
		self.collision_counter = 0

		self.digits = int(self.params['Número de dígitos'].get())

		self.display_blocks()

	
	def display_scenario(self):
		pass