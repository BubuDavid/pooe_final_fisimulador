from tkinter import *
from tkinter import ttk
import numpy as np

class Body:
	def __init__(self, canvas, x, y, vx, vy, r = 10, m = 1, color = 'purple'):
		self.center_x = x + r
		self.center_y = y + r
		self.r = r
		self.m = m
		self.P = np.array([self.center_x, self.center_y], dtype = np.float64)
		self.V = np.array([vx, vy], dtype = np.float64)
		self.canvas = canvas
		self.color = color

	def show(self):
		self.canvas_id = self.canvas.create_oval(
			self.P[0] - self.r,
			self.P[1] - self.r,
			self.P[0] + self.r,
			self.P[1] + self.r,
			fill = self.color
		)

	def destroy(self):
		self.canvas.delete(self.canvas_id)

	def distance(self, other):
		subs = self.P - other.P
		dist = subs[0]**2 + subs[1]**2
		return dist**(1/2)


	def move(self):
		self.canvas.move(
			self.canvas_id,
			self.V[0],
			self.V[1],
		)