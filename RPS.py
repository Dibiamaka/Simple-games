# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 05:54:54 2020

@author: DIBIAMAKA
"""
import time
import random

rock = 1
paper = 2
scissors = 3

names = {rock: "rock", paper: "paper", scissors: "scissors"}
rules = {rock: "scisors", paper: "rock", scissors: "paper"}

player_score = 0
computer_score = 0

def start():
    print ("Gentlemen, the game is rock, paper, scissors" ) 
    while game():
        pass
    scores()
    

def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def move():
    while True:
        print
        player = input("rock =1\nPaper =2\nScissors =3\nmake a move: ")
        try:
            player = int(player)
            if player in(1, 2, 3):
                return player
        except ValueError:
            pass
        print ("oops! i didnt understand that input, please enter 1, 2 or 3")
        
    
def result(player, computer):
    print("1.....")
    time.sleep(1)
    print("2....")
    time.sleep(1)
    print("3...")
    time.sleep(0.5)
    print("computer threw (0).:".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("This is a Tie!")
    else:
        if rules[player] == computer:
            print("Victoria Assata")
            player_score += 1
        else:
            print("HEHEHEHEHE do you realise you are loosing?")
            computer_score += 1
            
    

def play_again():
    answer = input("Would you like to play again ? Y/N" )
    if answer in ("y", "Y", "yes", "Yes", "YES"):
        return answer
    else:
        print("Thank you for playing our game")
        
        

def scores():
    global player_score , computer_score
    print("HIGH SCORES")
    print("Player:" , player_score)
    print("Computer: ", computer_score)
    
        
if __name__ == '__main__':
    start()
    
