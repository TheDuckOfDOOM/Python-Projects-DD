# first actual python project. i basically have no idea on how to use github
# By the duck, *TheDuckofD00M on Github*
from collections import Counter
import time,random,sys,os,threading,msvcrt
# Colors :DDD (ansi)-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""""
\033[38;5;0m"    # black
"\033[38;5;1m"    # red
"\033[38;5;2m"    # green
"\033[38;5;3m"    # yellow
"\033[38;5;4m"    # blue
"\033[38;5;5m"    # purple
"\033[38;5;6m"    # cyan
"\033[38;5;7m"    # white
"\033[38;5;8m"    # bright black
"\033[38;5;9m"    # bright red
"\033[38;5;10m"   # bright green
"\033[38;5;11m"   # bright yellow
"\033[38;5;12m"   # bright blue
"\033[38;5;13m"   # bright purple
"\033[38;5;14m"   # bright cyan
"\033[38;5;15m"   # bright white

"\033[38;5;196m"  # red
"\033[38;5;202m"  # orange
"\033[38;5;226m"  # yellow
"\033[38;5;46m"   # green
"\033[38;5;51m"   # cyan
"\033[38;5;21m"   # blue
"\033[38;5;201m"  # pink
"\033[38;5;129m"  # purple
"\033[38;5;208m"  # orange
"\033[38;5;82m"   # lime
"\033[38;5;45m"   # sky blue
"\033[38;5;213m"  # light pink
"\033[38;5;220m"  # gold
"\033[38;5;198m"  # hot pink
"\033[38;5;118m"  # light green
"\033[38;5;87m"   # light cyan

 BASIC
 "\033[30m"   # black
"\033[31m"   # red
"\033[32m"   # green
"\033[33m"   # yellow
"\033[34m"   # blue
"\033[35m"   # purple
"\033[36m"   # cyan
"\033[37m"   # white
"\033[0m"    # reset

"\033[90m"   # bright black
"\033[91m"   # bright red
"\033[92m"   # bright green
"\033[93m"   # bright yellow
"\033[94m"   # bright blue
"\033[95m"   # bright purple
"\033[96m"   # bright cyan
"\033[97m"   # bright white

 BASIC bgs

 "\033[40m"   # black bg
"\033[41m"   # red bg
"\033[42m"   # green bg
"\033[43m"   # yellow bg
"\033[44m"   # blue bg
"\033[45m"   # purple bg
"\033[46m"   # cyan bg
"\033[47m"   # white bg

Basic styles

"\033[1m"    # bold
"\033[2m"    # dim
"\033[3m"    # italic
"\033[4m"    # underline
"\033[5m"    # blink
"\033[7m"    # inverted
"\033[9m"    # strikethrough
"""

# DEFINITIONS --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# global vars
Done = False
hp = 10
answer = [None]
typed = ""

#Clear terminal
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    # clears the colors of the text
    print("\033[0m")
#typing effect
def texteffect(text, delay=0.05, typeeffect="character"):
    if typeeffect == "character":
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
    elif typeeffect == "words":
        for word in text.split():
            sys.stdout.write(word + " ")
            sys.stdout.flush()
            time.sleep(delay)
# countdown
def countdown(number=5):
    global Done,hp,typed
    for i in range(number, 0, -1):
        sys.stdout.write("\r\033[1A")
        sys.stdout.write(f"\r\033[32m time = {i}\033[0m    ")
        sys.stdout.write("\033[1B\r")
        sys.stdout.flush()
        time.sleep(1)
        if Done == True:
            return

def get_answer():
    global Done,typed
    sys.stdout.write("\033[2K\033[38;5;208m\rYour answer --\033[0m")
    sys.stdout.flush()
    while not Done:
        if msvcrt.kbhit():
            char = msvcrt.getch()
            if char == b"\r":
                answer[0] = typed
                sys.stdout.write(f"\033[2K\033[38;5;208m\rYour answer --\033[0m {typed}  ")
                sys.stdout.flush()
                Done = True
                return answer[0]

            elif char == b"\b":
                typed = typed[:-1]
                sys.stdout.write(f"\033[2K\033[38;5;208m\rYour answer --\033[0m {typed}  ")
                sys.stdout.flush()
            else:
                typed += char.decode()
                sys.stdout.write(f"\033[2K\033[38;5;208m\rYour answer --\033[0m {typed}  ")
                sys.stdout.flush()
            
## MAINIntro ---------------------------------------------------------------------------------------------------------------------------------------------------------------------        


clear()
texteffect("welcome to the number game", 0.03)
print()
time.sleep(2)
texteffect("Select your difficulty!",0.05,"words")
print("\n\033[1;35m 1 - easy(1-100)\033[33m\n 2 - medium(1-500)\033[31m\n 3 - hard(1-1000)\n\033[38;5;213m 4 - Random(chooses difficulty for you)\033[0m")
difficulty = int(input("difficulty = ").strip())
if difficulty == 1:
    texteffect("You have selected 1 - 100")
elif difficulty == 2:
    texteffect("You have selected 1 - 500")
elif difficulty == 3:
    texteffect("You have selected 1 - 1000")
else:
    difficulty=random.randint(1,3)
    if difficulty == 1:
        texteffect("You have selected Random\033[1;35m(1 - 100)\033[0m")
    elif difficulty == 2:
        texteffect("You have selected Random\033[1;33m(1 - 500)\033[0m")
    else:
        texteffect("You have selected Random\033[1;31m(1 - 1000)\033[0m")
clear()

# Game Def ------------------------------------------------------------------------------------------------------------------------------------------------------------------
x = 0
def gamerun(difficultyselector):
    global answer,hp,Done,typed,x
    # var
    if int(difficultyselector) == 1:
        x = random.randint(1, 100)
    elif int(difficultyselector) == 2:
        x = random.randint(1, 500)
    else:
        x = random.randint(1, 1000)

    # main
    print("start") 
    while hp > 0:
        typed = ""
        answer[0] = None
        Done = False
        print("\033[32m time = 5 \033[0m")
        count = threading.Thread(target=countdown)
        count.start()
        getanswer=threading.Thread(target=get_answer)
        getanswer.daemon=True
        getanswer.start()
        count.join()
        Done = True
        try:
            if answer[0] is None:
                texteffect("\033[1;31m Time Ran Out.. \033[0m")
                hp -= 1
            elif int(answer[0]) == x:
                texteffect("\033[1;32m YOU DID IT!!! \033[0m")
                texteffect(f"\n\033[1;46m You had\033[1;31m {hp} Hp remaining\033[0m")
                break
            elif int(answer[0]) > x:
                texteffect("Lower")
                hp -= 1
            elif int(answer[0]) < x:
                hp -= 1
                texteffect("Higher")
        except(ValueError, IndexError):
            pass
        texteffect(f"\n\033[1;31m Hp remaining: {hp}\033[0m")
        time.sleep(2)
        clear()
    if hp <= 0:
        texteffect("\033[1;31m Uh oh, you lost! \033[0m")
        texteffect(f"\033[1;45m The answer was {x}, \033[46m Try again perhaps?\033[0m")
        
# Main3


clear()
gamerun(difficulty)
