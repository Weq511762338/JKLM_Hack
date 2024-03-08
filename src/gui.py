import wx
import prompter
import keyboard

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(250, 300), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)

        self.SetIcon(wx.Icon('./img/prompter_icon.ico', wx.BITMAP_TYPE_ICO))  # Add application icon

        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a static box and a static box sizer
        static_box = wx.StaticBox(panel, label='Possible Words:')
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        # Create a static text control
        self.static_text = wx.StaticText(panel, label="")

        # Set a custom font for the static text
        font = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.static_text.SetFont(font)

        # Add static text control to the static box sizer, centering it
        static_box_sizer.Add(self.static_text, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        # Add static box sizer to the main sizer
        main_sizer.Add(static_box_sizer, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Create a horizontal box sizer for toggle buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add toggle buttons
        toggle_button1 = wx.ToggleButton(panel, label='Toggle 1')
        toggle_button2 = wx.ToggleButton(panel, label='Toggle 2')

        button_sizer.Add(toggle_button1, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        button_sizer.Add(toggle_button2, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        # Add button sizer to the main sizer
        main_sizer.Add(button_sizer, proportion=0, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(main_sizer)
        self.Center()
        
        # Bind toggle button events
        toggle_button1.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle_button)
        toggle_button2.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle_button)
        
        self.words_to_display = ['Welcome', 'to', 'JKLM_Prompter']
        self.display_words_in_rows(self.words_to_display)

    def on_toggle_button(self, event):
        button = event.GetEventObject()
        print(f'{button.GetLabel()} toggled: {button.GetValue()}')
        # You can perform actions based on which button is toggled here
        self.update_displayed_text(['lol', 'wsdgf'])
        
    def display_words_in_rows(self, words):
        display_text = '\n'.join(words)
        self.static_text.SetLabel(display_text)
        
    def update_displayed_text(self, new_words):
        self.words_to_display = new_words
        self.display_words_in_rows(self.words_to_display)

frame = None

def prompt():
    prompter.read_syllable()
    words = prompter.prompt_word()
    global frame
    frame.update_displayed_text(words)

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
    frame = MyFrame(None, "Display Words in Rows (Static Display with Buttons)")
    frame.Show()
    app.MainLoop()