#!~/anaconda3/bin/python

#RPG starter project

def showInstructions():
    # print a main menu and Commands
    print('''
RPG Game
========

Get to the garden with a key and a potion.
Avoid the monsters!

Commands:
    go [direction]
    get [item]
''')

def showStatus():
    #print the player's current showStatus
    print('-------------------------------')
    print('You are in the ' + currentRoom)
    # print th ecurrent inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to another rooms
rooms = {

            'Hall'      :      {
                    'south' : 'Kitchen',
                    'east'  : 'Dining Room',
                    'item'  : 'key'
                },

            'Kitchen'   :      {
                    'north' : 'Hall',
                    'item'  : 'monster'
                },

            'Dining Room'   :  {
                    'west'  : 'Hall',
                    'south' : 'Garden',
                    'item'  : 'potion'
                },

            'Garden'   :  {
                    'north' : 'Dining Room',
                    'west'  : "Kitchen"
                }

        }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

    showStatus()

    #get player's nect 'move'
    #.split() breaks it up in tn list array
    #e.g. typing 'go east'  would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed where they want to go
        if move[1] in rooms[currentRoom]:
            #set the currentRoom to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the rooms contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delet the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item is not there to get
        else:
            #tell them tehy can't get it
            print('Can\'t get ' + move[1] + '!')
    # if player enters a room with a monster they die and lose the Game
    if 'item' in rooms[currentRoom] and'monster' in rooms[currentRoom]['item']:
        print('You entered a room with a hungry monster that attacked and killed you. Game Over!')
        break
    # let player win the game if they collected key and magic potion and made it
    # to the garden alive
    if currentRoom == "Garden" and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house and win the game')
        break
