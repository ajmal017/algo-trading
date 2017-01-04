# From: http://stackoverflow.com/questions/11874767/real-time-plotting-in-while-loop-with-matplotlib
# Realtime plotting

import matplotlib.pyplot as plt
import numpy as np
plt.ion() ## Note this correction
fig=plt.figure()
#  range    X       Y
plt.axis([0,100,0,50])

i=0
x=list()
y=list()

while i <100:
    temp_y=np.random.randint(0,100);
    x.append(i);
    y.append(temp_y);
    plt.scatter(i,temp_y);
    i+=1;
    plt.show()
    plt.pause(0.0001) #Note this correction
