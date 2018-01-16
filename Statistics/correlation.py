import os
import sys
sys.path.append('C:\\Users\\martin\\Desktop\\DataScienceFromScratch\\LinearAlgebra')
from vectors import sum_of_squares, dot
from dispersion import standard_deviation, de_mean

def covariance(x, y):
	n = len(x)
	return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
	stdev_x = standard_deviation(x)
	stdev_y = standard_deviation(y)
	if stdev_x > 0 and stdev_y > 0:
		return covariance(x, y) / stdev_x / stdev_y
	else:
		return 0


daily_minutes = sorted([100, 49, 41, 40, 25, 17, 548, 200, 350, 114, 76])
num_friends = [100, 49, 41, 40, 25, 17, 548, 200, 350, 114, 76]
print("The correlations is: " + str(correlation(num_friends, daily_minutes)))
print("The covariance is: " + str(covariance(num_friends, daily_minutes)))