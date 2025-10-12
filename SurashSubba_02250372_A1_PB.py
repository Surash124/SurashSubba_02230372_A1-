#Defining a func for guess number game
def guess_number_play():
    import random 
    correct_number = random.randint(1, 100) 
    guesses_taken = 0 
    print("The number I am thinking between 1 and 100 is...? Make a guess.write 'q' to quit")
    while True:
        try:
            guess_input = input("Guess the number: ")
            if guess_input.lower() in ( 'q' ):
                print("The correct guess was ",correct_number)
                return 
            guess = int(guess_input)
            if not (1 <= guess <= 100):
                print("Please guess a number between 1 and 100.")
                continue 
        except ValueError:
            print("Invalid input! Enter whole number or 'q' to quit.")
            continue 
        guesses_taken += 1
        if guess < correct_number:
            print("Too low!.Try Again")
        elif guess > correct_number:
            print("Too high! Try Again")
        else:
            print("Congrats  It was: ",correct_number)
            print(f"guesses made: {guesses_taken}")
            break 

def rock_paper_scissors_play():#random
    import random 
    choices = ['rock', 'paper','scissors']
    print("\nLet's see what you Got.Type rock, paper,or scissors, else 'q' to quit.")
    
    while True:
        User = input("Enter rock, paper, or scissors: ").lower()
        if User == 'q':
            print("Thanks for playing. TRY AGAIN SOMETIME!")
            break 
            
        if User not in choices:
            print("Invalid choice.Please choose rock, paper, or scissors.")
            continue 
            
        Bot = random.choice(choices)
        print("Bot:", Bot)

        #condition
        if User == Bot:
            print("It is a tie! Play again.")
            
        #User wins
        elif (User == 'rock' and Bot == 'scissors') or \
             (User == 'scissors' and Bot == 'paper') or \
             (User == 'paper' and Bot == 'rock'):
            
            print("Congrats. You won..Hurray")
            
        #user lose
        else:
            print("You lose.Try Again")


def display_menu():#Menu
    while True:
        print("\nSelect a Game (1-3):")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors Game")
        print("3. Exit program")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error:Please enter a number (0-6).")
            continue

        if choice == 1:
            guess_number_play()

        elif choice == 2:
            rock_paper_scissors_play()

        elif choice == 3:
            print("Exiting program")
            break
            
        else:
            print("Error choice. Please select a number between 0 and 6.")
display_menu()