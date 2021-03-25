from tkinter import *

class Menu:
    def __init__(self):
        root = Tk()
        root.title("TOthello")
        root.state("zoomed")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        h = h/2
        print(w,'x', h)
        canvas = Canvas(root, width=h, height=h, background='yellow')
        canvas.create_line(h/2, 0, h/2, h)
        for i in range(8):
            canvas.create_line((h/8)*i, 0, (h/8)*i, h)
            canvas.create_line(0, (h/8)*i,h, (h/8)*i)
        canvas.pack()
        root.mainloop ()