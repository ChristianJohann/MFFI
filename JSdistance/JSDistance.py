from scipy.spatial import distance

def JSdistance(p, q, base = None):
    if base is not None:
        output = distance.jensenshannon(p, q, base)
    else:
        output = distance.jensenshannon(p,q)
    return output
