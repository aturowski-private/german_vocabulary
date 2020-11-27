import curses
import locale
from german_dictionary import vocabulary, ENG_IDX, GER_IDX

# positions to where display things in ncurses window (col, row)
ENGLISH_WORD_POS = (0, 0)
GERMAN_GENDER_POS = (0, 1)
GERMAN_WORD_POS = (4, 1)

def display_word_to_translate(word, stdscr):
    print(word)
    # display English word
    stdscr.addstr(  ENGLISH_WORD_POS[1],
                    ENGLISH_WORD_POS[0],
                    word[ENG_IDX][0])
    # display German word
    stdscr.addstr(  GERMAN_GENDER_POS[1],
                    GERMAN_GENDER_POS[0],
                    word[GER_IDX][0])
    stdscr.addstr(  GERMAN_WORD_POS[1],
                    GERMAN_WORD_POS[0],
                    word[GER_IDX][1])
    stdscr.refresh()


def main(stdscr):
    # clear screen
    stdscr.clear()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    
    # select the word to display
    word = vocabulary[0]['words'][0]
    print(vocabulary)
    print(word)

    # display something
    # display_word_to_translate(word, stdscr)

    stdscr.getch()

    # finish the application
    stdscr.keypad(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()


if __name__ == "__main__":
    print (locale.getpreferredencoding())
    curses.wrapper(main)
