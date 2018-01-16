from collections import Counter

def mean(x):
	return sum(x) / len(x)

def median(v):
	'''finds the middle-most value of v'''
	n = len(v)
	sorted_v = sorted(v)
	midpoint = n // 2

	if n % 2 == 1:
		# if odd, return the middle value
		return sorted_v[midpoint]
	else:
		# if even, return the average of the middle values
		lo = midpoint - 1
		hi = midpoint
		return (sorted_v[lo] + sorted_v[hi] / 2)

def quantile(x, p):
	'''returns the pth-percentile value in x'''
	p_index = int(p * len(x))
	return sorted(x)[p_index]

def mode(x):
	'''returns a list, might be more than one node'''
	counts = Counter(x)
	max_count = max(counts.values())
	for key, value in counts.items():
		if value == max_count:
			return key
	

if __name__ == '__main__':
	num_friends = [100, 49, 41, 41, 40, 25, 17, 548, 200, 350, 114, 76]
	print('Mean ' + str(mean(num_friends)))
	print('Median ' + str(median(num_friends)))
	print('Quantile of 90%: ' + str(quantile(num_friends, 0.90)))
	print('Mode: ' + str(mode(num_friends)))