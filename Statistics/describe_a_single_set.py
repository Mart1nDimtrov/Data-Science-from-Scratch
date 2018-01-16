from collections import Counter
import matplotlib.pyplot as plt

num_friends = [100, 49, 41, 40, 25, 17, 548, 200, 350, 114, 76]
friends_counts = Counter(num_friends)
xs = range(101)							# largest value is 100
ys = [friends_counts[x] for x in xs]	# height is just # of friends	
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]			
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]