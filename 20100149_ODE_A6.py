#Libraries
import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy.linalg import norm as norm
import pandas as pd
from numpy import exp as e
from numpy import sin as sin 
from numpy import cos as cos

#1.2.
print('1.2.')

def DE1(t,y,lam):
    return lam * (y - sin(t)) + cos(t)

def Forward_Euler(xstart, xend, ystart, h, n, lam):
    x=[]
    y=[]
    x.append(xstart)
    y.append(ystart);
    for i in range(n):
        x.append(x[i] + h)
        y.append(y[i] + h * DE1(x[i], y[i], lam))
    return x, y

def Heuns(xstart, xend, ystart, h, n, lam):
    x = []
    y = []
    x.append(xstart)
    y.append(ystart);
    for i in range(n):
        x.append(x[i] + h)
        ynew = y[i] + h * DE1(x[i], y[i],lam)
        ycorr = (DE1(x[i], y[i], lam) + DE1(x[i+1], ynew, lam))/2.  #Corrector 
        y.append( y[i] + h * ycorr)
    return x, y

h = 0.01
print("Step Size ", h)
n = 1/h
lam = [10,-10,-500]
t = np.linspace(0, 1, int(n)+1)

y_FE = []
y_H = []
y_E = []
j = 0
for i in lam:
    ti,yi  = Forward_Euler(0, 1, 1, h, int(n), i)
    tii,yii = Heuns(0, 1, 1, h, int(n), i)
    ye = e(i*t)+sin(t); 
    plt.plot(t,yi,'b', label='Forward Euler')
    plt.plot(t,yii,'r', label='Heuns Method')
    plt.plot(t,ye,'k', label='Exact Solution')
    plt.title("1.2. for Lambda =" + str(i))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    y_FE.append(yi)
    y_H.append(yii)
    y_E.append(ye)
    j = j + 1

for i in range(len(y_FE)):
    err_FE = npla.norm(abs(y_FE[i] - y_E[i]))/npla.norm(y_FE[i]);
    print('\nError using Forward Euler for lambda : ', lam[i], '=', err_FE)
    err_H = npla.norm(abs(y_H[i] - y_E[i]))/npla.norm(y_H[i]);
    print('\nError using Heuns Method for Lambda : ', lam[i], '=', err_H)

#2.2. and 2.3.
print('2.2. and 2.3.')
    
def DE2(x,y):
    return x*y

def RK2(x0,xn,y0,h,n):
    x = [x0]
    y = [y0]
    print('x0\ty0\tyn')
    for i in range(n):
        k1 =  (DE2(x0, y0))
        k2 =  (DE2((x0+h), (y0+h*k1)))
        yn = y0 + h*(k1+k2)/2
        print('%.4f\t%.4f\t%.4f'% (x0,y0,yn) )
        y0 = yn
        x0 = x0+h
        x.append(x0)
        y.append(y0)
    return x,y

def Relative_Error(y_actual,y_RK2):
    error = norm(np.subtract(y_actual,np.array(pd.DataFrame(y_RK2))))/norm(y)
    return error

step = [2,4,8]
h = ['0.2', '0.1', '0.05']
j = 0
errors = []
for i in step:
    x = np.linspace(1,1.4,i+1)
    y = odeint(DE2,1,x)
    x1,y1 = RK2(1,1.4,1,(0.4/i),i)
    RE = Relative_Error(y,y1)
    print('\nRelative Error for h = ', h[j], 'is equal to', RE)
    errors.append(RE)
    plt.plot(x,y, label = 'Analytical')
    plt.plot(x1,y1, label = 'Numerical')
    plt.title('2.3: h = ' + h[j])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    j = j+1
print('\nNote: Refer to .pdf for 2.3. Error Analysis')

#3.
print('3.')

def DE3(x,y):
    return 1/(x+y)

def RK4(x0, xn, y0, n):
    x = [x0]
    y = [y0]
    h = (xn-x0)/n

    print('x0\ty0\tyn')
    for i in range(n):
        k1 =  (DE3(x0, y0))
        k2 =  (DE3((x0+h/2), (y0+k1/2)))
        k3 =  (DE3((x0+h/2), (y0+k2/2)))
        k4 = (DE3((x0+h), (y0+k3)))
        yn = y0 + h*(k1 + 2*k2 + 2*k3 + k4)/6
        print('%.4f\t%.4f\t%.4f'% (x0,y0,yn) )
        y0 = yn
        x0 = x0+h
        x.append(x0)
        y.append(y0)
    return x,y

x2, y2 = RK4(0, 2, 1, 4)
x = np.linspace(0.,2., 5)
y = odeint(DE3, 1, x)
plt.plot(x, y, label = 'Analytical')
plt.plot(x2,y2, label = 'Numerical')
plt.title('3.')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()