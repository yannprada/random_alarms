import tkinter as tk
import os
import pathlib
script_location = pathlib.Path(__file__).parent


class AlarmContainer(tk.Frame):
    yaml_file = 'alarm/container.yaml'
    current_id = 0
    
    def init(self):
        # look for save files
        saves = os.listdir(f'{script_location}/saves/')
        if len(saves):
            self.load_alarms(saves)
    
    def load_alarms(self, files):
        # load files
        for filename in files:
            if filename.endswith('.yaml'):
                alarm = self.build()
                alarm.load(filename)
        
        self._update()
    
    def add(self):
        alarm = self.build()
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
