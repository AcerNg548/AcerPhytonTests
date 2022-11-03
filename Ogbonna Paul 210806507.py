from tkinter import *
from turtle import width 
def shift():
    x1,y1,x2,y2 = Canvas.bbox("Paul")
    if (x2<0 or y1<0):
        x1 = Canvas.winfo_width()
        y1 = Canvas.winfo_height()//2
        Canvas.coords("Paul",x1,y1)
    else:
        Canvas.move("Paul", -2, 0)
    Canvas.after(1000//fps,shift)
root = Tk()
root.title('Move Texx')
Canvas = Canvas(root,bg = 'black')
Canvas.pack(fill=BOTH, expand=1)
text_var = "Welcome to Mathematics Department"
text = Canvas.create_text(0, -2000,text=text_var,font=('Times New Roman',20,'bold'),fill='white',tags=("Paul",),anchor='w')
x1,y1,x2,y2 = Canvas.bbox("Paul")
width = x2-x1
height = y2-y1
Canvas['width'] = width
Canvas['height'] = height
fps = 70
shift()
root.mainloop()

## Ogbonna Paul
## 210806507
## Maths Science