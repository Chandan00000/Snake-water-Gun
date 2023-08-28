from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # To hide Pygame community message
from pygame import mixer
mixer.init()
from playsound import playsound
import random
import time
 # taking choice from user
def take_userInput():
    user = str.casefold(input("Choose SNAKE(s) or WATER(w) or GUN(g) :\n"))
    if(user == 's' or user=='snake' or user=='1'):
        print("'''You choose SNAKE'''")
        return 's'
    elif(user == 'w' or user=='water' or user=='2'):
        print("'''You choose WATER'''")
        return 'w'
    elif(user =='g' or user=='gun' or user=='3'):
        print("'''You choose GUN'''")
        return 'g'
    else:
        print("'''Invalid Option'''")
        return 0
    
# providing random choice for System
def system_input():
    index = random.randint(1, 3)
    if(index == 1):
        print("'''System choose SNAKE'''")
        system = "s"
    elif(index == 2):
        print("'''System choose WATER'''")
        system = "w"
    else:
        print("'''System choose GUN'''")
        system = "g"    
    return system

#  comparing both the choices between user and system
def comparision(user,system):       
    if(user == system):
            flag=None         
    elif(user == "s"):
        if(system == "w"):
            flag=True
        else:
            flag=False
    elif(user == "w"):
        if(system == "g"):
            flag=True
        else:
            flag=False
    elif(user == "g"):
        if(system == "s"):
            flag=True
        else:
            flag=False     
    return flag  
# star pattern
def pattern1():
    for i in range(3):
        print(" "*(6-i)+"*"*(2*i+1))
        time.sleep(1)
    for i in reversed(range(3)):
        print(" "*(6-i)+"*"*(2*i+1))
        time.sleep(1)
def pattern2():
    for i in range(3):
        print(" "*(6-i)+"*"*(2*i+1))
        time.sleep(1)
        
# Starting of Game
bg_song=mixer.music
bg_song.load(r".\game_music\bg.mpeg")
bg_song.play()              # playing welcome music
print("***WELCOME TO THE GAME***")
pattern1()               #Drawing some pattern
print("***YOU WILL PLAY 3 ROUNDS, OUT OF WHICH WINNER WILL BE ANNOUNCED***")
pattern2()
print("'''   GET   '''")
playsound(r".\game_music\get.mpeg")
print("'''   SET   '''")
playsound(r".\game_music\set.mpeg")
print("'''   GO    '''")
playsound(r".\game_music\go.mpeg")
u=0;s=0                 #Round win count
for i in range(1,4):      #Running a loop for three times to decide best of 3
    print()
    print(f"'''ROUND-{i} STARTS'''")      
    pattern2()
    user=take_userInput()
    system=system_input()
    if(user==0):             #if user gives wrong entry again input will be taken
        user=take_userInput()
    round_won=comparision(user,system)   #result of each round may be win,loss or tie
    pattern2()
    if(round_won==None):
        print("''Round Tie''")
        playsound(r".\game_music\tie.mpeg")
        u+=1
        s+=1
    elif round_won:
        print("''You Won This Round''")
        playsound(r".\game_music\win.mpeg")
        u+=1
    else:
        print("''System Won This Round''")
        playsound(r".\game_music\lose.mpeg")
        s+=1
pattern1()
print("***RESULT TIME***")     #showing the result after all the rounds
print()
time.sleep(2)
print(f"''System Won {s} times''")
time.sleep(2)
print(f"''You Won {u} times''")
time.sleep(2)
print()
if(u==s):
    print("'''Opps, Its a Tie'''")
    playsound(r".\game_music\tie.mpeg")
elif(u>s):
    print("'''CONGRATS!! You Won'''")
    playsound(r".\game_music\win.mpeg")
else:
    print("'''BETTER LUCK NEXT TIME!'''")
    playsound(r".\game_music\lose.mpeg")
pattern1()
print("***THANK YOU***")
bg_song.pause()