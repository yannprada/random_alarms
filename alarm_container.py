import tkinter as tk


class AlarmContainer(tk.Frame):
    yaml_file = 'alarm_container.yaml'
    alarm_id = 0
    alarm_count = 0
    
    def get_widget(self, id):
        return self.builder.tk_widgets[id]
    
    def get_alarms(self):
        return self.get_widget('alarm_inner_container').winfo_children()
    
    def add(self):
        self.builder.add_branch('Alarm', 'alarm_inner_container')
        self.alarm_count += 1
        self.alarm_id = self.alarm_count - 1
        self.update_display()
    
    def on_previous(self):
        self.alarm_id -= 1
        self.update_display()
    
    def on_next(self):
        self.alarm_id += 1
        self.update_display()
    
    def update_display(self):
        # make sure id is not out of bounds
        self.alarm_id = wrap_int(self.alarm_id, self.alarm_count - 1)
        display_id = 0 if self.alarm_count == 0 else self.alarm_id + 1
        
        # update text count
        text = f'{display_id}/{self.alarm_count}'
        self.tk_variables['alarm_count'].set(text)
        
        if self.alarm_count > 0:
            # hide all alarms
            alarms = self.get_alarms()
            for alarm in alarms:
                alarm.pack_forget()
            
            # show relevant alarm
            alarms[self.alarm_id].pack()


def wrap_int(x, maxi):
    if x < 0:
        return maxi
    if x > maxi:
        return 0
    return x
