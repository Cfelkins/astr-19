import sys
import numpy as np
from scypi.special import erf

def event_probability(x,mu=0.0,s=1.0):
    #x is value of event 
    #mu is gaussian mean
    #s is gaussian standard deviation
    z=np.fabs((x-mu/s))
    def zfunc(z):
        return 0.5*(1.0+erf(z/2**0.5))
        #return probability of getting event of magnitude >=x
    return 1.0-(zfunc(z)-zfunc(-1*z))

def main():
    x = 3.0
    
    #if another number is given on command line, reset x
    if(len(sys.argv)>1):
        x = float(sys.argv[1])
    prob = event_probability(x)
    print(f"The Gaussian probability of event larger than |{x}| is {prob*100:6.4f}%.")
    print(f"The Gaussian probability of event smaller than |{x}| is {(1-prob)*100:6.4f}%.") #6 intergers, 4 after decimal
if __name__=="__main__":
    main()