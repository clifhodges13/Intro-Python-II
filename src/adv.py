from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
line = '-'*40
# Make a new player object that is currently in the 'outside' room.
player_name = input('Welcome. Give your player a name: ')
if player_name == 'q':
    exit()
new_player = Player(player_name, room['outside'])
print(f'\n\nWelcome to {new_player.name}\'s Adventure. Good Luck!\n')
print(' Type \'q\' to quit.')
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
choice = ''
directions = { 'n', 's', 'e', 'w' }
dead_end = '\nThere doesn\'t seem to be anything that way.\n'
invalid_entry = '\n*** Invalid entry\n*** [Type \'help\' for a list of commands.]'
commands = (
    line,
    '\'n\'    : Move North',
    '\'s\'    : Move South',
    '\'e\'    : Move East',
    '\'w\'    : Move West',
    '\'q\'    : Quit',
    '\'help\' : View commands',
    line
)

while True:
    print(line)
    choice = input('\n    Which direction? => ')
    if choice == 'q':
        break
    if choice == 'help':
        for c in commands:
            print(c)
    if choice in directions:
        if hasattr(new_player.current_room, f'{choice}_to'):
            new_player.current_room = getattr(new_player.current_room, f'{choice}_to')
        else:
            print(dead_end)
            break
    elif choice not in directions:
        print(invalid_entry)
    print(new_player)

    # elif len(choice == 2):
    #     # if drop item
    #     if choice[0] == 'drop':
    #         pass