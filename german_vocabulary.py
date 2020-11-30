import argparse
import curses
import locale
import random
from german_dictionary import vocabulary, ENG_IDX, GER_IDX, Au, au, Ea, ea, Ou, ou, Uu, uu, Ss

class EnglishText:
    def __init__(self, winPos = (0, 0), winSize = (3, 50)):
        # lines, columns, start line, start column
        self.win = curses.newwin(winSize[0], winSize[1], winPos[0], winPos[1])

    def dispText(self, text):
        self.win.clear()
        self.win.addstr(0, 0, "English word:")
        self.win.addstr(1, 0, text)
        self.win.refresh()

class InputGermanText:
    def __init__(self, winPos = (5, 0), winSize = (5, 50)):
        self.input = ""
        # lines, columns, start line, start column
        self.win = curses.newwin(winSize[0], winSize[1], winPos[0], winPos[1])

    def printPrompt(self):
        self.win.addstr(0, 0, "1-"+Au+"   2-"+au+"   3-"+Ea+"   4-"+ea)
        self.win.addstr(1, 0, "5-"+Ou+"   6-"+ou+"   7-"+Uu+"   8-"+uu+"   9-"+Ss)
        self.win.addstr(2, 0, "German translation:")

    def getInput(self):
        self.win.clear()
        self.printPrompt()
        self.pos = 0
        self.input = ''
        while True:
            backspace = False
            k = self.win.getch()
            # now translate the key press into correct action
            if (k == curses.KEY_ENTER) or (k == 10) or (k == 13):
                # user pressed Enter
                break
            elif (k == curses.KEY_BACKSPACE) or (k == 8) or (k == 127):
                backspace = True
            elif (chr(k) == '1'):
                # german capital A umlaut
                char = Au
            elif (chr(k) == '2'):
                # german lower a umlaut
                char = au
            elif (chr(k) == '3'):
                # german capital E acute
                char = Ea
            elif (chr(k) == '4'):
                # german lower E acute
                char = ea
            elif (chr(k) == '5'):
                # german capital O umlaut
                char = Ou
            elif (chr(k) == '6'):
                # german lower o umlaut
                char = ou
            elif (chr(k) == '7'):
                # german capital U umlaut
                char = Uu
            elif (chr(k) == '8'):
                # german lower u umlaut
                char = uu
            elif (chr(k) == '9'):
                # german s ligature
                char = Ss
            elif (chr(k) == ' '):
                # space
                char = ' '
            elif (chr(k).isalpha()):
                # normal latin letters
                char = chr(k)

            if backspace:
                if (self.pos > 0):
                    self.pos = self.pos - 1
                    self.win.addstr(4, self.pos, ' ')
                    self.input = self.input[:-1]
            else:
                self.win.addstr(4, self.pos, char)
                self.pos = self.pos + 1
                self.input = self.input + char

        return self.input

class Result:
    def __init__(self, winPos = (9, 0), winSize = (4, 50)):
        # lines, columns, start line, start column
        self.win = curses.newwin(winSize[0], winSize[1], winPos[0], winPos[1])

    # def decapitalise(self, input):
    #     # get rid of capital letters to make the comparison not case sensitive
    def dispResult(self, input, germanWord):
        self.win.clear()
        passed = (input == germanWord)
        if (passed):
            self.win.addstr(0, 0, "Correct :)")
        else:
            self.win.addstr(0, 0, "ERROR :(")
            self.win.addstr(1, 0, "Got: "+ input)
            self.win.addstr(2, 0, "Should be: "+ germanWord)
        self.win.addstr(4, 0, "Press any key to continue")
        self.win.getch()
        self.win.clear()
        self.win.refresh()
        return passed

class Progress:
    def __init__(self, max, winPos= (13, 0), winSize = (4, 50)):
        self.max = max
        self.curr = 0
        # lines, columns, start line, start column
        self.win = curses.newwin(winSize[0], winSize[1], winPos[0], winPos[1])
        self.win.clear()

    def increment(self):
        self.curr = self.curr + 1
        self.win.clear()
        self.win.addstr(0, 0, "Done {:d}/{:d}".format(self.curr, self.max))
        self.win.refresh()

def main(stdscr):
    locale.setlocale(locale.LC_ALL, '')
    code = locale.getpreferredencoding()
   
    # clear screen
    stdscr.clear()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(True)
    
    # create all windows
    englishWindow = EnglishText((0, 0), (3, 50))
    germanWindow = InputGermanText((3, 0), (5, 50))
    resultWindow = Result((10, 0), (6, 50))
    progressWindow = Progress(args.words_count, (16, 0), (3,50))

    # select the word to test
    if (args.test == -1):
        # select Duolingo lesson words set at random
        words = vocabulary[random.randint(0, len(vocabulary)-1)]['words']
    else:
        # pick Duoling lesson word set as specified in the command line
        words = vocabulary[args.test]['words']
    # now create a random list of from these words
    randomWords = random.choices(words, k = args.words_count)
    for word in randomWords:
        if type(word[ENG_IDX]) is tuple:
            englishWord = word[ENG_IDX][0]  # pick first english word from the tuple
        else:
            englishWord = word[ENG_IDX]
        germanWord = word[GER_IDX]
        while(True):
            # test the same word up until user gets it right
            englishWindow.dispText(englishWord)
            input = germanWindow.getInput()
            passed = resultWindow.dispResult(input, germanWord)
            if passed:
                break
        progressWindow.increment()

    # finish the application
    stdscr.keypad(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Script tests German vocabulary')
    parser.add_argument('-t', '--test', type=int, default=-1,
                        help='Specifies Duolingo lesson from which the words will be tested')
    parser.add_argument('-n', '--words_count', type=int, default=50,
                        help='Specifies how many words should be tested in the session')
    args = parser.parse_args()
    if (len(vocabulary) < args.test):
        print("-t argument can only take values up to {:d}".format(len(vocabulary)))
        sys.exit(-1)
    curses.wrapper(main)
