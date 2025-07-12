import tkinter as tk
import webbrowser


class AlarmSound(tk.LabelFrame):
    yaml_file = 'alarm/sound.yaml'
    
    def help_instruments(self):
        webbrowser.open_new("http://www.ccarh.org/courses/253/handout/gminstruments/")
    
    def help_notes(self):
        webbrowser.open_new("https://computermusicresource.com/midikeys.html")
    
    def get_data(self):
        frame = self.children['!frame']
        data = {
            'volume': frame.children['volume_scale'].get(),
            'instruments': frame.children['instruments_scale'].get_values(),
            'notes': frame.children['notes_scale'].get_values(),
            'notes_length': frame.children['notes_length_scale'].get_values(),
            'notes_amount': frame.children['notes_amount_scale'].get_values(),
        }
        return data
    
    def load(self, data):
        frame = self.children['!frame']
        frame.children['volume_scale'].set(data['volume'])
        frame.children['instruments_scale'].set_values(data['instruments'])
        frame.children['notes_scale'].set_values(data['notes'])
        frame.children['notes_length_scale'].set_values(data['notes_length'])
        frame.children['notes_amount_scale'].set_values(data['notes_amount'])