from displayer import Displayer
from wall import Wall
from snake import Snake
from bug import Bug

import time
import threading
import msvcrt

displayer = Displayer()
wall = Wall()
snake = Snake()
bug = Bug(snake.points)

running = True


class InputThreading(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global running, snake
        while running:
            c = str(msvcrt.getch())  # 输入读取，无需回车
            if c == "b'q'":
                running = False
            elif c == "b'w'":
                snake.set_toward("UP")
            elif c == "b's'":
                snake.set_toward("DOWN")
            elif c == "b'a'":
                snake.set_toward("LEFT")
            elif c == "b'd'":
                snake.set_toward("RIGHT")


input_threading = InputThreading()  # 主线程进行时子线程也进行
input_threading.start()

while running:
    dead = snake.action(bug, wall.points)
    if dead:
        print("\n方儿子死了！！\n按Q退出\n")
        break
    displayer.expend_points(snake.points)
    displayer.expend_points(wall.points)
    displayer.expend_points(bug.point)

    displayer.draw_graphics(snake.score)
    displayer.clear()
    time.sleep(snake.sleep_time)
