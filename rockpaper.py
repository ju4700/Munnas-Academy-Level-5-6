import random

def rockpapers():
    options = ['rock', 'paper', 'scissors']
    turns = 3

    computer_point = 0
    user_point = 0
    while turns > 0:
        computer_choice = random.choice(options)
        user_choice = input("Choose rock, paper, or scissors: ")
        print("Computer's choice: ", computer_choice)

        if user_point > computer_point:
            print("You have won!")
        if user_choice == computer_choice:
            continue

        if user_choice == 'rock':
            if computer_choice == 'scissors':
                user_point += 1
            if computer_choice == 'paper':
                computer_point += 1

        elif user_choice == 'paper':
            if computer_choice == 'scissors':
                computer_point += 1
            if computer_choice == 'rock':
                user_point += 1

        elif user_choice == 'scissors':
            if computer_choice == 'rock':
                computer_point += 1
            if computer_choice == 'paper':
                user_point += 1


def main():
    print("Do you want to play Rock! Paper! Scissors!")
    user = input("Yes or No: ")
    if user == 'yes':
        rockpapers()
    else:
        print("Later!!!")


if __name__ == '__main__':
    main()
