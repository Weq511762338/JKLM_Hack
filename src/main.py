import keyboard
import pyautogui
import pyperclip
import util
import threading

terminate = False
prevSyllable = ''
curSyllable = ''
lock = threading.Lock()
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
    global curSyllable, prevSyllable
    if prevSyllable is not curSyllable and len(util.possible_words) != 0:
        words = util.get_word()
        pyperclip.copy(words[0])
        print(words)
        prevSyllable = curSyllable
    pass

keyboard.on_press_key("shift", lambda _:read_syllable(lock))
keyboard.on_press_key("esc", lambda _:quit())

# load the whole word list
util.load_word_list()

while not terminate:
    if not lock.locked():
        prompt_word()

print("Program quitted successfully!")
exit()