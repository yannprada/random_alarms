from datetime import datetime, timedelta
import random
import tkinter as tk


class AlarmTime(tk.LabelFrame):
    yaml_file = 'alarm/time.yaml'
    
    def post_build(self):
        self.toggle_grid(False)
        self._job = None
    
    def on_repeat_button(self):
        repeat = self.alarm_repeat
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
            'repeat': self.alarm_repeat.get(),
        }
        return data
    
    def load(self, data):
        self.starting_time_picker.set_value(data['starting_time'])
        self.from_time_picker.set_value(data['from_time'])
        self.to_time_picker.set_value(data['to_time'])
        self.alarm_repeat.set(data['repeat'])
        self.on_repeat_button()
    
    def start(self):
        delay = self.seconds_until_next_time()
        self.job_start(delay)
    
    def job_start(self, delay):
        self._job = self.after(delay * 1000, self.do_job)
    
    def do_job(self):
        self.event_generate('<<ALARM_RING>>')
        
        if self.alarm_repeat.get():
            delay = self.seconds_until_repeat()
            self.job_start(delay)
    
    def stop(self):
        if self._job:
            self.after_cancel(self._job)
    
    def seconds_until_next_time(self):
        starting_time = str(self.starting_time_picker)
        target_time = datetime.strptime(starting_time, "%H:%M:%S").time()
        
        now = datetime.now()
        target_datetime_today = datetime.combine(now.date(), target_time)
        
        if now >= target_datetime_today:
            target_datetime_today += timedelta(days=1)
        
        delay = target_datetime_today - now
        return int(delay.total_seconds())
    
    def seconds_until_repeat(self):
        from_ = self.from_time_picker.get_seconds()
        to = self.to_time_picker.get_seconds()
        return random.randint(from_, to)
