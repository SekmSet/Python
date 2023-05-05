# Le jeu du pendu

# Imports
import random

class HangmanGameClass ():
    # Variables
    start = '> Tu vas commencer à jouer au jeu du pendu, bonne chance !'
    winner = '> *O*  WAWE tu gagnes la partie !'
    looser = '> Dommage tu as perdu ... peut-être une prochaine fois !'
    end = "> Le jeu s'arrête ... revient me défier quand tu sera prêt.e"
    retry = '> Veux-tu ré-essayer ? Y/N : '
    proposal = '> Propose moi une lettre : '
    stop = "> Pour arrêter le jeu immédiatement utilise le code STOP"

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    words = ['sleepy', 'introduce', 'mist', 'wooden', 'flawless', 'merciful', 'cure', 'brush', 'plant', 'wrist', 'aback',
             'abrasive', 'helpless', 'painful', 'remove', 'farm', 'mind', 'reduce', 'efficacious', 'pretty']

    nbr_min = 0
    nbr_max = len(words)
    game = True

    # Functions
    def game_start(self):
        print(self.start)
        print(self.stop)

        while game:
            self.play()

            replay = input(self.retry)
            if replay == "N" or replay == "n":
                print(self.end)
                self.game = False


    def play(self):
        # Get a word
        index = self.random_int(self.nbr_min, self.nbr_max)
        word = self.random_word(index)

        # Split the word
        word_split = list(word)
        word_len = len(word_split)
        nbr_try = 0
        proposals = []

        convert_into_secret = self.string_transform(word_split)
        win = False
        while nbr_try <= (word_len - 1):
            # Ask user to write something in terminal (prompt)
            print('> Le mot à trouver : ', convert_into_secret)

            response = input(self.proposal)
            format = self.format_str(response)

            print('> Lettre proposée :', response)

            contains = self.array_contains(word_split, format)
            letter_proposed = self.array_contains(proposals, format)

            if response == 'STOP' or response == 'stop':
                print(self.end)
                nbr_try = self.nbr_max
            elif letter_proposed:
                print('> -.- Tu as déjà proposé cette lettre ')
            elif contains:
                print('> >< Le mot à trouver contient cette lettre ')
                convert_into_secret = self.reveal_letter(word_split, convert_into_secret, format)
                proposals.append(format)
            else:
                print('> T.T Le mot à trouver ne contient pas cette lettre ')
                proposals.append(format)

            # User find the complete word and win
            secret = ''.join(convert_into_secret)
            if format == word or secret == word:
                win = True
                nbr_try = self.nbr_max

            nbr_try += 1
            print("Nombre d'essaie : ", nbr_try)
            print("Tes propositions : ", proposals)
            print("---------- FIN DU TOUR ---------- ")

        if win:
            print(self.winner)
        else:
            print(self.looser)


    # Generate a random Return a random word
    def random_int(self, min, max):
        return random.randint(min, max - 1)

    # Get a word in array
    def random_word(self, index):
        return self.words[index]


    # Replace all caracters
    def string_transform(self, word):
        i = 0
        transform = []
        while i < len(word):
            transform.append('_')
            i += 1
        return transform

    # Verify if a letter exist in an array
    def array_contains(self, array, letter):
        count = 0

        for item in array:
            if item == letter:
                count += 1

        if count > 0:
            return True
        else:
            return False

    # Display found letter in the secret word
    def reveal_letter(self, word, secret_word, letter):
        i = 0
        for w in word:
            if w == letter:
                secret_word[i] = letter
            elif w == '_':
                secret_word[i] = '_'
            i += 1
        return secret_word

    # Format a letter : convert in lower case and remove spacing
    def format_str(self, str):
        strToLower = str.lower()
        return strToLower.strip()

game = HangmanGameClass()
game.game_start()
