import random
uname = input("Hello, what is your name?")
print("Hello,"+ uname,)
while True:
    question = input("Whould you like to play a game? [Y,N]")
    number = random.randint(1,100)
    if question =='n':
        print("ohh..ok!")
        break
    if question =='y':
        print("I'm thinking a number from 1 to 100")
        while True:
            guess = int(input("have a guess!"))
            if guess < number:
                print("guess higher!")            
            if guess > number:
                print("guess lower")
                continue                
            elif guess==number:
                print("Bingo!")
                break
            
        