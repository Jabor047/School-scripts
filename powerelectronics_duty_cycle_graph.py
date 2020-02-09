
import matplotlib.pyplot as plt
import math
import numpy as np

linei = []
lineii = []
linev = []
x = []

z = 0
i = 0
k = 0

for z in range(0, 6):
    # if z == 0:
    #     while i <= 1:
    #         k = (math.exp(0) - 1) / ((math.exp(0)) - 1)
    #         linei.append(abs(k))
    #         i += 0.01
    #     i = 0
    #     k =
    if z == 1:
        while i <= 1:
            k = (math.exp(i * (z ** -1)) - 1) / ((math.exp(z ** -1)) - 1)
            linei.append(abs(k))
            i += 0.01
        i = 0
        k = 0
    elif z == 2:
        while i <= 1:
            k = (math.exp(i * (z ** -1)) - 1) / ((math.exp(z ** -1)) - 1)
            lineii.append(abs(k))
            i += 0.01
        i = 0
        k = 0
    elif z == 4:
        i = 0
        k = 0
    elif z == 5:
        while i <= 1:
            k = (math.exp(i * (z ** -1)) - 1) / ((math.exp(z ** -1)) - 1)
            linev.append(abs(k))
            i += 0.01
        i = 0
        k = 0
    
while i <= 1:
    x.append(i)
    i += 0.01

plt.title("Duty ratio for the limit of continuous conduction")

plt.plot(x,linei,color='m',label="1")
plt.plot(x,lineii,label="2",color='g')
plt.plot(x,linev,color='r',label="5")

plt.xlabel("Duty Cycle")
plt.ylabel("g=F(a)")
plt.xticks(np.arange(min(x),1.2, 0.1))
plt.yticks(np.arange(min(x),1.2, 0.1))
plt.grid(color="k", linestyle='-',linewidth=0.5)
plt.legend(bbox_to_anchor =(1.05,1),loc=1,borderaxespad = 0 )
plt.show()
