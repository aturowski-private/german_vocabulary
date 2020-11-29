import curses
import locale
from german_dictionary import vocabulary, ENG_IDX, GER_IDX
from input_german_text import InputGermanText
# positions to where display things in ncurses window (col, row)
ENGLISH_WORD_POS = (0, 0)
GERMAN_GENDER_POS = (0, 1)
GERMAN_WORD_POS = (4, 1)

def display_word_to_translate(word, stdscr, code):
    print(word)
    # display English word
    stdscr.addstr(  ENGLISH_WORD_POS[1],
                    ENGLISH_WORD_POS[0],
                    word[ENG_IDX].encode(code))
    # display German word
    stdscr.addstr(  GERMAN_GENDER_POS[1],
                    GERMAN_GENDER_POS[0],
                    word[GER_IDX][0].encode(code))
    stdscr.addstr(  GERMAN_WORD_POS[1],
                    GERMAN_WORD_POS[0],
                    word[GER_IDX][1].encode(code))
    stdscr.refresh()


def main(stdscr):
    locale.setlocale(locale.LC_ALL, '')
    code = locale.getpreferredencoding()

    # clear screen
    stdscr.clear()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    
    # select the word to display
    word = vocabulary[0]['words'][3]
    # print(vocabulary)
    # print(word)

    # display something
    # display_word_to_translate(word, stdscr, code)
    # stdscr.getch()
    inputWindow = InputGermanText()
    inputWindow.getInput()

    # finish the application
    stdscr.keypad(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()


if __name__ == "__main__":
    # print(vocabulary)
    # word = vocabulary[0]['words'][3]
    # print(word)
    # print(word[1][0])
    # TRY=1
    # print(word[TRY][0])
    # print(GER_IDX)
    # # print('{:s} {:s}'.format(word[GER_IDX][0], word[GER_IDX][1]))

    curses.wrapper(main)
