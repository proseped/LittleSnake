from bug import Bug


class Snake:
    def __init__(self):
        self.__list = [(2, 2)]
        # 方向
        self.__toward = (0, 1)
        self.__lock = False

    # 让蛇控制时间
    @property
    def sleep_time(self):
        x = 10 - len(self.__list) * 0.5
        if x < 1:
            x = 1
        return x / 10

    # 积分
    @property
    def score(self):
        return len(self.__list) * 100 - 100

    # 蛇转向，可能为UP,DOWN,LEFT,RIGHT
    def set_toward(self, new_toward):
        if self.__lock:
            return
        dictionary = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }
        target__toward = dictionary[new_toward]
        if (target__toward[0] + self.__toward[0] == 0) and (target__toward[1] + self.__toward[1] == 0):
            return
        self.__toward = target__toward
        self.__lock = True

    @property
    def points(self):
        return self.__list

    # 编写蛇某一帧的行为，指屏幕刷新一次
    def action(self, bug: Bug, wall_points):
        self.__move()
        self.__eat(bug)
        return self.__death(wall_points)

    # 走
    def __move(self):
        for i in range(len(self.__list) - 1, 0, -1):
            self.__list[i] = self.__list[i - 1]

        # 蛇头坐标是蛇头原坐标加方向
        self.__list[0] = (self.__list[0][0] + self.__toward[0],
                          self.__list[0][1] + self.__toward[1])
        self.__lock = False

    # 吃，头和吃的坐标一致就吃
    def __eat(self, bug: Bug):
        if self.__list[0] == bug.point[0]:
            # 虫子瞬移
            bug.quickly_move(self.__list)
            # 蛇加长
            self.__list.append(self.__list[-1])

    # 蛇死亡判断，撞头或者撞身体
    def __death(self, points):
        if self.__list[0] in points:
            return True
        if self.__list[2:] in self.__list[0]:
            return True
        return False
