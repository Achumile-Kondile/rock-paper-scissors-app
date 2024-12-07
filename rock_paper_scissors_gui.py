import pygame
import tkinter as tk
import random
import os

def load_sound(file_name):
    if os.path.exists(file_name):
        return pygame.mixer.Sound(file_name)
    else:
        print(f"Warning: {file_name} not found.")
        return None

# Initialize pygame mixer for sound effects
pygame.mixer.init()

# Load sound effects
rock_sound = load_sound("rock.wav")
paper_sound = load_sound("paper.wav")
scissors_sound = load_sound("scissors.wav")
win_sound = load_sound("win.wav")
lose_sound = load_sound("lose.wav")
tie_sound = load_sound("tie.wav")

# Initialize the window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Initialize scores
user_score = 0
computer_score = 0
ties = 0

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score, ties
    if user_choice == computer_choice:
        ties += 1
        result = "It's a tie!"
        if tie_sound: tie_sound.play()  # Play tie sound if available
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        user_score += 1
        result = "You win!"
        if win_sound: win_sound.play()  # Play win sound if available
    else:
        computer_score += 1
        result = "You lose!"
        if lose_sound: lose_sound.play()  # Play lose sound if available

    # Update score display
    score_label.config(text=f"Score: You {user_score} - Computer {computer_score} | Ties: {ties}")
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

def user_choice(choice):
    computer_choice = get_computer_choice()
    if choice == 'rock' and rock_sound: rock_sound.play()  # Play rock sound if available
    elif choice == 'paper' and paper_sound: paper_sound.play()  # Play paper sound if available
    elif choice == 'scissors' and scissors_sound: scissors_sound.play()  # Play scissors sound if available
    determine_winner(choice, computer_choice)

def restart_game():
    global user_score, computer_score, ties
    user_score = 0
    computer_score = 0
    ties = 0
    score_label.config(text=f"Score: You {user_score} - Computer {computer_score} | Ties: {ties}")
    result_label.config(text="Choose your move!")

# Create GUI elements
score_label = tk.Label(window, text=f"Score: You {user_score} - Computer {computer_score} | Ties: {ties}",
                       font=('Arial', 16), bg='lightblue', width=40, height=2)
score_label.pack(pady=10)

result_label = tk.Label(window, text="Choose your move!", font=('Arial', 14), bg='lightgreen', width=40, height=3)
result_label.pack(pady=10)

rock_button = tk.Button(window, text="Rock", width=20, height=2, font=('Arial', 14), bg='lightcoral',
                        command=lambda: user_choice('rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", width=20, height=2, font=('Arial', 14), bg='lightgreen',
                         command=lambda: user_choice('paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", width=20, height=2, font=('Arial', 14), bg='lightyellow',
                            command=lambda: user_choice('scissors'))
scissors_button.pack(pady=5)

restart_button = tk.Button(window, text="Restart Game", width=20, height=2, font=('Arial', 14), bg='lightblue',
                           command=restart_game)
restart_button.pack(pady=10)

window.mainloop()
