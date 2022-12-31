# Calculating-the-Orbit-of-a-Celestial-Object-using-the-Euler-Method
This Python code calculates the orbits of celestial objects (such as planets or moons) around a central object (such as a planet or a star) using the Euler method.
The orbits are calculated based on the masses of the objects and their initial positions and velocities.

## Getting started:
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites:
This project requires the **numpy** Python package.

You can install these packages using 'pip':
pip install numpy

## Running the code
To run the code, clone the repository and navigate to the root directory of the project. Then, run the following command:

python_orbit.py

## Modifying the code
You can modify the code to change the initial conditions (such as the position and velocity of the celestial object), the mass of the objects, or the time step. You can also change the number of time steps to simulate the orbit for a longer or shorter period of time.


## Usage:
To use the code, set the following parameters:

G: Gravitational constant.

m: Mass of the celestial object.

r: Initial position of the celestial object (as a NumPy array).

v: Initial velocity of the celestial object (as a NumPy array).

M: Mass of the central object.

dt: Time step.

n_steps: Number of time steps.

Then, run the code to calculate the orbits of the celestial object. The positions and velocities of the object will be printed at each time step.

## Acknowledgments
This project was inspired by the equations of motion and the Euler method.
