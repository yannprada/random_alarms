import tkinter as tk
import os
import pathlib

script_location = pathlib.Path(__file__).parent
SAVES_PATH = script_location / 'saves'


class AlarmContainer(tk.Frame):
    yaml_file = 'alarm/container.yaml'
    current_id = 0
    
    def init(self):
        # Look for save files and load alarms
        self.load_alarms([f for f in os.listdir(SAVES_PATH) if f.endswith('.yaml')])
    
    def load_alarms(self, files):
        # Load files
        for filename in files:
            alarm = self.build()
            alarm.load(filename)
        self._update()
    
    def add(self):
        self.build()
        self._update()
    
    def build(self):
        alarm = self.builder.add_branch(branch_name='Alarm', name=None, 
                                        parent=self.alarm_inner_container)
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
        self.current_id = (self.current_id - 1) % self.get_alarm_count()
        self._update()
    
    def on_next(self):
        self.current_id = (self.current_id + 1) % self.get_alarm_count()
        self._update()
    
    def get_alarms(self):
        return self.alarm_inner_container.winfo_children()
    
    def get_alarm_count(self):
        return len(self.get_alarms())
    
    def _update(self):
        # Update current_id to be within bounds
        alarm_count = self.get_alarm_count()
        display_id = 0 if alarm_count == 0 else self.current_id + 1
        
        # Update text count
        text = f'{display_id}/{alarm_count}'
        self.tk_variables['alarm_count'].set(text)
        
        # Hide all alarms and show the relevant one
        for alarm in self.get_alarms():
            alarm.pack_forget()
        
        if alarm_count > 0:
            self.get_alarms()[self.current_id].pack()
