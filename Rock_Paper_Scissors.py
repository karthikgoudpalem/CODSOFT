import random

def user_choice():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    play_again = True

    while play_again:
        print("\n--- New Round ---")
        user__choice = user_choice()
        computer__choice = computer_choice()
        print(f"You chose: {user__choice}")
        print(f"Computer chose: {computer__choice}")
        result = winner(user__choice, computer__choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'

    print("\n--- Final Scores ---")
    print(f"Your final score: {user_score}")
    print(f"Computer's final score: {computer_score}")

if __name__ == "__main__":
    play_game()
