import keyboard
import pyautogui
import pyperclip
import util

terminate = False
prevSyllable = ''
curSyllable = ''
def quit():
    global terminate 
    terminate = True

def read_syllable():
    global curSyllable
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')
    curSyllable = pyperclip.paste().lower()
    print(curSyllable)
    util.find_word(curSyllable)

def prompt_word():
    global curSyllable, prevSyllable
    if prevSyllable is not curSyllable and len(util.possible_words) != 0:
        print(util.get_word())
        prevSyllable = curSyllable
    pass

keyboard.on_press_key("ctrl", lambda _:read_syllable())
keyboard.on_press_key("esc", lambda _:quit())

# load the whole word list
util.load_word_list()

while not terminate:
    prompt_word()

print("Program quitted successfully!")
exit()