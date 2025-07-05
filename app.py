import sys
sys.path.append('../yaml_tkinter')
import yamltk

from tkSliderWidget import tkSliderWidget
from tkinter import colorchooser
import tkinter as tk
import time
import colorsys

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


class AlarmLabelFrame(tk.LabelFrame):
    def show_grid(self, ids):
        self.toggle_grid(ids, True)
    
    def hide_grid(self, ids):
        self.toggle_grid(ids, False)
    
    def toggle_grid(self, ids, visible):
        for id in ids:
            if visible:
                self.builder.tk_widgets[id].grid()
            else:
                self.builder.tk_widgets[id].grid_remove()


class AlarmAppearance(AlarmLabelFrame):
    yaml_file = 'alarm_appearance.yaml'
    frame_fixed_id = 'alarm_frame_fixed'
    
    def init(self):
        alarm_frame_fixed = self.builder.tk_widgets[self.frame_fixed_id]
        
        # generate the options here, because less typing...
        self.alarm_position = tk.StringVar()
        
        for x in range(3):
            for y in range(3):
                b = tk.Radiobutton(alarm_frame_fixed, value=f'{x}{y}', 
                    variable=self.alarm_position)
                b.grid(row=x, column=y)
        
        self.alarm_color = tk.StringVar()
        self.set_color()
        
        self.after(100, lambda: self.alarm_position.set('11'))
    
    def on_random_button(self):
        is_random = self.tk_variables['is_random']
        self.toggle_grid([self.frame_fixed_id], not is_random.get())
    
    def on_color_button(self):
        color_code = colorchooser.askcolor(title ="Choose color")
        if color_code is None or color_code == (None, None):
            return
        self.set_color(color_code)
    
    def set_color(self, color=((255, 255, 255), 'white')):
        rgb = color[0]
        color_name = color[1]
        h, l, s = colorsys.rgb_to_hls(*rgb)
        fg = 'black' if l > 125 else 'white'
        
        self.alarm_color.set(color_name)
        self.builder.tk_widgets['color_button'].configure(bg=color_name, fg=fg)


class AlarmSound(AlarmLabelFrame):
    yaml_file = 'alarm_sound.yaml'


class Slider(tkSliderWidget.Slider):
    def __init__(self, master, **kwargs):
        kwargs['width'] = 100
        kwargs['height'] = 40
        kwargs['min_val'] = 0
        kwargs['max_val'] = 50
        kwargs['step_size'] = 1
        kwargs['init_lis'] = [1, 10]
        super().__init__(master, **kwargs)
        self.setValueChangeCallback(print)
    
    def getValues(self):
        values = super().getValues()
        return list(map(lambda value: int(round(value)), values))


class AlarmTime(AlarmLabelFrame):
    yaml_file = 'alarm_time.yaml'
    every_ids = ['alarm_every_label', 'alarm_every_entry']
    
    def init(self):
        self.hide_grid(self.every_ids)
    
    def on_repeat_button(self):
        repeat = self.tk_variables['alarm_repeat']
        self.toggle_grid(self.every_ids, repeat.get())


if __name__ == '__main__':
    branches = [Alarm, AlarmContainer, TimeEntry, AlarmSound, AlarmTime, 
        AlarmAppearance, Slider]
    builder = yamltk.Builder(Root, branches)
    
    button = builder.tk_widgets['button_add']
    alarm_container = builder.tk_widgets['alarm_container']
    button.configure(command=alarm_container.add)
    alarm_container.update_display()
    
    builder.root._update()
    builder.root.mainloop()