#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser, Menu, Spinbox, scrolledtext, messagebox as mb, filedialog as fd

import os

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""
    #===========================================
    def __init__(self, title, icon, theme):
        super().__init__()
        self.style = ttk.Style(self)
        self.resizable(False, False)
        self.title(title)
        self.iconbitmap(icon)
        self.style.theme_use(theme)

        self.init_UI()
        self.init_events()

    # INITIALIZER ==============================
    @classmethod
    def create_app(cls, app):
        return cls(app['title'], app['icon'], app['theme'])

    #===========================================
    def init_events(self):
        self.button.bind('<ButtonPress-1>', self.evt_run_ffplay)

    def init_UI(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self.main_frame)
        """
        you can specify any file extension you want to be displayed in the listbox.
        """
        for file in os.listdir():
            if file.endswith('.mp4'):
                self.listbox.insert(0, file)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.button = ttk.Button(self.main_frame, text='Start Movie')
        self.button.pack(side=tk.RIGHT, anchor=tk.NE)

    # METHODS -----------------------------------
    def evt_run_ffplay(self, event):
        if self.listbox.curselection():
            file = self.listbox.curselection()[0]

            # os.system(f'ffplay {self.listbox.get(file)}')
            os.startfile(self.listbox.get(file))

#===========================
# Start GUI
#===========================

def main(config):
    app = App.create_app(config)
    app.mainloop()

if __name__ == '__main__':
    main({
        'title' : 'Play File with FFPlay Version 1.0',
        'icon' : 'python.ico',
        'theme' : 'clam'
        })