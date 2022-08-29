import tkinter as tk
class RootWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('340x250')
        self.wait_visibility(self)
        self.wm_attributes('-alpha', 0)

root = RootWindow()
root.mainloop()
