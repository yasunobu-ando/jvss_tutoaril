import numpy as np
import matplotlib.pyplot as plt

def plot_sin():
    x = np.linspace(-np.pi, np.pi)
    y = np.sin(x)

    plt.plot(x,y)
    plt.show()
    return