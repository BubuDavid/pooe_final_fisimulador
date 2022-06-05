from .Coord import Coord

class Solid:
	def __init__(self, coords, velocity, acceleration, center):
		self.coords = coords
		self.velocity = velocity
		self.acceleration = acceleration
		self.center = center

	def unpack_coords(self):
		return [(coord.x, coord.y) for coord in self.coords]

	def show(self, canvas):
		self.canvas_object = canvas.create_polygon(
			self.unpack_coords(),
			fill = self.color
		)

		return self
	
	def update(self):
		for index in range(len(self.coords)):
			self.coords[index] += self.velocity

		return self

	def is_colliding(self, other_solid):
		# For this approx, we are assuming everything as a rectangle
		# An the coords are sorted clockwise from top-left corner
		# We are going to form a colliding vector full of False.
		# A component of this dictionary is going to be True if there 
		# are a collision in the represented side
		# top left, rop right, bottom rigth and bottom left
		colliding = [False, False, False, False]
		# [x1, y1], [x2, y1], [x2, y2], [x1, y2]
		for index, other_coord in enumerate(other_solid.coords):
			x = other_coord.x
			y = other_coord.y
			if x >= self.coords[0].x and x <= self.coords[1].x:
				if y >= self.coords[0].y and y <= self.coords[2].y:
					colliding[index] = True


		return colliding
