import tkinter as tk
import webbrowser


class AlarmSound(tk.LabelFrame):
    yaml_file = 'alarm/sound.yaml'
    
    def init(self):
        self.volume_scale.set(50)
        self.notes_amount_scale.set_values([1, 5])
    
    def help_instruments(self):
        webbrowser.open_new("http://www.ccarh.org/courses/253/handout/gminstruments/")
    
    def help_notes(self):
        webbrowser.open_new("https://computermusicresource.com/midikeys.html")
    
    def get_data(self):
        data = {
            'volume': self.volume_scale.get(),
            'instruments': self.instruments_scale.get_values(return_type=int),
            'notes': self.notes_scale.get_values(return_type=int),
            'notes_length': self.notes_length_scale.get_values(),
            'notes_amount': self.notes_amount_scale.get_values(return_type=int),
        }
        return data
    
    def load(self, data):
        self.volume_scale.set(data['volume'])
        self.instruments_scale.set_values(data['instruments'])
        self.notes_scale.set_values(data['notes'])
        self.notes_length_scale.set_values(data['notes_length'])
        self.notes_amount_scale.set_values(data['notes_amount'])