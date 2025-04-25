import random
from tkinter import *
import pygame.mixer

# Initialize window
root = Tk()
root.title("ROCK, PAPER, SCISSOR GAME")
width = 800
height = 650
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

# Game record
player_wins = 0
computer_wins = 0
ties = 0

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
    global player_wins, computer_wins, ties
    if player_option == 1:
        Label_Status.config(text="Game Tie")
        tie_sound.play()
        ties += 1
    elif player_option == 2:
        Label_Status.config(text="Player Win")
        win_sound.play()
        player_wins += 1
    elif player_option == 3:
        Label_Status.config(text="Computer Win")
        lose_sound.play()
        computer_wins += 1
    update_record()

def Comp_Paper():
    global player_wins, computer_wins, ties
    if player_option == 1:
        Label_Status.config(text="Computer Win")
        lose_sound.play()
        computer_wins += 1
    elif player_option == 2:
        Label_Status.config(text="Game Tie")
        tie_sound.play()
        ties += 1
    elif player_option == 3:
        Label_Status.config(text="Player Win")
        win_sound.play()
        player_wins += 1
    update_record()

def Comp_Scissor():
    global player_wins, computer_wins, ties
    if player_option == 1:
        Label_Status.config(text="Player Win")
        win_sound.play()
        player_wins += 1
    elif player_option == 2:
        Label_Status.config(text="Computer Win")
        lose_sound.play()
        computer_wins += 1
    elif player_option == 3:
        Label_Status.config(text="Game Tie")
        tie_sound.play()
        ties += 1
    update_record()

# Function for simulating a greedy approach
def Greedy():
    # Perform Monte Carlo simulations to determine the computer's move
    win_counts = {1: 0, 2: 0, 3: 0}  # Initialize win counts for each move
    total_simulations = 1000  # Number of simulations

    for _ in range(total_simulations):
        # Simulate random moves for both player and computer
        player_move = random.randint(1, 3)
        computer_move = random.randint(1, 3)

        # Determine the winner
        if player_move == computer_move:
            continue  # Tie
        elif (player_move % 3) + 1 == computer_move:
            win_counts[computer_move] += 1  # Computer wins
        else:
            win_counts[player_move] += 1  # Player wins

    # Choose the move with the highest win count (greedy approach)
    computer_move = max(win_counts, key=win_counts.get)
    return computer_move

# Function for matching
def Matching():
    computer_option = Greedy()  # Use the greedy function to determine computer's move
    if computer_option == 1:
        Image_Computer.configure(image=Computer_Rock)
        Comp_Rock()
    elif computer_option == 2:
        Image_Computer.configure(image=Computer_Paper)
        Comp_Paper()
    elif computer_option == 3:
        Image_Computer.configure(image=Computer_Scissor)
        Comp_Scissor()

# Function to update the game record
current_match = 0
match_limit = 0

def update_record():
    global current_match
    current_match += 1
    record_label.config(text=f"Player: {player_wins} | Computer: {computer_wins} | Ties: {ties} | Current Match: {current_match}/{match_limit}")

    if current_match == match_limit:
        if player_wins > computer_wins:
            Label_Status.config(text="Player is the overall winner!")
        elif computer_wins > player_wins:
            Label_Status.config(text="Computer is the overall winner!")
        else:
            Label_Status.config(text="It's a tie!")
        rock.config(state=DISABLED)
        paper.config(state=DISABLED)
        scissor.config(state=DISABLED)

# Get the match limit from the user
def set_match_limit():
    global match_limit
    match_limit = int(entry_match_limit.get())
    entry_match_limit.config(state=DISABLED)
    start_button.config(state=DISABLED)
    update_record()

# GUI Elements
Label_Status = Label(root, text="", font=('arial', 20), bg="#e3f4f1")
Label_Status.pack()

Image_Player = Label(root, image=Blank_img, bg="#e3f4f1")
Image_Player.pack(side=LEFT, padx=50, pady=20)

Image_Computer = Label(root, image=Blank_img, bg="#e3f4f1")
Image_Computer.pack(side=RIGHT, padx=50, pady=20)

frame_buttons = Frame(root, bg="#e3f4f1")
frame_buttons.pack()

rock = Button(frame_buttons, image=Player_Rock_ado, command=Rock, bg="#e3f4f1")
rock.grid(row=0, column=0, padx=10, pady=10)

paper = Button(frame_buttons, image=Player_Paper_ado, command=Paper, bg="#e3f4f1")
paper.grid(row=0, column=1, padx=10, pady=10)

scissor = Button(frame_buttons, image=Player_Scissor_ado, command=Scissor, bg="#e3f4f1")
scissor.grid(row=0, column=2, padx=10, pady=10)

record_label = Label(root, text=f"Player: {player_wins} | Computer: {computer_wins} | Ties: {ties} | Current Match: {current_match}/{match_limit}", font=('arial', 14), bg="#e3f4f1")
record_label.pack(pady=20)

entry_match_limit = Entry(root, font=('arial', 14))
entry_match_limit.pack()

start_button = Button(root, text="Start Game", command=set_match_limit, font=('arial', 14), bg="#e3f4f1")
start_button.pack(pady=10)

root.mainloop()
