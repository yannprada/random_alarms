import tkinter as tk
import os
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import pathlib
script_location = pathlib.Path(__file__).parent


class AlarmContainer(tk.Frame):
    yaml_file = 'alarm/container.yaml'
    alarm_id = 0
    alarm_count = 0
    
    def init(self):
        # look for save files
        files = os.listdir(f'{script_location}/saves/')
        files = list(filter(lambda f: f.endswith('.yaml'), files))
        if len(files):
            self.load_alarms(files)
    
    def load_alarms(self, files):
        # load files
        extension_length = len('.yaml')
        alarms_data = {}
        for filename in files:
            # filename template is: '{id}.yaml'
            id = int(os.path.splitext(filename)[0])
            
            filepath = f'{script_location}/saves/{filename}'
            with open(filepath) as f:
                alarms_data[id] = yaml.load(f, Loader=Loader)
        
        # build and pass data to Alarm object
        alarm_ids = sorted(alarms_data.keys())
        for id in alarm_ids:
            alarm = self.build()
            alarm.id = id
            alarm.load(alarms_data[id])
            self.alarm_count += 1
        
        self.alarm_id = self.alarm_count - 1
        self._update()
    
    def add(self):
        alarm = self.build()
        self.alarm_count += 1
        self.alarm_id = self.alarm_count - 1
        alarm.id = self.alarm_id
        self._update()
    
    def build(self):
        inner = self.alarm_inner_container
        return self.builder.add_branch(branch_name='Alarm', name=None, parent=inner)
    
    def save_all(self):
        for alarm in self.get_alarms():
            alarm.save()
    
    def on_previous(self):
        self.alarm_id -= 1
        self._update()
    
    def on_next(self):
        self.alarm_id += 1
        self._update()
    
    def get_alarms(self):
        return self.alarm_inner_container.winfo_children()
    
    def _update(self):
        # make sure id is not out of bounds
        self.alarm_id = wrap_int(self.alarm_id, self.alarm_count - 1)
        display_id = 0 if self.alarm_count == 0 else self.alarm_id + 1
        
        # update text count
        text = f'{display_id}/{self.alarm_count}'
        self.tk_variables['alarm_count'].set(text)
        
        if self.alarm_count > 0:
            # hide all alarms
            alarms = self.get_alarms()
            for alarm in alarms:
                alarm.pack_forget()
            
            # show relevant alarm
            alarms[self.alarm_id].pack()


def wrap_int(x, maxi):
    if x < 0:
        return maxi
    if x > maxi:
        return 0
    return x
