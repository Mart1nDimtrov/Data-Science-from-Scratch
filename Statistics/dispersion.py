from central_tendencies import quantile
import os
import sys
import math
sys.path.append('C:\\Users\\martin\\Desktop\\DataScienceFromScratch\\LinearAlgebra')
from vectors import sum_of_squares


def data_range(x):
	return max(x) - min(x)

def mean(x):
	return sum(x) / len(x)

def de_mean(x):
	'''translate x by substracting its mean (so the result has mean 0)'''
	x_bar = mean(x)
	return [x_i - x_bar for x_i in x]

def variance(x):
	'''assumes x has at least two elements'''
	n = len(x)
	deviations = de_mean(x)
	return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
	return math.sqrt(variance(x))

def interquartile_range(x):
	return quantile(x, 0.75) - quantile(x, 0.25)
	

if __name__ == '__main__':
	num_friends = [100, 49, 41, 40, 25, 17, 548, 200, 350, 114, 76]
	print('Range: ' + str(data_range(num_friends)))
	print('Variance: ' + str(variance(num_friends)))
	print('Standard deviation: ' + str(standard_deviation(num_friends)))
	print("Interquartile range: " + str(interquartile_range(num_friends)))
