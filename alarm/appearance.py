from tkinter import colorchooser
import tkinter as tk
import colorsys


class AlarmAppearance(tk.LabelFrame):
    yaml_file = 'alarm/appearance.yaml'
    
    def init(self):
        self.position_fixed_frame = self.builder.tk_widgets['position_fixed_frame']
        
        # generate the options here, because less typing...
        self.alarm_position = tk.StringVar()
        
        for x in range(3):
            for y in range(3):
                b = tk.Radiobutton(self.position_fixed_frame, value=f'{x}{y}', 
                    variable=self.alarm_position)
                b.grid(row=x, column=y)
        
        # color variables and buttons
        self.alarm_color = tk.StringVar()
        self.alarm_bg_color = tk.StringVar()
        self.color_button = self.builder.tk_widgets['color_button']
        self.bg_color_button = self.builder.tk_widgets['bg_color_button']
        self.set_color(self.alarm_color, self.color_button)
        self.set_color(self.alarm_bg_color, self.bg_color_button)
        
        self.on_transparent_button()
        
        # set default position to center (11 means x=1, y=1)
        self.after(100, lambda: self.alarm_position.set('11'))
    
    def on_random_button(self):
        if self.tk_variables['is_random'].get():
            self.position_fixed_frame.grid_remove()
        else:
            self.position_fixed_frame.grid()
    
    def on_transparent_button(self):
        if self.tk_variables['is_bg_transparent'].get():
            self.builder.tk_widgets['bg_color_label'].grid_remove()
            self.bg_color_button.grid_remove()
        else:
            self.builder.tk_widgets['bg_color_label'].grid()
            self.bg_color_button.grid()
    
    def on_color_button(self):
        color_code = self.pick_color()
        self.set_color(self.alarm_color, self.color_button, color_code)
    
    def on_bg_color_button(self):
        color_code = self.pick_color()
        self.set_color(self.alarm_bg_color, self.bg_color_button, color_code)
    
    def pick_color(self):
        color_code = colorchooser.askcolor(title ="Choose color")
        if color_code is None or color_code == (None, None):
            return
        return color_code
    
    def set_color(self, variable, button, color=((255, 255, 255), 'white')):
        rgb = color[0]
        color_name = color[1]
        h, l, s = colorsys.rgb_to_hls(*rgb)
        fg = 'black' if l > 125 else 'white'
        
        variable.set(color_name)
        button.configure(bg=color_name, fg=fg)
