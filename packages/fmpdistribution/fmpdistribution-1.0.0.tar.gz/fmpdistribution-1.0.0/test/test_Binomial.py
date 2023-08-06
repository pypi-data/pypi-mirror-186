#### Binomial Distribution ####
import math
import pytest
class Binomial:
    param = 0
    def __init__(self):
        self.param = 0
    
    def pdf(self,x,n,p):
        q=1-p
        e1 = n-x
        p = math.comb(n,x)*(p**x)*(q**e1)
        return(p)
    
    def cdf(self,x,n,p,steps=False):
        tp = 0
        terms = {}
        q=1-p
        tt = x+1
        for x in range(tt):
            e1=n-x
            tp=tp+(p**x)*math.comb(n,x)*(q**e1)
            if(steps):
                terms[x]=(p**x)*math.comb(n,x)*(q**e1)
            
        if(steps):
            terms["Prob"]=tp
            return(terms)
        else:
            return(tp)

    
    def sf(self,x,n,p):
        return(1-self.cdf(x,n,p))
    
    def stats(self,n,p):
        q=1-p
        mean = n*p
        med = math.floor(mean)
        mode = math.floor((n+1)*p)
        var = n*p*q
        skew = (q-p)/math.sqrt(n*p*q)
        kurt = (1-6*p*q)/(n*p*q)
        res = {"mean":mean,"median":med,"mode":mode,"variance":var,"skewnes":skew,"kurtosis":kurt}
        return(res)
def test_func():
    bn = Binomial()
    assert bn.pdf,bn.cdf,bn.sf,bn.stats
