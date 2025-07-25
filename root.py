import tkinter as tk
import time


class Root(tk.Tk):
    yaml_file = 'root.yaml'
    
    def post_init(self):
        self.button_add.configure(command=self.alarm_container.add)
        self.alarm_container._update()
        self._update()
    
    def _update(self):
        current_time = time.strftime('%H:%M:%S')
        self.current_time.set(current_time)
        self.after(100, self._update)
