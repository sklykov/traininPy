# -*- coding: utf-8 -*-
"""
k - nearest neighbour classificator
@author: ssklykov
"""
import numpy as np
import scipy.stats as scs
import random
# %% Various functions
def max_count_embed(votes):
    """Returning the mode (most frequent element in a an array) from a votes - list or array."""
    (mode,counts) = scs.mode(votes)
    # print(counts)
    return mode[0]

def max_vote(votes):
    """Manual bilding of counts and selection randomly the max vote (count) in the case of a tie"""
    counts = {}
    for vote in votes:
        if vote in counts.keys():
            counts[vote] += 1
        else:
            counts[vote] = 1
    # print(counts)
    # Building the list of max values
    most_frequent = []; maxCount = max(counts.values()) # In the case of a tie, there will be a few keys corresponding to the max
    for key,val in counts.items():
        if val == maxCount:
            most_frequent.append(key)
    return random.choice(most_frequent) # returning randomly single value in the case of multiple ones presented

def distance(point1,point2):
    """Simple calculation of Euclidian distance between two points with coordinates"""
    return np.sqrt(np.sum(np.power(point2-point1,2)))

# %% Testing
votesL = np.array([1,2,1,2,3,3,3,2])
modeL = max_count_embed(votesL)
modeL2 = max_vote(votesL)
p1 = np.array([0,0]); p2 = np.array([3,4]); print(distance(p1,p2))