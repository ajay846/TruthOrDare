import random
from time import sleep
import os
import sys
from dares import *     #Importing other .py file containing dares
from truths import *    #Importing other .py file containing truths
from errors import *    #Importing other .py file containing errors


clear = lambda: os.system("cls")    #clear()

def main():

    def sub_main():

        def excess():
            print("Players can't be more than '4' nor less than '2'")

        count = '0' #NOT IN USE

        global dict_players

        global player1
        global player2
        global player3
        global player4

        player1 = ""
        player2 = ""
        player3 = ""
        player4 = ""

        global players

        players = input("No of players (2-4): ")
        clear()
        print("Processing request")
        sleep(3.5)
        clear()
        try:
            if players == '2':
                player1 = input("Player 1st Name: ")
                print("Storing name for rest of the game")
                sleep(1)
                clear()
                player2 = input("Player 2nd Name: ")
                print("Storing name for rest of the game")
                sleep(1)
                clear()
                if player1 == player2:
                    print("The names of players can't be same!")
                    exit(0)
                elif player1 == '':
                    print("Enter both players names")
                    exit(0)
                elif player2 == '':
                    print("Enter both players names")
                    exit(0)
                else:
                    print("Hello "+player1.capitalize()+" and "+player2.capitalize())
                    sleep(2)
                    clear()
                    dict_players = (player1.capitalize(), player2.capitalize())

            elif players == '3':
                player1 = input("Player 1st Name: ")
                print("Storing name for rest of the game")
                sleep(1)
                clear()
                player2 = input("Player 2nd Name: ")
                print("Storing name for rest of the game")
                sleep(1)
                clear()
                player3 = input("Player 3rd Name: ")
                print("Storing name for rest of the game")
                sleep(1)
                clear()
                if player1 == player2 or player1 == player3 or player2 == player3:
                    print("The names of players can't be same!")
                    exit(0)
                elif player1 == '':
                    print("Enter all players names")
                    exit(0)
                elif player2 == '':
                    print("Enter all players names")
                    exit(0)
                elif player3 == '':
                    print("Enter all players names")
                    exit(0)
                else:
                    print("Hello "+player1.capitalize()+", "+player2.capitalize()+" and "+player3.capitalize())
                    sleep(2)
                    clear()
                    dict_players = (player1.capitalize(), player2.capitalize(), player3.capitalize())
            elif players == '4':
                player1 = input("Player 1st Name: ")
                print("Storing name for rest of the game")
                sleep(1)
                clear()
                player2 = input("Player 2nd Name: ")
                print("Storing name for rest of the game")
                sleep(1)
                clear()
                player3 = input("Player 3rd Name: ")
                print("Storing name for rest of the game")
                sleep(1)
                clear()
                player4 = input("Player 4th Name: ")
                print("Storing name for rest of the game")
                sleep(1)
                clear()
                if player1 == player2 or player1 == player3 or player1 == player4 or player2 == player3 or player2 == player4 or player4 == player1 or player4 == player2 or player4 == player3:
                    print("The names of players can't be same!")
                    exit(0)
                elif player1 == '':
                    print("Enter all players names")
                    exit(0)
                elif player2 == '':
                    print("Enter all players names")
                    exit(0)
                elif player3 == '':
                    print("Enter all players names")
                    exit(0)
                elif player4 == '':
                    print("Enter all players names")
                    exit(0)
                else:
                    print("Hello "+player1.capitalize()+", "+player2.capitalize()+", "+player3.capitalize()+" and "+player4.capitalize())
                    sleep(2)
                    clear()
                    dict_players = (player1.capitalize(), player2.capitalize(), player3.capitalize(), player4.capitalize())
            elif players >= '5' or players <= '1':
                excess()
                sleep(2)
                clear()
                sub_main()


        except:
            print(random.choice(error))

    sub_main()

    while True:
        response = input("To start spin press 'ENTER'")
        sleep(5)
        global player_select
        if response == '':
            clear()
            player_select = random.choice(dict_players)
            print("It's "+player_select+"'s turn")
            sleep(3)
            clear()
            def ask():
                global user_choice
                user_choice = input("Enter your choice truth(t) or dare(d) ")
            ask()
            try:
                def truth():
                    print("The question>> "+random.choice(t))

                def dares():
                    print("The dare>> "+random.choice(d))

                if  user_choice == 't' or user_choice == 'T':
                    truth()
                elif user_choice == 'd' or user_choice == 'D':
                    dares()

            except:
                print(random.choice(error))
        elif response != '':
            print("Unexpected Response!")

main()
