MIN_WORD_LENGTH = 5  # Minimum length of the word to be guessed
MAX_WORD_LENGTH = 8  # Maximum length of the word to be guessed
MAX_WRONG_GUESSES = 7  # Maximum number of wrong guesses allowed

SNOWMAN_IMAGES = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \( : )/ *',
    '* (_ : _)  ',
    '-----------',
]

def snowman(snowman_word, guessed_letters=None):
    if guessed_letters is None:
        guessed_letters = []

    word_dict = build_word_dict(snowman_word)  # Build a dictionary to track guessed letters in the word
    word_guessed = is_word_guessed(snowman_word, word_dict)  # Check if the word has been completely guessed
    wrong_guesses = []  # List to store the wrong guesses
    guesses_left = MAX_WRONG_GUESSES  # Number of guesses remaining

    while len(wrong_guesses) < MAX_WRONG_GUESSES and not word_guessed:
        print_word_progress(snowman_word, word_dict)  # Print the word progress with guessed letters and blanks
        print_snowman_graphic(len(wrong_guesses))  # Print the snowman graphic based on the number of wrong guesses
        print(f"\nWrong guesses: {', '.join(wrong_guesses)} - {guesses_left} guesses left!\n")

        user_input = get_letter_from_user(word_dict, wrong_guesses)  # Get a letter input from the user

        if user_input in word_dict:  # If the letter is in the word
            print("\nYou guessed a letter that's in the word!\n")
            word_dict[user_input] = True  # Mark the letter as guessed in the word dictionary
        else:  # If the letter is not in the word
            print(f"\nThe letter {user_input} is not in the word\n")
            wrong_guesses.append(user_input)  # Add the letter to the list of wrong guesses
            guesses_left = MAX_WRONG_GUESSES - len(wrong_guesses)  # Update the number of guesses left

        word_guessed = is_word_guessed(snowman_word, word_dict)  # Check if the word has been completely guessed

    if len(wrong_guesses) == MAX_WRONG_GUESSES and not word_guessed:
        print(f"Sorry, you lose! The word was {snowman_word}")
    else:
        print("Congratulations, you win!")

    return {
        'word': snowman_word,
        'guessed_letters': guessed_letters,
        'wrong_guesses': wrong_guesses,
        'word_progress': get_word_progress(snowman_word, word_dict)
    }

def get_word_progress(snowman_word, word_dict):
    progress = ""
    for letter in snowman_word:
        if word_dict[letter]:
            progress += letter
        else:
            progress += "_"
    return progress

def print_snowman_graphic(num_wrong_guesses):
    for i in range(num_wrong_guesses):
        print(SNOWMAN_IMAGES[i])  # Print the corresponding line of the snowman image

def get_letter_from_user(word_dict, wrong_guesses_list):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in word_dict and word_dict[user_input_string]:
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in wrong_guesses_list:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string

def build_word_dict(snowman_word):
    word_dict = {}
    for letter in snowman_word:
        word_dict[letter] = False  # Initialize all letters in the word as not guessed
    return word_dict

def print_word_progress(snowman_word, word_dict):
    output_string = ""
    for elem in snowman_word:
        if word_dict[elem]:
            output_string += elem  # Append the guessed letter
        else:
            output_string += "_"  # Append a blank for letters not yet guessed
        output_string += " "  # Add a space between letters
    print(output_string)

def is_word_guessed(snowman_word, word_dict):
    for elem in snowman_word:
        if not word_dict[elem]:
            return False  # If any letter is not guessed, return False
    return True  # All letters are guessed, return True
