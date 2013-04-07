dictionary = {(0, 1) : 'hello', (1, 2) : 'goodbye', (2, 2) : 'hola' , (3, 4) : 'adios', (4, 4) : 'sayonara' }

rows = [ 0, 1, 2, 3, 4 ]

columns = [ 0, 1, 2, 3, 4]


#make tuples (in this case, coordinates of a square grid)
for x in range(len(rows)):
	for y in range(len(columns)):
		coordinates = (x, y)
		# (0, 0)
		# (0, 1)
		# (0, 2)
		# (0, 3)
		# (0, 4)
		# (1, 0)

		# check if a value (in this case, a tuple) exists in the dictionary
		if coordinates in dictionary.keys():
			# print the corresponding value of a dictionary key
			print coordinates, dictionary.get(coordinates) 
		else:
			print "null"

# null
# (0, 1) hello
# null
# null
# null
# null
# null
# (1, 2) goodbye
# null
# null
# null
# null
# (2, 2) hola
# null
# null
# null
# null
# null
# null
# (3, 4) adios
# null
# null
# null
# null
# (4, 4) sayonara




#previous attempt - this does not work
# for x in range(len(rows)):
# 	for y in range(len(columns)):
# 		if (x, y) in (rows, columns) == dictonary.items():
# 			print (x, y)	