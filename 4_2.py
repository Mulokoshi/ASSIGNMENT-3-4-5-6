import numpy

class NBody:
    def __init__(self, mass, numpar, G=1.0):
        
        self.data = {}
        self.data['mass'] = mass
        self.data['numpar'] = numpar
        self.data['G'] = G
        
        self.m = numpy.ones(self.data['numpar'])*mass
        self.xpos = numpy.random.randn(self.data['numpar']) 
        self.ypos = numpy.random.randn(self.data['numpar'])
                    
    def p_energy(self):
        PE = 0
        for i in range(self.data['numpar']):
            PE += self.dada['G']*self.m[i]*self.m[i+1]/(numpy.sqrt(self.xpos[i]**2 + self.ypos[i]**2))
        return PE

if __name__=='__main__':
    sys = NBody(10.0,50,1.0)
    print 'the system has: ', repr(sys.data)
    print 'm as array is: ', repr(sys.m) 
    print 'the x positions are: ', repr(sys.xpos)
    print 'the y positions are: ', repr(sys.ypos)
    print 'the method is: ', repr(sys.p_energy)
                        
                             
                             

                                                                  
        
