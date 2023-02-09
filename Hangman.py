
# Generates a new word at the start of the program and when the player chooses to try again.
def new_word():
    import random
    words = ['dog', 'cat', 'book', 'car', 'pen', 'table', 'chair', 'house', 'computer', 'phone', 
             'television', 'watch', 'clock', 'flower', 'tree', 'plant', 'water', 'coffee', 'food', 'sun', 
             'moon', 'sky', 'cloud', 'rain', 'snow', 'wind', 'ocean', 'mountain', 'hill', 'valley']
 
    listed_word = []
    selected_word = random.choice(words).lower()
    word_len = '_' * len(selected_word)
    for i in word_len:
        listed_word.append(i)
    print(f'\033[36mYour word has {len(selected_word)} letters \033[m')
    return listed_word, selected_word, word_len

# Checks if the user guessed the word correctly or if the letter is in the selected_word
def guess_word(word, guess):
    global listed_word

    if word == guess:
        print(f'\033[32mYou won!, you guessed correctly the word {word.upper()}!\033[m')
        listed_word = word.upper()
        global win 
        print(win)
        return True
    else:
        if guess in word:
            for i, w in enumerate(word):
                if guess == w:
                    print(f"There's the letter {guess.upper()} in the position {i+1}!")

                    listed_word.insert(i, w)
                    listed_word.pop(i+1)
        else:
            if len(guess) > 1:
                print(f"\033[31m{guess.upper()} isn't the correct word!\033[m")
            else:
                print(f"\033[31mThe letter {guess.upper()} isn't in the word!\033[m")

# Checks if the 'revealed word' is the same as shown on the screen, return True if it is.
def word_check(w1, w2):
    word2 = []
    for i in w2:
        word2.append(i)
    if w1 == word2:
        print(f'\033[32mYou won! The word was {selected_word.upper()}\033[m')
        return True
    else:
        return False

# Asks the player if he wants to play again, returns True if so.
def play_again():
    while True:
        p_a = input('\033[37mDo you want to play again? Y/N: \033[m')
        if p_a not in 'YyNn':
            print('\033[31mPlease type Y or N\033[m')
            continue
        if p_a in 'Yy':
            return True
        else:
            return False

# Asks the player on what difficulty he wants to play
def difficulty():
    while True:
        difficulty = input('\033[32mWhich difficulty you want to play? [E]asy / [M]edium / [H]ard: \033[m')[0]
        if difficulty not in 'EeMmHh':
                print('\033[31mPlease type [E]asy, [M]edium or [H]ard\033[m')
        else:

            return difficulty

# Calls the difficulty def and assigns it to chances, then checks what value chances received
def tries():
    chances = difficulty()
    if chances in 'Hh':
        tries = 5
    elif chances in 'Mm':
        tries = 10
    elif chances in 'Ee':
        tries = 15
    return tries

# Prints the name of the game
print('\033[33m----Hangman----\033[m')

# Game loop
while True:
    win = False
    chances = tries() + 1
    listed_word, selected_word, word_len = new_word()
    while win is False:
        chances -= 1
        print(f'\033[34mYou have {chances} chances remaning\033[m')
        print()
        print(guessed_word := ''.join(listed_word).center(30).upper())
        print()
        if chances == 0:
            print(f'\033[31mYou lost! The word was {selected_word.upper()}')
            break
        win = guess_word(selected_word.lower(), input('\033[35mType a letter or the correct word: \033[m').lower())
        if win:
            break
        win = word_check(listed_word, selected_word)
    print(guessed_word := ''.join(listed_word).center(30).upper())

    # Calls the fuction play_again to check if the player wants to play again
    p_again = play_again()
    print()
    if not p_again:
        break
    else:
        win = False
print('\033[36mSee you next time.')
