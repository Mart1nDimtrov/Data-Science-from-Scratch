import random

four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)
# random.random() produces numbers uniformly between 0 and 1
# it's the random function we'll use most often

random.seed(10) # set the seed to 10
print(random.random())
random.seed(10) # reset the seed to 10
print(random.random())

random.randrange(10) # choose randomly from range(10) = [0, 1, ..., 9]
random.randrange(3, 6) # choose randomly from range(3, 6) = [3, 4, 5]

up_to_ten = [x for x in range(10)]
random.shuffle(up_to_ten)
print(up_to_ten)

my_best_friend = random.choice(["Alice", "Bob", "Charlie"]) # pick one element at random
print(my_best_friend)

lottery_numbers = [x for x in range(60)]
winning_numbers = random.sample(lottery_numbers, 6) # a sample with no duplicates
print(winning_numbers)

four_with_replacement = [random.choice(range(10))
						 for _ in range(4)]
print(four_with_replacement)