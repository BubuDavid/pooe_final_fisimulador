class Scenario:
	def __init__(self, canvas, simulation, params):
		self.canvas = canvas
		self.simulation = simulation
		self.params = params
		self.have_buttons = True

	def validate_params(self):
		for param in self.simulation.get("params", []):
			limits = param.get('limits', False)
			if limits:
				name = param['name']
				current_value = self.params[name].get()
				if not len(current_value.strip()): 
					return False
				try:
					current_value_float = float(current_value)
				except:
					return False
					
				if current_value_float < limits[0] or current_value_float > limits[1]:
					return False
				

		return True

	def set_params(self, simulation, params):
		self.simulation = simulation
		self.params = params