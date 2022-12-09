import turtle as tur
import colorsys as cs
tur.setup(800,800)
tur.speed(100000)
tur.width(2)
tur.bgcolor("black")
for j in range(25):
	for i in range(8):
		tur.color(cs.hsv_to_rgb(i/10, j/25,1))
		tur.right(90)
		tur.circle(200-j*4,90)
		tur.left(90)
		tur.circle(200-j*4,90)
		tur.right(180)
		tur.circle(50,24)
tur.hideturtle()
tur.done()