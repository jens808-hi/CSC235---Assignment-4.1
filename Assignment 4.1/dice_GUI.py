import tkinter as tk #Using Tkinter to create the graphical user interface (GUI)
from PIL import Image, ImageTk #Using Pillow library (PIL) for handling and manipulating images
import random #This module generates random numbers for dice rolling
import os #This module interacts with the operating system to access file paths
import webbrowser #Used for opening a URL in the default web browser

#Function used to create a gradient background on the canvas
def create_gradient(canvas, width, height, color1, color2):
    """Creates a gradient background on the canvas.
    Args:
        canvas: The Tkinter canvas to draw on.
        width: Width of the canvas.
        height: Height of the canvas.
        color1: Starting color of the gradient (Hex format).
        color2: Ending color of the gradient (Hex format)."""
    gradient_steps = 100 #Defines the number of steps to create the gradient effect
    for i in range(gradient_steps): #loops to create each step and calculates the color at that step
        ratio = i / gradient_steps #Calculates the ratio for the gradient transition of color1 and color2 to blend at each step
        #Calculate the RGB values for the current gradient step
        red = int((1 - ratio) * int(color1[1:3], 16) + ratio * int(color2[1:3], 16))
        green = int((1 - ratio) * int(color1[3:5], 16) + ratio * int(color2[3:5], 16))
        blue = int((1 - ratio) * int(color1[5:7], 16) + ratio * int(color2[5:7], 16))
        color = f"#{red:02x}{green:02x}{blue:02x}" #Converts RGB back to a hex color string 
        #Draws a horizontal rectangle for each step of the gradient. Each rectangle will fill part of the canvas
        canvas.create_rectangle(0, i * (height / gradient_steps), width, (i + 1) * (height / gradient_steps), fill=color, outline="") #No outline for smooth appearance
    
#Main functions of the Game

def roll_dice():
    """Rolls the dice, updates the dice image, and displays a message based on the result."""
    message_label.config(text="") #Clears any previous message
    dice_result = random.randint(1, 6) #Generates a random dice roll (1-6) 
    result_label.config(text=f"🎲 You rolled: {dice_result}", fg="black", bg="white") #Updates the label with the dice result, set text color to black, set background color of result label to white
    dice_image_label.config(image=dice_images[dice_result - 1]) #Changes the dice image to reflect the rolled value
    
    if dice_result == 5:
        message_label.config(text=f"🎉 Congratulations! You rolled a: {dice_result} Your guess was correct!")
        dice_image_label.config(image=dice_images[dice_result - 1])
    else:
        message_label.config(text=f"❌ Wrong guess! Try again. {dice_result}")


def check_guess():
    """Checks the user's guess and displays a message based on the result."""
    try:
        user_guess = int(guess_spinbox.get())  # Get user's guess from spinbox # Gets the user's guess from the spinbox
    except ValueError:
        message_label.config(text="❌ Please enter a valid number (1-6).")
        return
    
    if 1 <= user_guess <= 6:
        dice_result = random.randint(1, 6)
        result_label.config(text=f"🎲 The dice rolled: {dice_result}")
        dice_image_label.config(image=dice_images[dice_result - 1])
        
        if user_guess == dice_result:
            message_label.config(text="🎉 Correct! You guessed it right! 🎉")
        else:
            message_label.config(text="❌ Wrong guess! Try again.")
    else:
        message_label.config(text="❌ Please enter a number between 1 and 6.")

#Function used to open the URL for other dice games
def open_dice_games_url():
    """Opens an external URL to other dice games."""
    url = "https://www.playonlinedicegames.com/"
    webbrowser.open(url)

def clear_message_label(*args):
    """Clears the message label when the spinbox value changes."""
    message_label.config(text="")

#Setup of the GUI

#Creates the main window of the application
root = tk.Tk() #Initailizes the TKinter root window 
root.geometry("550x500") #Set the deimensions of the window (550x500 pixels)
root.title("🎲 Dice Rolling Game") #Names the title of the window

#Creates a canvas for the gradient background
canvas = tk.Canvas(root, width=550, height=500) #Creates a canvas with dimensions 550x500 pixels
canvas.pack(fill="both", expand=True) #Packs the canvas into the window, ensuring it expands to fill the window

