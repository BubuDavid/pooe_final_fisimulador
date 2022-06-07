from time import sleep
import numpy as np

from .Solid import Solid

class Block(Solid):
	def __init__(
		self,
		window, 
		canvas, 
		x1, y1, 
		x2, y2, 
		vx = 0, vy = 0, 
		ax = 0, ay = 0, 
		color = 'red', 
		m = 1
	):
		coords = [
			np.array([x1, y1], dtype = np.float64), 
			np.array([x2, y1], dtype = np.float64), 
			np.array([x2, y2], dtype = np.float64),
			np.array([x1, y2], dtype = np.float64),
		]
		velocity = np.array([vx, vy], dtype = np.float64)
		acceleration = np.array([ax, ay], dtype = np.float64)
		center = np.array([(x2 - x1)/2, (y2 - y1)/2], dtype = np.float64)
		super().__init__(coords, velocity, acceleration, center)
		
		self.color = color
		self.window = window
		self.canvas = canvas
		self.m = m

	def move(self, dx, dy):
		self.canvas.move(
			self.canvas_object,
			dx,
			dy
		)
		for index, _ in enumerate(self.coords):
			self.coords[index] += np.array([dx, dy], dtype = np.float64)

	def update(self, sleep_time = 0):
		sleep(sleep_time)
		self.move(self.velocity[0], self.velocity[1])

	def collide(self, other):
		coords = self.coords
		other = other.coords
		return not (coords[1][0] <= other[0][0] or coords[0][0] >= other[1][0])


	def bounce(self, other_block):
		# 1 dimension
		u1 = self.velocity[0]
		u2 = other_block.velocity[0]
		m1 = self.m
		m2 = other_block.m

		sumM = m1 + m2
		new_v = (m1 - m2) / sumM * u1 + (2 * m2) / sumM * u2

		return new_v

	def snap_back(self, other, side):
		if side == 'l':
			while self.coords[0][0] < other.coords[1][0]:
				self.move(1, 0)
		if side == 'r':
			while self.coords[1][0] > other.coords[0][0]:
				self.move(-1, 0)