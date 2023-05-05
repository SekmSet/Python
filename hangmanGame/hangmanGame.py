# Le jeu du pendu

# Imports
import random

# Variables
start = '> Tu vas commencer à jouer au jeu du pendu, bonne chance !'
winner = '> *O*  WAWE tu gagnes la partie !'
looser = '> Dommage tu as perdu ... peut-être une prochaine fois !'
end = "> Le jeu s'arrête ... revient me défier quand tu sera prêt.e"
retry = '> Veux-tu ré-essayer ? Y/N : '
proposal = '> Propose moi une lettre : '
stop = "> Pour arrêter le jeu immédiatement utilise le code STOP"

words = ['sleepy', 'introduce', 'mist', 'wooden', 'flawless', 'merciful', 'cure', 'brush', 'plant', 'wrist', 'aback',
         'abrasive', 'helpless', 'painful', 'remove', 'farm', 'mind', 'reduce', 'efficacious', 'pretty']

nbr_min = 0
nbr_max = len(words)

life = 10

# Functions
def game_start():
    print(start)
    print(stop)
    game = True

    while game:
        play()
        replay = input(retry)

        if replay == "N" or replay == "n":
            print(end)
            game = False


def play():
    # Get a word
    index = random_int(nbr_min, nbr_max)
    word = random_word(index)

    # Split the word
    word_split = list(word)
    convert_into_secret = string_transform(word_split)


    nbr_try = 0
    can_play = True
    proposals = []
    win = False

    while can_play:
        # Ask user to write something in terminal (prompt)
        print('> Le mot à trouver : ', convert_into_secret)

        response = input(proposal)
        format = format_str(response)

        print('> Lettre proposée :', response)

        contains = array_contains(word_split, format)
        letter_proposed = array_contains(proposals, format)

        if response == 'STOP' or response == 'stop':
            print(end)
            can_play = False
        elif letter_proposed:
            print('> -.- Tu as déjà proposé cette lettre ')
        elif contains:
            print('> >< Le mot à trouver contient cette lettre ')
            convert_into_secret = reveal_letter(word_split, convert_into_secret, format)
            proposals.append(format)
        else:
            print('> T.T Le mot à trouver ne contient pas cette lettre ')
            proposals.append(format)

        # User find the complete word and win
        secret = ''.join(convert_into_secret)
        if format == word or secret == word:
            win = True
            can_play = False

        if nbr_try == life:
            can_play = False

        nbr_try += 1
        print("Nombre d'essaie : ", nbr_try)
        print("Tes propositions : ", proposals)
        print("---------- FIN DU TOUR ---------- ")

    if win:
        print(winner)
    else:
        print(looser)


# Generate a random Return a random word
def random_int(min, max):
    return random.randint(min, max - 1)


# Get a word in array
def random_word(index):
    return words[index]


# Replace all caracters
def string_transform(word):
    return len(word)*("_")

# Verify if a letter exist in an array
def array_contains(array, letter):
    count = 0

    for item in array:
        if item == letter:
            count += 1

    if count > 0:
        return True
    else:
        return False

# Display found letter in the secret word
def reveal_letter(word, secret_word, letter):
    i = 0
    for w in word:
        if w == letter:
            secret_word[i] = letter
        elif w == '_':
            secret_word[i] = '_'
        i += 1
    return secret_word

# Format a letter : convert in lower case and remove spacing
def format_str(str):
    strToLower = str.lower()
    return strToLower.strip()

game_start()
