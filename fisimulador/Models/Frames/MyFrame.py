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