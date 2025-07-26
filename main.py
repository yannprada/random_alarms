import tkinter as tk

from tk_double_scale import DoubleScale
from tk_digital_time_picker import TimePicker
import yamltk


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