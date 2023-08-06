#### Multinomial Distribution ####
import math
import pytest
class Multinomial:
    param = 0
    def __init__(self):
        param = 0
    
    def pdf(self,n,outcomes,prob):
        F = math.factorial(n)
        E =math.prod([p**o for o,p in zip(outcomes,prob)] )
        O =math.prod([math.factorial(x) for x in outcomes])
        p = F*E/O
        return(p)

    def cov(self,n,prob):
        cv=[]
        for i in range(len(prob)):
            row =[]
            for j in range(len(prob)):
                if(i==j):
                    v = n*(prob[j]-prob[j]**2)
                else:
                    v = -n*prob[i]*prob[j]
                row.append(v)
            cv.append(row)
        return(cv)

    def stats(self,n,outcomes,prob):
        mean =sum([p*o for o,p in zip(outcomes,prob)])
        var = sum([p*(o-mean)**2 for o,p in zip(outcomes,prob)])
        sd = math.sqrt(var)
        res ={"mean":mean,"variance":var}
        return(res)

def test_func():
    mn = Multinomial()
    assert mn.pdf,mn.cov,mn.stats
