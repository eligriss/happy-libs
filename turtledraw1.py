import turtle
# See also: http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
colors = ["red", "blue", "pink", "purple","orange","green","yellow","salmon", "alice blue", "azure", "brown"]
t = turtle.Pen()
turtle.bgcolor("black")
sides = 8
for x in range(360):
  t.pencolor(colors[x%sides])
  t.forward(x * 3/sides + x)
  t.left(360/sides + 1)
  t.width(x*sides/200)
