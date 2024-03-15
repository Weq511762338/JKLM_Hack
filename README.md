# JKLM_Prompter 💣
![](https://img.shields.io/badge/pip_install-wxpython-blue)
![](https://img.shields.io/badge/pip_install-keyboard-blue)
![](https://img.shields.io/badge/pip_install-PyAutoGUI-blue)
![](https://img.shields.io/badge/pip_install-pyperclip-blue)

## What is this?
A prompter program that will prompt words in real-time to assist players on the word game <ins>BombParty</ins> on [jklm.fun](jklm.fun).

<img src="https://miro.medium.com/v2/resize:fit:1400/1*xoD1tB9c7UQhfCb9YW7y7g.png" width="400"/>

## User Guide 📖
### Instruction
1. Hover the cursor over the word in the center
2. When it is your turn, press `shift` to select the word for processing
3. Type in the prompted word!

### Features
- If `Auto Paste Mode` is on, the 1st word on the list will be auto-pasted after processing the selected syllable
- If `Long Word Mode` is on, the prompted words will be as long as possible, essentially for a higher chance of using more letters and earning an extra life.

## Installation 💻
- Require `python` installed.
- Should work on Windows and MacOS

1. After downloading the prompter, run `$ pip install -r requirements.txt` to get all Python packages used.
2. Then just run `$ python ./JKLM_Prompter/src/main.py`
3. A `wxpython` window should pop up :)

## Important Notes
- `keyboard` module will read keypresses from the whole OS. So remember to close the program if you are going to use `shift` key somewhere else
- The wordlist for JKLM BombParty is not published publicly. Some of the words may be rejected. Just pick another one!
- Do not move the cursor from the syllable in the center. Adjust its position so that pressing `shift` can accurately select the word.
- This is for educational purpose only.

## License
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
