""" 
    Find the k nearest neighbors of points and return the indexes of nearest neigbor k
    usage: 
        //Generate points.
        points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
        p = np.array(2.5, 2)
        
        //Get the index of nearest points
        ind = find_nearest_neighbors(p, points, 2); 
    
        //Print result.
        print(points[ind]);
        
        OUTPUT:  
            [[2 2]
            [3 2]]
"""

import numpy as np

def find_nearest_neighbors(p, points, k=5):    
    distances = np.zeros(points.shape[0])
    #loop through
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
        
    index = np.argsort(distances)
    return index[:k]
