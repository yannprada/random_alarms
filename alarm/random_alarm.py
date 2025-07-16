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
class RandomAlarm:
    def __init__(self, appearance_data, sound_data):
        self.appearance_data = appearance_data
        self.sound_data = sound_data
