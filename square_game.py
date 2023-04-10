import tkinter
from random import randint
from tkinter import messagebox

x1, y1, x2, y2 = 100, 400, 200, 500 # начальные координаты квадрата
xa1, ya1, xa2, ya2 = 425, 275, 475, 325 # начальные координаты яблока
count_apple = 0
rand = 0
supeeeeer_speed = 0

def change_color(): # функция для смены цвета у квадрата
    try:
        canvas.itemconfig(square, fill= '#' + str(hex(randint(0,255))[2:]) + str(hex(randint(0,255))[2:]) + str(hex(randint(0,255)))[2:])
    except tkinter.TclError:
        pass

def change_apple(): # функция для смены положения яблока и увеличения счетчикa
    global count_apple, rand, supeeeeer_speed
    global stick, leaflet, apple, square
    global x1, x2, y1, y2, xa1, xa2, ya1, ya2
    if (xa1 in range(x1, x2 + 1) or xa2 in range(x1, x2 + 1)) and (ya1 in range(y1, y2 + 1) or ya2 in range(y1, y2 + 1)):
        canvas.delete(apple)
        canvas.delete(stick)
        canvas.delete(leaflet)
        xa1 = randint(0, 750)
        xa2 = xa1 + 50
        ya1 = randint(0, 550)
        ya2 = ya1 + 50
        last_rand = rand
        rand = randint(0, 20)
        if last_rand == 20:
            count_apple += 5
        elif last_rand == 19:
            supeeeeer_speed = 20
            count_apple += 1
        elif last_rand == 18:
            supeeeeer_speed = 0
            count_apple += 1
        else:
            count_apple += 1
        if rand == 20:
            apple = canvas.create_oval(xa1, ya1, xa2, ya2, fill='Yellow')
        elif rand == 19:
            apple = canvas.create_oval(xa1, ya1, xa2, ya2, fill='Blue')
        elif rand == 18:
            apple = canvas.create_oval(xa1, ya1, xa2, ya2, fill='Green')
        else:
            apple = canvas.create_oval(xa1, ya1, xa2, ya2, fill='Red')
        leaflet = canvas.create_rectangle(xa1 + 28, ya1 - 15, xa1 + 38, ya1 - 5, fill='Green')
        stick = canvas.create_rectangle(xa1 + 22, ya1 - 15, xa2 - 22, ya1, fill='Brown')
        label['text'] = f'Apples: {count_apple}'

def move_left(): # двигает квадрат влево
    global square
    global x1, x2,y1,y2, supeeeeer_speed
    if x1 <= 0 or x2 >= 800 or y1 <= 0 or y2 >= 600:
        messagebox.showerror('lose', 'you lose')
        window.quit()
    else:
        canvas.delete(square)
        x1 -= (20 + supeeeeer_speed)
        x2 -= (20 + supeeeeer_speed)
        square = canvas.create_rectangle(x1, y1, x2, y2)
        change_color()
        change_apple()

def move_right():# двигает квадрат вправо
    global square
    global x1, x2, y1, y2, supeeeeer_speed
    if x1 <= 0 or x2 >= 800 or y1 <= 0 or y2 >= 600:
        messagebox.showerror('lose', 'you lose')
        window.quit()
    else:
        canvas.delete(square)
        x1 += (20 + supeeeeer_speed)
        x2 += (20 + supeeeeer_speed)
        square = canvas.create_rectangle(x1, y1, x2, y2)
        change_color()
        change_apple()

def move_up():# двигает квадрат вверх
    global square
    global x1, x2, y1, y2, supeeeeer_speed
    if x1 <= 0 or x2 >= 800 or y1 <= 0 or y2 >= 600:
        messagebox.showerror('lose', 'you lose')
        window.quit()
    else:
        canvas.delete(square)
        y1 -= (20 + supeeeeer_speed)
        y2 -= (20 + supeeeeer_speed)
        square = canvas.create_rectangle(x1, y1, x2, y2)
        change_color()
        change_apple()

def move_down():# двигает квадрат вниз
    global square
    global x1, x2, y1 ,y2, supeeeeer_speed
    if x1 <= 0 or x2 >= 800 or y1 <= 0 or y2 >= 600:
        messagebox.showerror('lose', 'you lose')
        window.quit()
    else:
        canvas.delete(square)
        y1 += (20 + supeeeeer_speed)
        y2 += (20 + supeeeeer_speed)
        square = canvas.create_rectangle(x1, y1, x2, y2)
        change_color()
        change_apple()

def key_presed(event):#функция  овечающая за движение по клавишам
    if event.keysym == 'w':
        move_up()
    elif event.keysym == 'a':
        move_left()
    elif event.keysym== 's':
        move_down()
    elif event.keysym == 'd':
        move_right()

def rules():
    messagebox.showinfo('Rules', 'Red apple - 1\n'
                                   'Gold apple - 5\n'
                                   'Blue apple - 1, + 20 speed\n'
                                   'Green apple - 1, normal speed\n'
                                   'keyboard controls - wasd\n'
                                   'if you crash into the border, you lose\n'
                                   'Have a good game!')

window = tkinter.Tk()
window.geometry('1000x750')
window.title('Window')
window.bind('<Key>', key_presed)
label = tkinter.Label(text=f'Apples: {count_apple}', font=20)
label.pack()
canvas = tkinter.Canvas(width=800, height=600, bg='White')
canvas.pack()

leaflet = canvas.create_rectangle(453, 260, 463, 270, fill='Green')
stick = canvas.create_rectangle(447, 260, 453, 275, fill='Brown')
apple = canvas.create_oval(xa1, ya1, xa2, ya2, fill='Red')
square = canvas.create_rectangle(x1, y1, x2, y2, fill='Green')

button_left = tkinter.Button(text='left',width=5, height=2, command=move_left)
button_left.place(x = 400, y = 660)
button_right = tkinter.Button(text='right',width=5, height=2, command=move_right)
button_right.place(x = 550, y = 660)
button_up = tkinter.Button(text='up',width=5, height=2, command=move_up)
button_up.place(x = 475, y = 640)
button_down = tkinter.Button(text='down',width=5, height=2, command=move_down)
button_down.place(x = 475, y = 700)
button_rules = tkinter.Button(text='Rules',width=10, height=2, command=rules)
button_rules.place(x = 800, y = 650)
window.mainloop()