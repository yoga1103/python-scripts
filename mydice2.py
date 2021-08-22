#My dice program
#repeats n number of times using a for loop
#first import module random

import random

#use a for loop to repeat the operation n number of times

for i in range(6):
	#A dice has 6 sides, let's generate a random number between 1 and 6
	r = random.randint(1,6)

	#now print the generated random number
	print("You rolled: ", r)
