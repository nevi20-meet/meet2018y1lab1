import turtle

# Everything that comes after the # is a 
# comment.
# It is a note to the person reading the code.
# The computer ignores it.
# Write your code below here...

turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-200,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
turtle.pendown() #Put the pen down to start
                 #drawing
#Draw the M:
turtle.goto(-200,-100+200) 
turtle.goto(-200+50,-100) 
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)
#Draw the E:
turtle.penup() #Pick up the  pen so it doesn't
               #draw
turtle.goto(-200+150,-100)
turtle.pendown()
turtle.goto(-200+150,+100)
turtle.goto (-200+250,+100)
turtle.goto (-200+150,+100)
turtle.goto (-200+150,+0)
turtle.goto (-200+250,+0)
turtle.goto (-200+150,+0)
turtle.goto (-200+150,-100)
turtle.goto (-200+250,-100)
#Draw the E:
turtle.penup() #Pick up the  pen so it doesn't
               #draw
turtle.goto(-200+300,-100)
turtle.pendown()
turtle.goto(-200+300,+100)
turtle.goto (-200+400,+100)
turtle.goto (-200+300,+100)
turtle.goto (-200+300,+0)
turtle.goto (-200+400,+0)
turtle.goto (-200+300,+0)
turtle.goto (-200+300,-100)
turtle.goto (-200+400,-100)
#Draw the T:
turtle.penup() #Pick up the pen so it doesn't
               #Draw
turtle.goto (-200+500,-100)
turtle.pendown()
turtle.goto (-200+500,+100)
turtle.goto (-200+450,+100)
turtle.goto (-200+550,+100)

# ...and end it before the next line.
turtle.mainloop()
