import random

hang_man_score = {'Wins': 0, 'Losses': 0, 'Games Played': 0}


def hang_man_rules():

    print()

    print('Welcome to Hangman!')

    print()

    print('Try and guess the letters of a word to reveal more of the word, or guess the word if you know what it is!')
    print('If you guess the letter correctly, it will appear and nothing happens to the man.')
    print('However, if you guess incorrectly then the man gradually gets drawn to look like he\'s hanging!')
    print('If that happens then you lose and the man dies!')
    print('So try and guess correctly and use your big brain!')
    print('Oh, and you also have 6 lives, broken into 7 stages!')
    print()
    input('Type any key to continue: ')
    print()
    print('Here\'s the different stages of the man being drawn.')
    print()
    print('Stage 1:')
    print('It\'s just the noose.')
    print(''
          '   __________\n'
          '   |        |\n'
          '            |\n'
          '            |\n'
          '            |\n'
          '            |\n')
    print()
    print('Stage 2:')
    print('The head is added.')
    print(''
          '   __________\n'
          '   |        |\n'
          '   O        |\n'
          '            |\n'
          '            |\n'
          '            |\n')
    print()
    print('Stage 3:')
    print('The body is added.')
    print(''
          '   __________\n'
          '   |        |\n'
          '   O        |\n'
          '   |        |\n'
          '            |\n'
          '            |\n')
    print()
    print('Stage 4:')
    print('The left arm is added.')
    print(''
          '   __________\n'
          '   |        |\n'
          '   O        |\n'
          '   |\       |\n'
          '            |\n'
          '            |\n')
    print()
    print('Stage 5:')
    print('The right arm is added.')
    print(''
          '   __________\n'
          '   |        |\n'
          '   O        |\n'
          '  /|\       |\n'
          '            |\n'
          '            |\n')
    print()
    print('Stage 6:')
    print('The left leg is added.')
    print(''
          '   __________\n'
          '   |        |\n'
          '   O        |\n'
          '  /|\       |\n'
          '    \       |\n'
          '            |\n')
    print()
    print('Stage 7:')
    print('The right leg is added. And the man dies :(')
    print(''
          '   __________\n'
          '   |        |\n'
          '   O        |\n'
          '  /|\       |\n'
          '  / \       |\n'
          '            |\n')
    print()
    input('Type any key to continue: ')
    print()
    print()
    print()

    print('Let\'s get started!')


def hang_man_word_generator():

    hang_man_word_list = ['python', 'computer', 'hacker', 'pancakes', 'apollo', 'programming', 'telephone', 'network', 'website', 'gameplay', 'airpods', 'apple', 'component']

    hang_man_word_choice = random.choice(hang_man_word_list)

    return hang_man_word_choice


def hang_man_gameplay(hang_man_word):

    hang_man_lives = 6

    hang_man_word_length = len(hang_man_word)

    hang_man_current_word_list = []

    hang_man_gameplay_list = []

    hang_man_guessed_letters_list = []

    for letter in hang_man_word:

        hang_man_current_word_list.append(letter)

    while hang_man_word_length > 0:

        hang_man_gameplay_list.append('_')

        hang_man_word_length -= 1

    while True:

        if hang_man_lives == 6:

            print(''
                  '   __________\n'
                  '   |        |\n'
                  '            |\n'
                  '            |\n'
                  '            |\n'
                  '            |\n')

        elif hang_man_lives == 5:

            print(''
                  '   __________\n'
                  '   |        |\n'
                  '   O        |\n'
                  '            |\n'
                  '            |\n'
                  '            |\n')

        elif hang_man_lives == 4:

            print(''
                  '   __________\n'
                  '   |        |\n'
                  '   O        |\n'
                  '   |        |\n'
                  '            |\n'
                  '            |\n')

        elif hang_man_lives == 3:

            print(''
                  '   __________\n'
                  '   |        |\n'
                  '   O        |\n'
                  '   |\       |\n'
                  '            |\n'
                  '            |\n')

        elif hang_man_lives == 2:

            print(''
                  '   __________\n'
                  '   |        |\n'
                  '   O        |\n'
                  '  /|\       |\n'
                  '            |\n'
                  '            |\n')

        elif hang_man_lives == 1:

            print(''
                  '   __________\n'
                  '   |        |\n'
                  '   O        |\n'
                  '  /|\       |\n'
                  '    \       |\n'
                  '            |\n')

        else:

            print(''
                  '   __________\n'
                  '   |        |\n'
                  '   O        |\n'
                  '  /|\       |\n'
                  '  / \       |\n'
                  '            |\n')

            print('You ran out of lives!')
            print()
            print('The word was '+hang_man_word+'.')

            hang_man_score['Losses'] += 1

            break

        print(*hang_man_gameplay_list)

        if '_' not in hang_man_gameplay_list:

            print('You guessed the word correctly!')

            hang_man_score['Wins'] += 1

            break

        print()
        print()

        print('Letters guessed:')

        print(*hang_man_guessed_letters_list)

        hang_man_user_word_guess = input('Guess a letter of the word, or guess the entire word: ')

        if hang_man_user_word_guess.lower() == hang_man_word:

            print('Congrats! That\'s the right word!')

            hang_man_score['Wins'] += 1

            break

        elif hang_man_user_word_guess.lower() in hang_man_guessed_letters_list:

            print('You already guessed that!')

            print()

        elif len(hang_man_user_word_guess) == len(hang_man_word):

            print('Good guess, but that\'s not the right word!')

            hang_man_lives -= 1

            print()

        elif not (hang_man_user_word_guess.lower().isalpha()) or (1 < len(hang_man_user_word_guess) < len(hang_man_word)) or (len(hang_man_user_word_guess) > len(hang_man_word)):

            print('This isn\'t in the alphabet!')

            print()

        elif hang_man_user_word_guess.lower() in hang_man_current_word_list:

            print(hang_man_user_word_guess.upper(), 'is a letter of the word!')

            for index in (i for i, letter in enumerate(hang_man_current_word_list) if letter == hang_man_user_word_guess):

                hang_man_gameplay_list[index] = hang_man_user_word_guess

            hang_man_guessed_letters_list.append(hang_man_user_word_guess)

        else:

            print(hang_man_user_word_guess.upper(), 'isn\'t one of the letters of the word!')

            print()

            hang_man_lives -= 1

            hang_man_guessed_letters_list.append(hang_man_user_word_guess)


def hang_man_replay():

    print()

    print('Here\'s the score:')

    print(hang_man_score)

    print()

    while True:

        hang_man_user_replay = input('Would you like to play again? ("Yes"/"No") ')

        if hang_man_user_replay.lower() == 'yes':

            print('Okay, let\'s play again!')

            print()

            break

        elif hang_man_user_replay.lower() == 'no':

            print('Okay, thanks for playing!')

            exit()

        else:

            print('Please type either "Yes" or "No"!')


hang_man_rules()

while True:

    hang_man_computer_word = hang_man_word_generator()

    hang_man_gameplay(hang_man_computer_word)

    hang_man_score['Games Played'] += 1

    hang_man_replay()
