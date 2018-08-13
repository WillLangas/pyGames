import random

guessesTaken = 0
print("Hello, what is your name?")
name = input()

number = random.randint(1,30) #generates number 1-30, range can be changed

print("Nice to meet you " + name + ", I am thinking of a number 1 to 30")

def playGame():
    guessesTaken = 0 #keeps track of guesses used
    guessMax = 10 #maximum amount of guesses that can be used

    for i in range(guessMax):
        print("Take a guess")
        guess = int(input()) 

        if guess < number:
            print("Your guess is too low")
            guessesTaken = guessesTaken + 1
        elif guess > number:
            print("Your guess is too high")
            guessesTaken = guessesTaken + 1
        elif guess == number:
            print("You ran out of tries!")
            break
 
    if guess == number: #if correct
        guessesTaken = str(guessesTaken + 1) 
        print("Good job " + name + ". You guessed my number in " + guessesTaken + " tries")

    print("Would you like to play again")
    playAgain = input().lower() 

    if playAgain == 'yes':
        print("I am thinking of a number 1 to 30")
        playGame()
    else:
        print("Thanks for playing!")

playGame() #runs game
