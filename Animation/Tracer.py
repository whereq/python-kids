# importing package
import turtle

# loop for motion with
# default tracer as 1
for i in range(20):
	turtle.forward(1+1*i)
	turtle.right(45)

# set tracer values as (2,0)
# 2 -> for screen update
# 0 -> delay
turtle.tracer(n=2, delay=0)

# loop for motion with
# above tracer values
for i in range(20, 40):
	turtle.forward(1+1*i)
	turtle.right(45)

# set tracer values as (1,50)
# 1 -> for screen update
# 50 -> delay
turtle.tracer(n=1, delay=50)

# loop for motion with
# above tracer values
for i in range(40, 60):
	turtle.forward(1+1*i)
	turtle.right(45)
