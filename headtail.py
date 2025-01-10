import random


def toss():
    print("It's time for the toss!")
    user_choice = input("Choose Heads or Tails (H/T): ").strip().upper()
    if user_choice not in ["H", "T"]:
        print("Invalid choice! Defaulting to Heads.")
        user_choice = "H"

    toss_result = random.choice(["H", "T"])
    print(f"Toss result: {'Heads' if toss_result == 'H' else 'Tails'}")

    if user_choice == toss_result:
        print("You won the toss!")
        decision = input("Do you want to Bat or Bowl first? (Bat/Bowl): ").strip().lower()
        if decision == "bowl":
            return "computer"
        return "user"
    else:
        print("Computer won the toss and chooses to bat first!")
        return "computer"


def user_turn():
    user_run = 0
    wickets = 3
    while wickets > 0:
        print(f"Your total runs: {user_run}")
        user_hit = int(input("Take runs between 1-12: "))
        if user_hit < 1 or user_hit > 12:
            print("Invalid input! Please choose a number between 1 and 12.")
            continue

        computer_guess = random.randint(1, 12)
        print(f"Computer guessed: {computer_guess}")

        if user_hit == computer_guess:
            print("OUT!!!")
            wickets -= 1
            print(f"Remaining wickets: {wickets}")
        else:
            user_run += user_hit

    print(f"Your innings ends. Computer needs {user_run + 1} runs to win!")
    return user_run


def computer_turn(target):
    computer_run = 0
    wickets = 3
    while wickets > 0:
        if computer_run > target:
            print("Computer wins the game!")
            return True

        print(f"Computer's total runs: {computer_run}")
        computer_hit = random.randint(1, 12)
        print(f"Computer takes: {computer_hit} runs")

        user_guess = int(input("Guess the computer's shot (1-12): "))
        if user_guess < 1 or user_guess > 12:
            print("Invalid input! Please choose a number between 1 and 12.")
            continue

        if user_guess == computer_hit:
            print("OUT!!!")
            wickets -= 1
            print(f"Remaining wickets for computer: {wickets}")
        else:
            computer_run += computer_hit

    print(f"Computer's innings ends with {computer_run} runs.")
    return computer_run > target


def main():
    print("Welcome to HeadTail Cricket Game!")
    print(
        "Rules: Score runs by choosing a number between 1 and 12. If your number matches the opponent's guess, you're OUT!")
    print("Each player has 3 wickets.")

    toss_winner = toss()

    if toss_winner == "user":
        user_run = user_turn()
        target = user_run + 1
        print(f"Target for computer: {target} runs.")

        if computer_turn(target):
            print("Computer wins the match!")
        else:
            print("You win the match!")
    else:
        computer_run = computer_turn(float('inf'))
        target = computer_run + 1
        print(f"Target for you: {target} runs.")

        user_run = user_turn()
        if user_run >= target:
            print("You win the match!")
        else:
            print("Computer wins the match!")


if __name__ == "__main__":
    main()