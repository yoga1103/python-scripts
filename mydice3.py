#My dice program
#first import module random

import random

#use an infinite while loop to repeat the program forever 

while True:
	#get input from the user
	c = input('Press R to roll dice, Q to quit.\n>')

	#if input is r or R, let's roll
	if c.lower() == 'r':
		#A dice has 6 sides, let's generate a random number between 1 and 6
		r = random.randint(1,6)

		#now print the generated random number
		print('You rolled: ', r)

	#if input is q or Q, quit the game.
	elif c.lower() == 'q':
		print('Game Over!')
		quit();

	#else keep repeating loop