'''lambda function is a small
anonymous function that can take any number of arguments but can only have one expression.
which that mean: it is a function that is defined without a name.
 when we usef it in our program the function will be called and the rows and columns will passed to it so it 
 will never used again and when we reset will be created again in teh new game'''
 
#window.geometry("200x200")  you can use it if you want to set the size of the window 


#to import the modules we will use :
from tkinter import*
import random

#step one : define all the functions we will use in the game

#to create a function to fill the button with x or o and to check if the player has won or not
def next_turn(row,column):
    global player
    #now we will check if the button is empty or not
    if button[row][column]['text']=="" and check_winner() is False: 
        #then we fill it with x , o ot whatever and the first player will play 
        if player==players[0]:
            button[row][column]['text']=player
           # button[row][column]['fg']="white"
            if check_winner() is False:
                player=players[1]
                label.config(text=players[1]+" turn")
            elif check_winner() is True:
                label.config(text="the player which used (" +players[0]+") won")   
            elif check_winner() is "tie":
                label.config(text="tie")
        else:
            #the second player turn
            button[row][column]['text']=player
            #button[row][column]['fg']="white"
            if check_winner() is False:
                player=players[0]
                label.config(text=players[0]+" turn")
            elif check_winner() is True:
                label.config(text="the player which used (" +players[1]+") won")   
            elif check_winner() is "tie":
                label.config(text="tie")
        
                 
#to check if the player has won or not or if it is a tie
def check_winner():
    #first step we will check the horizontal lines win 
    for row in range(3):
        if button[row][0]['text']==button[row][1]['text']==button[row][2]['text']  !="":
            button[row][0].config(bg="green")
            button[row][1].config(bg="green")
            button[row][2].config(bg="green")
            return True
        
    # now to check the vertical lines wins    
    for column in range(3):
        if button[0][column]['text']==button[1][column]['text']==button[2][column]['text'] !="":
            button[0][column].config(bg="green")
            button[1][column].config(bg="green")
            button[2][column].config(bg="green")
            return True
        
    #now to check the diagonal lines wins
    if button[0][0]['text']==button[1][1]['text']==button[2][2]['text'] !="":
        button[0][0].config(bg="green")
        button[1][1].config(bg="green")
        button[2][2].config(bg="green")
        return True
    
    #now to check the other diagonal lines wins 
    elif button[0][2]['text']==button[1][1]['text']==button[2][0]['text'] !="":
        button[0][2].config(bg="green")
        button[1][1].config(bg="green")
        button[2][0].config(bg="green")
        return True
    
    elif empty_spaces() is False:
        #to make it yellow if the game is tie
        for row in range(3):
            for column in range(3):
                button[row][column].config(bg="yellow")
        #to check if there is no empty spaces in the buttons and the game is tie
        return "we have a two great players and they are equal"
    else:
        return False
    
       
#to check if there is empty spaces in the buttons or not
def empty_spaces():
    spaces=9
    for row in range(3):
        for column in range(3):
            if button[row][column]['text'] !="":
                spaces-=1
    if spaces ==0:
        return False
    else:
        return True
#to create a function to reset the game and start a new one

def new_game():
    global player
    player=random.choice(players) #to choose a random player to start the game
    label.config(text="the player which used ("+player+") turn")
    for row in range(3):
        for column in range(3):
            button[row][column].config(text="",bg="black")
            
            
#to crete a window as an interface
window=Tk()
window.title("Tic Tac Toe")
window.config(bg="black") #to set the background color of the window
players=["X","O"] #to create a list of the players
#to make it choose an random played to start :
player=random.choice(players)

#to create the buttons :
button=[[0,0,0],
        [0,0,0],
        [0,0,0]  ]
#now we will create a reset button and to make the user able to know about the player who is playing now 
label=Label(text=player+" turn", font=("consolas",20),bg="black",fg="light blue")
label.pack(side="top")
reset_button=Button(text="reset",font=("consolas",20),command=new_game,bg="black",fg="light blue")
reset_button.pack(side="bottom")

#now to create the frame 
frame=Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        button[row][column]=Button(frame,text="",font=("consolas",20),width=10,height=3,bg="black",fg="light blue",
                                   command=lambda row=row,column=column:next_turn(row,column))
        button[row][column].grid(row=row,column=column)
#with this step we finally finish our body of the game now we will create the function to make the game work 
window.mainloop() #to run the window 

