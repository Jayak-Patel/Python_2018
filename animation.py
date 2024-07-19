# Updated Animation Starter Code

from tkinter import *

####################################
# customize these functions
####################################

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def init(data):
    data.x=600
    data.y=0

def mousePressed(event, data):
    data.x=event.x
    data.y=event.y

def keyPressed(event, data):
    if event.keysym=="w":
        data.y=data.y-15
    if event.keysym=="a":
        data.x=data.x-15
    if event.keysym=="s":
        data.y=data.y+15
    if event.keysym=="d":
        data.x=data.x+15

def timerFired(data):
    data.y=data.y-1

def redrawAll(canvas, data):
    canvas.create_rectangle(0,0,600,600,fill="light blue")
    canvas.create_oval(data.x-100,data.y-100,data.x+100,data.y+100,fill="yellow")
    lightbrown = rgbString(229, 175, 105)
    canvas.create_rectangle(150,300,450,600,fill="red")
    canvas.create_polygon(150,300,450,300,300,250,fill="purple")
    canvas.create_rectangle(250,500,350,600, fill=lightbrown)
    canvas.create_line(300,500,300,600)
    
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 600)
