import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

'''
Kindly, note that I compiled my assignment before the update about the typo in question 3
Therefore, I have analysed the critical values and convergence to the best of my conceptual
base and online research
'''

# 3.1.

def solver_plotter(x0, y0, plotdecision):
    
    f0 = [x0, y0]                          # Initial conditions on displacement and velocity
    t = np.linspace(0,50,100)
    def system(f,t):                       # Defining the system
        x,y = f
        return [y, (2*np.sin(x))]
    x = odeint(system, f0, t)[:,0]         # ODEINT Solver
    if plotdecision == 1:
        plt.plot(t,x)                      # Plotter
        plt.title(x0)
        plt.xlabel('t')
        plt.ylabel('x')
        plt.show()
    return x,t

xa, ta = solver_plotter(0.25, 0, 1)
print('3.1.\n\nalpha = 0.25\nRefer to plot titled : "0.25"\nEstimates from plot : Amplitude is around ', max(xa), ' and Period is around ', 50/5, '\n\n')

xb, tb = solver_plotter(0.1, 0, 1)
print('alpha = 0.1\nRefer to plot titled : "0.1"\nEstimates from plot : Amplitude is around ', max(xb), ' and Period is around ', 50/4, '\n\n')

xc, tc = solver_plotter(0.05, 0, 1)
print('alpha = 0.05\nRefer to plot titled : "0.05"\nEstimates from plot : Amplitude is around ', max(xc), ' and Period is around ', 50/3.5, '\n\n')

'''
For estimation of period I have divided the total time by number of phases of Wave
For estimation of amplitude I have considered the max value of the x array returned by system solver
'''

# 3.2.

xd, td = solver_plotter(0.01, 0, 1)
print('3.2.\n\nAditionally,\n\nalpha = 0.01\nRefer to plot titled : "0.01"\nEstimates from plot : Amplitude is around ', max(xd), ' and Period is around ', 50/2.7, '\n\n')
A = [max(xa), max(xb), max(xc), max(xd)]
T = [50/5, 50/4, 50/3.5, 50/2.7]
alpha = [0.25, 0.1, 0.05, 0.01]
plt.scatter(alpha, A)
plt.xlabel('Alpha')
plt.ylabel('Aplitude')
plt.title('Amplitude as alpha approaches 0')
plt.show()
plt.scatter(alpha, T)
plt.xlabel('Alpha')
plt.ylabel('Period')
plt.title('Period as alpha approaches 0')
plt.show()
print('Estimating values of amplitude and period as alpha (angular displacement) is reduced, reveals that as alpha approaches to zero: \n\nAmplitude increases linearly\nPeriod keeps increases exponentially and approaches infinity as alpha approaches 0\n\nAlso refer to plots of amplitude and period as alpha aproaches zero\n\n')

# 3.3

ALPHA = np.linspace(0,25,100)
AMPLITUDE = []
for alp in ALPHA:
    x, t = solver_plotter(alp, 0, 0)
    AMPLITUDE.append(max(x))
plt.plot(ALPHA, AMPLITUDE)
plt.xlabel('Alpha')
plt.ylabel('Amplitude')
plt.title('Critical values of Alpha')
plt.show()

print('3.3.\n\nRefer to "critical values of alpha" plot to visualise the jumps in convergence of amplitude as alpha takes substantially large values\n\nClose observation of these critical values reveal that these occur at whole no. multiples of pi\n\nSimilar shift in Period can be observed by passing 1 in the Solver function and analysisng the changes in Time Period of the plotted graphs')