class Coord:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other_coord):
		result_x = self.x + other_coord.x
		result_y = self.y + other_coord.y

		return Coord(result_x, result_y)

	def __iadd__(self, other_coord):
		return self + other_coord
	
	def __sub__(self, other_coord):
		result_x = self.x - other_coord.x
		result_y = self.y - other_coord.y

		return Coord(result_x, result_y)

	def __neg__(self):
		return Coord(-self.x, -self.y)

	def __isub__(self, other_coord):
		return self - other_coord

	def __mul__(self, other_coord):
		result_x = self.x * other_coord.x
		result_y = self.y * other_coord.y

		return result_x + result_y

	def __isub__(self, other_coord):
		return self * other_coord

	def norm(self):
		return (self * self)**(1/2)

	def __lt__(self, other_coord):
		if self.norm() < other_coord.norm():
			return True
		return False

	def __gt__(self, other_coord):
		if self.norm() > other_coord.norm():
			return True
		return False

	def __le__(self, other_coord):
		if self.norm() <= other_coord.norm():
			return True
		return False

	def __ge__(self, other_coord):
		if self.norm() >= other_coord.norm():
			return True
		return False

	def __eq__(self, other_coord):
		if self.norm() == other_coord.norm():
			return True
		return False

	def __ne__(self, other_coord):
		if self.norm() != other_coord.norm():
			return True
		return False