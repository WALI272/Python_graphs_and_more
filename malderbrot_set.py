import numpy as np 
import matplotlib.pyplot as plt

def mandelbrot(c, max_iterations):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iterations:
        z = z*z + c
        n += 1
    return n 

def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iterations):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    c = X + 1J * Y
    mandelbrot_matrix = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            mandelbrot_matrix[i, j] = mandelbrot(c[i, j], max_iterations)

    return mandelbrot_matrix

def plot_mandelbrot(mandelbrot_matrix, x_min, x_max, y_min, y_max):
    plt.imshow(mandelbrot_matrix, extent=(x_min, x_max, y_min, y_max), cmap='hot', interpolation='bilinear')
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()

if __name__ == "__main__":
    width, height = 800, 600
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    max_iterations = 500

    mandelbrot_matrix = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iterations)
    plot_mandelbrot(mandelbrot_matrix, x_min, x_max, y_min, y_max)