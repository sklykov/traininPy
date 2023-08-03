# -*- coding: utf-8 -*-
"""
k - nearest neighbour classificator (as an exercise from the edX course).

@author: sklykov
@license: The Unlicense

"""
import numpy as np
import scipy.stats as scs
import random
import matplotlib.pyplot as plt


# %% Various functions
def max_count_embed(votes):
    """Return the mode (most frequent element in a an array) from a votes - list or array."""
    (mode, counts) = scs.mode(votes)  # Something changed in implementation, it returns scalar now
    # print(mode)
    return mode


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
    most_frequent = []; maxCount = max(counts.values())  # In the case of a tie, there will be a few keys corresponding to the max
    for key, val in counts.items():
        if val == maxCount:
            most_frequent.append(key)
    return random.choice(most_frequent)  # returning randomly single value in the case of multiple ones presented


def distance(point1, point2):
    """Calculate Euclidian distance between two points with coordinates."""
    return np.sqrt(np.sum(np.power(point2-point1, 2)))


def find_nearest_neighbours(point_of_interest, points, k: int = 5):
    """
    Define distances between point of interest and other points.

    Returning k nearest points.
    """
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(point_of_interest, points[i])
    indicies = np.argsort(distances)  # print(indicies); print(distances)
    indicies = indicies[0:k]
    return indicies


def kNN_predict(point_of_interest, points, outcomes, k: int = 5):
    """Calculate simple kNN predictor."""
    indicies = find_nearest_neighbours(point_of_interest, points, k)
    majorVote = max_vote(outcomes[indicies])
    return majorVote


def generateSyntheticData(n: int = 10):
    """Creation of two classes of normally distributed points."""
    # print(scs.norm(0,1).rvs((n,2)))
    points = np.concatenate((scs.norm(0, 1).rvs((n, 2)), scs.norm(1, 1).rvs((n, 2))), axis=0)
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes)


def make_prediction_grid(predictors, outcomes, limits, h, k):
    """Classify each point on the prediction grid."""
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)
    prediction_grid = np.zeros(xx.shape, dtype=int)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            p = np.array([x, y])
            prediction_grid[j, i] = kNN_predict(p, predictors, outcomes, k)
    return (xx, yy, prediction_grid)


def plot_prediction_grid(xx, yy, prediction_grid):
    """Plot kNN predictions for every point on the grid - rewritten from the edX course."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap(["hotpink", "lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap(["red", "blue", "green"])
    plt.figure(figsize=(8, 8))
    plt.pcolormesh(xx, yy, prediction_grid, cmap=background_colormap, alpha=0.6)
    plt.scatter(predictors[:, 0], predictors[:, 1], c=outcomes, cmap=observation_colormap, s=50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim(np.min(xx), np.max(xx))
    plt.ylim(np.min(yy), np.max(yy))


# %% Testing
votesL = np.array([1, 2, 1, 2, 3, 3, 3, 2])
modeL = max_count_embed(votesL)
modeL2 = max_vote(votesL)
p1 = np.array([0, 0]); p2 = np.array([3, 4]); print(distance(p1, p2))
points = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]])
indicies = find_nearest_neighbours([2, 2.5], points, 2)
print(points[indicies])
outcomes = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
print(kNN_predict([1.0, 2.7], points, outcomes, 2))
arr1 = np.array([[1, 1], [1, 2]])
res1 = arr1.shape

# %% Testing on synthetic data
n = 20
(points2, outcomes2) = generateSyntheticData(n)
plt.figure()
plt.plot(points2[0:n, 0], points2[0:n, 1], 'ro')
plt.plot(points2[n:2*n, 0], points2[n:2*n, 1], 'bo')

# %% Testing predictions
(predictors, outcomes) = generateSyntheticData(50)
k = 20; limits = (-3, 4, -3, 4); h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid)
