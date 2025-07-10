import tkinter as tk
import webbrowser


class AlarmSound(tk.LabelFrame):
    yaml_file = 'alarm/sound.yaml'
    
    def help_instruments(self):
        webbrowser.open_new("http://www.ccarh.org/courses/253/handout/gminstruments/")
    
    def help_notes(self):
        webbrowser.open_new("https://computermusicresource.com/midikeys.html")