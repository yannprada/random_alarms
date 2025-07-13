import tkinter as tk


FONT_FAMILIES =  [
    'System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 
    'MS Sans Serif', 'Small Fonts', 'Marlett', 'Arial', 'Arabic Transparent', 
    'Arial Baltic', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Arial Black', 
    'Bahnschrift Light', 'Bahnschrift SemiLight', 'Bahnschrift', 'Bahnschrift SemiBold', 
    'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde', 
    'Bahnschrift SemiCondensed', 'Bahnschrift SemiBold SemiConden', 
    'Bahnschrift Light Condensed', 'Bahnschrift SemiLight Condensed', 
    'Bahnschrift Condensed', 'Bahnschrift SemiBold Condensed', 'Calibri', 'Calibri Light', 
    'Cambria', 'Cambria Math', 'Candara', 'Candara Light', 'Comic Sans MS', 'Consolas', 
    'Constantia', 'Corbel', 'Corbel Light', 'Courier New', 'Courier New Baltic', 
    'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 
    'Ebrima', 'Franklin Gothic Medium', 'Gabriola', 'Gadugi', 'Georgia', 'Impact', 
    'Ink Free', 'Javanese Text', 'Leelawadee UI', 'Leelawadee UI Semilight', 
    'Lucida Console', 'Lucida Sans Unicode', 'Malgun Gothic', '@Malgun Gothic', 
    'Malgun Gothic Semilight', '@Malgun Gothic Semilight', 'Microsoft Himalaya', 
    'Microsoft JhengHei', '@Microsoft JhengHei', 'Microsoft JhengHei UI', 
    '@Microsoft JhengHei UI', 'Microsoft JhengHei Light', '@Microsoft JhengHei Light', 
    'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light', 
    'Microsoft New Tai Lue', 'Microsoft PhagsPa', 'Microsoft Sans Serif', 
    'Microsoft Tai Le', 'Microsoft YaHei', '@Microsoft YaHei', 'Microsoft YaHei UI', 
    '@Microsoft YaHei UI', 'Microsoft YaHei Light', '@Microsoft YaHei Light', 
    'Microsoft YaHei UI Light', '@Microsoft YaHei UI Light', 'Microsoft Yi Baiti', 
    'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB', '@PMingLiU-ExtB', 
    'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'MingLiU_MSCS-ExtB', 
    '@MingLiU_MSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic', 'MS UI Gothic', 
    '@MS UI Gothic', 'MS PGothic', '@MS PGothic', 'MV Boli', 'Myanmar Text', 
    'Nirmala UI', 'Nirmala UI Semilight', 'Nirmala Text', 'Nirmala Text Semilight', 
    'Palatino Linotype', 'Sans Serif Collection', 'Segoe Fluent Icons', 
    'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black', 
    'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light', 'Segoe UI Semibold', 
    'Segoe UI Semilight', 'Segoe UI Symbol', 'Segoe UI Variable Small Light', 
    'Segoe UI Variable Small Semilig', 'Segoe UI Variable Small', 
    'Segoe UI Variable Small Semibol', 'Segoe UI Variable Text Light', 
    'Segoe UI Variable Text Semiligh', 'Segoe UI Variable Text', 
    'Segoe UI Variable Text Semibold', 'Segoe UI Variable Display Light', 
    'Segoe UI Variable Display Semil', 'Segoe UI Variable Display', 
    'Segoe UI Variable Display Semib', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 
    'SimSun-ExtB', '@SimSun-ExtB', 'Sitka Small', 'Sitka Small Semibold', 'Sitka Text', 
    'Sitka Text Semibold', 'Sitka Subheading', 'Sitka Subheading Semibold', 
    'Sitka Heading', 'Sitka Heading Semibold', 'Sitka Display', 'Sitka Display Semibold', 
    'Sitka Banner', 'Sitka Banner Semibold', 'Sylfaen', 'Symbol', 'Tahoma', 
    'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE', 
    'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 
    'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings', 'Yu Gothic', '@Yu Gothic', 
    'Yu Gothic UI', '@Yu Gothic UI', 'Yu Gothic UI Semibold', '@Yu Gothic UI Semibold', 
    'Yu Gothic Light', '@Yu Gothic Light', 'Yu Gothic UI Light', '@Yu Gothic UI Light', 
    'Yu Gothic Medium', '@Yu Gothic Medium', 'Yu Gothic UI Semilight', 
    '@Yu Gothic UI Semilight', 'SimSun-ExtG', '@SimSun-ExtG', 'Cascadia Code ExtraLight', 
    'Cascadia Code Light', 'Cascadia Code SemiLight', 'Cascadia Code', 
    'Cascadia Code SemiBold', 'Cascadia Mono ExtraLight', 'Cascadia Mono Light', 
    'Cascadia Mono SemiLight', 'Cascadia Mono', 'Cascadia Mono SemiBold'
]


