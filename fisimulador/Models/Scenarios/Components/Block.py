from time import sleep
from .Solid import Solid
from .Coord import Coord

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
			Coord(x1, y1), 
			Coord(x2, y1), 
			Coord(x2, y2),
			Coord(x1, y2),
		]
		velocity = Coord(vx, vy)
		acceleration = Coord(ax, ay)
		center = Coord((x2 - x1)/2, (y2 - y1)/2)
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
			self.coords[index] += Coord(dx, dy)

	def update(self, sleep_time = 0):
		sleep(sleep_time)
		self.move(self.velocity.x, self.velocity.y)

	def collide(self, other):
		coords = self.coords
		other = other.coords
		return not (coords[1].x <= other[0].x or coords[0].x >= other[1].x)


	def bounce(self, other_block):
		# 1 dimension
		u1 = self.velocity.x
		u2 = other_block.velocity.x
		m1 = self.m
		m2 = other_block.m

		sumM = m1 + m2
		new_v = (m1 - m2) / sumM * u1 + (2 * m2) / sumM * u2

		return new_v

	def snap_back(self, other, side):
		if side == 'l':
			while self.coords[0].x < other.coords[1].x:
				self.move(1, 0)
		if side == 'r':
			while self.coords[1].x > other.coords[0].x:
				self.move(-1, 0)