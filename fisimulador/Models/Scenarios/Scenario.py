class Scenario:
	def __init__(self, canvas, simulation, params):
		self.canvas = canvas
		self.simulation = simulation
		self.params = params

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
					
				if not current_value_float in list(range(limits[0], limits[1] + 1)):
					return False
				

		return True