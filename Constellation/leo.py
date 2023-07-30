import turtle

class Solution:
  def draw(self):
    my_window = turtle.Screen()
    my_window.bgcolor("black")
    my_pen = turtle.Turtle()
    my_pen.speed("fastest")
    my_pen.color("yellow")
    my_pen.hideturtle()

    # Draw Leo constellation
    stars = [
      (-200, 0, 30),
      (-130, 100, 30),
      (200, 250, 20),
      (150, 270, 25),
      (270, 400, 35),
      (250, 400, 25),
      (270, 260, 20),
      (320, 200, 30),
      (-100, 70, 25),
    ]

    for i, (x, y, size) in enumerate(stars):
      # self.drawStar(my_pen, x, y, size)
      self.drawCircle(my_pen, x, y, 3, "white")
      my_pen.penup()
      my_pen.goto(x, y)
      my_pen.pendown()
      my_pen.goto(stars[i - 1][0], stars[i - 1][1])
        
    

  def drawCircle(self, pen, x, y, radius, color):
    pen.up()
    pen.goto(x, y)
    pen.down()

    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


  def drawStar(self, pen, x, y, size):
    pen.up()
    pen.goto(x, y)
    pen.down()

    pen.fillcolor("white")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()


if __name__ == '__main__':
  solution = Solution()
  solution.draw()

  turtle.done
  turtle.Screen().exitonclick()