class AlarmAppearance(tk.LabelFrame):
    yaml_file = 'alarm/appearance.yaml'
    
    def init(self):
        frame = self.children['!frame']
        self.move_each_note_button = frame.children['move_each_note_button']
        self.position_fixed_frame = frame.children['position_fixed_frame']
        self.color_button = frame.children['color_button']
        self.bg_color_label = frame.children['bg_color_label']
        self.bg_color_button = frame.children['bg_color_button']
        self.font_family_listbox = frame.children['font_family_listbox']
        
        # generate the options here, because less typing...
        self.alarm_position = tk.StringVar()
        
        for x in range(3):
            for y in range(3):
                b = tk.Radiobutton(self.position_fixed_frame, value=f'{x}{y}', 
                                   variable=self.alarm_position)
                b.grid(row=x, column=y)
        
        # populate font families
        for family in FONT_FAMILIES:
            self.font_family_listbox.insert('end', family)
        
        # manual trigger to change visibility depending on checkboxes inital values
        self.on_random_button()
        self.on_transparent_button()
        
        # set default position to center (11 means x=1, y=1)
        self.after(100, lambda: self.alarm_position.set('11'))
    
    def on_random_button(self):
        if self.tk_variables['is_random'].get():
            self.position_fixed_frame.grid_remove()
            self.move_each_note_button.grid()
        else:
            self.position_fixed_frame.grid()
            self.move_each_note_button.grid_remove()
    
    def on_transparent_button(self):
        if self.tk_variables['is_bg_transparent'].get():
            self.bg_color_label.grid_remove()
            self.bg_color_button.grid_remove()
        else:
            self.bg_color_label.grid()
            self.bg_color_button.grid()
    
    def get_font_family(self):
        selection = self.font_family_listbox.curselection()
        id = selection[0] if len(selection) else 0
        return FONT_FAMILIES[id]
    
    def set_font_family(self, font_family):
        id = FONT_FAMILIES.index(font_family)
        self.font_family_listbox.select_set(id)
    
    def get_data(self):
        data = {
            'is_position_random': self.tk_variables['is_random'].get(),
            'move_each_note': self.tk_variables['move_each_note'].get(),
            'alarm_position': self.alarm_position.get(),
            'color': self.color_button.get_color(),
            'bg_color': self.bg_color_button.get_color(),
            'is_bg_transparent': self.tk_variables['is_bg_transparent'].get(),
            'font_family': self.get_font_family(),
            'font_size': self.tk_variables['font_size'].get(),
            'font_bold': self.tk_variables['font_bold'].get(),
            'font_italic': self.tk_variables['font_italic'].get(),
        }
        return data
    
    def load(self, data):
        self.tk_variables['is_random'].set(data['is_position_random'])
        self.tk_variables['move_each_note'].set(data['move_each_note'])
        self.alarm_position.set(data['alarm_position'])
        self.color_button.set_color_name(data['color'])
        self.bg_color_button.set_color_name(data['bg_color'])
        self.tk_variables['is_bg_transparent'].set(data['is_bg_transparent'])
        self.set_font_family(data['font_family'])
        self.tk_variables['font_size'].set(data['font_size'])
        self.tk_variables['font_bold'].set(data['font_bold'])
        self.tk_variables['font_italic'].set(data['font_italic'])
        
        self.on_random_button()
        self.on_transparent_button()