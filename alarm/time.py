import tkinter as tk


class AlarmTime(tk.LabelFrame):
    yaml_file = 'alarm/time.yaml'
    repeat_ids = ['alarm_every_label', 'alarm_every_entry',
                  'alarm_to_label', 'alarm_to_entry']
    
    def init(self):
        self.toggle_grid(self.repeat_ids, False)
    
    def on_repeat_button(self):
        repeat = self.tk_variables['alarm_repeat']
        self.toggle_grid(self.repeat_ids, repeat.get())
    
    def toggle_grid(self, ids, visible):
        for id in ids:
            if visible:
                self.builder.tk_widgets[id].grid()
            else:
                self.builder.tk_widgets[id].grid_remove()
