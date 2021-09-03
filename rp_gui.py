import tkinter as tk
from tkinter.constants import ANCHOR, CENTER

MAIN_HEIGHT = 600
MAIN_WIDTH = 1000

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Main container frame
        self.main_frame = tk.Frame(parent, bg="Red", width=MAIN_WIDTH, height=MAIN_HEIGHT)
        self.main_frame.config(relief='groove',borderwidth="3")
        self.main_frame.pack(padx = 5, pady = 5, anchor=tk.W, fill=tk.BOTH, expand = True)

        # Left frame - character img and stats
        self.char_frame = tk.Frame(self.main_frame, bg="Green")
        self.char_frame.place(x = 0, y = 0, anchor=tk.NW, width=MAIN_WIDTH*0.43, height=MAIN_HEIGHT-17)

        ## Name label
        self.char_name_lab = tk.Label(self.char_frame, text="<character name here>")
        self.char_name_lab.place(relx = 0.5, y = 12, anchor=tk.CENTER)
        
        ## 

        """
        # Right top frame - randomness center
        self.rand_frame = tk.Frame(self.main_frame, bg="Yellow")
        self.rand_frame.grid(column=2, row = 1)

        # Right bottom frame - equipment (i guess)
        self.eq_frame = tk.Frame(self.main_frame, bg="Blue")
        self.eq_frame.grid(column=2, row = 2)
        """
        

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.title("RP UI")
    root.geometry(f"{MAIN_WIDTH}x{MAIN_HEIGHT}")
    root.resizable(False,False)
    root.mainloop()