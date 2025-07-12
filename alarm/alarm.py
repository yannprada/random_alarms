import tkinter as tk
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import pathlib
script_location = pathlib.Path(__file__).parent


class Alarm(tk.Frame):
    yaml_file = 'alarm/alarm.yaml'
    
    def init(self):
        alarm_run = self.children['!frame'].children['!alarmrun']
        alarm_run.bind('<<SAVE_RUN>>', lambda e: self.save_run())
        alarm_run.bind('<<SAVE>>', lambda e: self.save())
        alarm_run.bind('<<STOP>>', lambda e: self.stop())
    
    def save_run(self):
        self.save()
        print('alarm run')
    
    def save(self):
        # collect alarm data
        alarm_appearance = self.children['!alarmappearance']
        alarm_sound = self.children['!alarmsound']
        alarm_time = self.children['!frame'].children['!alarmtime']
        
        data = {
            'appearance': alarm_appearance.get_data(),
            'sound': alarm_sound.get_data(),
            'time': alarm_time.get_data(),
        }
        
        # event_generate cannot send data... save it directly from here?
        filename = f'{script_location}/saves/{self.id}.yaml'
        with open(filename, mode='w') as f:
            yaml.dump(data, f, Dumper=Dumper)
    
    def stop(self):
        print('alarm stop')