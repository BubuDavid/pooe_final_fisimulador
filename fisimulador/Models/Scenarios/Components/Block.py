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

	def update(self, sleep_time = 0):
		sleep(sleep_time)
		self.canvas.move(
			self.canvas_object, 
			self.velocity.x, 
			self.velocity.y
		)

		for index, _ in enumerate(self.coords):
			self.coords[index] += self.velocity

	def collide(self, other_block):
		coords = self.coords
		other = other_block.coords
		return not (coords[1].x < other[0].x or coords[0].x > other[1].x)


	def bounce(self, other_block):
		pass