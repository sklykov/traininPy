"""
Regression Demo using built-in libraries.

@author: sklykov
@license: The Unlicense

"""

# %% Import section (standard way)
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# %% Generation of sample data for regression (again - in other repo I've developed another example)
N = 100
a = 2.0; b = 5.0  # For linear dependence generation y = a*x + b
np.random.seed(1)  # For making consistency with the course
x = 10*stats.uniform.rvs(size=N)  # generation of random values from range [0,10]
y = a*x + b + stats.norm.rvs(loc=0, scale=1, size=N)  # Generation of values with additive noise
xMean = np.mean(x); yMean = np.mean(y)
ySample = a*x + b
plt.figure(); plt.plot(x, y, "bo"); plt.plot(x, ySample, "ro")
# xSteps = np.arange(0, 10, 10/N)


# %%  Residual sum of squares calculation (sum of squares difference between two arrays)
def rssCalc(yEstimated, ySample) -> float:
    """Residual sum of squares calculation."""
    return sum(np.power(yEstimated - ySample, 2))


# %% Running tests
rssDif = rssCalc(y, ySample)  # Estimation of difference between noised and without any noise values
