import random

def guess_number():
    while True:  # Loop to restart the game if user chooses to play again
        number_to_guess = random.randint(1, 100)
        guess = None
        attempts = 0

        print("\nWelcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")

        while guess != number_to_guess:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a number!")
                continue  # Skip this iteration if input is not a number

            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break  # Exit the loop and end the game

if __name__ == "__main__":
    guess_number()
