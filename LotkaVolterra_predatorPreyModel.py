import numpy as np
import matplotlib.pyplot as plt

'''
Rabbits: dr/dt =  ax - bxy
Foxes: df/dt = -cx + dxy
'''

#2.a.

x0 = 100
y0 = 11

xe = 200
ye = 4

a = 8
c = 1
d = c/xe
b = a/ye

t = np.linspace(0,10,1000)

def LV_FE(x0, y0, a, b, c, d, t):
    x = []
    y = []
    
    x.append(x0)
    y.append(y0)
    
    for n in range(len(t)-1):
        dt = t[n+1] - t[n]
        x.append(x[n]*(1 + a*dt - b*dt*y[n]))
        y.append(y[n]*(1 - c*dt + d*dt*x[n]))
        
    return x,y

x1, y1 = LV_FE(x0, y0, a, b, c, d, t)

plt.plot(t, x1, label = 'Rabbits')
plt.plot(t, y1, label = 'Foxes')
plt.xlabel('Time')
plt.ylabel('population')
plt.legend()
plt.title('2.a: Lotka-Volterra using Forward Euler')
plt.show()

plt.plot(x1,y1)
plt.xlabel('Rabbits')
plt.ylabel('Foxes')
plt.title('2.a: Contour Plot')
plt.show()
print('2.a.\n\nRefer to plots 2.a:\n\n')

#2.b.

def LV_RK4(x0, y0, a, b, c, d, t): 
    x= []
    y= []
    
    x.append(x0)
    y.append(y0)
    
    for n in range(len(t)-1): 
        dt = t[n+1] - t[n]
        k1=[a*x[n] - b*x[n]*y[n], -c*y[n] + d*x[n]*y[n]] 
        k2=[a*(x[n] + dt*k1[0]/2) - b*(x[n] + dt*k1[0]/2)*(y[n] + dt*k1[1]/2), -c*(y[n] + dt*k1[1]/2) + d*(x[n]+dt*k1[0]/2)*(y[n] + dt*k1[1]/2)]
        k3=[a*(x[n] + dt*k2[0]/2) - b*(x[n] + dt*k2[0]/2)*(y[n] + dt*k2[1]/2), -c*(y[n] + dt*k2[1]/2) + d*(x[n]+dt*k2[0]/2)*(y[n] + dt*k2[1]/2)]
        k4=[a*(x[n] + dt*k3[0]) - b*(x[n] + dt*k3[0])*(y[n] + dt*k3[1]), -c*(y[n] + dt*k3[1]) + d*(x[n]+dt*k3[0])*(y[n] + dt*k3[1])]
        x.append(x[n] + dt*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/6)
        y.append(y[n] + dt*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/6) 
        
    return x,y

x2, y2 = LV_RK4(x0, y0, a, b, c, d, t)

plt.plot(t, x2, label = 'Rabbits')
plt.plot(t, y2, label = 'Foxes')
plt.xlabel('Time')
plt.ylabel('population')
plt.legend()
plt.title('2.b: Lotka-Volterra using RK4')
plt.show()

plt.plot(x1, y1, label = 'FE')
plt.plot(x2, y2, label = 'RK4')
plt.xlabel('Rabbits')
plt.ylabel('Foxes')
plt.legend()
plt.title('2.b: Contour Plot')
plt.show()

print('2.b.\n\nRefer to plots 2.b:\n\n')

#2.c.

x3, y3 = LV_FE(xe+0.01, ye+0.01, a, b, c, d, t) 

plt.plot(x3,y3)
plt.xlabel('Rabbits')
plt.ylabel('Foxes')
plt.title('2.c: Lotka-Volterra using Forward Euler with slight perturbations')
plt.show()

print('2.c.\n\nRefer to plots 2.c:\n\n')

#2.d. (BONUS)

x4, y4 = LV_FE(100, 1, a, b, c, d, t)
x5, y5 = LV_FE(100, 3, a, b, c, d, t)

plt.plot(x4, y4, label = '100 Rabbits and 1 Fox')
plt.plot(x5, y5, label = '100 Rabbits and 3 Foxes')
plt.xlabel('Rabbits')
plt.ylabel('Foxes')
plt.legend()
plt.title('2.d: Contour Plot')
plt.show()

print('2.d.\n\nRefer to plots 2.d:\n\n')
