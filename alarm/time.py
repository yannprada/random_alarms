import tkinter as tk


class AlarmTime(tk.LabelFrame):
    yaml_file = 'alarm/time.yaml'
    
    def init(self):
        self.frame_repeat = self.children['!frame'].children['frame_repeat']
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
        frame = self.children['!frame']
        frame_repeat = frame.children['frame_repeat']
        data = {
            'starting_time': str(frame.children['starting_time_picker']),
            'from_time': str(frame_repeat.children['from_time_picker']),
            'to_time': str(frame_repeat.children['to_time_picker']),
            'repeat': self.tk_variables['alarm_repeat'].get(),
        }
        return data
    
    def load(self, data):
        frame = self.children['!frame']
        frame.children['starting_time_picker'].set_value(data['starting_time'])
        
        frame_repeat = frame.children['frame_repeat']
        frame_repeat.children['from_time_picker'].set_value(data['from_time'])
        frame_repeat.children['to_time_picker'].set_value(data['to_time'])
        
        self.tk_variables['alarm_repeat'].set(data['repeat'])
        self.on_repeat_button()
