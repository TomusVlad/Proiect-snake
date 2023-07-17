import turtle
import random


point_size = 1
delay = 100
score = 0
dist = {
    "Up": (0, 10),
    "Down": (0, -10),
    "Left": (-10, 0),
    "Right": (10, 0)
}


def reset():
    global snake, s_direction, point_position, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 60]]
    s_direction = "Up"
    point_position = get_random_point_position()
    point.goto(point_position)
    move_snake()


def move_snake():
    global s_direction

    head = snake[-1].copy()
    head[0] = snake[-1][0] + dist[s_direction][0]
    head[1] = snake[-1][1] + dist[s_direction][1]

    if head in snake[:-1]:
        reset()
    else:
        snake.append(head)
        if not point_collision():
            snake.pop(0)

        if snake[-1][0] > 700 / 2:
            snake[-1][0] -= 700
        elif snake[-1][0] < - 700 / 2:
            snake[-1][0] += 700
        elif snake[-1][1] > 350 / 2:
            snake[-1][1] -= 350
        elif snake[-1][1] < - 350 / 2:
            snake[-1][1] += 350

            reset()
        pen.clearstamps()

        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()

        turtle.ontimer(move_snake, delay)


def point_collision():
    global point_position
    if get_distance(snake[-1], point_position) < 20:
        point_position = get_random_point_position()
        point.goto(point_position)
        return True
    return False


def get_random_point_position():
    x = random.randint(- 700 / 2 + point_size, 700 / 2 - point_size)
    y = random.randint(- 350 / 2 + point_size, 350 / 2 - point_size)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance




def down():
    global s_direction
    if s_direction != "Up":
        s_direction = "Down"


def left():
    global s_direction
    if s_direction != "Right":
        s_direction = "Left"

def up():
    global s_direction
    if s_direction != "Down":
        s_direction = "Up"


def right():
    global s_direction
    if s_direction != "Left":
        s_direction = "Right"

screen = turtle.Screen()
screen.setup(700, 350)
screen.title("Snake_Tomus_Vlad")
screen.bgcolor("white")
screen.setup(700,350)
screen.tracer(0)

pen = turtle.Turtle("circle")
pen.penup()

point = turtle.Turtle()
point.shape("circle")
point.color("black")
point.shapesize(point_size )
point.penup()

screen.listen()
screen.onkey(up, "Up")
screen.onkey(right, "Right")
screen.onkey(down, "Down")
screen.onkey(left, "Left")



reset()
turtle.done()





