from tkinter import *
from tkinter import ttk

from time import sleep
from .Components import *

class Collisions:
	def __init__(self, canvas, window):
		self.running = False
		self.canvas = canvas
		self.window = window
		self.collision_counter = 0
		self.display_background()
		self.display_blocks()

	def display_blocks(self):
		digits = 2
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
			m = self.block1.m * 100 ** (digits - 1)
		)

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
		while self.running:
			if self.block1.collide(self.block2):
				self.collision_counter += 1
				new_velocity1 = self.block1.bounce(self.block2)
				new_velocity2 = self.block2.bounce(self.block1)
				self.block1.velocity = Coord(new_velocity1, 0)
				self.block2.velocity = Coord(new_velocity2, 0)
				
				self.block2.snap_back(self.block1, 'l')

			if self.block1.collide(self.wall):
				self.collision_counter += 1
				self.block1.velocity = -self.block1.velocity
				self.block1.snap_back(self.wall, 'l')

			self.counter_text.set(f"Pi ~ {self.collision_counter}")
			self.block1.update(0.001)
			self.block2.update(0.001)
			self.window.update()
			print(self.block1.velocity, self.block2.velocity)

	def close(self):
		if not self.running:
			self.window.destroy()
			
		self.running = False

		self.window.destroy()