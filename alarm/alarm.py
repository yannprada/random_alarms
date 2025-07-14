import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import tkinter as tk
import uuid
import os
import pathlib

script_location = pathlib.Path(__file__).parent
SAVES_PATH = script_location / 'saves'
SAVES_SUFFIX = '.yaml'


class Alarm(tk.Frame):
    yaml_file = 'alarm/alarm.yaml'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = uuid.uuid1()
    
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
        filepath = self.get_savefile_path()
        with open(filepath, mode='w') as f:
            yaml.dump(data, f, Dumper=Dumper)
    
    def load(self, filename):
        self.id = pathlib.Path(filename).stem
        
        filepath = self.get_savefile_path(filename)
        with open(filepath) as f:
            data = yaml.load(f, Loader=Loader)
        
        self.alarm_appearance.load(data['appearance'])
        self.alarm_sound.load(data['sound'])
        self.alarm_time.load(data['time'])
    
    def stop(self):
        print('alarm stop')
    
    def remove(self):
        # delete save file
        filepath = self.get_savefile_path()
        os.remove(filepath)
        
        # notify container
        self.event_generate('<<REMOVE_ME>>')
    
    def get_savefile_path(self, filename=None):
        return SAVES_PATH / (filename if filename else f"{self.id}{SAVES_SUFFIX}")