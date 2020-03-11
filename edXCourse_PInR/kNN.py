# -*- coding: utf-8 -*-
"""
k - nearest neighbour classificator
@author: ssklykov
"""
import numpy as np
import scipy.stats as scs
import random
import matplotlib.pyplot as plt
# %% Various functions
def max_count_embed(votes):
    """Returning the mode (most frequent element in a an array) from a votes - list or array."""
    (mode,counts) = scs.mode(votes)
    # print(counts)
    return mode[0]

def max_vote(votes):
    """Manual bilding of counts and selection randomly the max vote (count) in the case of a tie."""
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
    """Simple calculation of Euclidian distance between two points with coordinates."""
    return np.sqrt(np.sum(np.power(point2-point1,2)))

def find_nearest_neighbours(point_of_interest,points,k:int=5):
    """Defining distances between point of interest and other points. Returning k nearest points."""
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(point_of_interest,points[i])
    indicies = np.argsort(distances); # print(indicies); print(distances)
    indicies = indicies[0:k]
    return indicies

def kNN_predict(point_of_interest,points,outcomes,k:int=5):
    """Simple kNN predictor."""
    indicies = find_nearest_neighbours(point_of_interest,points,k)
    majorVote = max_vote(outcomes[indicies])
    return majorVote

def generateSyntheticData(n:int=10):
    """Creation of two classes of normally distributed points."""
    # print(scs.norm(0,1).rvs((n,2)))
    points = np.concatenate((scs.norm(0,1).rvs((n,2)), scs.norm(1,1).rvs((n,2))),axis=0)
    outcomes = np.concatenate((np.repeat(0,n),np.repeat(1,n)))
    return (points,outcomes)

# %% Testing
votesL = np.array([1,2,1,2,3,3,3,2])
modeL = max_count_embed(votesL)
modeL2 = max_vote(votesL)
p1 = np.array([0,0]); p2 = np.array([3,4]); print(distance(p1,p2))
points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
indicies = find_nearest_neighbours([2,2.5],points,2)
print(points[indicies])
outcomes = np.array([0,0,0,0,1,1,1,1,1])
print(kNN_predict([1.0,2.7],points,outcomes,2))
arr1 = np.array([[1,1],[1,2]])
res1 = arr1.shape

# %% Testing on synthetic data
n = 20
(points2,outcomes2) = generateSyntheticData(n)
plt.figure()
plt.plot(points2[0:n,0],points2[0:n,1],'ro')
plt.plot(points2[n:2*n,0],points2[n:2*n,1],'bo')