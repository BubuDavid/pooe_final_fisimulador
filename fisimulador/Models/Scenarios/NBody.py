from time import sleep
import numpy as np

from ..Components.Body import Body
from .Scenario import Scenario
from .tools import *

class NBody(Scenario):
	def __init__(self, canvas, simulation = None, params = None):
		super().__init__(canvas, simulation, params)

		self.running = False
		self.dt = 0.1
		self.softening = 1
		self.bodies = []
	
	def set_params(self, simulation, params):
		self.simulation = simulation
		self.params = params

		self.n_bodies = int(self.params['Número de cuerpos'].get())
		self.gravity = float(self.params['Intensidad de Gravedad'].get()) * 100

		self.display_scenario()

	def display_scenario(self):
		self.reset_bodies()
		if not self.validate_params():
			self.canvas.not_validation_error()
			return

		for i in range(self.n_bodies):
			temp_body = self.create_body()

			self.bodies.append(temp_body)
			self.bodies[i].show()

	def create_body(self):
		creating = True

		while creating:
			temp_body = Body(
					self.canvas,
					np.random.randint(
						self.canvas.winfo_width()/2 - 500,
						self.canvas.winfo_width()/2 + 500,
					),
					np.random.randint(
						self.canvas.winfo_height()/2 - 100,
						self.canvas.winfo_height()/2 + 100
					),
					np.random.uniform(-1, 1),
					np.random.uniform(-1, 1),
			)
			creating = False
			for body in self.bodies:
				dist = temp_body.distance(body)
				if dist <= body.r + temp_body.r:
					creating = True
					break
			
		return temp_body

	def reset_bodies(self):
		for body in self.bodies:
			body.destroy()

		self.bodies = []

	def run(self):
		self.running = True
		pos, vel, mass = get_vectors(self.bodies)
		self.acc = get_acceleration(pos, mass, self.gravity, self.softening)
		while self.running:
			self.update()
			
			# sleep(self.dt)
			self.canvas.update()


	def update(self):
		# Here I have to update the velocities
		pos, vel, mass = get_vectors(self.bodies)
		vel += self.acc * self.dt / 2.0
		pos += vel * self.dt
		self.acc = get_acceleration(pos, mass, self.gravity, self.softening)
		vel += self.acc * self.dt / 2.0
		set_bodies(pos, vel, self.bodies)

		# Redraw all the bodies
		for i in range(len(self.bodies)):
			self.bodies[i].destroy()
			self.bodies[i].show()


	def pause(self):
		self.running = False