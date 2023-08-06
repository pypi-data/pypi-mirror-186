import numpy as np
import numpy.linalg as la
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

"""Sigmoid transfer function"""
def sigmoid(A, l=1, h=0):
    return 1.0 / (1.0 + np.exp(-l*(A-h)))

"""Hyperbolic transfer function"""
def hyperbolic(A):
    return np.tanh(A)

"""Rescaled transfer function"""
def rescaled(A):
    if la.norm(A)==0.0:
        return np.zeros(A.shape)
    else:
        return A / la.norm(A)

"""Recurrent reasoning process"""
def reasoning(W, A, names, T=50, phi=0.8, plot=True, indexes=[0,12], case="age", function=rescaled):
    
    states = np.zeros([len(A), T, len(W)])
    states[:,0,:] = A
    
    for t in range(1,T):
        A = states[:,t,:] = (phi * function(np.matmul(A, W)) + (1-phi) * states[:,0,:])

    if plot:
        
        plt.figure(figsize=(6,4))
        
        for idx in indexes:
            for i in range(len(states)):
                val = plt.plot(states[i,:,idx], label=names[idx], marker='o')

                plt.xlabel(r'$t$', fontsize=14)
                plt.ylabel(r'$a_i^{(t)}$', fontsize=14)
                plt.ylim(0, 0.35)
        
        ax = plt.gca()
        ax.xaxis.get_major_locator().set_params(integer=True)
        plt.legend(loc='best')
        plt.margins(x=0)
        plt.show()        
    
        return A
    else:
        return states

import sys
if __name__ == "__main__":
    double_args = reasoning(sys.argv)
    print("In mymodule:",double_args)
    