import os
# A brief description of your program goes here

##### ACTIONS #####
#  if you add an action it goes here   you_swam is only an example
def you_swam(what):
    print("you swam")

### END ACTIONS ###
### CHARACTERS ###
#  if you add a character it goes here
### END CHARACTERS ###

##### ROOMS #####
# code about what happens in the purple room
# FIRST, you should print your ascii art that shows what is in the room
# Next you should print a line of description about what they see
# Ask them what they want to do (use an input statements
# Use if statements to react to their choice and make the events happen from your description
# You may call actions  you_swam("water")    or character    modules

def purple_room():
	print_xxxx()
	print("The purple room")
	next_move = input("> ")
# code to do what the choices say

##### END ROOMS #####

#### ASCII ART ####
def print_xxxx():
    # Series of print statements to print out your ASCII art.   xxxx is replaced by the name of what
	# you are printing
    print("This is ascii art")
#### END ASCII ART ####
def main():
	# call the module for your room
    purple_room()

    print("\nThe end\n")


if __name__ == '__main__':
    main()