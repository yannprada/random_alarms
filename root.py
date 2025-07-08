import tkinter as tk
import time


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
