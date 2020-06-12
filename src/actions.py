dead_end = '\nThere doesn\'t seem to be anything that way.\n'

def actions(p1, choice, room, key):
    if choice[0] == 'take':
        if len(choice) < 2:
            print(f'What do you want to {choice[0]}?')
        else:
            if len(p1.current_room.items) == 0:
                print('There\'s nothing to {choice[0]}.')
            elif choice[1] in p1.current_room.items[0].name:
                p1.items.append(p1.current_room.items[0])
                p1.current_room.items = []
                message = p1.items[0].on_take()
                print(f'{message}')
            else:
                print('Hmmm... That item doesn\'t appear to be in the room.')
    elif choice[0] == 'drop':
        if len(choice) < 2:
            print(f'What do you want to {choice[0]}?')
        else:
            if len(p1.items) == 0:
                print('There\'s nothing to {choice[0]}.')
            elif choice[1] in p1.items[0].name:
                p1.current_room.items.append(p1.items[0])
                p1.items = []
                message = p1.current_room.items[0].on_drop()
                print(f'{message}')
            else:
                print('Hmmm... That item doesn\'t appear to be in your inventory.')
    elif hasattr(p1.current_room, f'{choice[0]}_to'):
        if hasattr(p1.current_room, 'n_to') and p1.current_room.n_to.name == 'Treasure Chamber':
            if key not in p1.items:
                print('The door seems to be locked.')
                p1.current_room = room['narrow']
            else:
                p1.current_room = room['treasure']
        else:
            p1.current_room = getattr(p1.current_room, f'{choice[0]}_to')
        print(p1.current_room.name)
    else:
        print(dead_end)