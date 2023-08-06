import math
import pytest
#### Poisson Distribution ####
class Poisson:
    param = 0
    def __init__(self):
        self.param = 0
    
    def pdf(self,x,mu):
        p = (math.exp(-mu) * (mu)**x)/math.factorial(x)
        return(p)
    
    def cdf(self,x,mu,steps=False):
        tp = 0
        terms ={}
        for x in range(x+1):
            p = (math.exp(-mu) * (mu)**x)/math.factorial(x) 
            if(steps):
                terms[x]=p
            tp = tp + p
        if(steps):
            terms["Prob"]=tp
            return(terms)
        else:
            return(tp)
    
    def sf(self,x,mu):
        return(1-self.cdf(x,mu))
    
    def stats(self,mu):
        mean = mu
        med = mu + 1/3-(1/(50*mu))
        mode = math.floor(mu)
        var = mu
        skew = 1/math.sqrt(mu)
        kurt = 1/mu
        res = {"mean":mean,"median":med,"mode":mode,"variance":var,"skewnes":skew,"kurtosis":kurt}
        return(res)

def test_func():
    p = Poisson()
    assert p.pdf,p.cdf,p.sf,p.stats
