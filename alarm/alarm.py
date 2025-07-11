import tkinter as tk


class Alarm(tk.Frame):
    yaml_file = 'alarm/alarm.yaml'
    
    def init(self):
        alarm_run = self.children['!frame'].children['!alarmrun']
        alarm_run.bind('<<SAVE_RUN>>', lambda e: self.save_run())
        alarm_run.bind('<<SAVE>>', lambda e: self.save())
        alarm_run.bind('<<STOP>>', lambda e: self.stop())
    
    def save_run(self):
        self.save()
        print('alarm run')
    
    def save(self):
        print('alarm save')
    
    def stop(self):
        print('alarm stop')
