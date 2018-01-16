# enumerate produces tuples
for i, document in enumerate(documents):
	do_something(i, document)

# if we want just the indexes
for i, _ in enumerate(documents): do_something(i)

