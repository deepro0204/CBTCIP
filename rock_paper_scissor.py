import random

def get_computer_choice():
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissor): ").lower()
    while user_choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice. Please choose again.")
        user_choice = input("Enter your choice (rock, paper, scissor): ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
