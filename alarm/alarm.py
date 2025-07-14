import tkinter as tk
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import os
import pathlib
script_location = pathlib.Path(__file__).parent


class Alarm(tk.Frame):
    yaml_file = 'alarm/alarm.yaml'
    
    def init(self):
        self.alarm_run.bind('<<SAVE_RUN>>', lambda e: self.save_run())
        self.alarm_run.bind('<<SAVE>>', lambda e: self.save())
        self.alarm_run.bind('<<STOP>>', lambda e: self.stop())
        self.alarm_run.bind('<<REMOVE>>', lambda e: self.remove())
    
    def save_run(self):
        self.save()
        print('alarm run')
    
    def save(self):
        # collect alarm data
        data = {
            'appearance': self.alarm_appearance.get_data(),
            'sound': self.alarm_sound.get_data(),
            'time': self.alarm_time.get_data(),
        }
        
        # event_generate cannot send data... save it directly from here?
        filepath = self.get_file_path()
        with open(filepath, mode='w') as f:
            yaml.dump(data, f, Dumper=Dumper)
    
    def load(self, filename):
        self.id = os.path.splitext(filename)[0]
        
        filepath = f'{script_location}/saves/{filename}'
        with open(filepath) as f:
            data = yaml.load(f, Loader=Loader)
        
        self.alarm_appearance.load(data['appearance'])
        self.alarm_sound.load(data['sound'])
        self.alarm_time.load(data['time'])
    
    def stop(self):
        print('alarm stop')
    
    def remove(self):
        # delete save file
        filepath = self.get_file_path()
        os.remove(filepath)
        
        # notify container
        self.event_generate('<<REMOVE_ME>>')
    
    def get_file_path(self):
        return f'{script_location}/saves/{self.id}.yaml'