simulations = [
	{
		"name": "collisions_pi",
		"display_name": "Calculando PI con\ncolisiones elásticas",
		"params": [
			{'name': 'Número de dígitos', 'limits': [1, 6], 'default': '1'},
		],
		"image": "collisions_pi.jpg"
	},
	{
		"name": "free_fall",
		"display_name": "Caída Libre",
		'params': [
			{"name": "Puedes colocar objetos \n donde quieras"},
			{"name": "Gravedad", 'dLimits': [1, 100], 'default': '9.8'},
		],
		"image": "freefall.jpg"
	},
	{
		"name": "n-body",
		"display_name": "Simulación de N cuerpos",
		"params": [
			{'name': 'Número de cuerpos', 'limits': [2, 100], 'default': '2'},
			{'name': 'Intensidad de Gravedad', 'limits': [0.001, 100], 'default':"1.0"}
		],
		"image": "n-body.jpg"
		
	},
	
]