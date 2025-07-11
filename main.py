import sys
sys.path.append('../yaml_tkinter')
sys.path.append('../tk_double_scale')
sys.path.append('../tk_time_picker')
import yamltk
from tk_double_scale import DoubleScale as _DoubleScale
from tk_time_picker import TimePicker as _TimePicker

import tkinter as tk

from root import Root
from color_button import ColorButton
from time_entry import TimeEntry
from alarm.container import AlarmContainer
from alarm.alarm import Alarm
from alarm.appearance import AlarmAppearance
from alarm.sound import AlarmSound
from alarm.time import AlarmTime
from alarm.run import AlarmRun


class DoubleScale(tk.Frame):
    def inner_config(self, kwargs):
        self._scale = _DoubleScale(self, **kwargs)
        self._scale.pack()
    
    def get_values(self):
        return self._scale.get_values()


class TimePicker(tk.Frame):
    def inner_config(self, kwargs):
        self._picker = _TimePicker(self, **kwargs)
        self._picker.pack()
    
    def __str__(self):
        return str(self._picker)


if __name__ == '__main__':
    branches = [AlarmContainer, Alarm, AlarmAppearance, AlarmSound, AlarmTime, AlarmRun,
                ColorButton, DoubleScale, TimeEntry, TimePicker]
    builder = yamltk.Builder(Root, branches)
    
    button_add = builder.tk_widgets['button_add']
    alarm_container = builder.tk_widgets['alarm_container']
    button_add.configure(command=alarm_container.add)
    alarm_container._update()
        
    builder.root._update()
    builder.root.mainloop()