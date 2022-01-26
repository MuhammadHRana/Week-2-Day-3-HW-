# # Main running function
# # Letter checker?
# # Replacer of LETTERS to ' _ '
# # 



from ctypes.wintypes import WORD
import random
from tkinter import LEFT




def main():
    play = input('Would you like to play hangman? Yes/No ').lower()
    chances = 10
    done = False
    word_list = ['Python', 'Gamify', 'Pythonic', 'HTML']
    word = random.choice(word_list)
    word = word.lower()

    word_empty = word
    for i in range(len(word_empty)):
        word_empty = word_empty.replace(word_empty[i], '_')
    word_empty = " ".join(word_empty) + " "

    if play == 'yes':
        print(f'The word you have to guess has {len(word)} letters! ')
        print(word_empty)
        found = []
        while not done:
            let = input('Guess a letter! (enter a single letter) ').lower()
            if let == 'stop':
                print('Goodbye! ')
                return
            elif let.isalpha() == False:
                print('Your entry was not part of the alphabet. Please enter a single character! ')
            elif len(let) > 1:
                print('You did not follow instructions! Please enter only 1 character from the alphabet! ')
            chosen = let
            let_space = chosen + ' '
            
            last_index = -1
            word_list = list(word)
            check = word_empty.replace(" ", "")

            while True:
                try:
                    last_index = word.index(let, last_index+1)
                except ValueError:
                    break
                else:
                    found.append(last_index)
            new = list(check)
            for i in found:
                new[i] = word_list[i]
            new = ' '.join(new) + " "
            print(new)
            chances = chances -1
            done= False
            if new.__contains__("_") == False:
                print('Congratulations, you won!!!! ')
                done = True
                break
            elif chances <= 0:
                print("Game Over!")
                done = True
                break
            print(f'You have {chances} left! ')
            
    elif play == 'no':
        return "Game over."
    elif play.isalpha() == False:
        print('Your entry was not part of the alphabet. Please enter Yes or No! ')
        return main()
    elif len(play) > 3:
        print('You did not follow instructions! Please enter Yes or No! ')
        return main()
    else:
        print('You have entered an invalid response. Please try again')
        return main()


main()