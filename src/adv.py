from room import Room
from player import Player
from help_menu import line, commands, command_key
from room_dict import room
from item import key
from actions import actions

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# set items in rooms
room['overlook'].items.append(key)

#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player_name = input('Welcome. Give your player a name: ')
if player_name == 'q':
    exit()
p1 = Player(player_name, room['outside'])
print(f'\n\nWelcome to {p1.name}\'s Adventure. Good Luck!\n\n{p1.current_room}\n')
print(' Type \'q\' to quit.')
print(' Type \'help\' for command list.')
print(line)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
invalid_entry = '\n*** Invalid entry\n*** [Type \'help\' for a list of commands.]'

while True:
    print(line)
    choice = input('\n      Enter Command:  ').split(' ')
    # Quit
    if choice[0] == 'q':
        break
    # Help
    if choice[0] == 'help':
        for c in command_key:
            print(c)
    # Check if command is valid
    if choice[0] in commands:
        actions(p1, choice, room, key)
    # if the command is not valid,
    elif choice[0] not in commands:
        # show error message with help hint
        print(invalid_entry)
    print(f'\n{p1}\n')