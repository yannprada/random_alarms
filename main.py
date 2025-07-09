import sys
sys.path.append('../yaml_tkinter')
sys.path.append('../tk_double_scale')
import yamltk
from tk_double_scale import DoubleScale as _DoubleScale

import tkinter as tk

from root import Root
from time_entry import TimeEntry
from alarm.container import AlarmContainer
from alarm.alarm import Alarm
from alarm.appearance import AlarmAppearance
from alarm.sound import AlarmSound
from alarm.time import AlarmTime


class DoubleScale(tk.Frame):
    def inner_config(self, kwargs):
        self._scale = _DoubleScale(self, **kwargs)
        self._scale.pack()
    
    def get_values(self):
        return self._scale.get_values()


if __name__ == '__main__':
    branches = [AlarmContainer, Alarm, AlarmAppearance, AlarmSound, AlarmTime,
                DoubleScale, TimeEntry]
    builder = yamltk.Builder(Root, branches)
    
    button_add = builder.tk_widgets['button_add']
    alarm_container = builder.tk_widgets['alarm_container']
    button_add.configure(command=alarm_container.add)
    alarm_container._update()
    
    builder.root._update()
    builder.root.mainloop()