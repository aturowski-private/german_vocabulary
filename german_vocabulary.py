import curses
import locale
import random
from german_dictionary import vocabulary, ENG_IDX, GER_IDX, Au, au, Ea, ea, Ou, ou, Uu, uu, Ss

class EnglishText:
    def __init__(self, winPos = (0, 0), winSize = (3, 50)):
        self.winPos = winPos
        self.winSize = winSize
        self.createWindow()

    def createWindow(self):
        # lines, columns, start line, start column
        self.win = curses.newwin(self.winSize[0], self.winSize[1], self.winPos[0], self.winPos[1])

    def dispText(self, text):
        self.win.clear()
        self.win.addstr(0, 0, "English word:")
        self.win.addstr(1, 0, text)
        self.win.refresh()

class InputGermanText:
    def __init__(self, winPos = (5, 0), winSize = (5, 50)):
        self.winPos = winPos
        self.winSize = winSize
        self.input = ""
        self.createWindow()

    def createWindow(self):
        # lines, columns, start line, start column
        self.win = curses.newwin(self.winSize[0], self.winSize[1], self.winPos[0], self.winPos[1])

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
        self.winPos = winPos
        self.winSize = winSize
        self.createWindow()

    def createWindow(self):
        # lines, columns, start line, start column
        self.win = curses.newwin(self.winSize[0], self.winSize[1], self.winPos[0], self.winPos[1])

    def clear(self):
        self.win.clear()

    def dispResult(self, input, germanWord):
        self.clear()
        if (input == germanWord):
            self.win.addstr(0, 0, "Correct :)")
        else:
            self.win.addstr(0, 0, "ERROR :(")
            self.win.addstr(1, 0, "Got: "+ input)
            self.win.addstr(2, 0, "Should be: "+ germanWord)
        self.win.addstr(5, 0, "Press any key to continue")
        self.win.getch()
        self.clear()
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

    # select the word to display
    words = vocabulary[0]['words']
    randomWords = random.choices(words, k = 50)
    for word in randomWords:
        if type(word[ENG_IDX]) is tuple:
            englishWord = word[ENG_IDX][0]  # pick first english word from the tuple
        else:
            englishWord = word[ENG_IDX]
        germanWord = word[GER_IDX]
        englishWindow.dispText(englishWord)
        input = germanWindow.getInput()
        resultWindow.dispResult(input, germanWord)

    # finish the application
    stdscr.keypad(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
