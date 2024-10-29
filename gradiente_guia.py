import numpy as np # lib para trabajar con arreglos
import matplotlib.pyplot as plt # lib para graficar

# 1. defino una funcion objetivo que sera optimizada
def f(x):
    return x**2

# 2. defino el gradiente de la funcion
def gradient(x):
    return 2 * x

# 3. defino el gradiente descendiente
def gradien_desce(x_start, alpha, num_iterations):
    x = x_start
    trayectory = [x]
    for _ in range(num_iterations):
        x = x - alpha*gradient(x) # actualizar trayectoria de gradiente
        trayectory.append(x) # almacena la nueva solucion
        return np.array(trayectory) # devuelve los valores almacenados del gradiente

# 4. inicializar los parametros del gradiente
x_start = 5 # inicializar x en un lugar aleatorio de la funcion
alpha = 0.1 # tasa de aprendizaje
num_iterations = 20 # numero de iteraciones hasta que encuentre un maximo o minimo local

trayectory = gradien_desce(x_start, alpha, num_iterations)
# 5. graficar la funcion objetivo y sus soluciones
x = np.linspace(-6, 6, 400)
y = f(x)

plt.figure(figsize=(8,6))
plt.plot(x, y, label='$f(x)=x^2$', color='blue')
plt.scatter(trayectory, f(trayectory), color='red', zorder=5)
plt.plot(trayectory, f(trayectory), color='red', linestyle='--', label='trayectoria del gradiente')
plt.xlabel('$x$')
plt.xlabel('$f(x)$')
plt.title('gradiente descendente')
plt.legend()
plt.grid(True)
plt.show()
#%%