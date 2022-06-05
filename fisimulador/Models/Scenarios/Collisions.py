from time import sleep
from .Components import *

class Collisions:
	def __init__(self, canvas, window):
		self.running = False
		self.canvas = canvas
		self.window = window
		self.display_background()
		self.display_blocks()

	def display_blocks(self):
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
			m = 1
		)

		self.block1.show(self.canvas)
		self.block2.show(self.canvas)

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
				self.block1.bounce(self.block2)

			self.block1.update(0.01)
			self.block2.update(0.01)
			self.window.update()

	def close(self):
		if not self.running:
			self.window.destroy()
			
		self.running = False

		self.window.destroy()