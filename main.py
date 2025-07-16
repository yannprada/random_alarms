import sys
sys.path.append('../yaml_tkinter')
sys.path.append('../tk_double_scale')
sys.path.append('../tk_time_picker')
import yamltk
from tk_double_scale import DoubleScale as _DoubleScale
from tk_time_picker import TimePicker as _TimePicker

import tkinter as tk


class DoubleScale(tk.Frame):
    def inner_config(self, kwargs):
        self._scale = _DoubleScale(self, **kwargs)
        self._scale.pack()
    
    def get_values(self):
        return self._scale.get_values()
    
    def set_values(self, data):
        self._scale.set_values(*data)


class TimePicker(tk.Frame):
    def inner_config(self, kwargs):
        self._picker = _TimePicker(self, **kwargs)
        self._picker.pack()
    
    def __str__(self):
        return str(self._picker)
    
    def get_seconds(self):
        return self._picker.get_seconds()
    
    def set_value(self, value):
        self._picker.set_value(value)


from root import Root
from color_button import ColorButton
from alarm.container import AlarmContainer
from alarm.alarm import Alarm
from alarm.appearance import AlarmAppearance
from alarm.sound import AlarmSound
from alarm.time import AlarmTime
from alarm.run import AlarmRun


BRANCHES = [AlarmContainer, Alarm, AlarmAppearance, AlarmSound, AlarmTime, AlarmRun,
            ColorButton, DoubleScale, TimePicker]


if __name__ == '__main__':
    builder = yamltk.Builder(Root, BRANCHES)
    builder.root.post_init()
    
    def on_exit():
        builder.root.alarm_container.save_all()
        builder.root.destroy()
    
    builder.root.protocol("WM_DELETE_WINDOW", on_exit)
    
    builder.root.mainloop()