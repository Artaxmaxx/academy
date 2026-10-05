import turtle as t

for i in range(50):
    i=int(i)
    t.colormode(255)
    t.color(i * 3, i * 3, 80 + i * 2)
    t.circle(i)