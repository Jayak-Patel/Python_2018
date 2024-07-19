from tkinter import *
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)


def draw(canvas, width, height):
    canvas.create_rectangle(0,0,600,600,fill="light blue")
    lightbrown = rgbString(229, 175, 105)
    canvas.create_rectangle(150,300,450,600,fill="red")
    canvas.create_polygon(150,300,450,300,300,250,fill="purple")
    canvas.create_rectangle(250,500,350,600, fill=lightbrown)
    canvas.create_line(300,500,300,600)
 #   canvas.create_rectangle(
    

def runDrawing(width=600, height=600):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()



runDrawing(600, 600)
