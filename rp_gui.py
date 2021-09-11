from os import makedirs, stat
import tkinter as tk
from tkinter.ttk import Notebook

from stats_cell import stats_cell

from PIL import Image, ImageTk

# CONSTANTS
MAIN_WIN_HEIGHT = 600
MAIN_WIN_WIDTH = 1000

CHAR_IMG_SIZE = 420

#tmp
STAT_LIST = ["Siła", "Zręczność", "Budowa", "Inteligencja", "Mądrość", "Charyzma"]
STAT_VALS = [5,5,5,5,5,5]

def rnrImage(path: str) -> ImageTk.PhotoImage:
    """Read and Resize Image from path"""
    img = Image.open(path)
    width, height = img.size
    if max(width,height) > CHAR_IMG_SIZE:
        ratio = min(CHAR_IMG_SIZE/width, CHAR_IMG_SIZE/height)
        img = img.resize((round(width*ratio),round(height*ratio)),Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Menu bar
        self.menubar = tk.Menu(parent)

        self.filemenu = tk.Menu(self.menubar, tearoff= 0)
        self.filemenu.add_command(label = "Stwórz")
        self.filemenu.add_command(label = "Wczytaj")
        self.filemenu.add_command(label = "Zapisz")
        self.menubar.add_cascade(label = "Postać", menu = self.filemenu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label = "How to")
        self.helpmenu.add_command(label = "About")
        self.menubar.add_cascade(label = "Help", menu = self.helpmenu)

        self.master.configure(menu = self.menubar)

        # Main container frame
        self.main_frame = tk.Frame(parent, bg="Red", width=MAIN_WIN_WIDTH, height=MAIN_WIN_HEIGHT)
        self.main_frame.config(relief='groove',borderwidth="3")
        self.main_frame.pack(padx = 5, pady = 5, anchor=tk.W, fill=tk.BOTH, expand = True)

        # Left frame - character img and stats
        self.char_frame = tk.Frame(self.main_frame, bg="Green")
        self.char_frame.place(x = 0, y = 0, anchor=tk.NW, width=MAIN_WIN_WIDTH*0.43, height=MAIN_WIN_HEIGHT-17)

        ## Name label
        self.char_name_lab = tk.Label(self.char_frame, text="<character name here>")
        self.char_name_lab.place(relx = 0.5, y = 17, anchor=tk.CENTER)
        
        ## Img frame
        self.char_img_frame = tk.Frame(self.char_frame, bg = "White")
        self.char_img_frame.config(relief='groove',borderwidth="2")
        self.char_img_frame.place(rely = 0.43, relx=0.5,anchor=tk.CENTER, width=MAIN_WIN_WIDTH*0.43, height=MAIN_WIN_WIDTH*0.43)

        ### Temporary image
        try:
            self.photo = rnrImage("char_images/char_elfff.png") 
        except FileNotFoundError:
            self.photo = rnrImage("char_images/cool_guy.png")
        self.img_label = tk.Label(self.char_img_frame, image=self.photo)
        self.img_label.place(relx= 0.5, rely = 0.5, anchor=tk.CENTER)

        ## Stats frame
        self.char_stats_frame = tk.Frame(self.char_frame)
        self.char_stats_frame.config(relief='groove',borderwidth="2")
        self.char_stats_frame.place(rely = 0.899, relx=0.5, anchor=tk.CENTER,width=MAIN_WIN_WIDTH*0.43, height=115)
        
        ### Stats table
        self.table_container = tk.Frame(self.char_stats_frame)
        cooridates = [(1,1),(2,1),(1,2),(2,2),(1,3),(2,3)] #lazy way, should change
        self.stat_wig_cont = []
        for stat_name,stat_val,xy in zip(STAT_LIST,STAT_VALS, cooridates):
            w = stats_cell(self.table_container, stat_name, stat_val)
            w.grid(row=xy[0], column=xy[1])
            self.stat_wig_cont.append(w)
        self.table_container.place(rely= 0.5, relx= 0.5, anchor=tk.CENTER)

        # Top right frame - randomness center
        self.rand_frame = tk.Frame(self.main_frame, bg = "Yellow")
        self.rand_frame.config(relief='groove',borderwidth="2")
        self.rand_frame.place(relx = 1, rely = 0, anchor=tk.NE, width=MAIN_WIN_WIDTH*0.5535, height=MAIN_WIN_HEIGHT*0.5)

        self.rand_label = tk.Label(self.rand_frame, text= "<dice table here>")
        self.rand_label.place(relx= 0.5, rely = 0.5, anchor=tk.CENTER)

        # Bottom right frame - equipment
        self.eq_frame = tk.Frame(self.main_frame, bg = "Orange")
        self.eq_frame.config(relief='groove',borderwidth="2")
        self.eq_frame.place(relx = 1, rely = 1, anchor=tk.SE, width=MAIN_WIN_WIDTH*0.5535, height=MAIN_WIN_HEIGHT*0.475)

        ## Equipment notebook for reasons?
        self.eq_notebook = Notebook(self.eq_frame)
        self.eq_page1 = tk.Frame(self.eq_notebook)
        self.eq_text = tk.Text(self.eq_page1, width=67, height= 15, wrap=tk.WORD)
        self.eq_text.pack()
        self.eq_page2 = tk.Frame(self.eq_notebook)
        self.eq_notebook.add(self.eq_page1, text = "Page 1")
        self.eq_notebook.add(self.eq_page2, text = "Page 2")
        
        self.eq_notebook.place(relx=0.5,rely= 0.5, anchor=tk.CENTER)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.title("RP UI")
    root.geometry(f"{MAIN_WIN_WIDTH}x{MAIN_WIN_HEIGHT}")
    root.resizable(False,False)
    root.mainloop()
