from .Coord import Coord
from .Solid import Solid


class Limit(Solid):
	def __init__(self, x1, y1, x2, y2, width = 6, color = 'black'):
		coords = [
			Coord(x1, y1),
			Coord(x2, y2),
		]
		center = Coord((x2 - x1)/2, (y2 - y1)/2)
		super().__init__(coords, 0, 0, center)

		self.width = width,
		self.color = color

	def show(self, canvas):
		canvas.create_line(
			self.unpack_coords(),
			fill = self.color,
			width = self.width
		)