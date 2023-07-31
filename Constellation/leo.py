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
    # x, y, radius, color, if connect to previous star
    stars = [
      (-200, 0, 3, "white", 1),
      (-130, 100, 3, "white", 1),
      (200, 250, 3, "white", 1),
      (150, 270, 3, "white", 1),
      (270, 400, 3, "white", 1),
      (250, 400, 3, "white", 1),
      (270, 260, 3, "white", 1),
      (320, 200, 3, "white", 1),
      (-100, 70, 3, "white", 1),
    ]

    for i, (x, y, r, color, isConnected) in enumerate(stars):
      self.drawCircle(my_pen, x, y, r, color)
      my_pen.penup()
      my_pen.goto(x, y)
      my_pen.pendown()

      if isConnected == 1: 
        my_pen.goto(stars[i - 1][0], stars[i - 1][1])
        
    

  def drawCircle(self, pen, x, y, radius, color):
    pen.up()
    pen.goto(x, y)
    pen.down()

    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


if __name__ == '__main__':
  solution = Solution()
  solution.draw()

  turtle.done
  turtle.Screen().exitonclick()