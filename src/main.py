import keyboard
import pyautogui
import pyperclip
import util
import threading

# flag to terminate the program
terminate = False
prevSyllable = ''
curSyllable = ''

# sync lock between finding the possible words and prompting words
lock = threading.Lock()

# modes
auto_mode = False
long_word_mode = True

def quit():
    global terminate 
    terminate = True

def read_syllable(lock):
    lock.acquire()
    global curSyllable
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')
    curSyllable = pyperclip.paste().lower()
    pyautogui.hotkey('tab')
    print(curSyllable)
    util.find_word(curSyllable)
    lock.release()

def prompt_word():
    global curSyllable, prevSyllable, long_word_mode
    if prevSyllable is not curSyllable and len(util.possible_words) != 0:
        words = util.get_word(long_word_mode)
        # store the first word found to the clipboard so that user can directly paste
        pyperclip.copy(words[0])
        print(words)
        prevSyllable = curSyllable
    pass

keyboard.on_press_key("shift", lambda _:read_syllable(lock))
keyboard.on_press_key("esc", lambda _:quit())

# load the whole word list
util.load_word_list()

# main loop
while not terminate:
    if not lock.locked():
        prompt_word()

print("Program quitted successfully!")
exit()