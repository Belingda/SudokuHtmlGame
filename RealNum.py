# coding=utf-8
import random
import json


def RandomRect():
    datalst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    randomRect = random.sample(datalst, len(datalst))
    return randomRect


class Rect:
    TopLeftCorner = 0
    MiddleTop = 1
    TopRightCorner = 2
    MiddleLeft = 3
    Middle = 4
    MiddleRight = 5
    LowerLeftCorner = 6
    MiddleLower = 7
    LowerRightCorner = 8

    def __init__(self):
        self.sudulst = []
        initRect = RandomRect()
        self.MiddleRectRow = {
            0: [initRect[0], initRect[1], initRect[2]],
            1: [initRect[3], initRect[4], initRect[5]],
            2: [initRect[6], initRect[7], initRect[8]]
        }
        self.MiddleRectCol = {
            0: [initRect[0], initRect[3], initRect[6]],
            1: [initRect[1], initRect[4], initRect[7]],
            2: [initRect[2], initRect[5], initRect[8]]
        }
        self.middleLeftRect = {0: [], 1: [], 2: []}
        self.middleRightRect = {0: [], 1: [], 2: []}
        self.middleTop = {0: [], 1: [], 2: []}
        self.middleDown = {0: [], 1: [], 2: []}
        self.topLeftCorcer = {0: [], 1: [], 2: []}
        self.topRightCorcer = {0: [], 1: [], 2: []}
        self.downLeftCorcer = {0: [], 1: [], 2: []}
        self.downRightCorcer = {0: [], 1: [], 2: []}

    def createSudoku(self):
        # 生成中间矩阵两边的矩阵
        self.middleLeftRect[0] = self.MiddleRectRow[1]
        self.middleRightRect[0] = self.MiddleRectRow[2]

        self.middleLeftRect[1] = self.MiddleRectRow[2]
        self.middleRightRect[1] = self.MiddleRectRow[0]

        self.middleLeftRect[2] = self.MiddleRectRow[0]
        self.middleRightRect[2] = self.MiddleRectRow[1]

        # 生成中间矩阵上下的矩阵

        self.middleTop[0].append(self.MiddleRectRow[0][2])
        self.middleTop[1].append(self.MiddleRectRow[1][2])
        self.middleTop[2].append(self.MiddleRectRow[2][2])

        self.middleTop[0].append(self.MiddleRectRow[0][0])
        self.middleTop[1].append(self.MiddleRectRow[1][0])
        self.middleTop[2].append(self.MiddleRectRow[2][0])

        self.middleTop[0].append(self.MiddleRectRow[0][1])
        self.middleTop[1].append(self.MiddleRectRow[1][1])
        self.middleTop[2].append(self.MiddleRectRow[2][1])

        self.middleDown[0].append(self.MiddleRectRow[0][1])
        self.middleDown[1].append(self.MiddleRectRow[1][1])
        self.middleDown[2].append(self.MiddleRectRow[2][1])

        self.middleDown[0].append(self.MiddleRectRow[0][2])
        self.middleDown[1].append(self.MiddleRectRow[1][2])
        self.middleDown[2].append(self.MiddleRectRow[2][2])

        self.middleDown[0].append(self.MiddleRectRow[0][0])
        self.middleDown[1].append(self.MiddleRectRow[1][0])
        self.middleDown[2].append(self.MiddleRectRow[2][0])

        # 生成第一行中间矩阵的左右两个矩阵
        self.topLeftCorcer[0] = self.middleTop[1]
        self.topRightCorcer[0] = self.middleTop[2]

        self.topLeftCorcer[1] = self.middleTop[2]
        self.topRightCorcer[1] = self.middleTop[0]

        self.topLeftCorcer[2] = self.middleTop[0]
        self.topRightCorcer[2] = self.middleTop[1]

        # 生成第三行中间矩阵的左右两个矩阵
        self.downLeftCorcer[0] = self.middleDown[1]
        self.downRightCorcer[0] = self.middleDown[2]

        self.downLeftCorcer[1] = self.middleDown[2]
        self.downRightCorcer[1] = self.middleDown[0]

        self.downLeftCorcer[2] = self.middleDown[0]
        self.downRightCorcer[2] = self.middleDown[1]

    def getSuduLst(self):
        if len(self.sudulst) > 0:
            return self.sudulst
        for row in range(3):
            for i in range(3):
                self.sudulst.append(self.topLeftCorcer[row][i])
            for i in range(3):
                self.sudulst.append(self.middleTop[row][i])
            for i in range(3):
                self.sudulst.append(self.topRightCorcer[row][i])

        for row in range(3):
            for i in range(3):
                self.sudulst.append(self.middleLeftRect[row][i])
            for i in range(3):
                self.sudulst.append(self.MiddleRectRow[row][i])
            for i in range(3):
                self.sudulst.append(self.middleRightRect[row][i])

        for row in range(3):
            for i in range(3):
                self.sudulst.append(self.downLeftCorcer[row][i])
            for i in range(3):
                self.sudulst.append(self.middleDown[row][i])
            for i in range(3):
                self.sudulst.append(self.downRightCorcer[row][i])
        return self.sudulst

    def showView(self):
        for i in range(len(self.sudulst)):
            if (i + 1) % 9 == 0:
                print self.sudulst[i]
            else:
                print self.sudulst[i],


def GetSuduInit():
    ob = Rect()
    ob.createSudoku()
    lst = ob.getSuduLst()
    return json.dumps(lst)
