import tkinter as tk
import tkinter.font as tkfont


class AlarmAppearance(tk.LabelFrame):
    yaml_file = 'alarm/appearance.yaml'
    tk_variable_keys = ['is_position_random', 'move_each_note', 'is_bg_transparent',
                        'font_size', 'font_bold', 'font_italic', 'message',
                        'font_underline', 'font_overstrike']
    
    def init(self):
        # generate the options here, because less typing
        self.alarm_position = tk.StringVar()
        
        for x in range(3):
            for y in range(3):
                b = tk.Radiobutton(self.position_fixed_frame, value=f'{x}{y}', 
                                   variable=self.alarm_position)
                b.grid(row=x, column=y)
        
        # populate font families
        for family in tkfont.families():
            self.font_family_listbox.insert('end', family)
        
        self.active = False
        self.font_family = 'System'
        self.tk_variables['font_size'].set(self.tk_variables['font_size'].get() or 10)
        self._refresh()
        
        self.after(100, self.post_init)
    
    def post_init(self):
        # manual trigger to change visibility depending on checkboxes inital values
        self.on_random_button()
        self.on_transparent_button()
        
        if not self.alarm_position.get():
            # set default position to center (11 means x=1, y=1)
            self.alarm_position.set('11')
    
    def on_random_button(self):
        if self.tk_variables['is_position_random'].get():
            self.position_fixed_frame.grid_remove()
            self.move_each_note_button.grid()
        else:
            self.position_fixed_frame.grid()
            self.move_each_note_button.grid_remove()
    
    def on_transparent_button(self):
        if self.tk_variables['is_bg_transparent'].get():
            self.bg_color_label.grid_remove()
            self.bg_color_button.grid_remove()
        else:
            self.bg_color_label.grid()
            self.bg_color_button.grid()
    
    def _refresh(self):
        if self.active:
            # save the selected font family
            selection = self.font_family_listbox.curselection()
            id = selection[0] if len(selection) else 0
            self.font_family = tkfont.families()[id]
            
            # reflect the current font on the preview label
            is_bg_transparent = self.tk_variables['is_bg_transparent'].get()
            fg = self.color_button.get_color()
            bg = None if is_bg_transparent else self.bg_color_button.get_color()
            
            self.message_preview_label.configure(font=tkfont.Font(
                family=self.font_family,
                size=self.tk_variables['font_size'].get(),
                weight='bold' if self.tk_variables['font_bold'].get() else 'normal',
                slant='italic' if self.tk_variables['font_italic'].get() else 'roman',
                underline=self.tk_variables['font_underline'].get(),
                overstrike=self.tk_variables['font_overstrike'].get(),
            ), fg=fg, bg=bg)
            # self.message_preview_label.configure(bg=bg)
        
        self.after(250, self._refresh)
    
    def set_font_family(self, font_family):
        self.font_family = font_family
        self.set_font_family_cursor()
    
    def set_font_family_cursor(self):
        id = tkfont.families().index(self.font_family)
        self.font_family_listbox.select_set(id)
    
    def get_data(self):
        data = {
            'alarm_position': self.alarm_position.get(),
            'color': self.color_button.get_color(),
            'bg_color': self.bg_color_button.get_color(),
            'font_family': self.font_family,
        }
        for key in self.tk_variable_keys:
            data[key] = self.tk_variables[key].get()
        return data
    
    def load(self, data):
        self.alarm_position.set(data['alarm_position'])
        self.color_button.set_color_name(data['color'])
        self.bg_color_button.set_color_name(data['bg_color'])
        self.set_font_family(data['font_family'])
        
        for key in self.tk_variable_keys:
            self.tk_variables[key].set(data[key])
    
    def toggle_active(self, active):
        self.active = active
        if self.active:
            self.set_font_family_cursor()
