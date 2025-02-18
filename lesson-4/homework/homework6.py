# Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.

import random


def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
            (player == "scissors" and computer == "paper") or \
            (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"


def play_game():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("First to 5 points wins the match.")

    while player_score < 5 and computer_score < 5:
        player_choice = input("\nEnter rock, paper, or scissors: ").lower()

        if player_choice not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Com

