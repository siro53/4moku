import pygame
from pygame.locals import *
import board

COLUMN = 7  # 列
ROW = 6  # 行
BOX_SIZE = 60
RADIUS = 30


class Player:
    # board = 盤面オブジェクト、pos = マウスでクリックした座標、flag = 自分のターンか否か
    def __init__(self, screen, color, bd, flag):
        self.screen = screen
        self.color = color
        self.flag = flag
        self.bd = bd

    def turn_check(self):  # どっちのターンなのかをチェック
        if self.flag == False:
            self.flag = True
        else:
            self.flag = False

    def put_stone(self, pos, puted_pos_list, my_puted_pos_list):  # マウスクリックした場所に駒を置くメソッド
        board_pos_dict = self.bd.get_pos_dict()
        for i in range(COLUMN):
            for j in range(ROW):
                if ((self.bd.startX + BOX_SIZE * i) < pos[0] and pos[0] < (self.bd.startX + BOX_SIZE * (i + 1))) and ((self.bd.startY + BOX_SIZE * j) < pos[1] and pos[1] < (self.bd.startY + BOX_SIZE * (j + 1))):
                    puted_pos_list.append(board_pos_dict[i][j])
                    if self.flag == True:
                        my_puted_pos_list.append(board_pos_dict[i][j])
