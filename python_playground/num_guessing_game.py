import random
from time import sleep

print("\n" + "-"*40)
print("Welcome to the Number Guessing Game!")
print("-"*40)

#game function
def guess_game(random_number, min_value, max_value):
    tries_counter = 0
    while True:
        guess = get_valid_input("What is your guess?: ", min_value, max_value)
        last_guess = guess
        tries_counter += 1
        if guess == random_number:
            print("Congratulations")
            print(random.choice(quotes))
            print(f"You guessed it with: {tries_counter} tries.")
            print("Going back to Main Menu")
            sleep(2)
            break
        else:
            print("Nope, Try again.")
        hints(tries_counter, random_number, min_value, max_value, last_guess)

#difficulties 
def difficulties(inp):
    match inp:
        case "1":
            print("\nThinking of a number between 1-10")
            return random.randint(1, 10), 1, 10
        case "2":
            print("\nThinking of a number between 1-25")
            return random.randint(1, 25), 1, 25
        case "3":
            print("\nThinking of a number between 1-50")
            return random.randint(1, 50), 1, 50
        case "4":
            print("\nThinking of a number between 1-100")
            return random.randint(1, 100), 1, 100
        case "5":
            min_range = get_valid_input("Enter the minimum number for the range: ", 1, 1000)
            max_range = get_valid_input("Enter the maximum number for the range: " , 1, 10000)
            if min_range < max_range:
                print(f"\nThinking of a number between {min_range}-{max_range}")
                return random.randint(min_range, max_range), min_range, max_range
            else:
                print("Minimum value must be less than the maximum value. Please try again.")
        case _:
            raise ValueError("Invalid difficulty level. Please choose a number between 1-4.")


#checks validation of user input
def get_valid_input(prompt, min_value, max_value):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            num = int(user_input)
            if min_value <= num <= max_value:
                return num
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        else:
            print("Invalid input. Please enter a valid number.") 

#hint function
def hints(tries, random_number, min_value, max_value, last_guess):
    if tries % 3 == 0:
        if random_number % 2 == 0:
            print("\nHint: The number is even.")
        else:
            print("\nHint: The number is odd.")
    elif tries % 5 == 0:
        if random_number % 3 == 0:
            print("\nHint: The number is divisible by 3.")
        elif random_number % 5 == 0:
            print("\nHint: The number is divisible by 5.")
        else:
            print("\nHint: The number is not divisible by 3 or 5.")
    elif tries % 7 == 0:
        midpoint = (min_value + max_value) // 2
        if random_number > midpoint:
            print(f"Hint: The number is greater than {midpoint}.")
        else:
            print(f"Hint: The number is less than or equal to {midpoint}.")
 

def menu():
    while True:
        print("\nMain Menu")
        print("1: Easy")
        print("2: Normal")
        print("3: Hard")
        print("4: Professional")
        print("5: Costum challenge")
        print("6: Quit")
        user_choice = get_valid_input("Choose a difficulty level (1-5, choose 6 to quit): ", 1, 6)
        if user_choice == 6:
            print("Thanks for playing the game!")
            break
        else:
            try:
                random_num, min_val, max_val = difficulties(str(user_choice))
                guess_game(random_num, min_val, max_val)
            except ValueError as e:
                print("There was an error processing the game difficulty", e)

quotes = [
    "Amazing! You’ve got the magic touch!",
    "Wow, you nailed it!",
    "Sharp mind! Impressive guess!",
    "Legendary guessing skills!",
    "Fantastic! You’re unstoppable!",
    "Brilliant! You cracked the code!",
    "Exceptional! You’re a natural!",
    "Hats off! You’re a true guesser!",
    "You’ve got the number wizardry!",
    "Phenomenal! You’re a star!",
    "Astonishing guess! Well done!",
    "Spectacular! You’re a pro!",
    "Superb! That’s some talent!"
]


menu()


