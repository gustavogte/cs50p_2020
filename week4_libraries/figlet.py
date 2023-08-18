from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

# argument can only be 1 or 3
# print(len(sys.argv))
if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")
# print(len(sys.argv))

if len(sys.argv) == 1:
    text = input("Input: ")
    figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(text))

elif sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("Invalid Usage")
else:
    try:
        figlet.setFont(font=sys.argv[2])
        text = input("Input: ")
        print(figlet.renderText(text))
    except:
        sys.exit("Invalid Usage")
