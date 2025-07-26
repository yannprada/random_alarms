import tkinter as tk

from tk_double_scale import DoubleScale as _DoubleScale
from tk_digital_time_picker import TimePicker as _TimePicker
import yamltk


class DoubleScale(tk.Frame):
    def inner_config(self, kwargs):
        self._scale = _DoubleScale(self, **kwargs)
        self._scale.pack()
    
    def get_values(self, return_type=float):
        return self._scale.get_values(return_type)
    
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
from widgets.color_button import ColorButton
from alarm.container import AlarmContainer
from alarm.alarm import Alarm
from alarm.appearance import AlarmAppearance
from alarm.sound import AlarmSound
from alarm.time import AlarmTime
from alarm.run import AlarmRun


BRANCHES = [AlarmContainer, Alarm, AlarmAppearance, AlarmSound, AlarmTime, AlarmRun,
            ColorButton, DoubleScale, TimePicker]


if __name__ == '__main__':
    root = yamltk.build(Root, BRANCHES)
    root.post_init()
    
    def on_exit():
        root.alarm_container.save_all()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_exit)
    
    root.mainloop()