import tkinter as tk


class AlarmContainer(tk.Frame):
    yaml_file = 'alarm/container.yaml'
    alarm_id = 0
    alarm_count = 0
    
    def get_alarms(self):
        return self.children['alarm_inner_container'].winfo_children()
    
    def add(self):
        branch_name = 'Alarm'
        alarm_name = None
        inner_container = self.children['alarm_inner_container']
        
        self.builder.add_branch(branch_name, alarm_name, inner_container)
        self.alarm_count += 1
        self.alarm_id = self.alarm_count - 1
        self._update()
        
        # give current alarm its id
        alarms = self.get_alarms()
        alarms[self.alarm_id].id = self.alarm_id
    
    def on_previous(self):
        self.alarm_id -= 1
        self._update()
    
    def on_next(self):
        self.alarm_id += 1
        self._update()
    
    def _update(self):
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
