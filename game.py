import random
import tkinter as tk
from tkinter import *

window=tk.Tk()
window.geometry("500x500")
window.title("Scissor Paper Rock @Diwas ")


imageList = []

scissorImg = PhotoImage( file = 'scissors.gif' )
imageList.append( scissorImg.subsample( 3, 3) )

paperImg = PhotoImage( file = 'paper.gif' )
imageList.append( paperImg.subsample( 3, 3) )

stoneImg = PhotoImage( file = 'stone.gif' )
imageList.append( stoneImg.subsample( 3, 3) )



#global variables
USER_SCORE=0
COMP_SCORE=0
USER_CHOICE=""
COMP_CHOICE=""



def choice_to_number(choice):
    rps={'scissor':0,'paper':1,'rock':2}
    return rps[choice]

# def number_to_choice(number):
#         rps={0:'scissor',1:'paper',2:'rock'}
#         return rps[number]
    
def random_computer_choice():
    items = ['scissor', 'paper', 'rock']
    choice = random.choice(items)

    Label( window, image = imageList[ items.index( choice ) ] ).grid( column = 25, row = 2 )

    return  choice

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE

    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)

    if(user==comp):
        print("Tie")

    elif( ( user-comp ) % 3 == 1 ):

         print("Sorry !! Com win")
         COMP_SCORE += 1
    else:
        print("Congarts !! You win")

        USER_SCORE += 1
       

    #Text
    text_area=tk.Text( master = window, height = 12, width = 30)
    text_area.grid( column = 20, row = 5 )

    answer="Your Choice: {uc} \nComputer's Choice : {cc} \nYour Score : {u} \nComputer Score : {c}  \n\n made by sowmy wayne ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE, font=('arial',24,'bold'))
    text_area.insert(tk.END,answer)


#Event Handling
def rock():

    global USER_CHOICE
    global COMP_CHOICE
    
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def paper():

    global USER_CHOICE
    global COMP_CHOICE
    
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def scissor():

    global USER_CHOICE
    global COMP_CHOICE
    
    USER_CHOICE='scissor'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
    


#buttons
button1 = tk.Button( image = imageList[0] ,command = scissor  )
button1.grid( column = 15, row = 2 )

button2=tk.Button(image = imageList[ 2 ], command=rock )
button2.grid( column = 15, row = 4)

button3=tk.Button(image = imageList[ 1 ], command=paper )
button3.grid(column = 15, row = 3)

#Label
Label( window, text = 'User' ).grid( column = 15, row = 1 )
Label( window, text = 'Computer' ).grid( column = 25, row = 1 )

window.mainloop()
