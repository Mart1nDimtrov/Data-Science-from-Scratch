def lazy_range(n):
	"""a lazy range of range"""
	i = 0
	while i < n:
		yield i
		i += 1

for i in lazy_range(10):
	print(i)

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
print(type(lazy_evens_below_20)) # get the type of the variable
print(list(lazy_evens_below_20))
