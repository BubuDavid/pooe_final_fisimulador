import numpy as np

def get_vectors(bodies):
	N = len(bodies)
	pos = np.random.randn(N, 2)
	vel = np.random.randn(N, 2)
	mass = np.ones((N, 1))
	for i, body in enumerate(bodies):
		vel[i, 0] = body.V[0]
		vel[i, 1] = body.V[1]
		pos[i, 0] = body.P[0]
		pos[i, 1] = body.P[1]
		mass[i, 0] = body.m

	vel -= np.mean(mass * vel,0) / np.mean(mass)
	return pos, vel, mass
	

def get_acceleration(pos, mass, G, softening):
	# Credits https://github.com/pmocz/nbody-python/blob/master/nbody.py
	x = pos[:,0:1]
	y = pos[:,1:2]

	# matrix that stores all pairwise particle separations: r_j - r_i
	dx = x.T - x
	dy = y.T - y

	# matrix that stores 1/r^3 for all particle pairwise particle separations 
	inv_r3 = (dx**2 + dy**2 + softening**2)
	inv_r3[inv_r3>0] = inv_r3[inv_r3>0]**(-1.5)

	ax = G * (dx * inv_r3) @ mass
	ay = G * (dy * inv_r3) @ mass
	
	# pack together the acceleration components
	a = np.hstack((ax,ay))

	return a


def set_bodies(pos, vel, bodies):
	for i, body in enumerate(bodies):
		body.V[0] = vel[i, 0] 
		body.V[1] = vel[i, 1]
		body.P[0] = pos[i, 0]
		body.P[1] = pos[i, 1]