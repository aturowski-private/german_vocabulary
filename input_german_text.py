import curses
import locale

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
            if (k == curses.KEY_ENTER) or (k == 10) or (k == 13):
                break
            self.win.addstr(1, self.pos, chr(k))
            self.pos = self.pos + 1
            self.input = self.input + chr(k)
        return self.input
