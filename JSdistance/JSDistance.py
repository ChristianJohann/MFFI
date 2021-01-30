from scipy.spatial import distance

def JSdistance(p, q, base = None):
    """
    calculates the Jenson-Shannon distance between two distributions
    
    Input:
    p: a list of floats or numpy array specifying a pdf or pmf
    q: a list of floats or numpy array specifying a pdf or pmf
    base: optional argument specifying the base of the logarithm
    """"
    if base is not None:
        output = distance.jensenshannon(p, q, base)
    else:
        output = distance.jensenshannon(p,q)
    return output
