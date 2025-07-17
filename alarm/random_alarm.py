import pygame.midi
import random
import tkinter as tk
import tkinter.font as tkfont

# appearance_data:
# {'alarm_position': '11', 'is_position_random': False, 'move_each_note': False, 

# Class in charge spawning the actual message, and play the notes
class RandomAlarm(tk.Frame):
    def __init__(self, master, appearance_data, sound_data):
        super().__init__(master)
        self.sound = Sound(master, **sound_data)
        self.toast = Toast(master, **appearance_data)
        self.sound.bind('<<NOTE_OFF>>', self.on_note_off)
        self.sound.pack()
        self.pack()
        self.ring()
    
    def ring(self):
        print(self.sound.remaining_notes)
        if self.sound.remaining_notes <= 0:
            self.remove()
        else:
            self.sound.remaining_notes -= 1
            self.sound.play()
    
    def on_note_off(self, event):
        self.ring()
    
    def remove(self):
        self.sound.destroy()
        self.toast.destroy()
        self.destroy()


class Sound(tk.Frame):
    def __init__(self, master, **kwargs):
        self.__dict__.update(kwargs)
        super().__init__(master)
        
        pygame.midi.init()
        self.midi_player = pygame.midi.Output(device_id=0)
        
        self.remaining_notes = random.randint(*self.notes_amount)
        
    def play(self):
        # http://www.ccarh.org/courses/253/handout/gminstruments/
        instrument = random.randint(*self.instruments)
        self.midi_player.set_instrument(instrument)
        
        note = random.randint(*self.notes)
        self.midi_player.note_on(note, self.volume)
        
        delay = random.uniform(*self.notes_length)
        delay = int(delay * 1000)
        self.after(delay, lambda: self.note_off(note))
    
    def note_off(self, note):
        self.midi_player.note_off(note, self.volume)
        self.event_generate('<<NOTE_OFF>>')
    
    def __del__(self):
        del self.midi_player
        pygame.midi.quit()


class Toast(tk.Toplevel):
    def __init__(self, master, **kwargs):
        self.__dict__.update(kwargs)
        super().__init__(master)
        
        self.title('Alarm toast message')
        self.overrideredirect(True)             # hide the window border and top bar
        self.attributes('-topmost', True)       # make it top level
        self.hide()
        
        if self.is_bg_transparent:
            if self.color == self.bg_color:
                self.bg_color = 'green' if self.color == 'red' else 'red'
            self.attributes('-transparentcolor', self.bg_color)
        
        # create message
        label_font = tkfont.Font(
            family=self.font_family,
            size=self.font_size, 
            weight='bold' if self.font_bold else 'normal',
            slant='italic' if self.font_italic else 'roman',
            underline=self.font_underline,
            overstrike=self.font_overstrike
        )
        label = tk.Label(self, bg=self.bg_color, fg=self.color, text=self.message, 
                         font=label_font)
        label.pack()
        
        # get the size of the window and the screen
        self.update()
        self.size_x, self.size_y = self.winfo_width(), self.winfo_height()
        self.max_x = self.winfo_screenwidth() - self.size_x
        self.max_x = self.winfo_screenheight() - self.size_y
    
    def place_random(self):
        # place at a random position on the screen
        x = random.randint(0, self.max_x)
        y = random.randint(0, self.max_x)
        self.geometry(f'{self.size_x}x{self.size_y}+{x}+{y}')
        self.update()
    
    def place_fixed(self, position):
        pass
    
    def show(self):
        self.attributes('-alpha', 1.0)
        self.update()
    
    def hide(self):
        self.attributes('-alpha', 0.0)
        self.update()