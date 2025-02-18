import random
num = random.randint(1, 100)

def guesser(num):
    counter = 10
    while counter > 0:
        guess = int(input("Enter your guess: "))
        if guess > num:
            print("Too high")
            counter -= 1
        elif guess < num:
            print("Too low")
            counter -= 1
        elif guess == num:
            print("You guessed it right!")
            break
        else:
            print("you lost!")



guesser(num)
again = input("Want to play again? ")

if again =='Y' or again == 'YES' or again =='y' or again == 'yes' or again == 'ok':
    num = random.randint(1, 100)
    guesser(num)




