class Solid:
	def __init__(self, coords, velocity, acceleration, center):
		self.coords = coords
		self.velocity = velocity
		self.acceleration = acceleration
		self.center = center

	def unpack_coords(self):
		return [(coord[0], coord[1]) for coord in self.coords]

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
