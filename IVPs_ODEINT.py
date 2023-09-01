import matplotlib.pyplot as plt 
import numpy as np 
from scipy.integrate import odeint
from scipy.integrate import quad
import math

#3.2

def vfunc(v,y):
    return (-1)/(v*((1+y)**2))

for i in range (3):
    v0 = 2*i+1  #v0 value
    ys = np.arange(0,10, 0.001)
    vs = odeint(vfunc, v0, ys)
    plt.plot(ys, vs, label = 2*i+1)
    plt.xlabel('y(s)')
    plt.ylabel('v(s)')
    plt.legend()
    plt.show()
print('QUESTIOIN 3 PART 2 REFER to plots')

#3.3
def funcy(y,v):
    return v
def funcv(v,y):
    return (-1)/((1+y)**2)

ys = np.arange(-0.999,15.001, 0.001)
vs = np.arange(-2,3.001,0.001)
y0 = 0
yss = odeint(funcy, y0, vs)
for i in range (1,4):
    v0 = i/2
    vss = odeint(funcv, v0, ys)
    plt.plot(ys,vss, label = 'v(y)')
    plt.plot(yss,vs, label = 'y(v)')
    plt.xlabel('y(s)')
    plt.ylabel('v(s)')
    plt.legend()
    plt.show()
print(np.max(yss))
print()
print('QUESTIOIN 3 PART 3 REFER to plots')

#1.1 and 1.2
#Could not manage to use quad function to integrate successively in a loop with variable upper limit 't'
#I have hard coded the evaluated terms instead
#kindly consider for partial credit as we did not cover integration in python in class formally
'''
t = np.linspace(0, 1, 100)
x = 2 + 0*t

for i in range (1,7):
    plt.plot(t, x, label = i-1)
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('x')
    x = x + (2**((5**i)/(3**i)))*(t**i)

t = np.linspace(0, 1, 100)
x = 2 + 0*t

for i in range (1,7):
    plt.plot(t, x, label = i-1)
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('x')
    x = x + (2**((5**i)/(3**i)))*(t**i)

t = np.linspace(0, 5, 100)

x0 = 1 + 0*t
x1 = 1 + math.cos(1)*t
x2 = 1 + (math.sin(t*(math.cos(1))+1))/(math.cos(1))
x3 = 2 + (2**(5/3))*t + (2**(25/9))*(t**2) + (2**(125/27))*(t**3) 
plt.plot(t, x0, 'b')
plt.plot(t, x1, 'r')
plt.plot(t, x2, 'g')
plt.plot(t, x3, 'y')
'''
