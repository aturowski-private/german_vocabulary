import curses
import locale
from german_dictionary import Au, au, Ea, ea, Ou, ou, Uu, uu, Ss

class InputGermanText:
    def __init__(self, winPos = (1, 0), expectedText = ""):
        self.winPos = winPos
        self.expectedText = expectedText
        self.input = ""
        self.pos = 0
        self.createWindow()
        self.printPrompt()

    def createWindow(self):
        # lines, columns, start line, start column
        self.win = curses.newwin(2, 50, self.winPos[0], self.winPos[1])

    def printPrompt(self):
        self.win.addstr(0, 0, "German translation:")

    def getInput(self):
        self.printPrompt()
        while True:
            k = self.win.getch()
            # now translate the key press into correct action
            if (k == curses.KEY_ENTER) or (k == 10) or (k == 13):
                # user pressed Enter
                break
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
            elif (chr(k).isalpha()):
                # normal latin letters
                char = chr(k)

            self.win.addstr(1, self.pos, char.encode('utf-8'))
            self.pos = self.pos + 1
            self.input = self.input + char
        return self.input
