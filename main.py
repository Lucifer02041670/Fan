import turtle

window = turtle.Screen()
Pan = turtle.Turtle()

window.setup(500, 500)

Get = input("Каким числом будет константа: Целое, Комплексное? \n Введите номер:")

if Get == "1":
    Com = int(input())
elif Get == "2":
    h = float(input())
    g = float(input())
    Com = complex(h, g)
else:
    print("Введен неверный номер!")
    exit()

P = 200
scale = P / 3
n_iter = 100
Pan.speed(0)


def mnJul():
    x = Pan.position()[0]
    y = Pan.position()[1]
    for x in range(-P, P):
        for y in range(-P, P):
            a = x / scale
            b = y / scale
            z = complex(a, b)
            for n in range(n_iter):
                z = z ** 2 + Com
                if abs(z) > 2:
                    break
            else:

                Pan.up()
                Pan.setposition(x, y)
                Pan.down()
                Pan.setposition(x + 1, y + 1)


def Ex():
    exit()


window.onkey(mnJul, "Up")

window.listen()
window.mainloop()
