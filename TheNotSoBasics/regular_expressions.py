import re

print(all([
	not re.match("a", "cat"),                # all of these are true, because
	re.search("a", "cat"),                   # * 'cat' doesn't start with 'a'
	not re.search("c", "dog"),               # * 'dog' doesn't have a 'c' in it
	3 == len(re.split("[ab]", "carbs")),     # * split on a or b to ['c', 'r', 's']
	"R-D-" == re.sub("[0-9]", "-", "R2D2")   # * replace digits with dashes
	])) # prints True