import random

def player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors (or q to quit): ").strip().lower()
        if choice in ("q", "quit"):
            return None
        if choice in ("rock", "paper", "scissors"):
            return choice

def computer_choice():
    return random.choice(("rock", "paper", "scissors"))

def winner(player, computer):
    if player == computer:
        return "tie"
    if (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        return "player"
    return "computer"

def main():
    scores = {"player": 0, "computer": 0, "tie": 0}
    while True:
        player = player_choice()
        if player is None:
            break
        computer = computer_choice()
        result = winner(player, computer)
        print(f"You chose {player}, computer chose {computer}.")
        if result == "tie":
            scores["tie"] += 1
            print("It's a tie!")
        elif result == "player":
            scores["player"] += 1
            print("You win!")
        else:
            scores["computer"] += 1
            print("Computer wins!")
    print(f"Final scores -> You: {scores['player']} Computer: {scores['computer']} Ties: {scores['tie']}")

if __name__ == "__main__":
    main()
