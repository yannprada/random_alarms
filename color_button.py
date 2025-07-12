import tkinter as tk
from tkinter import colorchooser
import colorsys
import PIL.ImageColor as ImageColor


class ColorButton(tk.Button):
    yaml_file = 'color_button.yaml'
    
    def init(self):
        self.color_name = tk.StringVar()
        self.set_color()
    
    def on_click(self):
        color_code = colorchooser.askcolor(title ="Choose color")
        if color_code is None or color_code == (None, None):
            return
        self.set_color(color_code)
    
    def set_color(self, color=((255, 255, 255), 'white')):
        rgb = color[0]
        color_name = color[1]
        h, l, s = colorsys.rgb_to_hls(*rgb)
        # set the text color black or white depending on the bg luminance
        fg = 'black' if l > 125 else 'white'
        
        self.color_name.set(color_name)
        self.configure(bg=color_name, fg=fg)
    
    def set_color_name(self, color_name):
        rgb = ImageColor.getrgb(color_name)
        self.set_color((rgb, color_name))
    
    def get_color(self):
        return self.color_name.get()