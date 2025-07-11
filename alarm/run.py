import tkinter as tk


class AlarmRun(tk.LabelFrame):
    yaml_file = 'alarm/run.yaml'
    
    def init(self):
        self.alarm = self.parent.parent
    
    def on_save_run_button(self):
        self.alarm.event_generate('<<SAVE_RUN>>')
    
    def on_save_button(self):
        self.alarm.event_generate('<<SAVE>>')
    
    def on_stop_button(self):
        self.alarm.event_generate('<<STOP>>')
