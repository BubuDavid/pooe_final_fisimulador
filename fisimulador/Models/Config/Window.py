from tkinter import *
from tkinter import ttk

from ..Frames.MenuFrame import MenuFrame
from ...assets.data.menu import simulations

from .Styles import Styles

class Window(Tk):
	def __init__(self):
		super().__init__()
		self._frame = None

		self.initial_configuration()
		self.switch_to_menu()
		Styles()

	def initial_configuration(self):
		# Logo
		self.logo_img = PhotoImage(file='fisimulador/assets/images/logo.png')
		self.tk.call('wm', 'iconphoto', self._w, self.logo_img)

		# Full screen
		try:
			self.attributes('-zoomed', True)
		except:
			self.state('zoomed')

		# Standard dimensions
		window_props = {
			"width": 1024,
			"height": 812,
			"posx": 400,
			"posy": 100,
		}
		self.geometry(f'{window_props["width"]}x{window_props["height"]}+{window_props["posx"]}+{window_props["posy"]}')		
		
	def switch_frames(self, frame, **args):

		if self._frame is not None:
			self._frame.destroy()

		new_frame = frame(self, **args)
		self._frame = new_frame

	def switch_to_menu(self):
		self.switch_frames(
			MenuFrame,
			simulations = simulations,
			borderwidth = 1,
			relief = 'raised',
			padding = 16
		)