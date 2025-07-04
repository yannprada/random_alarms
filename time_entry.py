import tkinter as tk
import re


class TimeEntry(tk.Entry):
    yaml_file = 'time_entry.yaml'
    patterns = [
        r'^[0-2]$',
        r'^([01]\d|2[0-3])$',
        r'^([01]\d|2[0-3]):$',
        r'^([01]\d|2[0-3]):[0-5]$',
        r'^([01]\d|2[0-3]):[0-5]\d$',
        r'^([01]\d|2[0-3]):[0-5]\d:$',
        r'^([01]\d|2[0-3]):[0-5]\d:[0-5]$',
        r'^([01]\d|2[0-3]):[0-5]\d:[0-5]\d$',
    ]
    
    def init(self, name):
        self.name = name
        self.insert(0, '00:00:00')
        self.no_user_input = True
        self.bind('<FocusIn>', self.on_focus_in)
        self.bind('<KeyRelease>', self.on_key_release)
    
    def on_focus_in(self, event):
        if self.no_user_input:
            self.no_user_input = False
            self.delete(0, 99)
    
    def on_key_release(self, event):
        if not self.validate(self.get()):
            i = self.index("insert")
            self.delete(i-1)
    
    def validate(self, time_string):
        l = len(time_string)
        if l == 0:
            return True
        elif l == 2 or l == 5:
            self.insert(l, ':')
        elif l > 8:
            return False
        pattern = self.patterns[l-1]
        return re.match(pattern, time_string)
