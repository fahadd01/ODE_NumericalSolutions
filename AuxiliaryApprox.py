
import numpy as np
import math
from numpy import pi
import matplotlib.pyplot as plt

dis = 5

x0 = np.linspace(0,pi,dis)  #discretize x
t = np.linspace(0,1,dis)    #discretize t

Vx = np.zeros(dis)          #velocity at each x 

u = np.zeros((dis,dis),float)

for n in range (1,10):          #for summation
    for i in range (dis):           #for x
        Vx[i] += ((4*(1-(-1)**n))*(np.sin(n*x0[i])))/(pi*(n**3))
        for j in range (dis):           #for t
            u[i][j] = ((Vx[i])*(math.exp((-2+math.sqrt(4-(n**2))*t[j])-math.exp((-2-math.sqrt(4-(n**2)))*t[j]))))/(2*(math.sqrt(4-(n**2))))
print(u)
#u[0] = 0
#u[dis-1] = 0
#u[i][j] += Tn[j]*np.sin(n*x0[i])
#print(u)
#plt.plot(t,x0,u)
#plt.show()













'''
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use('dark_background')

fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.add_subplot(1,1,1)

x0 = np.linspace(0,pi,10000)
#Wave speed
for i in range (10000):
    c = ((4-4*((-1)**i))*(np.sin(i*x0)))/(pi*(i**3))

#x axis
x0 = np.linspace(0,pi,10000)

#Initial time
t0 = 0

#Time increment
dt = 0.05

#Wave equation solution
def u(x,t):
    return 0.5*(np.sin(x+c*t) + np.sin(x-c*t))

a = []

for i in range(500):
    value = u(x0,t0)
    t0 = t0 + dt
    a.append(value)

k = 0
def animate(i):
    global k
    x = a[k]
    k += 1
    ax1.clear()
    plt.plot(x0,x,color='cyan')
    plt.grid(True)
    plt.ylim([-2,2])
    plt.xlim([0,pi])
    
anim = animation.FuncAnimation(fig,animate,frames=360,interval=20)
plt.show()
'''
