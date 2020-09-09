from tkinter import *
root=Tk()
root.geometry("400x400")
root.title('Star Shape ')
c=Canvas(root,width="300",height="300")
c.pack()
points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
c.create_oval(60, 60, 140,140,width=4,fill='#00FF7F',outline='#0000CD')
c.create_polygon(points,outline='#008000',fill='yellow', width=3)
root.mainloop()

