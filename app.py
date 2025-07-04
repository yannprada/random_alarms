import sys
sys.path.append('../yaml_tkinter')
import yamltk
import tkinter as tk
import time
import re


class Root(tk.Tk):
    yaml_file = 'root.yaml'
    
    def _update(self):
        current_time = time.strftime('%H:%M:%S')
        self.tk_variables['current_time'].set(current_time)
        self.after(100, self._update)


class AlarmContainer(tk.Frame):
    yaml_file = 'alarm_container.yaml'
    alarm_id = 0
    alarm_count = 0
    
    def get_widget(self, id):
        return self.builder.tk_widgets[id]
    
    def get_alarms(self):
        return self.get_widget('alarm_inner_container').winfo_children()
    
    def add(self):
        self.builder.add_branch('Alarm', 'alarm_inner_container')
        self.alarm_count += 1
        self.alarm_id = self.alarm_count - 1
        self.update_display()
    
    def on_previous(self):
        self.alarm_id -= 1
        self.update_display()
    
    def on_next(self):
        self.alarm_id += 1
        self.update_display()
    
    def update_display(self):
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


class Alarm(tk.Frame):
    yaml_file = 'alarm.yaml'


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
    
    def init(self, _name):
        self._name = _name
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


def wrap_int(x, maxi):
    if x < 0:
        return maxi
    if x > maxi:
        return 0
    return x


if __name__ == '__main__':
    branches = [Alarm, AlarmContainer, TimeEntry]
    builder = yamltk.Builder(Root, branches)
    
    button = builder.tk_widgets['button_add']
    alarm_container = builder.tk_widgets['alarm_container']
    button.configure(command=alarm_container.add)
    alarm_container.update_display()
    
    builder.root._update()
    builder.root.mainloop()