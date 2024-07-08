from tkinter import *
from PIL import Image,ImageTk
from random import choice

root = Tk()
root.title("Rock Paper Scissor Game By ritik")
root.geometry("1300x500")
label = Label(root, text="Rock Paper Scissor Game", font = "bold", bg="grey", fg="white")
label.grid(row=0,column=2)

# Function to resize image
def resize_image(image_path, size):
    image = Image.open(image_path)
    resized_image = image.resize(size)
    return ImageTk.PhotoImage(resized_image)

# Desired size for images
image_size = (300,300)

# Resized pictures
Rock_img_user = resize_image("rock.jpg", image_size)
paper_img_user = resize_image("paper.jpeg", image_size)
scissor_img_user = resize_image("scissor.jpeg", image_size)
Rock_img_computer = resize_image("rock.jpg", image_size)
paper_img_computer = resize_image("paper.jpeg", image_size)
scissor_img_computer = resize_image("scissor.jpeg", image_size)

# insert pictures
user_image_label = Label(root,image=Rock_img_user)
user_image_label.grid(row=1,column=0)
computer_image_label = Label(root, image=Rock_img_computer)
computer_image_label.grid(row=1,column=4)

#scores
playerscore = Label(root, text=0, font="bold",fg="black")
playerscore.grid(row=1,column=1)
computerscore = Label(root, text=0, font="bold",fg="black")
computerscore.grid(row=1,column=3)

# indicators 
user_indicator = Label(root, text="USER", font="bold",fg="black")
user_indicator.grid(row=0,column=1)
computer_indicator = Label(root, text="COMPUTER", font="bold",fg="black")
computer_indicator.grid(row=0,column=3)

# message
messagge = Label(root,font="bold",fg="black")
messagge.grid(row=3,column=2)

#update message
def updateMessage(x):
    messagge['text'] = x

# update user score
def updateUserscore():
    score = int(playerscore["text"])
    score  = score + 1
    playerscore["text"] = str(score)

#update computer score
def updateComputerscore():
    score = int(computerscore["text"])
    score  = score + 1
    computerscore['text'] = str(score)

# checking winner
def checkWin(player,computer):
    if(player == computer):
        updateMessage("It's a Tie!!")
    elif(player == "rock"):
        if(computer == "paper+button"):
            updateMessage("you loose!!")
            updateComputerscore()
        else:
            updateMessage("you win!!")
            updateUserscore()
    elif(player == "paper"):
        if(computer == "rock_button"):
            updateMessage("you  win!!")
            updateUserscore()
        else:
            updateMessage("you loose!")
            updateComputerscore()
    elif(player == "scissor"):
        if(computer == "rock"):
            updateMessage("you loose!!")
            updateComputerscore()
        else:
            updateMessage("You win !!")
            updateUserscore()
    else:
        pass

#choices
choices = ["rock","paper","scissor"]
def updateChoice(x):
    #computer choices
    computer_choice = choice(choices)
    if(computer_choice =="rock"):
        computer_image_label.config(image=Rock_img_computer)
    elif(computer_choice =="paper"):
        computer_image_label.config(image=paper_img_computer)
    else:
        computer_image_label.config(image=scissor_img_computer)

    #user choice
    if(x == "rock"):
        user_image_label.config(image=Rock_img_user)
    elif(x =="paper"):
        user_image_label.configure(image=paper_img_user)
    else:
        user_image_label.configure(image=scissor_img_user)
    checkWin(x,computer_choice)

# button
rock = Button(root,command=lambda:updateChoice("rock"),font="bold", width=20,height=2,text="ROCK",fg="black")
rock.grid(row=2,column=1,padx=3)
paper = Button(root,command=lambda:updateChoice("paper"),font="bold",width=20,height=2,text="PAPER",fg="black")
paper.grid(row=2,column=2,padx=3)
scissor = Button(root, command=lambda:updateChoice("scissor"),width=20,height=2,font="bold",text="SCISSOR",fg="black")
scissor.grid(row=2,column=3,padx=3)

root.mainloop()
