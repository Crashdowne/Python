
print  "*************************************************************************"
print  "*                                                                       *"
print  "*                         CSC 106 Assignment 3                          *"
print  "*                                                                       *"
print  "*                 Welcome to the Number Guessing Game!                  *"
print  "*                                                                       *"
print  "*          Presented by: Marina Retseptor and Bryan Kesteloo            *"
print  "*                                                                       *"
print  "*************************************************************************"


#Imports library required to generate randome numbers
from random import randint

#Sets up a boolean to determine if the program needs to terminate or not
quit = False

#Creates the variable for the random number
randint(1,100)

#Generates the random number
random_number = randint(1,100)

print "\nRANDOM NUMBER FOR TESTING PURPOSES: "
print random_number

#Loop containing the game runs until the program produces "True" and terminates on "True"
while quit == False:

	#Prompts the user to input a number and puts the input into a variable
	user_guess_input = raw_input(">>> Enter your guess between 1 and 100! -->  ")
	
	#Detects if the user wants to quit early or not
	if user_guess_input == "q":
		print "\n>>> We're sorry to see you go"
		quit = True
	
	#Checks to see if the input is a whole integer, it also excludes negative numbers
	elif user_guess_input.isdigit() == False:
	
		#Prints an error if anything other than a whole integer is entered
		print "\n>>> Invalid input, please input a number whole number between 1 and 100\n" 
	
	else:
	
		#Converts the string input into a number. Float allows the program to distinguish +/- numbers
		user_guess = float(user_guess_input)
	
		#Checks to see if the number is > 100 and generates an error
		if user_guess > 100:
			print "\n>>> Invalid input, please enter a whole number between 1 and 100\n"

		#Checks to see if the user's guess is correct
		elif user_guess == random_number:
			print "\n>>> You are correct!!!"
			print ">>> Your guess was: " + user_guess_input + "\n"
			print ">>> We hope you had fun!"
			quit = True
				
		#Checks to see if the guess is greater than the random number		
		elif user_guess > random_number:
			
			print "\n>>> Your guess was too high"
			print ">>> You guessed -->  " + user_guess_input + "\n"
			print ">>> You can press 'q' at any time to quit <<\n"
				
		#Checks to see if the guess is smaller than the random number		
		else:
			
			print "\n>>> Your guess was too low"
			print ">>> You guessed -->  " + user_guess_input + "\n"
			print ">>> You can press 'q' at any time to quit <<\n"