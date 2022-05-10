#The tkinter program whichc generates the GUI
from tkinter import *
import random

#Create the tkinter instance
root = Tk("Dice Game")
#Create the geometry
root.geometry("900x1000")

#Enter user input for number of dice
dice_amount = (input("How many dice do you want to roll? [1-6] "))
num_dice = []

#GUI will have three basic components
#1.Button which will trigger the rolling of dice
#2.Exite button to close the page
#3.Dice label
l1 = Label(root, font = ("Helvetica", 260))

def roll():
  #create a number variable in which the list of all the ASCII characters of the string will be stored
  #Use backslash because unicode must have a backslash 
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

#Hopefully this will controll the number of dice rolled

    if dice_amount == "1":
        l1.config(text = f'{random.choice(dice)}')
        l1.pack()
    elif dice_amount == "2":
        l1.config(text = f'{random.choice(dice)}{random.choice(dice)}')
        l1.pack()
    elif dice_amount == "3":
        l1.config(text = f'{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}')
        l1.pack()
    elif dice_amount == "4":
        l1.config(text = f'{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}')
        l1.pack()
    elif dice_amount == "5":
        l1.config(text = f'{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}')
        l1.pack()
    elif dice_amount == "6":
        l1.config(text = f'{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}')
        l1.pack()

#This will create the dice roll button
b1 = Button(root,text = "Roll the Dice!",foreground = 'blue',command = roll)
b1.place(x = 300,y = 0)
b1.pack()
#This will create the Exit button
b2 = Button(root, text = "Exit", foreground = 'blue', command = root.destroy)
b2.place(x = 600, y = 0)
b2.pack()

root.mainloop()
