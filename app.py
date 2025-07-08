import sys
sys.path.append('../yaml_tkinter')
sys.path.append('../tk_double_scale')
import yamltk
from tk_double_scale import DoubleScale as _DoubleScale

import tkinter as tk
import time

from time_entry import TimeEntry
from alarm_container import AlarmContainer
from alarm_appearance import AlarmAppearance


class Root(tk.Tk):
    yaml_file = 'root.yaml'
    
    def _update(self):
        current_time = time.strftime('%H:%M:%S')
        self.tk_variables['current_time'].set(current_time)
        self.after(100, self._update)


class Alarm(tk.Frame):
    yaml_file = 'alarm.yaml'


class AlarmSound(tk.LabelFrame):
    yaml_file = 'alarm_sound.yaml'


class AlarmTime(tk.LabelFrame):
    yaml_file = 'alarm_time.yaml'
    every_ids = ['alarm_every_label', 'alarm_every_entry']
    
    def init(self):
        self.toggle_grid(self.every_ids, False)
    
    def on_repeat_button(self):
        repeat = self.tk_variables['alarm_repeat']
        self.toggle_grid(self.every_ids, repeat.get())
    
    def toggle_grid(self, ids, visible):
        for id in ids:
            if visible:
                self.builder.tk_widgets[id].grid()
            else:
                self.builder.tk_widgets[id].grid_remove()


class DoubleScale(tk.Frame):
    def inner_config(self, kwargs):
        self._scale = _DoubleScale(self, **kwargs)
        self._scale.pack()
    
    def get_values(self):
        return NotImplementedError()


if __name__ == '__main__':
    branches = [Alarm, AlarmContainer, TimeEntry, AlarmSound, AlarmTime, 
        AlarmAppearance, DoubleScale]
    builder = yamltk.Builder(Root, branches)
    
    button = builder.tk_widgets['button_add']
    alarm_container = builder.tk_widgets['alarm_container']
    button.configure(command=alarm_container.add)
    alarm_container.update_display()
    
    builder.root._update()
    builder.root.mainloop()