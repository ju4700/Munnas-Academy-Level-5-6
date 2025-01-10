import random

print("Welcome!")

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    user_point = 0
    computer_point = 0
    turn = 3

    while turn > 0:
        computer_choice = random.choice(options)
        print("Guess Rock, Paper or Scissors")
        user_input = input("Enter your choice: ")
        print("Computer choice: ", computer_choice)
        if user_input == computer_choice:
            print("It's a tie!")
            continue
        elif user_input == "rock" and computer_choice == "scissors":
            print("You win!")
            user_point += 1
        elif user_input == "paper" and computer_choice == "rock":
            print("You win!")
            user_point += 1
        elif user_input == "scissors" and computer_choice == "paper":
            print("You win!")
            user_point += 1
        elif user_input == "rock" and computer_choice == "paper":
            print("Computer Won!")
            computer_point += 1
        elif user_input == "paper" and computer_choice == "scissors":
            print("Computer Won!")
            computer_point += 1
        elif user_input == "scissors" and computer_choice == "rock":
            print("Computer Won!")
            computer_point += 1
        turn -= 1

    if user_point >= 2:
        print(f"You win! Your Points: {user_point}")
    elif computer_point >= 2:
        print(f"Computer Won! Computer Points {computer_point}")
    else:
        print("Draw")

def main():



if __name__ == "__main__":
    main()

