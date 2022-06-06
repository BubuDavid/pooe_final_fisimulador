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

	def label(self):
		# Styles for Labels
		self.configure(
			'TLabel',
			background = 'white',
			font = "Helvetica 12"
		)
		self.configure(
			'Title.TLabel',
			font = "Helvetica 20"
		)
		self.configure(
			'CanvasLabel.TLabel',
			font = "Helvetica 20",
			background = "#F0D9FF"
		)
