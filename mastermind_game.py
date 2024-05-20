def get_hidden_number():
    while True:
        number = input("Enter a multi-digit number for the opponent to guess: ")
        if number.isdigit() and len(number) > 1:
            return number
        else:
            print("Invalid input. Please enter a multi-digit number.")

def get_guess():
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit() and len(guess) > 1:
            return guess
        else:
            print("Invalid guess. Please enter a multi-digit number.")

def provide_hint(hidden_number, guess):
    hint = []
    for h_digit, g_digit in zip(hidden_number, guess):
        if h_digit == g_digit:
            hint.append(h_digit)
        else:
            hint.append('_')
    return ''.join(hint)

def play_round(player_name, hidden_number):
    attempts = 0
    while True:
        guess = get_guess()
        attempts += 1
        if guess == hidden_number:
            print(f"Congratulations {player_name}! You guessed the number in {attempts} attempts.")
            return attempts
        else:
            hint = provide_hint(hidden_number, guess)
            print(f"Hint: {hint}")

def main():
    print("Welcome to the Mastermind game!")
    
    # Player 1 sets the number and Player 2 guesses
    print("\nPlayer 1, set the number for Player 2 to guess.")
    player1_number = get_hidden_number()
    
    print("\nPlayer 2, it's your turn to guess.")
    player2_attempts = play_round("Player 2", player1_number)
    
    # Player 2 sets the number and Player 1 guesses
    print("\nPlayer 2, set the number for Player 1 to guess.")
    player2_number = get_hidden_number()
    
    print("\nPlayer 1, it's your turn to guess.")
    player1_attempts = play_round("Player 1", player2_number)
    
    # Determine the winner
    if player1_attempts < player2_attempts:
        print("\nPlayer 1 wins the game and is crowned Mastermind!")
    elif player2_attempts < player1_attempts:
        print("\nPlayer 2 wins the game and is crowned Mastermind!")
    else:
        print("\nIt's a tie!")

if __name__ == "__main__":
    main()
