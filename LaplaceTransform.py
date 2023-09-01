import sympy as sym
from sympy.abc import t,s
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform
'''
def L(f):
    return  laplace_transform(f, t, s, noconds=True)

def invL(F):
    return inverse_laplace_transform(F, s, t)

#1.1.
print("1.1.\n")
f = t*sym.exp(-2*t) + t*sym.sin(t)
Fs = L(f)
print(Fs)

#1.2.
print("\n1.2.\n")
f = 10 + 5*t + t**2 -4*t**3
Fs = L(f)
print(Fs)

#2.1.
print("\n2.1.\n")
f = (3*s+9)/((s**2)-(8*s)+7)
f = f.apart(s)
print(f)
x = invL(f)
print(x)

#2.2.
print("\n2.2.\n")
f = (s**2)/((s**2)+4*s+5)
f = f.apart(s)
print(f)
x = invL(f)
print(x)

#2.3.
print("\n2.3.\n")
f = sym.exp(-4*s) + 1 + 1/s
x = invL(f)
print(x)
'''
'''
The answers for Qs 1 and 2 match using the python implemenmtation, except the inclusion of a
heavyside function (for values of t => 0) in 2.1. and 2.2. to cater to in built domain of 
-inf to inf in the sympy library in python.
'''

#4.2.
f = 4*sym.exp(-t)
iLF = 4*sym.exp(-t) + 4 -4*sym.exp(1-t)     # convulation integral from 4a(a and b)
p = sym.plot(f.subs({-1: 2}), iLF.subs({-1: 2}),
               xlim=(-2, 2), ylim=(0, 100), show=False)
p[1].line_color = 'red'
p.show()

iLF2= 4 -4*sym.exp(-1-t)     # convulation integral from 4a(c and d)
p = sym.plot(f.subs({-1: 2}), iLF2.subs({-1: 2}),
               xlim=(-2, 2), ylim=(0, 100), show=False)
p[1].line_color = 'red'
p.show()
