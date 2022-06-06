from PIL import Image, ImageTk

class MyImage:
	def __init__(self, path, width, height):
		self.path = path
		self.width = width
		self.height = height

	def get_image(self):
		img = Image.open(self.path)
		resized_img = img.resize((self.width, self.height), Image.ANTIALIAS)
		self.image =  ImageTk.PhotoImage(resized_img)
		return self.image