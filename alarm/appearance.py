import tkinter as tk


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
        
        # manual trigger
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
            self.builder.tk_widgets['bg_color_button'].grid_remove()
        else:
            self.builder.tk_widgets['bg_color_label'].grid()
            self.builder.tk_widgets['bg_color_button'].grid()
