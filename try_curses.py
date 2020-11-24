import curses
import locale

# German letters
Au = "\u00c4"   # A umlaut
au = "\u00e4"   # a umlaut
Ea = "\u00c9"   # E acute
ea = "\u00e9"   # e acute
Ou = "\u00d6"   # O umlaut
ou = "\u00f6"   # o umlaut
Uu = "\u00dc"   # U umlaut
uu = "\u00fc"   # u umlaut
Ss = "\u00df"   # s ligature

def main(stdscr):
    # clear screen
    stdscr.clear()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    
    # display something
    stdscr.addstr(0, 0 , "Cos tam", curses.A_REVERSE)
    stdscr.addstr(1, 0 , "Cos tam 2")
    stdscr.addstr(2, 0 , Au + au + Ea + ea + Ou + ou + Uu + uu + Ss)

    stdscr.refresh()
    stdscr.getch()

    # finish the application
    stdscr.keypad(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()


if __name__ == "__main__":
    print (locale.getpreferredencoding())
    curses.wrapper(main)
