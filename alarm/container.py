import tkinter as tk
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import uuid
import os
import pathlib
script_location = pathlib.Path(__file__).parent


class AlarmContainer(tk.Frame):
    yaml_file = 'alarm/container.yaml'
    current_id = 0
    
    def init(self):
        # look for save files
        files = os.listdir(f'{script_location}/saves/')
        files = list(filter(lambda f: f.endswith('.yaml'), files))
        if len(files):
            self.load_alarms(files)
    
    def load_alarms(self, files):
        # load files
        alarms_data = {}
        for filename in files:
            # filename template is: '{uuid}.yaml'
            alarm_uuid = os.path.splitext(filename)[0]
            
            filepath = f'{script_location}/saves/{filename}'
            with open(filepath) as f:
                alarms_data[alarm_uuid] = yaml.load(f, Loader=Loader)
        
        # build and pass data to Alarm object
        alarm_uuids = sorted(alarms_data.keys())
        for alarm_uuid in alarm_uuids:
            alarm = self.build()
            alarm.id = alarm_uuid
            alarm.load(alarms_data[alarm_uuid])
        
        self._update()
    
    def add(self):
        alarm = self.build()
        alarm.id = uuid.uuid1()
        self._update()
    
    def build(self):
        inner = self.alarm_inner_container
        alarm = self.builder.add_branch(branch_name='Alarm', name=None, parent=inner)
        alarm.bind('<<REMOVE_ME>>', lambda e: self.remove(alarm))
        self.current_id = self.get_alarm_count() - 1
        return alarm
    
    def remove(self, alarm):
        alarm.pack_forget()
        alarm.destroy()
        self.on_previous()
    
    def save_all(self):
        for alarm in self.get_alarms():
            alarm.save()
    
    def on_previous(self):
        self.current_id -= 1
        self._update()
    
    def on_next(self):
        self.current_id += 1
        self._update()
    
    def get_alarms(self):
        return self.alarm_inner_container.winfo_children()
    
    def get_alarm_count(self):
        return len(self.alarm_inner_container.children)
    
    def _update(self):
        alarm_count = self.get_alarm_count()
        
        # make sure id is not out of bounds
        self.current_id = wrap_int(self.current_id, alarm_count - 1)
        display_id = 0 if alarm_count == 0 else self.current_id + 1
        
        # update text count
        text = f'{display_id}/{alarm_count}'
        self.tk_variables['alarm_count'].set(text)
        
        if alarm_count > 0:
            # hide all alarms
            alarms = self.get_alarms()
            for alarm in alarms:
                alarm.pack_forget()
            
            # show relevant alarm
            alarms[self.current_id].pack()


def wrap_int(x, maxi):
    if x < 0:
        return maxi
    if x > maxi:
        return 0
    return x
