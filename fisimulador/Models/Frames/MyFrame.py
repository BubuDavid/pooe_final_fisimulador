from tkinter import *
from tkinter import ttk

from ..Components.MyImage import MyImage

class MyFrame(ttk.Frame):
	def __init__(self, parent, **args):
		super().__init__(parent, **args)


	def initial_configuration(self, columns, rows):
		self.grid(
			column = 0,
			row = 0,
			sticky = "NSEW"
		)
		
		
		self.columnconfigure(columns, weight = 1)
		self.rowconfigure(rows, weight = 1)
		self.pack(fill = 'both', expand = 1)
		self.parent.update_idletasks()
		width = self.winfo_width()
		height = self.winfo_height()

		# img = MyImage('./fisimulador/assets/images/bg.jpg', width, height).get_image()
		# lbl = ttk.Label(self.parent, image=img)
		# lbl.img = img  # Keep a reference in case this code put is in a function.
		# lbl.place(relx = 0, rely = 0)  # Place label in center of parent.