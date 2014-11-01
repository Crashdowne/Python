
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

#Initializes a counter
count = 0 

#Generates the random number
random_number = randint(1,100)

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
		if user_guess > 100 or user_guess == 0:
			print "\n>>> Invalid input, please enter a whole number between 1 and 100\n"
			
		#Checks to see if the user's guess is correct
		elif user_guess == random_number:
			print "\n>>> You are correct!!!"
			print ">>> Your guess was: " + user_guess_input + "\n"
			print ">>> We hope you had fun!"
			quit = True
				
		#Checks to see if the guess is greater than the random number, prints 	
		elif user_guess > random_number:
			
			#The following code gives the user hints on how close they are to the number
			if user_guess - random_number <= 10:
				print "\n>>> Almost there!!"
				print ">>> Your guess was too high"
				print ">>> You guessed -->  " + user_guess_input + "\n"
				print ">>> You can press 'q' at any time to quit <<\n"
				
			elif user_guess - random_number > 10 and user_guess - random_number <= 15:
				print "\n>>> Close!"
				print ">>> Your guess was too high"
				print ">>> You guessed -->  " + user_guess_input + "\n"
				print ">>> You can press 'q' at any time to quit <<\n"
			
			elif user_guess - random_number > 15 and user_guess - random_number <= 20:
				print "\n>>> Getting there!"
				print ">>> Your guess was too high"
				print ">>> You guessed -->  " + user_guess_input + "\n"
				print ">>> You can press 'q' at any time to quit <<\n"
				
			else:
				print "\n>>> Your guess was too high"
				print ">>> You guessed -->  " + user_guess_input + "\n"
				print ">>> You can press 'q' at any time to quit <<\n"
				
		#Checks to see if the guess is smaller than the random number		
		else:
			
			#The following code gives the user hints on how close they are to the number
			if random_number - user_guess <= 10:
				print "\n>>> Almost there!"
				print ">>> Your guess was too low"
				print ">>> You guessed -->  " + user_guess_input + "\n"
				print ">>> You can press 'q' at any time to quit <<\n"
		
			elif random_number - user_guess > 10 and random_number - user_guess <= 15:
				print "\n>>> Close!"
				print ">> Your guess was too low"
				print ">>> You guessed -->  " + user_guess_input + "\n"
				print ">>> You can press 'q' at any time to quit <<\n"
		
			elif random_number - user_guess > 15 and random_number - user_guess <= 20:
			
				print "\n>>> Getting there!"
				print ">>> Your guess was too low"
				print ">>> You guessed -->  " + user_guess_input + "\n"
				print ">>> You can press 'q' at any time to quit <<\n"
				
			else:
			
				print "\n>>> Your guess was too low"
				print ">>> You guessed -->  " + user_guess_input + "\n"
				print ">>> You can press 'q' at any time to quit <<\n"
				
		#Increments the counter
		count = count + 1
		print ">>> You have made " + str(count) + " guess(es)\n"

"""
	Python is different than some of the other programming languages in how the code is complied. In python the code is not compiled at all,
rather, it uses an interpreter. Interpreters are similar to compilers in the way that they translate high-level languages into machine code.
But they differ in the way that they translate the code. Interpreters execute the code sequentially, that is, line by line, and will halt when
an error is found. The code is converted into 'intermediate code', and executed line by line.  Whereas, compilers builds the entire program, 
then translates it into machine code(1). Other differences between Python and other languages are the code conventions. Python uses indentation,
handles variables more dynamically, and can be more straight forward that other languages(2). Python does not make use of brackets, rather it uses
indentation, which is different than other languages. It also does not require the user to define variables explicitly, which allows it to handle
variables more dynamically. Python also uses some more natural language in its code, such as 'or' rather than '||' (which is used in Java)(2).

	With this information, we can see some pros and cons to the use of Python. The first, and quite possibly the most important, con to using Python
is that it is slower. This is due to the nature of an interpreter than a compiler. Because an interpreter executes lie by line, it performs slower
than a compiler, which will execute a chunk of code(2). Python also appears to be a bit more friendly than other languages, such as Java, for 
beginners. This is because the code feels more like English than other languages. It is also more forgiving than some other languages, in the way
that variables do not have to be explicitly defined, it can interpret them. Whereas, other languages are more strict. with this in mind, it appears 
as though Python may be a good starting point for beginners, rather than a more strict programming language.

	We have already taken CSC 110, we found Python to be much more comfortable than Scratch. In some ways Scratch felt more clunky
and even somewhat confusing. It feels like Scratch is a step backwards, and its simplicity actually makes it more difficult to use. Because of our
previous experience with Java, we were able to catch onto Python fairly quickly. Albeit it still takes time to really learn a new programming 
language.

	Pair programming is a programming methodology that is, as the name implies, about programming in pairs. More specifically, two programmers sit side-by-side, 
with both focused on the code. The programmers can slide the keyboard and mouse between each other, so they can both contribute to the code, directly and 
indirectly(3). The argument for paired programming is that, even though you have two programmers on the same computer (which may seem less efficient),
there is no added cost, as the code will be of higher quality. Which is worth more in the long run(4). Of course, we have to assume that the partners
can actually work together, and adjust to the new methodology. 

	With regard to paired programming, in this and last assignment, we worked together on the programs. Because we found Scratch to be a bit more
challenging, we worked together, on one person's computer to get things working. While we didn't practice perfect paired programming, we did
benefit from the collaboration, especially when using each other as sounding boards.
	
(1) http://www.engineersgarage.com/contribution/difference-between-compiler-and-interpreter
(2) https://www.udemy.com/blog/python-vs-java/
(3) http://www.extremeprogramming.org/rules/pair.html
(4) http://guide.agilealliance.org/guide/pairing.html

"""