"""

Program to compute the final velocity of an object, given initial velocity,
acceleration and distance traveled

https://www.khanacademy.org/science/physics/one-dimensional-motion/kinematic-formulas/a/what-are-the-kinematic-formulas

v^2 = v0^2 + 2 a (X - X0)

Inputs:
    - Initial velocity (float)
    - Acceleration (float)
    - Initial position in X (float)
    - Final position in X (float)

Output:
    - Final velocity (float)

Gilberto Echeverria
16/08/2020
"""

import math

# Get the inputs
v_0 = float(input("Ingrese la velocidad inicial: "))
a = float(input("Enter acceleration: "))
x_0 = float(input("Enter initial position: "))
x = float(input("Enter final position: "))

v = math.sqrt(v_0**2 + 2 * a * (x - x_0))

print(f"Final velocity: {v}")
