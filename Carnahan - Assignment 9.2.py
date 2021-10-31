##############################################################################
# Author: Jacob Carnahan
# Class : CIS 245-T302
# Date : October 28, 2021
# Description:
#       Assignment 9.2 - Below is a simple program with 10 issues (some are
#                        syntax errors and some are logic errors.  You need to
#                        identify the issues and correct them.
##############################################################################


import random
import time

def displayIntro():
	#--------------------------------------------------------------
    #print('''You are in a land full of dragons. In front of you,
	#you see two caves. In one cave, the dragon is friendly
	#and will share his treasure with you. The other dragon
	#is greedy and hungry, and will eat you on sight.''')
    #
    # Ought to work technically, but won't display as intended.
    # Let's be a little more deliberate in our output:
	#--------------------------------------------------------------
    print('You are in a land full of dragons.\nIn front of you,'
        'you see two caves.\nIn one cave, the dragon is friendly '
        'and will share his treasure with you.\nThe other dragon '
        'is greedy and hungry, and will eat you on sight.\n')

    #--------------------------------------------------------------    
    #print()
    # Why? Incredibly inefficient way to print a newline. Just
    # add it to the previous print.
    #--------------------------------------------------------------    

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    #--------------------------------------------------------------
    #return caves
    # Wrong variable name!
    #--------------------------------------------------------------
    return cave
    
def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    #--------------------------------------------------------------	
    #time.sleep(3)
    # Comment indicates intended sleep time of 2 secs not 3, fixed:
    #--------------------------------------------------------------
    time.sleep(2)
    #--------------------------------------------------------------
    #print('A large dragon jumps out in front of you! He opens his jaws and...')
    #print()
    # ^ Another extraneous print call.
    #--------------------------------------------------------------
    print('A large dragon jumps out in front of you! He opens his jaws and...\n')
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
    #--------------------------------------------------------------
    #	print 'Gobbles you down in one bite!'
    # Improper function call. Missing parentheses.
    #--------------------------------------------------------------
        print('Gobbles you down in one bite!')

playAgain = 'yes'
#--------------------------------------------------------------
#while playAgain = 'yes' or playAgain = 'y':
# Assignment, not comparison...
#--------------------------------------------------------------
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    #--------------------------------------------------------------
    #caveNumber = choosecave()
    # Invalid call, 'c' ^ should be capitalized.
    #--------------------------------------------------------------
    caveNumber = chooseCave()
    checkCave(caveNumber)
    
	
    #print('Do you want to play again? (yes or no)')
    # Nothing wrong with this line. Commented out for rewrite.
    #--------------------------------------------------------------
    #playAgain = input()
    # What if user capitalizes? Add call to convert to lowercase...
    #--------------------------------------------------------------
    #if playAgain == "no":
    # Issues:
    # -Inconsistent with main loop logic. Add check for 'n' as well.
    # -Needs prior input validation. Message won't print if value other
    #  than 'no' is entered and interpreted as an exit condition. 
    #
    # Side Note:
    # Whole main loop would be more efficient in a do...while format 
    # with a call to exit() after "no/n" input validation. 
    # See end of file.
    #--------------------------------------------------------------
    #	print("Thanks for planing")
    #       "playing", not...^ 
    #--------------------------------------------------------------
    while True:
        print('Do you want to play again? (yes or no)')
        playAgain = input().lower()
        if playAgain == 'yes' or playAgain == 'y' or playAgain == 'no' or playAgain == 'n':
            break
    
    if playAgain == 'no' or playAgain == 'n':
        print('Thanks for playing!')
        
#--------------------------------------------------------------
# Above code is ugly and inefficient. Chose to do it this way so
# as to not modify too much of the original code's structure. 
# Recommend rewriting as such:
#
# (remove original playAgain assignment here)
#while True:
#   displayIntro()
#   caveNumber = chooseCave()
#   checkCave(caveNumber)
#
#   while True:
#       print('Do you want to play again? (yes or no)')
#       playAgain = input().lower()
#       if playAgain == 'yes' or playAgain == 'y':
#           break
#       if playAgain == 'no' or playAgain == 'n':
#           print('Thanks for playing!')
#           exit()
#--------------------------------------------------------------