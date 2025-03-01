import random

def guess():
    x = 100 #Fixed max number
    randomNum = random.randint(1, x)
    user_guess = 0
    while user_guess != randomNum:
        try:
            user_guess = int(input(f'Guess a number between 1 and {x}: '))
            if user_guess < randomNum:
                print('Ooops! Too Low, guess again >.<')
            elif user_guess > randomNum:
                print('Oh no! Too High! Try again')
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f'Yay, congrats! You have guessed the number {randomNum} correctly! <3')

def comp_guess():
    x = 100 # Fixed max number
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # when low = high

        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer guessed your number, {guess}, correctly!')

def main():
    while True:
        print("\nChoose a guessing game:")
        print("1. You guess the number")
        print("2. Computer guesses your number")
        print("3. Exit")

        gameChoice = input("Enter Your Choice: ")

        if gameChoice == '1':
            guess()
        elif gameChoice == '2':
            comp_guess()
        elif gameChoice == '3':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the menu
main()
