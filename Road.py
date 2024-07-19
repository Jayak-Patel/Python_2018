# Updated Animation Starter Code
 #import magic
import random
import tensorflow as tf
from tkinter import *
 
####################################
# customize these functions
####################################
def car(data,xPos,cycles,first=False):
    tf.reset_default_graph()
    input_data=tf.placeholder(dtype=tf.float32,shape=None)
    output_data=tf.placeholder(dtype=tf.float32,shape=None)
    slope=tf.Variable(0.1,dtype=tf.float32)
    intercept=tf.Variable(3,dtype=tf.float32)
    model_operation=slope*input_data+intercept
    error=model_operation-output_data
    squared_error=tf.square(error)
    loss=tf.reduce_mean(squared_error)
    optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.005)
    train=optimizer.minimize(loss)
    init=tf.global_variables_initializer()
    x_values=[]
    y_values=[]
    for i in range(2):
        if first:
            x_values.append(data.topX[xPos+i]/100)
            y_values.append(data.topY[xPos+i]/100)
        else:
            x_values.append(data.topX[xPos+i+1]/100)
            y_values.append(data.topY[xPos+i+1]/100)
    with tf.Session() as sess:
        sess.run(init)
        for i in range(cycles):
            sess.run(train,feed_dict={input_data:x_values,output_data:y_values})
            if i>=cycles-1:
                answer=sess.run(slope)
    return answer
    
 
def init(data):
    
    data.carx=0
    data.cary=data.height/2
    data.interval=0
    # For the road
    data.thick = 100
    data.roadlen = 8
    data.randHeight = random.randint(data.height/2-data.thick, data.height/2+data.thick)
    data.topX = [0]
    data.botX = [0]
    data.topY = [data.height/2 - (data.thick/2)]
    data.botY = [data.height/2 + (data.thick/2)]
    # Maing the road peices    
    for x in range(data.roadlen):
          data.topX.append((x+1)*data.width/data.roadlen)
          data.botX.append((x+1)*data.width/data.roadlen)
          data.randHeight = data.topY[x]+random.randint(-data.thick, data.thick)
          data.topY.append(data.randHeight)
          data.botY.append(data.randHeight + data.thick)
    data.slope=car(data,int(data.carx//(data.width/data.roadlen)),10000,True)
    data.xspeed=10
    data.yspeed=data.slope*data.xspeed
 
def mousePressed(event, data):
    init(data)
 
def keyPressed(event, data):
    pass
 
def timerFired(data):
    data.interval=data.interval+data.xspeed
    if data.interval>=data.width/data.roadlen:
        data.slope=car(data,int(data.carx//(data.width/data.roadlen)),10000)
        data.yspeed=data.slope*data.xspeed
        data.interval=0
    data.carx=data.carx+data.xspeed
    data.cary=data.cary+data.yspeed
    if data.carx>=1000:
        init(data)
        
 
def redrawAll(canvas, data):
    # Creates Road
    for i in range(data.roadlen):
        canvas.create_polygon(data.topX[i], data.topY[i], data.topX[i+1],
                              data.topY[i + 1], data.botX[i + 1], data.botY[i + 1],
                              data.botX[i], data.botY[i], fill =  "gray")
    canvas.create_rectangle(data.carx-50,data.cary-25,data.carx+50,data.cary+25,fill="silver")
             
 
####################################
# use the run function as-is
####################################
 
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='green', width=0)
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
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
 
run(1200, 600)
