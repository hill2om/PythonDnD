import os
# A little puzzle room. There are three rooms to enter at first. The left houses a monster
# from which you can flee, or you die if you choose any other option (options TBD).
# The second room is the puzzle room with three levers. You must pull the levers in the right
# order to survive and escape the room. You die otherwise through various means depending on
# the wrong order (maybe, lots of unnecessary work). The third room is a room with treasure,
# and a book that you can read to learn that there's a key in the room that will unlock the
# puzzle door automatically.

##### GLOBAL VARIABLES #####
have_key = False
##### END GLOBAL VARIABLES #####

##### ACTIONS #####
# clear_screen, pull_lever(lever), get_treasure(treasure), read_book, flee_monster, die

def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def pull_lever(lever):
    print(lever)

def get_treasure(treasure):
    print(treasure)

def read_book():
    print("read_book()")

def die(flavor):
    clear_screen()
    print_game_over()
    print(flavor)
    print("Your vision goes dark and the world shimmers around you.")
    exit()

### END ACTIONS ###

### CHARACTERS ###
#  if you add a character it goes here
### END CHARACTERS ###

##### ROOMS #####
def lime_room():
    clear_screen()
    print_doorway()
    print("You enter a room with three doors. There's one on the left, one in front of you in the middle, and one on the right.")
    print("Which door would you like to try?")
    door_picked = input("[ left | middle | right ] > ")

    # Pick a door and we go to a room and something else happens
    if door_picked == "left":
        incoming_death_and_mayhem()
    elif door_picked == "middle":
        endless_lever_pulling_madness()
    elif door_picked == "right":
        treasure_mountain_of_kings()
    else:
        die("Your hesitation to choose a door has cost you. A skeleton rises up from the corner of the room and stabs you in the back.")

def incoming_death_and_mayhem():
    clear_screen()
    print_reaper()
    print("A robed figure stands before you.")
    print("A menacing presence emanates from the being.")
    print("Do you turn and run, attack the creature, or attempt to communicate with it?")

    next_move = input("[ flee | fight | talk ] > ")

    if next_move.lower() == "flee":
        lime_room()
    else:
        die("You chose wrong. The being approaches you swiftly and touches you, causing your chest to burn as you feel something being torn away.")


def endless_lever_pulling_madness():
    clear_screen()
    print_levers()
    print("You find yourself in a hallway with two doors on opposite ends, having entered from one.")
    print("Along the wall are three levers that you can pull.")
    print("Both doors suddently shut, and you hear a loud 'chunk' as they are locked.")
    print("Might as well try a lever! Do you want to pull the left, middle, or right one?")

    leversum = 0
    ##### EDIT THIS LATER TO REFLECT HAVING THE KEY, WHEN WE GET THERE #####
    player_choice = input("[ left | middle | right ] > ")
    ##### NEEDS TO BE LOOKED AT, IFFY #####
    if player_choice.lower() == "left":
        leversum = leversum + pull_lever("left", leversum)
    elif player_choice.lower() == "middle":
        leversum = leversum + pull_lever("middle", leversum)
    elif player_choice.lower() == "right":
        leversum = leversum + pull_lever("right", leversum)
    else:
        die("Your inability to make a decision leads to a trap spike rising up from the floor to impale you.")

def treasure_mountain_of_kings():
    clear_screen()
    global have_key
    if not have_key:
        print_chest()
        treasure_chest = ["diamonds", "gold", "a key", "silver", "a sword"]
        print("You enter the room to see a mountain of treasure lying before you!")
        print("In particular, a gilded chest catches your eye that contains some interestingly valuable items.")
        print("Hiding behind the chest appears to be a tattered book of some sort.")
        print("What would you like to do?")

        action = input("[ chest | book | return ] > ")

        if action.lower() == "chest":
            print("You decide to inspect the chest. Let's see what's in here....")
            print("You find some")
            for treasure in treasure_chest:
                print(treasure)
            print("What do you want to do?")
            print("Take the diamonds (1), gold (2), key (3), etc.")
            print("Leave it (0)")
            treasure_choice = input(" > ")
            if treasure_choice == "3":
                print("You pick up the key, and suddenly the piles of treasure vanish around you. The key remains in your hand.")
                have_key = True
            elif treasure_choice == "0":
                treasure_mountain_of_kings()
            else:
                die("You touch one of the treasures. You feel a curse weighing heavyily upon you.")
        elif action.lower() == "book":
            read_book()
        else:
            lime_room()
    else:
        print_book()
        print("You enter the now-empty room.")
        print("The lone book lies before you, looking sad and lonely without the piles of riches around.")
        action = input("[ book | return ] > ")

        if action.lower() == "book":
            read_book()
        else:
            lime_room()

##### END ROOMS #####

