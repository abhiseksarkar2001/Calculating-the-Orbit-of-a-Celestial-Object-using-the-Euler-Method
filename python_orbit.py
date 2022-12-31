#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing necessary packages
import numpy as np

# Gravitational constant
G = 6.67430e-11

# Mass of the celestial object
m = 1.0

# Initial position and velocity of the object
r = np.array([1.0, 0.0])
v = np.array([0.0, 1.0])

# Mass of the central object (such as a planet or a star)
M = 1.0

# Time step
dt = 1.0

# Number of time steps
n_steps = 100

for i in range(n_steps):
  # Calculate the distance between the celestial object and the central object
  r_vec = r - np.array([0.0, 0.0])
  r_mag = np.sqrt(np.dot(r_vec, r_vec))
  
  # Calculate the gravitational force acting on the object
  F = G * m * M / r_mag**2
  
  # Calculate the acceleration of the object
  a = F / m
  
  # Calculate the new velocity of the object
  v = v + a * dt
  
  # Calculate the new position of the object
  r = r + v * dt
  
  # Print the position and velocity of the object
  print(f"Position: {r}")
  print(f"Velocity: {v}")

