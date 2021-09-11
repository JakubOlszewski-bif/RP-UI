import tkinter as tk
from tkinter.font import Font
from tkinter.ttk import Spinbox

class stats_cell(tk.Frame):
    def __init__(self, parent, stat_name: str, stat_value: int, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.stat_name = stat_name
        self.spin_val = tk.StringVar(master=self, value=stat_value, name="STAT_SPIN_VAL")

        self.container_frame = tk.Frame(master=self) #is this even necessary?
        self.container_frame.pack(fill=tk.BOTH)

        self.stat_lab = tk.Label(master=self.container_frame, text=self.stat_name)
        self.stat_val_box = Spinbox(master=self.container_frame, from_=0, to=99, textvariable=self.spin_val,
                                    font=Font(family= 'Courier', size = 13), width=5, justify=tk.CENTER)
        self.stat_lab.pack(side=tk.LEFT)
        self.stat_val_box.pack(side=tk.RIGHT)

    
    def change_stat_value(self, new_stat: int):
        self.spin_val.set(str(new_stat))