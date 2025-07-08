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
        
        self.alarm_color = tk.StringVar()
        self.set_color()
        
        self.after(100, lambda: self.alarm_position.set('11'))
    
    def on_random_button(self):
        is_random = self.tk_variables['is_random']
        if is_random.get():
            self.position_fixed_frame.grid_remove()
        else:
            self.position_fixed_frame.grid()
    
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
