import tkinter
import time

def play_animation():
    canvas.move(ovl,2,2)
    canvas.update()
    top.after(50, play_animation)

x, y = 10, 10

top = tkinter.Tk()

top.geometry('600x600')

top.title('Unknow')

top.resizable(False,False)

top.wm_attributes('-topmost',1)

canvas = tkinter.Canvas(top, width=600,height=600,bd=0,highlightthickness=0)

canvas.create_rectangle(0,0,600,600,fill='grey')

ovl = canvas.create_oval(10,10,60,60,fill='red')

canvas.pack()

top.update()

play_animation()

tkinter.mainloop()