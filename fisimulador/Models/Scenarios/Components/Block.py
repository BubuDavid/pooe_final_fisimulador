from .Solid import Solid
from .Coord import Coord

class Block(Solid):
	def __init__(self, x1, y1, x2, y2, vx=0, vy=0, ax=0, ay=0, color='red'):
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