#Gradient background (light pink to blue)
gradient_color1 = "#FFB6C1"  # Light pink
gradient_color2 = "#0000FF"  # Blue
create_gradient(canvas, 550, 500, gradient_color1, gradient_color2)

#Adds a label to display the dice roll result, without any background color 
result_label = tk.Label(root, text="🎲 Roll the dice!", font=("Helvetica", 20, "bold"), fg=gradient_color1, pady=10, bg="white")
result_label.place(relx=0.5, rely=0.15, anchor="center") #Places the label directly at the center horizontally (relx=.5) and slightly towards the top (rely=0.15) on the canvas

#Instructions for the guess section
canvas.create_text(270, 325, text="Guess the dice roll (1-6):", font=("Helvetica", 14), fill="black") 

#Spinbox for user's guess input
guess_spinbox_var = tk.StringVar() #String variable for spinbox
bg="#B19CD9", 
guess_spinbox = tk.Spinbox(root, from_=1,to=6,font=("Helvetica", 12),justify="center",textvariable=guess_spinbox_var, bg="#B19CD9",fg="black", bd=0, highlightthickness=0,width=3)
guess_spinbox.place(relx=0.4, rely=0.8, anchor="center") #Places the label directly at the center horizontally (relx=0.4) and near the bottom (rely=0.8) on the canvas
guess_spinbox_var.trace_add("write", clear_message_label)  #Clears message on change

#Guess button
guess_button = tk.Button(root, text="Guess", font=("Helvetica", 12), command=check_guess, bg="green", fg="white")
guess_button.place(relx=0.55, rely=0.8, anchor="center") #Places the label directly at the center horizontally (relx=0.55) and near the bottom (rely=0.8) on the canvas

#Message label for feedback
message_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
message_label.place(relx=0.5, rely=0.71, anchor="center") #Places the label directly at the center horizontally (relx=0.5) and slightly near the bottom (rely=0.71) on the canvas 

#Loads dice images from a specific directory where my dice images are stored
image_directory = r"C:\Users\kahil\UAT\CSC235 - Python Programming\Module 4\Assignment 4.1\images"
dice_images = [] #List to hold the dice images 
for i in range(1, 7): #For Loop through numbers 1 - 6 to load each dice image into the list
    image_path = os.path.join(image_directory, f"dice{i}.jpg") #Contains the full file path for each dice image
    image = Image.open(image_path).resize((100, 100), Image.Resampling.LANCZOS) #Opens and resizes the image to 100x100 pixels
    dice_images.append(ImageTk.PhotoImage(image)) #Converts the image to a format Tkinter can use and add it to the list

#Adds a label to display the dice image. The first dice image is the default image
dice_image_label = tk.Label(root, image=dice_images[0]) #Default image, initialized with the first dice image
dice_image_label.place(relx=0.5, rely=0.35, anchor="center") #Places the image label near the center of the window

#Adds a button to roll the dice. When button is clicked, it triggers the roll_dice function (button with its own background color)
roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 16), command=roll_dice, bg="blue", fg="light pink", padx=20)
#Sets the button's text, font, background color (bg), text color (fg), and padding around the text
roll_button.place(relx=0.5, rely=0.53, anchor="center") #Places the button at the center horizontally (relx=0.5) and near the bottom (rely=0.80)

#Adds a button to link to other dice games
link_button = tk.Button(root, text="Other Dice Games", font=("Arial", 16), command=open_dice_games_url, bg="light pink", fg="dark blue", padx=10)
#Sets the button's text, font, background color (bg), text color (fg), and padding around the text
link_button.place(relx=0.5, rely=0.90, anchor="center") #Places the button at the center horizontally (relx=0.5) and below the dice image(rely=0.90)

#Adds a button to quit the application
quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Helvetica", 12), bg="#8B0000", fg="white")
#Sets the button's text, font, background color (bg), text color (fg), and padding around the text
quit_button.place(relx=0.9, rely=0.55, anchor="ne") #Places the button just a bit under the dice image horizontally (relx=0.90) and off to the right-side of the window (rely=0.60)

#Starts the Tkinter event loop, waits for interactions from the user and runs the GUI application
root.mainloop() #Runs the application, which waits for user action, clicking the button


