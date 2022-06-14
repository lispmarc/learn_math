import math
import matplotlib.pyplot as plt 

from numpy import arange

def waves_plot(wave):
    x=list(arange(-3*math.pi,3*math.pi,0.1))
    y=[wave(i) for i in x]
    fig,ax = plt.subplots()
    ax.plot(x,y)
    plt.show()
    