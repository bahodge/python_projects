import random


def random_number_generator(low_number, high_number):
    return random.randint(low_number, high_number)


def input_low_number():
    return int(input("Please Select a Low Number"))


def input_high_number():
    return int(input("Please Select a High Number"))


def start_game():
    response = input("Would You Like to Play?")
    response = response.lower()
    if response == "y" or response == "yes":
        return True
    else:
        return False


def generate_secret_number(low, high):
    return random_number_generator(low, high)


def end_game(secret, guess_count):
    print(f"{secret} was guess in {guess_count}")
    return


def play_game():
    guess_count = 0
    while start_game():
        floor = input_low_number()
        ceiling = input_high_number()
        secret_number = generate_secret_number(floor, ceiling)
        guess = random_number_generator(floor, ceiling)
        while guess != secret_number:
            guess_count += 1
            if guess < secret_number:
                print(f"Guess: {guess} - Higher")
                floor = guess
                guess = int((floor + ceiling) / 2)
            elif guess > secret_number:
                print(f"Guess: {guess} - Lower")
                ceiling = guess
                guess = int((ceiling + floor) / 2)
        print(f"Secret Number - {secret_number}")
        print(f"Guess Secret Number in: {guess_count} guesses")
    print("Buh Bye!")


play_game()
