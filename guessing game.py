import random


def main():
    print("WELCOME TO THE GUESSING GAME!")

    play = True
    play_two = True

    while play:
        user_num3 = input("Do you want to play single Player or 2 Players (1/2): ")
        if user_num3 == 1:
            print("1 - Easy(10) 2 - Medium(20) 3 - Hard(100)")
            user_num2 = int(raw_input("Choose what level you want to play:"))
            if user_num2 == 1:
                random_num = random.randrange(1, 11)
                user_num = int(raw_input("Try to guess the number between 1 - 10:"))
                while user_num != random_num:
                    if user_num < random_num:
                        user_num = int(raw_input("Higher:"))
                    elif user_num > random_num:
                        user_num = int(raw_input("Lower:"))
                print("Great job! You got it! It was:", random_num)

            elif user_num2 == 2:
                random_num = random.randrange(1, 21)
                user_num = input("Try to guess the number between 1 - 20:")
                while user_num != random_num:
                    if user_num < random_num:
                        user_num = int(raw_input("Higher:"))
                    elif user_num > random_num:
                        user_num = int(raw_input("Lower:"))
                print("Great job! You got it! It was:", random_num)

            elif user_num2 == 3:
                random_num = random.randrange(1, 101)
                user_num = input("Try to guess the number between 1 - 100:")
                while user_num != random_num:
                    if user_num < random_num:
                        user_num = int(raw_input("Higher:"))
                    elif user_num > random_num:
                        user_num = int(raw_input("Lower:"))
                print("Great job! You got it! It was:", random_num)

            print("Would you like to play again?(Y/N)")
            choice = raw_input("Please enter your choice:")
            if choice == 'N':
                play = False

        elif user_num3 == 2:
            guess_one = 0
            guess_two = 0
            print("1 - Easy(10) Whoever reaches over 10 guesses loses / 2 - Medium(20) Whoever reaches over 15 guesses loses / Whoever reaches over 30 guesses loses 3 - Hard(100)")
            user_num2 = int(raw_input("Choose what level you want to play:"))
            if user_num2 == 1:
                random_num = random.randrange(1, 11)
                user_num = int(raw_input("Player 1, try to guess the number between 1 - 10:"))
                guess_one += 1
                while user_num != random_num:
                    if user_num < random_num:
                        user_num = int(raw_input("Higher:"))
                        guess_one += 1
                    elif user_num > random_num:
                        user_num = int(raw_input("Lower:"))
                        guess_one += 1
                print("Great job! You got it! It was:", random_num)
                print(guess_one)

                random_num = random.randrange(1, 11)
                user_num = int(raw_input("Player 2, try to guess the number between 1 - 10:"))
                guess_two += 1
                while user_num != random_num:
                    if user_num < random_num:
                        user_num = int(raw_input("Higher:"))
                        guess_two += 1
                    elif user_num > random_num:
                        user_num = int(raw_input("Lower:"))
                        guess_two += 1
                print("Great job! You got it! It was:", random_num)
                print(guess_two)


            elif user_num2 == 2:
                random_num = random.randrange(1, 21)
                user_num = input("Player 1, try to guess the number between 1 - 20:")
                guess_one += 1
                while user_num != random_num:
                    if user_num < random_num:
                        user_num = int(raw_input("Higher:"))
                        guess_one += 1
                    elif user_num > random_num:
                        user_num = int(raw_input("Lower:"))
                        guess_one += 1
                print("Great job! You got it! It was:", random_num)

                random_num = random.randrange(1, 21)
                user_num = int(raw_input("Player 2, try to guess the number between 1 - 20:"))
                guess_two += 1
                while user_num != random_num:
                    if user_num < random_num:
                        user_num = int(raw_input("Higher:"))
                        guess_two += 1
                    elif user_num > random_num:
                        user_num = int(raw_input("Lower:"))
                        guess_two += 1
                print("Great job! You got it! It was:", random_num)

            elif user_num2 == 3:
                random_num = random.randrange(1, 101)
                user_num = input("Player 1, try to guess the number between 1 - 100:")
      4          guess_one += 1
                while user_num != random_num:
                    if user_num < random_num:
                        user_num = int(raw_input("Higher:"))
                        guess_one += 1
                    elif user_num > random_num:
                        user_num = int(raw_input("Lower:"))
                        guess_one += 1
                print("Great job! You got it! It was:", random_num)

                random_num = random.randrange(1, 101)
                user_num = int(raw_input("Player 2, try to guess the number between 1 - 100:"))
                guess_two += 1
                while user_num != random_num:
                    if user_num < random_num:
                        user_num = int(raw_input("Higher:"))
                        guess_two += 1
                    elif user_num > random_num:
                        user_num = int(raw_input("Lower:"))
                        guess_two += 1
                print("Great job! You got it! It was:", random_num)

            if guess_one >= 10 and guess_one > guess_two:
                print("Player 1 used:", guess_one, "guesses")
                print("Player 2 used", guess_two, "guesses")
                print("Player 2 is the winner!.")
                play = False

            elif guess_two >= 10 and guess_one < guess_two:
                print("Player 1 used:", guess_one, "guesses")
                print("Player 2 used", guess_two, "guesses")
                print("Player 1 is the winner!")
                play = False


                print("Would you like to play again?(Y/N)")
                choice = raw_input("Please enter your choice:")
                if choice == 'N':
                    play = False
main()