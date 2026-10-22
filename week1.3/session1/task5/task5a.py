# Week 1.3, Session 1: Task 5a

course = "computer science"

for ch in course:
	print(ch)


# create a list data structure of the characters from the course string
def charreturn():
	for ch in course:
	 characters = [(ch) for ch in course]
	 return characters
	
characters = charreturn()
print (characters)

# sort the list into alphabetical order

characters.sort()
print (characters)