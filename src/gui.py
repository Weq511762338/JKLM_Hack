import wx
import prompter
import keyboard

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 400), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)

        self.SetIcon(wx.Icon('./JKLM_Prompter/img/prompter_icon.ico', wx.BITMAP_TYPE_ICO))

        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a static box and a static box sizer
        possible_word_box = wx.StaticBox(panel, label='Possible Words:')
        possible_word_sizer = wx.StaticBoxSizer(possible_word_box, wx.VERTICAL)

        syllable_box = wx.StaticBox(panel, label='Syllable:')
        syllable_sizer = wx.StaticBoxSizer(syllable_box, wx.VERTICAL)

        # text list of possible words
        self.possible_words = wx.StaticText(panel, label="")
        # text for syllable
        self.syllable = wx.StaticText(panel, label="")

        # set a custom font for the static text
        font = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.possible_words.SetFont(font)
        self.syllable.SetFont(font)

        # Add static text control to the static box sizer, centering it
        syllable_sizer.Add(self.syllable, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        possible_word_sizer.Add(self.possible_words, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        # Add static box sizer to the main sizer
        main_sizer.Add(syllable_sizer, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        main_sizer.Add(possible_word_sizer, proportion=8, flag=wx.EXPAND | wx.ALL, border=10)

        # Create a horizontal box sizer for toggle buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add toggle buttons
        auto_mode_button = wx.ToggleButton(panel, label='Auto Paste Mode')
        long_word_button = wx.ToggleButton(panel, label='Long Word Mode')

        button_sizer.Add(auto_mode_button, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        button_sizer.Add(long_word_button, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        # Add button sizer to the main sizer
        main_sizer.Add(button_sizer, proportion=0, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(main_sizer)
        self.Center()
        
        # Bind toggle button events
        auto_mode_button.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle_button)
        long_word_button.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle_button)
        
        # Greeting texts
        self.display_syllable('^-^')
        self.display_words_in_rows(['Welcome', 'to', 'JKLM Prompter', ':)'])

    def on_toggle_button(self, event):
        button = event.GetEventObject()
        print(f'{button.GetLabel()} toggled: {button.GetValue()}')

        if button.GetLabel() == 'Auto Paste Mode':
            prompter.auto_paste_mode = not prompter.auto_paste_mode
        elif button.GetLabel() == 'Long Word Mode':
            prompter.long_word_mode = not prompter.long_word_mode
        
    def display_words_in_rows(self, words):
        display_text = '\n'.join(words)
        self.possible_words.SetLabel(display_text)

    def display_syllable(self, syllable):
        self.syllable.SetLabel(syllable)

frame = None

def prompt():
    syllable = prompter.read_syllable()
    words = prompter.prompt_word()
    global frame
    frame.display_words_in_rows(words)
    frame.display_syllable(syllable)

def run():
    global frame
    # start gui
    app = wx.App()
    frame = MyFrame(None, "JKLM Prompter")

    keyboard.on_press_key("shift", lambda _:prompt())
    # keyboard.on_press_key("esc", lambda _:wx.Exit())

    prompter.init()

    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, "JKLM Prompter")
    frame.Show()
    app.MainLoop()