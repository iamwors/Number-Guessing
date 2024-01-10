import random

def main() -> None:
    NUMBER = int(random.randint(0,100))
    CHANCES = 7
    Count = 0 
    
    print("\n\tGuess the number between 0 to 100 . You have 7 chances.\n\tGood Luck!.")
    
    while Count < CHANCES:
        guess = int(input(f"\nLIFE [{"💖 "*(CHANCES - Count)}{"❌ "*Count}] Guess the Number : "))
        Count += 1
        
        if guess > NUMBER:
            print("Your guess is too high.")
        elif guess < NUMBER:
            print("Your guess is too small.")
        else:
            return print("Your guess is correct.\n\tYOU WIN!")
    
    print("GAME OVER")


if __name__ == "__main__":
    main()
