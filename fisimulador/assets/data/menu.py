simulations = [
	{
		"name": "collisions_pi",
		"display_name": "Calculando PI con\ncolisiones elásticas",
	},
	{
		"name": "free_fall",
		"display_name": "Caída Libre",
	},
	{
		"name": "n-body",
		"display_name": "Simulación de N cuerpos",
		"params": [
			{'name': 'Número de cuerpos', 'limits': [2, 100], 'default': '2'},
			{'name': 'Intensidad de Gravedad', 'limits': [1, 100], 'default':"1.0"}
		]
	},
	{
		"name": "launch",
		"display_name": "Lanzamiento de Objetos",
	},
	
]