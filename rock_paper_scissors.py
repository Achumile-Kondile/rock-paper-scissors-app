import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    # Ensure valid input from user
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice, please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    # Initialize scores
    user_score = 0
    computer_score = 0
    ties = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    
    # Main game loop
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Update scores based on result
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        else:
            ties += 1
        
        # Show current score
        print(f"Score: You {user_score} - Computer {computer_score} | Ties: {ties}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
