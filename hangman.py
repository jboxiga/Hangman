from os import system
import random
from resources import hangman_resources

def random_word():
    with open("./resources/words_library.txt", 'r', encoding='utf-8') as f:
        list_of_words=[line for line in f]
    word=random.choice(list_of_words).rstrip('\ns')

    return word

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def hangman():
    word = random_word()
    word_to_guess = [letter for letter in word]
    word_to_show = ['_' for letter in word_to_guess]
    chars_guessed = []
    lifes = 6
    gameplay_result="lose"


    while lifes > 0:

        is_in_chars_guessed = False
        is_in_the_word = False

        while True:

            system('cls')
            
            print(f"Intentos: {lifes}")
    

            #PRINTING THE HINTS
            print(hangman_resources.hm_status[-1-(lifes)])
            for letter in word_to_show:
                print(letter, end=" ")
            print("\n\nLetras intentadas:")                       
            for i in chars_guessed:
                print(i, end=", ")
            

            #ASKING FOR A LETTER
            try:
                char=input("\n\nIngrese una letra: ").lower()
                if normalize(char.replace(" ", "")) == normalize(word):
                    word_to_show = [letter for letter in word]
                    break
                elif char.isalpha() == False or char == '' or len(char) > 1:
                    system('cls')
                    raise ValueError
                else:
                    for i in chars_guessed:
                        if char == i:
                            is_in_chars_guessed = True
                    if is_in_chars_guessed == True:
                        is_in_chars_guessed = False
                        continue
                    if is_in_chars_guessed == False:
                        chars_guessed.append(char)
                    break
            except:
                pass

        #COMPARING IF THE LETTER IS IN THE WORD
        for count, j in enumerate(word_to_guess):
            if char == normalize(j):
                word_to_show[count] = j
                is_in_the_word=True
        #UPDATING LIFES
        if is_in_the_word == False:
            lifes-=1
        
        #WIN CONDITION 
        if word_to_show == word_to_guess:
            gameplay_result="win"
            break

    return gameplay_result, word

def run():
    # GAME HISTORY VARIABLES
    games_w=0
    games_l=0

    system('cls')
    play=input(hangman_resources.menu)
    if play == "" or len(play) > 0:
        result=hangman()

    # PLAY AGAIN
    while True:
        if result[0] == "win":
            games_w+=1
            while True:
                system('cls')
                print(f"Partidas ganadas: {games_w} | Partidas perdidas {games_l}"
                f"\n{hangman_resources.win} \n\nGanaste, la palabra correcta fue: {result[1]}")
                replay = input("Deseas volver a jugar? y/n: ").lower()
                if replay == "y" or replay == "n":
                    break
            if replay == "y":
                result=hangman()
            elif replay == "n":
                break
        elif result[0] == "lose":
            games_l+=1
            while True:
                system('cls')
                print(f"Partidas ganadas: {games_w} | Partidas perdidas {games_l}"
                f"\n{hangman_resources.hm_status[6]} \n\nPerdíste, la palabra correcta era: {result[1]}")
                replay = input("Deseas volver a jugar? y/n: ").lower()
                if replay == "y" or replay == "n":
                    break
            if replay == "y":
                result=hangman()
            elif replay == "n":
                break
    

    

if __name__ == '__main__':
    run()