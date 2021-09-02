import tkinter as tk

MAIN_HEIGHT = 600
MAIN_WIDTH = 1000

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Main container frame
        self.main_frame = tk.Frame(parent, bg="Red", width=MAIN_WIDTH, height=MAIN_HEIGHT)
        self.main_frame.configure(relief='groove',borderwidth="3")
        self.main_frame.pack(padx = 5, pady = 5,anchor=tk.W, fill=tk.Y, expand=False)

        # Left frame - character img and stats

        # Right top frame - randomness center

        # Right bottom frame - equipment (i guess)

        

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.title("RP UI")
    root.geometry(f"{MAIN_WIDTH}x{MAIN_HEIGHT}")
    root.resizable(False,False)
    root.mainloop()