'''
Rock/Paper/Scrissors game
The computer plays the game with the user
User gets to select an option of Rock/Paper/Scissors
Computer(program) selects a random option
The program compares the selections and declares the winner
rock breaks the Scissors, Scissors cut the paper, paper wraps the rock
'''

import random

print("Let's play a game of Rock/Paper/Scissors.")
print("Rock crushes scissors")
print("Scissors cut paper")
print("Paper wraps rock")
print("You choose your option, computer will select on randomly.")
print("First one to win three games is the winner")
print("=========================================================")

#A list to store the three options
choices = ['Rock','Paper','Scissors']

cs = 0
us = 0
#ask user to select their choice

while True:

	user = input("What are you?\nRock[1] Paper[2] Scissors[3]")
	if user not in ['1','2','3']:
		print("Couldn't understand your choice.")
		continue

	print("You chose ", choices[int(user)-1])

	comp = random.randint(1,3)

	print("Computer chose to be ", choices[comp-1])

	#if user and computer select same option, it's a tie
	if comp == int(user):
		print("Both of us chose to be ", choices[comp-1])
		print("It's a tie!")
	#some simple math here to see if comp is 1 step ahead of user in the cyclic list
	elif comp - (int(user)%3) == 1:
		print("Computer wins this round.")
		cs = cs+1
	else:
		print("You win this time.")
		us = us+1

	print("The score is User-",us," Comp-",cs)

	if cs > 2 or us > 2:
		if cs>us:
			print("point, game, set: Computer!")
		else:
			print("point, game, set: You!")
		break