import tkinter as tk


class AlarmRun(tk.LabelFrame):
    yaml_file = 'alarm/run.yaml'
    
    def init(self):
        self.stop()
        self.frame.columnconfigure(0, weight=1)
    
    def start(self):
        self.stop_button.grid()
        self.start_button.grid_remove()
    
    def stop(self):
        self.start_button.grid()
        self.stop_button.grid_remove()
