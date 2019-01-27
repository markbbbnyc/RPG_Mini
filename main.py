#!/bin/python3
#RPG starter project

def showInstructions():
    # print a main menu and commands
    print('''
    RPG Game
    ========
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
    if item in rooms(currentRoom):
        print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")

# an inventory, which is initially empty
inventory = []

#a dictionary linking a room to another roomsroom
rooms = {
            'Hall' : {
                    'south' : 'Kitchen'
                },
            'Kitchen' : {
                    'north' : 'Hall'
                }
        }
#start the player in teh Hall
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
        print('You can\'t go that way')

    #if tehy type 'get' first
    if move[0] == 'get':
        #if the rooms contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + 'got!')
            #delet eth eitem from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item is not there to get
        else:
            #tell them tehy can't get it
            print('Can\'t get ' + move[1] + '!')
