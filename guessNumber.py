import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if (userGuess == randNumber):
        print("You guessed it right! ")
    else:
        if(userGuess>randNumber):
            print("you guessed it wrong! Enter a smaller number")
        else:
            print("you guessed it wrong! Enter a larger number")
print(f"you guessed the number in {guesses} guesses") 
with open("G:\\python\\highscore.txt","r") as f:
    highscore = int(f.read())

if(guesses<highscore):
    print("you have just broken the high score!")
    with open("G:\\python\\highscore.txt","w") as f:
        f.write(str(guesses))

