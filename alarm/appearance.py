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
    tk_variable_keys = ['is_position_random', 'move_each_note', 'is_bg_transparent',
                        'font_size', 'font_bold', 'font_italic', 'message']
    
    def init(self):
        frame = self.children['!frame']
        self.move_each_note_button = frame.children['move_each_note_button']
        self.position_fixed_frame = frame.children['position_fixed_frame']
        self.color_button = frame.children['color_button']
        self.bg_color_label = frame.children['bg_color_label']
        self.bg_color_button = frame.children['bg_color_button']
        self.font_family_listbox = frame.children['font_family_listbox']
        
        # generate the options here, because less typing
        self.alarm_position = tk.StringVar()
        
        for x in range(3):
            for y in range(3):
                b = tk.Radiobutton(self.position_fixed_frame, value=f'{x}{y}', 
                                   variable=self.alarm_position)
                b.grid(row=x, column=y)
        
        # populate font families
        for family in FONT_FAMILIES:
            self.font_family_listbox.insert('end', family)
        
        self.after(100, self.post_init)
    
    def post_init(self):
        # manual trigger to change visibility depending on checkboxes inital values
        self.on_random_button()
        self.on_transparent_button()
        
        if not self.alarm_position.get():
            # set default position to center (11 means x=1, y=1)
            self.alarm_position.set('11')
    
    def on_random_button(self):
        if self.tk_variables['is_position_random'].get():
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
            'alarm_position': self.alarm_position.get(),
            'color': self.color_button.get_color(),
            'bg_color': self.bg_color_button.get_color(),
            'font_family': self.get_font_family(),
        }
        for key in self.tk_variable_keys:
            data[key] = self.tk_variables[key].get()
        return data
    
    def load(self, data):
        self.alarm_position.set(data['alarm_position'])
        self.color_button.set_color_name(data['color'])
        self.bg_color_button.set_color_name(data['bg_color'])
        self.set_font_family(data['font_family'])
        
        for key in self.tk_variable_keys:
            self.tk_variables[key].set(data[key])
