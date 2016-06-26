## Tutorial3 Question1a:
##

import numpy as np
from matplotlib import pyplot as plt
def convl(f,arb):
    ft = np.fft.fft(f)
    return np.real(np.fft.ifft(ft*arb))

x = np.linspace(-2*np.pi,2*np.pi,200)
f= np.sin(x)
N = len(x)
k = np.arange(N)
J = np.complex(0,1)
dx = 25.0 
arb = np.exp(-2*np.pi*J*k*dx/N)
h = convl(f,arb)

plt.plot(x,f,'b')
plt.plot(x,h,'r')
plt.grid(True)
plt.title('Sin function shift by pi/2')
plt.show()
