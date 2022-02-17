'''THE HANGMAN GAME'''

name=input("Enter your name:")
print ("Hello",name,"! Time to play HANGMAN!")

import random
import turtle


fobj=open('Words.txt','r')
l=fobj.readlines()
word=[]
for i in range(len(l)):
    r=l[i].rstrip('\n')
    word.append(r)

chance=7
a=random.randint(0,len(word)-1)             # selects a word randomly from file 'Words.txt'
secret=word[a]
guesses=' '
print ('You have 7 chances to guess the place')

while chance>0:
    c=0
    for i in secret:
        if i in guesses:
            print (i),
        else:
            print (' __ '),
            c+=1
    print ('\n')
    
    if c==0:                         # no blanks left, won game
        print ('Bravo!!! You Won :-) ')
        break
    guess=input('Guess letter:')
    guesses+=guess
    
    if guess not in secret:
        chance-=1
        print ("You guessed a wrong letter")
        print ("You have",chance,"more chances left",'\n')
        
        if chance ==6:              # face
            turtle.lt(90)
            turtle.up()
            turtle.fd(200)
            turtle.down()
            turtle.circle(50)
            turtle.lt(90)
            turtle.up()
            turtle.fd(50)
            turtle.lt(90)
            turtle.fd(50)
            turtle.down()
            
        if chance ==5:              # body
            turtle.down()
            turtle.fd(150)
            
        if chance ==4:              # leg
             turtle.lt(45)
             turtle.fd(100)
             turtle.bk(100)
             turtle.rt(90)
             
        if chance ==3:              # leg
             turtle.fd(100)
             turtle.bk(100)
             turtle.rt(135)
             
        if chance ==2:              # arm
            turtle.fd(90)
            turtle.lt(135)
            turtle.fd(100)
            turtle.bk(100)
            
        if chance ==1:              # arm
            turtle.lt(90)
            turtle.fd(100)
            turtle.bk(100)
            turtle.lt(135)
            turtle.up()
            turtle.fd(160)
            turtle.down()
            
        if chance ==0:              # hanging man
            turtle.fd(30)
            turtle.rt(90)
            turtle.fd(100)
            turtle.rt(90)
            turtle.fd(500)
            turtle.lt(90)
            turtle.fd(300)
            turtle.bk(600)
            
            print ("You lose  :-( ",'\n')                                              # lost game
            print ("The word was",secret,'\n' "Try again")                # game over
            
         
      

                
