import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import tkinter as tk
import tkinter.messagebox as messagebox
import uuid
import pathlib

script_location = pathlib.Path(__file__).parent
SAVES_PATH = script_location / 'saves'
SAVES_SUFFIX = '.yaml'

from .random_alarm import RandomAlarm


class Alarm(tk.Frame):
    yaml_file = 'alarm/alarm.yaml'
    auto_save_delay = 60 * 1000
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = uuid.uuid1()
        self.is_running = False
    
    def init(self):
        self.alarm_run.bind('<<TEST>>', lambda e: self.ring())
        self.alarm_run.bind('<<START_STOP>>', lambda e: self.start_stop())
        self.alarm_run.bind('<<REMOVE>>', lambda e: self.remove())
        self.alarm_time.bind('<<ALARM_RING>>', lambda e: self.ring())
        self.after(self.auto_save_delay, self.auto_save)
    
    def start_stop(self):
        if self.is_running:
            self.stop()
        else:
            self.start()
        self.is_running = not self.is_running
    
    def start(self):
        self.save()
        self.alarm_time.start()
        self.alarm_run.start()
    
    def stop(self):
        self.alarm_time.stop()
        self.alarm_run.stop()
    
    def remove(self):
        answer = messagebox.askyesno(title='Remove this alarm', 
                                     message='Are you sure?')
        if not answer:
            return
        
        self.stop()
        
        # delete savefile
        savefile = self.get_savefile_path()
        if savefile.exists():
            savefile.unlink()
        
        # notify container
        self.event_generate('<<REMOVE_ME>>')
    
    def ring(self):
        data = self.get_data()
        random_alarm = RandomAlarm(data['appearance'], data['sound'])
    
    def auto_save(self):
        self.save()
        self.after(self.auto_save_delay, self.auto_save)
    
    def get_data(self):
        return {
            'appearance': self.alarm_appearance.get_data(),
            'sound': self.alarm_sound.get_data(),
            'time': self.alarm_time.get_data(),
        }
    
    def save(self):
        data = self.get_data()
        
        # event_generate cannot send data... save it directly from here
        filepath = self.get_savefile_path()
        with open(filepath, mode='w') as f:
            yaml.dump(data, f, Dumper=Dumper)
    
    def load(self, path):
        with open(path) as f:
            data = yaml.load(f, Loader=Loader)
        
        self.id = path.stem
        self.alarm_appearance.load(data['appearance'])
        self.alarm_sound.load(data['sound'])
        self.alarm_time.load(data['time'])
    
    def get_savefile_path(self, filename=None):
        return SAVES_PATH / (filename if filename else f"{self.id}{SAVES_SUFFIX}")
    
    def toggle_active(self, active):
        self.alarm_appearance.toggle_active(active)