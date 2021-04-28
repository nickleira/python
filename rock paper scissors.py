# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 00:39:56 2021

@author: nleir
"""
import random
state = 'y'
score = [0,0]
print('would you like to play [r]ock [p]aper [s]cissors? [y]/[n]? ')
state = input()
while state == 'y':
    if state == 'y':
        print('rock')
        print('paper')
        print('scissors')
        print('shoot!')
        choice = input('you draw ')
        if choice == 'r':
            choice = 0
        elif choice == 'p':
            choice = 1
        elif choice == 's':
            choice = 2
        elif choice == 'shoot!':
            print('nice try kimosabe')
            continue
        else:
            print('that is not an option!')
            continue
        bot = random.randrange(0,3,1)
        if bot == 0:
            print('bot draws r')
        elif bot == 1:
            print('bot draws p')
        elif bot == 2:
            print('bot draws s')
        result = choice - bot
        if result == -2 or result == 1:  
            score[0] = score[0]+1
            print('you won!')
        elif result == -1 or result == 2:
            score[1] = score[1] + 1
            print('you lost!')
        else:
            print('its a tie!')    
        print('the score is now ' +str(score[0])+' to ' + str(score[1]))
        if score[0] == 3: 
            print('game over, you win')
            state = 'n'
        elif score[1] == 3:
            print('game over, you lose')
            state = 'n'
    elif state != 'n':
       print('what did you say?')    
       state = 'y'
    elif state == 'n':     
        print('thanks for playing!')     
        
    
        
  
   
        
   