import pygame.midi
import random
import tkinter as tk

# test data:
# appearance_data:
# {'alarm_position': '11', 'color': '#000000', 'bg_color': '#8080ff', 'font_family': 
    # 'System', 'is_position_random': False, 'move_each_note': False, 
    # 'is_bg_transparent': True, 'font_size': 10, 'font_bold': False, 
    # 'font_italic': False, 'message': 'Voluptate hic ...', 
    # 'font_underline': False, 'font_overstrike': False}
# sound_data:
# {'volume': 35, 'instruments': [0, 127], 'notes': [0, 127], 'notes_length': [0.1, 8], 
# 'notes_amount': [6, 6]}

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
