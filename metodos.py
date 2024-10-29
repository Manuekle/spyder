import numpy as np 

# Función cuadrática 

def f(theta): 

    return theta**2 + 3*theta + 4 

# Derivada de la función 

def gradient(theta): 

    return 2*theta + 3 

# Gradiente descendente 

theta = 10  # Punto inicial 

alpha = 0.1  # Tasa de aprendizaje 

for _ in range(100): 

    grad = gradient(theta) 

    theta = theta - alpha * grad 

print(f"El valor mínimo de theta es: {theta}") 

import numpy as np 

# Función cuadrática negativa 

def f(theta): 

    return -(theta**2 + 3*theta + 4) 

  

# Derivada de la función 

def gradient(theta): 

    return - (2*theta + 3) 

  

# Gradiente ascendente 

theta = 10  # Punto inicial 

alpha = 0.1  # Tasa de aprendizaje 

  

for _ in range(100): 

    grad = gradient(theta) 

    theta = theta + alpha * grad 

  

print(f"El valor máximo de theta es: {theta}") 

import sympy as sp 

  

x = sp.symbols('x') 

f = x**2 + 3*x + 4 

  

# Derivada de la función 

f_prime = sp.diff(f, x) 

  

# Evaluar la derivada en un punto, por ejemplo, x = 2 

valor_derivada = f_prime.subs(x, 2) 

print(f"La derivada de la función en x=2 es: {valor_derivada}") 