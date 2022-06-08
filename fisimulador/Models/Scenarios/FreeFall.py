from time import sleep
import numpy as np

from ..Components.Body import Body
from .Scenario import Scenario

class FreeFall(Scenario):
	def __init__(self, window, canvas, simulation = None, params = None):
		super().__init__(canvas, simulation, params)
		self.set_params(simulation, params)
		self.bodies = []
		self.r = 10
		self.gravity = 1
		self.have_buttons = False
		self.window = window
		self.start_after = True

		self.add_interaction()

	def add_interaction(self):
		self.canvas.bind("<B1-Motion>", self.draw_body)

	def set_params(self, simulation, params):
		try:
			self.gravity = float(params['Gravedad'].get())
			print(self.gravity)
		except:
			pass

	def draw_body(self, event):
		temp_body = Body(
			canvas = self.canvas,
			x = event.x,
			y = event.y,
			vx = 0,
			vy = 0,
		)
		temp_body.show()
		self.bodies.append(temp_body)

	def run(self):
		while True:
			self.update_bodies()
			sleep(0.01)
			self.window.update()

	def update_bodies(self):
		for body in self.bodies:
			body.V += np.array([0, self.gravity])
			body.move()