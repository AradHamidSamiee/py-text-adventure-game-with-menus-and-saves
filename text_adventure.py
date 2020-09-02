import os
import random

class Player:
    name = 'NULL'
    age = 0
    home = ''
    strength = 0
    health = 0
    money = 0

def GameMenu():
    os.system('cls')
    print(' --- Text Adventure Game --- \n\n')
    print('1) New Game')
    print('2) Load Game')
    print('3) Exit Game')
    print('4) test save')
    while True:
        command = input('> ')
        if command == '1' or command.lower() == 'new' or command.lower().replace(' ', '') == 'newgame':
            NewGame()
        elif command == '2' or command.lower() == 'load' or command.lower().replace(' ', '') == 'loadgame':
            LoadGame()
        elif command == '3' or command.lower() == 'exit' or command.lower().replace(' ', '') == 'exitgame':
            quit()
        elif command == '4':
            SaveGame()

def SaveGame():
    ofile = open('save.tags', 'w')
    for i in range(3):
        ofile.write(str(random.randint(1,10)) + ' - ')

def NewGame():
    command = input(' enter name > ')
    player = Player()
    player.name = command

def LoadGame():
    os.system('cls')
    command = input(' enter [file.tags] > ')
    file = open(command)

    data_list = list()
    for line in file:
        for word in line.replace(' ',''):
            if word != '-' and word != '':
                data_list.append(word)
    print(data_list[0], ': strength')
    print(data_list[1], ': health')
    print(data_list[2], ': wealth')

def stats():
    print(player)
    print(player.name)

def GameWorld():
    while True:
        command = input('> ')

# --------------- main ---------------
GameMenu()
