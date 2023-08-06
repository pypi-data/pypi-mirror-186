#### Exponential Distribution ####
import math
import pytest
class Exponential:
    param = 0
    def __init__(self):
        self.param = 0
    
    def pdf(self,x,mu):
        if(x<0):
            return(0)
        rate = 1/mu
        p = rate*math.exp(-rate*x)
        return(p)
    
    def sf(self,x,mu):
        return(1-self.cdf(x,mu))
    
    def cdf(self,x,mu):
        rate = 1/mu
        p = 1-math.exp(-rate*x)
        return(p)
    
    def stats(self,x,mu):
        rate = 1/mu
        mean = 1/rate
        med = math.log(2)/rate
        mode = 0
        var = 1/rate**2
        skew = 2
        kurt = 6
        res={"mean":mean,"median":med,"mode":mode,"variance":var,"skewness":skew,
            "kurtosis":kurt}
        return(res)

def test_func():
    ex = Exponential()
    assert ex.pdf,ex.cdf,ex.sf,ex.stats
