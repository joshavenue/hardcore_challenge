import os
import nltk
from nltk.book import *

def os_clear():
    if os.name == 'nt':
        os.system('clr')
    else:
        os.system('clear')

def book_list_1(book_1):
    if book_1.lower() == 'text1':
        c = text1
        return c
    elif book_1.lower() == 'text2':
        c = text2
        return c
    elif book_1.lower() == 'text3':
        c = text3
        return c
    elif book_1.lower() == 'text4':
        c = text4
        return c
    elif book_1.lower() == 'text5':
        c = text5
        return c
    elif book_1.lower() == 'text6':
        c = text6
        return c
    elif book_1.lower() == 'text7':
        c = text7
        return c
    elif book_1.lower() == 'text8':
        c = text8
        return c
    elif book_1.lower() == 'text9':
        c = text9
        return c
    else:
        print('Text do not exist')
        raise SystemExit

def book_list_2(book_2):
    if book_2.lower() == 'text1':
        g = text1
        return g
    elif book_2.lower() == 'text2':
        g = text2
        return g
    elif book_2.lower() == 'text3':
        g = text3
        return g
    elif book_2.lower() == 'text4':
        g = text4
        return g
    elif book_2.lower() == 'text5':
        g = text5
        return g
    elif book_2.lower() == 'text6':
        g = text6
        return g
    elif book_2.lower() == 'text7':
        g = text7
        return g
    elif book_2.lower() == 'text8':
        g = text8
        return g
    elif book_2.lower() == 'text9':
        g = text9
        return g
    else:
        print('Text do not exist')
        raise SystemExit

def ask_word():
    while True:

        x = str(input('Enter the word you wish to search in the book. \n Word : '))

        print('The word, {} , appeared {} times in the book of Genesis.'.format(x, text3.count(x)))

        y = str(input('Do you wish to search again? Y/N : '))

        if y.lower() == 'n':
            break
        else:
            del x
            del y
            os_clear()
            pass

def word_game():
    while True:

        print(texts())

        a = str(input('Would you like to compare vocabulary richness of the books instead? Y/N '))

        if 'y' in a.lower():
            while True:

                b = str(input('Enter the Book entry number. (E.g : text1 for the first book. \n Enter : '))

                book_list_1(b)

                d = str(input('Enter the second book you wish to compare with. \n Enter : '))

                book_list_2(d)

                print('The number of words in {} is {}.'.format(book_list_1(b), len(book_list_1(b))))
                print('The number of words in {} is {}.'.format(book_list_2(d), len(book_list_2(d))))

                h = float(len(set(book_list_1(b))) / len(book_list_1(b)))
                k = float(len(set(book_list_2(d))) / len(book_list_2(d)))

                f = len(book_list_1(b)) + len(book_list_2(d))

                print('The first text {} and second text {} has a combined words of {}.'.format(book_list_1(b),book_list_2(d),f))

                print('The first text has {} sets of word.'.format(len(set(book_list_1(b)))))
                print('The lexical diversity of the first text is : {}.'.format(h))
                print('The second text has {} sets of word.'.format(len(set(book_list_2(d)))))
                print('The lexical diversity of the second text is : {}.'.format(k))

                if h > k:
                    e = h - k
                    print('{} has richer vocabulary than {}.'.format(b,d))
                elif h < k:
                    e = k - h
                    print('{} has richer vocabulary than {}.'.format(d,b))
                else:
                    print('Both books has similar lexical diversity.')

                if b.lower() not in text_check or d.lower() not in text_check:
                    print('Invalid text')
                    break
                else:
                    pass

                l = str(input('Try again? Y/N : '))

                if l.lower() == 'y':
                    os_clear()
                    word_game()
                    pass
                elif l.lower() == 'n':
                    count_word()
                    raise SystemExit
                else:
                    break

        os_clear()

        if 'n' in a.lower():
            print('Okay then!')
            del a
            raise SystemExit
            

def count_word():
    o = sorted(word for word in set(text3) if word.startswith('I'))
    print('Do you know? There are {} words that starts with I in the book of Genesis!'.format(len(o)))

text_check = ['text1','text2','text3','text4','text5','text6','text7','text8','text9']
os_clear()
print('The book of Genesis.')

ask_word()
os_clear()
word_game()
