import keyboard
import pyautogui
import pyperclip
import threading
import util

# flag to terminate the program
terminate = False
prevSyllable = ''
curSyllable = ''

# modes
auto_paste_mode = False
long_word_mode = False

# --------------------------------------------------------------

def quit():
    global terminate 
    terminate = True

def read_syllable():
    global curSyllable
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')
    curSyllable = pyperclip.paste().lower().strip()
    pyautogui.hotkey('tab')
    print(curSyllable)
    util.find_word(curSyllable)
    return curSyllable

def prompt_word():
    global long_word_mode, auto_paste_mode
    words = util.get_word(long_word_mode)
    print(words)

    if len(words) != 0:
        # store the first word found to the clipboard so that user can directly paste
        pyperclip.copy(words[0])
    
    if auto_paste_mode:
        paste_word()

    return words

def paste_word():
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')

# --------------------------------------------------------------

def init():
    # load the whole word list
    util.load_word_list()

# --------------------------------------------------------------

# probbaly not gonna work
if __name__ == '__main__':
    keyboard.on_press_key("shift", lambda _:read_syllable())
    keyboard.on_press_key("esc", lambda _:quit())

    # load the whole word list
    util.load_word_list()

    # main loop
    while not terminate:
        if prevSyllable is not curSyllable and len(util.possible_words) != 0:
            prompt_word()
            if auto_paste_mode:
                paste_word()
            prevSyllable = curSyllable

    print("Program quitted successfully!")
    exit()