#### ASCII ART ####
def print_doorway():
    print()
    print("   _________________________________________________________________________________________")
    print(" /|     -_-                                             _-                              _-  |\ ")
    print("/ |_-_- _                                         -_- _-                          -_- _-   -| \ ")
    print("  |                            _-  _--                         _-  _--                      |")
    print("  |                            ,                               ,                            |")
    print("  |      .-'````````'.        '(`        .-'```````'-.        '(`        .-'```````'-.      |")
    print("  |    .` |           `.      `)'      .` |           `.      `)'      .` |           `.    |")
    print("  |   /   |   ()        \      U      /   |    ()       \      U      /   |    ()       \   |")
    print("  |  |    |    ;         | o   T   o |    |    ;         | o   T   o |    |    ;         |  |")
    print("  |  |    |     ;        |  .  |  .  |    |    ;         |  .  |  .  |    |    ;         |  |")
    print("  |  |    |     ;        |   . | .   |    |    ;         |   . | .   |    |    ;         |  |")
    print("  |  |    |     ;        |    .|.    |    |    ;         |    .|.    |    |    ;         |  |")
    print("  |  |    |____;_________|     |     |    |____;_________|     |     |    |____;_________|  |")
    print("  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |     !     |   /     `'() _ -  |  |")
    print("  |  |  / __  ()        -|        -  |  /  __--      -   |        -  |  /  __--      -   |  |")
    print("  |  | /        __-- _   |   _- _ -  | /        __--_    |   _- _ -  | /        __--_    |  |")
    print("  |__|/__________________|___________|/__________________|___________|/__________________|__|")
    print(" /                                             _ -                              _ -          \ ")
    print("/   -_- _ -             _- _---                       -_-   _- _---                   -_-  -_ \ ")
    print()

def print_book():
    print()
    print("         ,..........   ..........,")
    print("     ,..,'          '.'          ',..,")
    print("    ,' ,'            :            ', ',")
    print("   ,' ,'             :             ', ',")
    print("  ,' ,'              :              ', ',")
    print(" ,' ,'............., : ,.............', ',")
    print(",'  '............   '.'   ............'  ',")
    print(" '''''''''''''''''';''';''''''''''''''''''")
    print("                    '''")
    print()

def print_chest():
    print()
    print("                      _.--. ")
    print("                  _.-'_:-'|| ")
    print("              _.-'_.-::::'|| ")
    print("         _.-:'_.-::::::'  || ")
    print("       .'`-.-:::::::'     || ")
    print("      /.'`;|:::::::'      ||_ ")
    print("     ||   ||::::::'     _.;._'-._ ")
    print("     ||   ||:::::'  _.-!oo @.!-._'-. ")
    print("     ('.  ||:::::.-!()oo @!()@.-'_.| ")
    print("      '.'-;|:.-'.&$@.& ()$%-'o.'-U|| ")
    print("        `>'-.!@%()@'@_%-'_.-o _.|'|| ")
    print("         ||-._'-.@.-'_.-' _.-o  |'|| ")
    print("         ||=[ '-._.-+U/.-'    o |'|| ")
    print("         || '-.]=|| |'|      o  |'|| ")
    print("         ||      || |'|        _| '; ")
    print("         ||      || |'|    _.-'_.-' ")
    print("         |'-._   || |'|_.-'_.-' ")
    print("          '-._'-.|| |' `_.-' ")
    print("              '-.||_/.-' ")
    print()

def print_game_over():
    print()
    print("   _____          __  __ ______    ______      ________ _____  ")
    print("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ ")
    print(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |")
    print(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / ")
    print(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ ")
    print("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\\")
    print()

def print_levers():
    print()
    print("      ___ (@)           ___ (@)           ___ (@)")
    print("     |.-.|/            |.-.|/            |.-.|/")
    print("     || |/             || |/             || |/")
    print("     || /|             || /|             || /|")
    print("     ||/||             ||/||             ||/||")
    print("     || ||             || ||             || ||")
    print("     ||_||             ||_||             ||_||")
    print("     '---'             '---'             '---'")
    print()

def print_reaper():
    print()
    print("            *********")
    print("           *************")
    print("          *****     *****")
    print("         ***           ***")
    print("        ***             ***")
    print("        **    0     0    **")
    print("        **               **                  ____")
    print("        ***             ***             //////////")
    print("        ****           ****        ///////////////")
    print("        *****         *****    ///////////////////")
    print("        ******       ******/////////         |  |")
    print("      *********     ****//////               |  |")
    print("   *************   **/////*****              |  |")
    print("  *************** **///***********          *|  |*")
    print(" ************************************    ****| <=>*")
    print("*********************************************|<===>* ")
    print("*********************************************| <==>*")
    print("***************************** ***************| <=>*")
    print("******************************* *************|  |*")
    print("********************************** **********|  |*")
    print("*********************************** *********|  |")
    print()
#### END ASCII ART ####

def main():
    clear_screen()
	# call the module for your room
    lime_room()

    print("\nThe end\n")


if __name__ == '__main__':
    main()
