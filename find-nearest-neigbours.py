import numpy as np

def find_nearest_neighbors(p, pofints, k=5):
    """ Find the k nearest neighbors of points"""
    
    distances = np.zeros(point s.shape[0])
    #loop through
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
        
    index = np.argsort(distances)
    return index[:k]
