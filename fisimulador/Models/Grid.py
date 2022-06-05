from tkinter import *
from tkinter import ttk

class Grid(Canvas):
	def __init__(self, window, parent, **options):
		super().__init__(parent, options)
		window.update_idletasks()
		self.width = window.winfo_width()
		self.height = window.winfo_height()
		self.create_grid()

	def create_grid(self):
		w = self.width
		h = self.height
		# horizontal lines
		self['bg'] = "#F3F1F5"
		for pos in range(0, w, 50):
			self.create_line(0, pos, w, pos, fill = "#F0D9FF", width = 1)
			self.create_line(pos, 0, pos, h, fill = "#F0D9FF", width = 1)


	def reset(self):
		self.delete('all')
		self.create_grid()