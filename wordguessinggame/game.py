name = input("What is your name player1 ? ")
name2= input("What is your name player2 ? ")

# print(name,name1, "play hangman!")
print(f"HEY {name} and {name2} !!! LET'S PLAY HANGMAN ")

word = input(name2," enter the word: ")
print(name, "you have 10 guesses\n")

print("---guess the characters---")

guesses = ''

turns = 10

while turns > 0:

    failed = 0
    for char in word:

        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print(f"{name} YOU WON !! , LET {name2} HAVE A CHANCE")
        break

    guess = input("guess a character: ")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Failed attempt")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print(f" {name} You Loose !! , {name2} can have a chance!!!")

