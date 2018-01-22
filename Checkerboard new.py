from turtle import *
def square (pencolor):
    color (pencolor)
    begin_fill()
    for x in range(4): #This loop will make one square
        left(90)
        forward(20)
    end_fill()
    

def rowR(col): #This makes the red Row
    pu() #brings the pen up
    goto(0, col)
    pd() #brings the pen down 
    for i in range(4):
        square('red') #red square
        forward(20) #forward
        square('black') # black square
        if i == 3: 
            break
        forward(20)
        
def rowB(col): #This makes the black Row 
    pu()
    goto(0, col)
    pd()
    for i in range(4):
        square('black')
        forward(20)
        square('red')
        if i == 3:
            break
        forward(20)
        
def Red_loop(): #This loops RowR
    speed(0)
    for i in range(1, 8, 2): #start at row 1
        rowR(i * 20)
print (Red_loop())

def Black_loop(): #This loops RowB
    for i in range(0,8,2): #start at row 0
        rowB(i * 20)
print (Black_loop())

