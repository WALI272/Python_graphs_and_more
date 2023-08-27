import numpy as np
import matplotlib.pyplot as plt

# Definimos el rango de valores de r en radianes
r_values = np.linspace(0, 2*np.pi, 1000)

# Calculamos los valores correspondientes de e^{i*r}
complex_values = np.exp(1j * r_values)

# Extraemos las partes real e imaginaria
real_part = np.real(complex_values)
imaginary_part = np.imag(complex_values)

# Creamos la gráfica
plt.figure(figsize=(8, 6))
plt.plot(r_values, real_part, label='Parte Real')
plt.plot(r_values, imaginary_part, label='Parte Imaginaria')
plt.xlabel('r (radianes)')
plt.ylabel('Valor')
plt.title('Representación de e^{i*r}')
plt.legend()
plt.grid(True)
plt.show()
