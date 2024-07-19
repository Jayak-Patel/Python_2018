# Updated Animation Starter Code
import math
import random
from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.x1=60
    data.y1=50
    data.x2=540
    data.y2=50
    data.ballx=300
    data.bally=300
    data.directionx=5
    data.directiony=5

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym=="w" and data.y1>0:
        data.y1=data.y1-15
    if event.keysym=="s" and data.y1<600:
        data.y1=data.y1+15
    '''
    if event.keysym=="Up" and data.y2>0:
        data.y2=data.y2-15
    if event.keysym=="Down" and data.y2<600:
        data.y2=data.y2+15
    '''
        
def timerFired(data):
    global left
    global right
    data.ballx=data.directionx+data.ballx
    data.bally=data.directiony+data.bally
    if data.ballx>data.x2-12 and abs(data.y2-data.bally)<100:
        data.directionx*=-1.5
        data.ballx=data.x2-12
        data.directiony+=random.randint(-2,2)
    if data.ballx<data.x1+12 and abs(data.y1-data.bally)<100:
        data.directionx*=-1.5
        data.ballx=data.x1+12
        data.directiony+=random.randint(-2,2)
    if data.bally>=600:
        data.directiony*=-1
    if data.bally<=0:
        data.directiony*=-1
   # if data.directionx>=30:
    #    data.directionx=30
    if data.ballx>=650:
        left=left+1
        init(data)
    if data.ballx<=-50:
        right=right+1
        init(data)
    data.y2+=(data.bally-data.y2)/10

def redrawAll(canvas, data):
    global left
    global right
    canvas.create_rectangle(data.x1-15,data.y1-50,data.x1+15,data.y1+50,fill="white")
    canvas.create_rectangle(data.x2-15,data.y2-50,data.x2+15,data.y2+50,fill="white")
    canvas.create_rectangle(data.ballx+7,data.bally+7,data.ballx-7,data.bally-7,fill="white")
    canvas.create_text(data.width/2,100,text=str(left)+" - "+str(right), fill="white",font="bold 20")
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='black', width=0)
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

global right
global left
right=0
left=0
run(600,600)
