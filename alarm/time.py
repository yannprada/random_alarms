import tkinter as tk


class AlarmTime(tk.LabelFrame):
    yaml_file = 'alarm/time.yaml'
    
    def init(self):
        self.toggle_grid(False)
    
    def on_repeat_button(self):
        repeat = self.tk_variables['alarm_repeat']
        self.toggle_grid(repeat.get())
    
    def toggle_grid(self, visible):
        if visible:
            self.frame_repeat.grid()
        else:
            self.frame_repeat.grid_remove()
    
    def get_data(self):
        data = {
            'starting_time': str(self.starting_time_picker),
            'from_time': str(self.from_time_picker),
            'to_time': str(self.to_time_picker),
            'repeat': self.tk_variables['alarm_repeat'].get(),
        }
        return data
    
    def load(self, data):
        self.starting_time_picker.set_value(data['starting_time'])
        self.from_time_picker.set_value(data['from_time'])
        self.to_time_picker.set_value(data['to_time'])
        self.tk_variables['alarm_repeat'].set(data['repeat'])
        self.on_repeat_button()
