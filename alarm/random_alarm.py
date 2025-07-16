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
class RandomAlarm(tk.Toplevel):
    def __init__(self, appearance_data, sound_data):
        super().__init__()
        self.appearance_data = appearance_data
        self.sound_data = sound_data
        
        pygame.midi.init()
        self.midi_player = pygame.midi.Output(device_id=0)
        
        self.remaining_notes = random.randint(*self.sound_data['notes_amount'])
        self.play()
    
    def play(self):
        if self.remaining_notes <= 0:
            self.destroy()
        
        self.remaining_notes -= 1
        
        # http://www.ccarh.org/courses/253/handout/gminstruments/
        instrument = random.randint(*self.sound_data['instruments'])
        self.midi_player.set_instrument(instrument)
        
        note = random.randint(*self.sound_data['notes'])
        self.midi_player.note_on(note, self.sound_data['volume'])
        
        delay = random.uniform(*self.sound_data['notes_length'])
        self.after(int(delay * 1000), lambda: self.note_off(note))
    
    def note_off(self, note):
        self.midi_player.note_off(note, self.sound_data['volume'])
        self.play()
    
    def __del__(self):
        del self.midi_player
        pygame.midi.quit()
