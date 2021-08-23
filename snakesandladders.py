'''Snakes and ladder game
- it has a board that starts at 1, ends at 100
- player rolls a dice and moves forward the number of places they get on the dice
- there are snakes and ladders on the board
- snakes swallow the player taking them back (from the head to the tail)
- ladders allow the users to climb to a higher place (from bottom to top)
- player must get 4 or 6 to start the game
- player must land on 100 exactly to end the game
- this version is one player game
- this is text based game, no graphic display
'''

import random

#player starts at 0 pos is the variable to denote the player's current position

pos = 0

#This is a set of key:value pairs of all the snakes and ladders on the board.
#if the player's pos is in the snl set, send them to the value of that key.
#1,4,8,21,50,71,80 are ladders, they help the player to climb to a higher place.
#32,36,48,62,88,95,97 are snakes, if stepped upon they swallow the player to a lower place.

snl = {1:34, 4:14, 8:30, 21:42, 32:10, 36:6, 48:26, 50:67, 62:18, 71:92, 80:99, 88:24, 95:26, 97:78}

#use an infinite while loop to repeat the program forever 
while True:
	#get input from the user
	c = input('Press R to roll dice, Q to quit.\n>')
	
	#if input is r or R, let's roll
	if c.lower() == 'r':
		#A dice has 6 sides, let's generate a random number between 1 and 6
		r = random.randint(1,6)
		pos = pos + r
		#now print the generated random number
		print('You rolled: ', r)
		print('Now you are on', pos)

		#Let's check if the player has landed on a snake or a ladder.
		#If they land in the snake's mouth, they go to the tail of the snake: get swallowed
		#IF they land and the foot of a ladder, they climb to the top
		if pos in snl:
			#if key is lower than the value, it is a ladder
			if pos < snl[pos]:
				print("Wow, you got a ladder.\nClimb it to ", snl[pos])
			#if key is higher than the value, it's a snake	
			else:
				print("Oops, you stepped on a snake.")
				print("You got swallowed. Go to ", snl[pos])
			pos = snl[pos]

		#if the pos is 100, player has reached home, tell them and end the game.
		if pos == 100:
			print("Congratulations, you reached home.\nWinner, winner, chicken dinner!")
			quit()

		#if the player lands on a number higher than 100, they can't move, they stay in the same place.
		elif pos > 100:
			print("You really can't move to ", pos)
			print("Go back to ", pos-r)
			print("Wait for the next turn to 100 exactly.")
			pos = pos - r


	#if input is q or Q, quit the game.
	elif c.lower() == 'q':
		print('You quit the game!\nLoser!')
		quit();

	#else keep repeating loop