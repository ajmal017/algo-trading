import matplotlib.pyplot as plt
from numpy import linspace, sin, pi
plt.ion()
print "Is interactive:?", plt.isinteractive()

x = linspace(-pi, pi, 1001)
plt.plot(x, sin(x))

raw_input() #keep the window open
