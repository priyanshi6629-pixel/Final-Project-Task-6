import random
print("Number Guessing Game")
print("Welcome to the Game!")
print("I have selected a number between 1 and 100.")
print("Can you Guess it?")
secret_number=random.randint(1,100)
attempts=0
max_attempts=7
while attempts<max_attempts:
    guess=int(input("\nEnter your Guess:"))
    attempts+=1
    if guess==secret_number:
        print("Congrats!You Guessed The Number")
        break
    elif guess<secret_number:
        print("Too Low! Try a higher Number")      
    else:
        print("Too High! Try a Lower Number")
    print("attempts Remaining:",max_attempts-attempts)    
else:
    print("\n Game Over!")   
    print("The Correct Number was:",secret_number) 
print("\n Thank You For Playing!")