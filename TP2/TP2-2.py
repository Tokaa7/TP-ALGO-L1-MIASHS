"""

    TP2 - 2.Tracer une courbe d'une fonction continue calculée avec numpy.linspace

"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3-5*(x**2)+2*x+8

x=np.linspace(-3,5)
y=f(x)
plt.plot(x,y,'r')
plt.title("f(x)")
plt.xlabel("x")
plt.ylabel("x^3 - 5x^2 + 2x + 8")
plt.axvline(0,0)
plt.axhline(0,0)
plt.savefig("f(x).png")