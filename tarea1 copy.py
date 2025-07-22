import matplotlib.pyplot as plt
import numpy as np
import math

#grafica de la funcion seno para Python
x=np.linspace(-10,10,400)
seno= np.sin(x)
plt.figure(figsize = (10, 4))
plt.plot(x, seno, color = "blue", linewidth = 3) 

plt.title("Gráfica de la función seno")
plt.xlabel("X")
plt.ylabel("sin(x)")





plt.legend()
plt.show()

