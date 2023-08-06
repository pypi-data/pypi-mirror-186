#### Normal Distribution ####
import math
import pytest
class Normal:
    param = 0
    def __init__(self):
        self.param = 0
        
    def is_stdnoraml(self,mu,sd):
        if(mu == 0 and sd == 1):
            return(True)
        else:
            return(False)       
        
    def pdf(self,x,mu=0,sd=1):
        pi = math.pi
        p = (1/(sd*math.sqrt(2*pi)))*math.exp(-1/2*((x-mu)/sd)**2)
        return(p)
    
    def sf(self,x,mu=0,sd=1):
        return(1-self.cdf(x,mu,sd))
        
    def cdf(self,x,mu=0,sd=1):
        if(not self.is_stdnoraml(mu,sd)):
            x = (x-mu)/sd
        #'Cumulative distribution function for the standard normal distribution'
        return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

    def stats(self,mu=0,sd=1):
        mean = mu
        med = mu
        mode = mu
        var = sd**2
        skew = 0
        kurt = 0
        res = {"mean":mean,"median":med,"mode":mode,"variance":var,"skewnes":skew,"kurtosis":kurt}
        return(res)

def test_func():
    n = Normal()
    assert n.pdf,n.cdf,n.sf,n.stats
