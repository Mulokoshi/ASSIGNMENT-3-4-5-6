##    Tutorial3 Question4
#
from numpy import linspace,arange,real,sin,cos,exp,conj,insert,pi
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt
x = linspace(0,2*pi,200)
f = cos(x)
g = exp(-x)
for i in range(2):
    f = insert(f,len(f),0)
    g = insert(g,len(g),0) 

ftf = fft(f)
cjg = conj(fft(g)) 
convl = ifft(ftf*cjg)
plt.plot(real(convl))
plt.grid(True)
plt.show()

