from tkinter import *
from tkinter.ttk import  Style

class Styles(Style):
	def __init__(self):
		super().__init__()
		self.frame()
		self.label()
	
	
	def frame(self):
		# Styles for Frames
		self.configure(
			'TFrame', 
			background = 'white'
		)
		self.configure(
			'Menu.TFrame', 
			background = '#FFE0E1'
		)
		self.configure(
			'Focus.TFrame',
			background = "#FCCBCD"
		)

	def label(self):
		# Styles for Labels
		self.configure(
			'Menu.TLabel',
			background = '#FFE0E1',
			font = "Helvetica 12 bold",
			foreground = '#415A75'
		)
		self.configure(
			'TLabel',
			background = 'white',
			font = "Helvetica 12 bold",
			foreground = '#415A75'
		)
		self.configure(
			'Menu.Title.TLabel',
			font = "Helvetica 20 bold",
			background = '#FFE0E1',
		)
		self.configure(
			'Title.TLabel',
			font = "Helvetica 20 bold"
		)
		self.configure(
			'CanvasLabel.TLabel',
			font = "Helvetica 20",
			background = "#F0D9FF"
		)

		self.configure(
			'Error.TLabel',
			foreground = 'red'
		)
