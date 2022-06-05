from .Components import *

class Collisions:
	def __init__(self, canvas):
		self.display_background(canvas)
		self.display_blocks(canvas)

	def display_blocks(self, canvas):
		# Create blocks
		block1 = Block(
			100, 
			600, 
			200, 
			697,
			color = '#A760FF'
		)
		block2 = Block(
			400,
			400,
			700,
			697,
			color = '#7C3E66'
		)

		block1.show(canvas)
		block2.show(canvas)

	def display_background(self, canvas):
		fx1 = 0
		fx2 = 1400
		fy = 700
		floor = Limit(fx1, fy, fx2, fy)
		floor.show(canvas)

		wx = 50
		wy1 = 0
		wy2 = 800
		wall = Limit(wx, wy1, wx, wy2)
		wall.show(canvas)