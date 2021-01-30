import numpy as np

def kl_divergence(p, q, base=None):
    """
    calculates the Kullback-Leibler divergence between two distributions
    
    Input:
    p: a numpy array specifying the reference pdf or pmf
    q: a numpy array specifying an alternative pdf or pmf
    base: optional argument specifying the base of the logarithm
    """"
    output = np.sum(np.where(p != 0, p * np.log(p / q), 0)) # excludes infinite values from calculation
    if base is not None:
        output /= np.log(base)
    return output
