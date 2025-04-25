import random
from tkinter import *
import pygame.mixer

# Initialize window
root = Tk()
root.title("ROCK, PAPER, SCISSOR GAME ")
width = 650
height = 580
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
x = (window_width / 2) - (width / 2)
y = (window_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#e3f4f1")

# Initialize pygame mixer
pygame.mixer.init()

# Load sound effects
win_sound = pygame.mixer.Sound(file=r"C:\Users\Asus\OneDrive\Documents\VSC\PYTHON\project_2\resources\Win.wav")
lose_sound = pygame.mixer.Sound(file=r"C:\Users\Asus\OneDrive\Documents\VSC\PYTHON\project_2\resources\Lose.wav")
tie_sound = pygame.mixer.Sound(file=r"C:\Users\Asus\OneDrive\Documents\VSC\PYTHON\project_2\resources\Draw.wav")


# Load images
Blank_img = PhotoImage(file=r"C:\Users\Asus\OneDrive\Documents\VSC\PYTHON\project_2\resources\blank.png")
Player_Rock = PhotoImage(file=r"C:\Users\Asus\OneDrive\Documents\VSC\PYTHON\project_2\resources\rock_computer.png")
Player_Paper = PhotoImage(file=r"C:\Users\Asus\OneDrive\Documents\VSC\PYTHON\project_2\resources\paper_player.png")
Player_Scissor = PhotoImage(file=r"C:\Users\Asus\OneDrive\Documents\VSC\PYTHON\project_2\resources\scissor_player.png")
Computer_Rock = PhotoImage(file=r"C:\Users\Asus\OneDrive\Documents\VSC\PYTHON\project_2\resources\rock_computer.png")
Computer_Paper = PhotoImage(file=r"C:\Users\Asus\OneDrive\Documents\VSC\PYTHON\project_2\resources\paper_computer.png")
Computer_Scissor = PhotoImage(file=r"C:\Users\Asus\OneDrive\Documents\VSC\PYTHON\project_2\resources\scissor_computer.png")

# Subsample images
Player_Rock_ado = Player_Rock.subsample(3, 3)
Player_Paper_ado = Player_Paper.subsample(3, 3)
Player_Scissor_ado = Player_Scissor.subsample(3, 3)
Computer_Rock_ado = Computer_Rock.subsample(3, 3)
Computer_Paper_ado = Computer_Paper.subsample(3, 3)
Computer_Scissor_ado = Computer_Scissor.subsample(3, 3)

# Function for making rock paper scissor
def Rock():
    global player_option
    player_option = 1
    Image_Player.configure(image=Player_Rock)
    Matching()

def Paper():
    global player_option
    player_option = 2
    Image_Player.configure(image=Player_Paper)
    Matching()

def Scissor():
    global player_option
    player_option = 3
    Image_Player.configure(image=Player_Scissor)
    Matching()

# Function for making rock paper scissor for computer
def Comp_Rock():
    if player_option == 1:
        Label_Status.config(text="Game Tie")
        tie_sound.play()
    elif player_option == 2:
        Label_Status.config(text="Player Win")
        win_sound.play()
    elif player_option == 3:
        Label_Status.config(text="Computer Win")
        lose_sound.play()

def Comp_Paper():
    if player_option == 1:
        Label_Status.config(text="Computer Win")
        lose_sound.play()
    elif player_option == 2:
        Label_Status.config(text="Game Tie")
        tie_sound.play()
    elif player_option == 3:
        Label_Status.config(text="Player Win")
        win_sound.play()

def Comp_Scissor():
    if player_option == 1:
        Label_Status.config(text="Player Win")
        win_sound.play()
    elif player_option == 2:
        Label_Status.config(text="Computer Win")
        lose_sound.play()
    elif player_option == 3:
        Label_Status.config(text="Game Tie")
        tie_sound.play()

# Function for Monte Carlo Tree Search (MCTS)
def MCTS():
    # Perform Monte Carlo simulations to determine the computer's move
    win_rates = {1: 0, 2: 0, 3: 0}  # Initialize win rates for each move
    total_simulations = 1000  # Number of simulations

    for _ in range(total_simulations):
        # Simulate random moves for both player and computer
        player_move = random.randint(1, 3)
        computer_move = random.randint(1, 3)

        # Determine the winner
        if player_move == computer_move:
            continue  # Tie
        elif (player_move % 3) + 1 == computer_move:
            win_rates[computer_move] += 1  # Computer wins
        else:
            win_rates[player_move] += 1  # Player wins

    # Choose the move with the highest win rate
    computer_move = max(win_rates, key=win_rates.get)
    return computer_move

# Function for matching
def Matching():
    computer_option = MCTS()  # Use MCTS to determine computer's move
    if computer_option == 1:
        Image_Computer.configure(image=Computer_Rock)
        Comp_Rock()
    elif computer_option == 2:
        Image_Computer.configure(image=Computer_Paper)
        Comp_Paper()
    elif computer_option == 3:
        Image_Computer.configure(image=Computer_Scissor)
        Comp_Scissor()

# Function to exit the game
def Exit():
    root.destroy()
    exit()

# GUI setup
Image_Player = Label(root, image=Blank_img)
Image_Computer = Label(root, image=Blank_img)
Label_Player = Label(root, text="PLAYER")
Label_Player.grid(row=1, column=1)
Label_Player.config(bg="#e8c1c7", fg="black", font=('Times New Roman', 18, 'bold'))
Label_Computer = Label(root, text="COMPUTER")
Label_Computer.grid(row=1, column=3)
Label_Computer.config(bg="#e8c1c7", fg="black", font=('Times New Roman', 18, 'bold'))
Label_Status = Label(root, text="", font=('Times New Roman', 12))
Label_Status.config(fg="black", font=('Times New Roman', 20, 'bold', 'italic'))
Image_Player.grid(row=2, column=1, padx=30, pady=20)
Image_Computer.grid(row=2, column=3, pady=20)
Label_Status.grid(row=3, column=2)

rock = Button(root, image=Player_Rock_ado, command=Rock)
paper = Button(root, image=Player_Paper_ado, command=Paper)
scissor = Button(root, image=Player_Scissor_ado, command=Scissor)
button_quit = Button(root, text="Quit", bg="red", fg="white", font=('Times New Roman', 25, 'bold'), command=Exit)
rock.grid(row=4, column=1, pady=30)
paper.grid(row=4, column=2, pady=30)
scissor.grid(row=4, column=3, pady=30)
button_quit.grid(row=5, column=2)

if __name__ == '__main__':
    root.mainloop()
