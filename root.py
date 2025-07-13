import tkinter as tk
import time


class Root(tk.Tk):
    yaml_file = 'root.yaml'
    
    def post_init(self):
        button_add = self.children['!frame'].children['button_add']
        alarm_container = self.children['alarm_container']
        button_add.configure(command=alarm_container.add)
        alarm_container._update()
        self._update()
    
    def _update(self):
        current_time = time.strftime('%H:%M:%S')
        self.tk_variables['current_time'].set(current_time)
        self.after(100, self._update)
