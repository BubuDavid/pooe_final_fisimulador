from tkinter import *
from tkinter import ttk

class Styles:
	def __init__(self):
		# Initialize style
		self.styles = ttk.Style()
		self.frame()
		self.label()


	def frame(self):
		# Styles for Frames
		self.styles.configure(
			'TFrame', 
			background = 'white'
		)

	def label(self):
		# Styles for Labels
		self.styles.configure(
			'TLabel',
			background = 'white',
			font = "Helvetica 12"
		)
		self.styles.configure(
			'Title.TLabel',
			font = "Helvetica 20"
		)

	def canvas():
		pass

	