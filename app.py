import sys
sys.path.append('../yaml_tkinter')
import yamltk
import tkinter as tk
import time
import re
from time_entry import TimeEntry
from alarm_container import AlarmContainer


class Root(tk.Tk):
    yaml_file = 'root.yaml'
    
    def _update(self):
        current_time = time.strftime('%H:%M:%S')
        self.tk_variables['current_time'].set(current_time)
        self.after(100, self._update)


class Alarm(tk.Frame):
    yaml_file = 'alarm.yaml'
    
    def init(self):
        self.hide_frame_every()
    
    def on_repeat_button(self):
        repeat = self.tk_variables['alarm_repeat']
        if(repeat.get()):
            self.show_frame_every()
        else:
            self.hide_frame_every()
    
    def show_frame_every(self):
        self.builder.tk_widgets['alarm_frame_every'].pack()
    
    def hide_frame_every(self):
        self.builder.tk_widgets['alarm_frame_every'].pack_forget()


if __name__ == '__main__':
    branches = [Alarm, AlarmContainer, TimeEntry]
    builder = yamltk.Builder(Root, branches)
    
    button = builder.tk_widgets['button_add']
    alarm_container = builder.tk_widgets['alarm_container']
    button.configure(command=alarm_container.add)
    alarm_container.update_display()
    
    builder.root._update()
    builder.root.mainloop()