import option
import os

# 根据管理类，打印一个n*n矩形
class Displayer:

    # 存储坐标点
    def __init__(self):
        self.__list = []

    # 添加需要显示的坐标点
    def expend_points(self, points_list):
        self.__list.extend(points_list)

    # 清空这一帧的数据
    def clear(self):
        self.__list.clear()

    # 打印点阵图
    def draw_graphics(self, score):
        os.system("cls")
        print("".center(option.size * 2, "="))
        print(("score:%d" % score).center(option.size * 2, " "))
        print("".center(option.size * 2, "="))
        for i in range(option.size):
            for j in range(option.size):
                if (i, j) in self.__list:
                    print("方", end="")
                else:
                    print("  ", end="")
            print()
