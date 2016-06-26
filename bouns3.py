import numpy
def FFT3(x):
    N=x.shape[0]
    if N==1:
        return x
    N3 = N/3
    fact1 = numpy.exp(-2j*numpy.pi*numpy.arange(0,N3)/N)
    fact2 = numpy.exp(-4j*numpy.pi*numpy.arange(0,N3)/N)
    
    f1 = numpy.exp(-2j*numpy.pi/3)
    f2 = numpy.exp(-4j*numpy.pi/3)
    
    aft = FFT3(x[0::3])
    bft = FFT3(x[1::3])*fact1
    cft = FFT3(x[2::3])*fact2

    ft1 = aft+bft+cft
    ft2 = aft+bft*f1+cft*f2
    ft3 = aft+bft*f2+cft*f1
    return numpy.concatenate((ft1,ft2,ft3))


x = numpy.random.randn(243)
print len(x)
print numpy.allclose(FFT3(x),numpy.fft.fft(x))

