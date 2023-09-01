import numpy as np
import matplotlib.pyplot as plt

#QUESTION 1

x = np.linspace(-10, 10, 1000)
#initial value Y(0)=0 implies
Y_analytical_1 = (x**3)/2
Y_power = (x**3)/2
N = 1000
for i in range (4,N+1):
    Y_power += i*0
    error = np.sqrt((Y_analytical_1-Y_power)**2)
plt.plot(x,Y_analytical_1, label = 'Analytical Sol')
plt.plot(x,Y_power, label = 'Power Series Sol')
plt.xlabel('x')
plt.ylabel('y')
plt.title('c = 0')
plt.legend()
plt.show()
#initial value Y(2)=1 implies
Y_analytical_2 = (x**3-3*x)/2
Y_power = (x**3)/2
N = 1000
for i in range (4,N+1):
    Y_power += i*0
    error = np.sqrt((Y_analytical_2-Y_power)**2)
plt.plot(x,Y_analytical_2, label = 'Analytical Sol')
plt.plot(x,Y_power, label = 'Power Series Sol')
plt.xlabel('x')
plt.ylabel('y')
plt.title('c = -3/2')
plt.legend()
plt.show()

#Question 3

T = 2
def b_n(n):
    k = int(n)
    if (k%2 != 0 ):
        return ((-1)**((n+1)/2)*8)/((n**2)*((np.pi)**2))
    else:
        return 0
def w_n(n):
    global T
    wn = (n*np.pi)/T
    return wn
def FourierSeries(x, nMax=10):
    a0 = 0
    sums = a0
    for n in range(1, nMax):
        sums += b_n(n)* np.sin(w_n(n)*x)
    return sums
x_ = np.linspace(-1, 1, 100)
y = np.linspace(1, -1, 100)
fourier_series_approx = []
for i in x_:
    fourier_series_approx.append(FourierSeries(i, 10))
plt.plot(x_, y, label= "Triangle Wave")
plt.plot(x_, fourier_series_approx, label= "Fourier Series")
plt.legend()
def convergenceAnalysis(N):
    plt.clf()
    for n in N:
        fourier_series_approx.clear()
        for i in x_:
            fourier_series_approx.append(FourierSeries(i,n))
        plt.plot(x_, fourier_series_approx, label= "Fourier terms "+ str(n))             
    plt.plot(x_, y, label= "Triangle Wave")
    plt.legend()
convergenceAnalysis([5, 10, 20, 50, 100])
error = 10
N = 1
Sn = []
Fx = np.linspace(1, -1, 100)
while error > 10**-3:
    Sn.clear()
    for i in x_:
        Sn.append(FourierSeries(i, N))
    N = N + 1
    error = max(abs(Fx-Sn))
    #print(error, N)
print('N = ', N, 'Error = ', error)