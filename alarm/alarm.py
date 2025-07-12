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
        # collect alarm data
        alarm_appearance = self.children['!alarmappearance']
        alarm_sound = self.children['!alarmsound']
        alarm_time = self.children['!frame'].children['!alarmtime']
        
        appearance_data = alarm_appearance.get_data()
        sound_data = alarm_sound.get_data()
        time_data = alarm_time.get_data()
        
        # send data through an event to main, with alarm number
        self.event_generate('')
        # main should save it to yaml config file, along with other alarms data
        
    
    def stop(self):
        print('alarm stop')