import pygame
from pygame.locals import *

BOX_SIZE = 60
COLUMN = 7  # 列
ROW = 6  # 行


class Board:
    def __init__(self, screen, color, startX, startY):  # startX、startY = 始点
        self.screen = screen
        self.color = color
        self.startX = startX
        self.startY = startY

    def draw(self):
        for i in range(COLUMN + 1):
            pygame.draw.line(self.screen, self.color, (self.startX + BOX_SIZE * i,
                                                       self.startY), (self.startX + BOX_SIZE * i, self.startY + BOX_SIZE * ROW), 2)
        for j in range(ROW + 1):
            pygame.draw.line(self.screen, self.color, (self.startX, self.startY + BOX_SIZE * j),
                             (self.startX + BOX_SIZE * COLUMN, self.startY + BOX_SIZE * j), 2)

    def get_pos_dict(self):
        board_pos_dict = {0: [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 0, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i) for i in range(ROW)],
                          1: [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 1, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i) for i in range(ROW)],
                          2: [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 2, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i) for i in range(ROW)],
                          3: [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 3, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i) for i in range(ROW)],
                          4: [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 4, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i) for i in range(ROW)],
                          5: [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 5, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i) for i in range(ROW)],
                          6: [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 6, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i) for i in range(ROW)]
                          }  # board_pos_dict[COLUMN][ROW]
        return board_pos_dict

    def transfer_pos(self, pos):  # マウスで入力した座標をマスの中心座標に変換するメソッド
        board_pos_dict = self.get_pos_dict()
        for i in range(COLUMN):
            for j in range(ROW):
                if ((self.startX + BOX_SIZE * i) < pos[0] and pos[0] < (self.startX + BOX_SIZE * (i + 1))) and ((self.startY + BOX_SIZE * j) < pos[1] and pos[1] < (self.startY + BOX_SIZE * (j + 1))):
                    return board_pos_dict[i][j]

    def can_put_dict(self):  # そのマスに置けるかどうかの辞書を返す
        can_put_dict = {0: [[(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 0, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), True] if i == 5 else [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 0, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), False] for i in range(ROW)],
                        1: [[(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 1, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), True] if i == 5 else [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 1, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), False] for i in range(ROW)],
                        2: [[(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 2, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), True] if i == 5 else [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 2, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), False] for i in range(ROW)],
                        3: [[(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 3, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), True] if i == 5 else [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 3, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), False] for i in range(ROW)],
                        4: [[(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 4, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), True] if i == 5 else [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 4, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), False] for i in range(ROW)],
                        5: [[(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 5, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), True] if i == 5 else [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 5, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), False] for i in range(ROW)],
                        6: [[(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 6, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), True] if i == 5 else [(self.startX + (BOX_SIZE // 2) + BOX_SIZE * 6, self.startY + (BOX_SIZE // 2) + BOX_SIZE * i), False] for i in range(ROW)]
                        }  # can_put_dict[COLUMN][ROW][0] -> 座標 , can_put_dict[COLUMN][ROW][1] -> 置けるか否かを真偽値で返す
        return can_put_dict

    def search_win(self, my_puted_pos_list):  # 勝利判定
        new_my_puted_pos_list = []
        for pos in my_puted_pos_list:
            column = (pos[0] - self.startX - BOX_SIZE // 2) // BOX_SIZE
            row = (pos[1] - self.startY - BOX_SIZE // 2) // BOX_SIZE
            new_my_puted_pos_list.append((column, row))
        num_puted_pos_list = [(pos[0] + 1) + 7 * pos[1]
                              for pos in new_my_puted_pos_list]

        for i in range(COLUMN - 3):
            for j in range(ROW - 3):
                if 1+i+7*j in num_puted_pos_list and 9+i+7*j in num_puted_pos_list and 17+i+7*j in num_puted_pos_list and 25+i+7*j in num_puted_pos_list:
                    return True  # 下斜め
                if 4+i+7*j in num_puted_pos_list and 10+i+7*j in num_puted_pos_list and 16+i+7*j in num_puted_pos_list and 22+i+7*j in num_puted_pos_list:
                    return True  # 上斜め
        for i in range(COLUMN - 3):
            for j in range(ROW):
                if 1+i+7*j in num_puted_pos_list and 2+i+7*j in num_puted_pos_list and 3+i+7*j in num_puted_pos_list and 4+i+7*j in num_puted_pos_list:
                    return True  # 横
        for i in range(COLUMN):
            for j in range(ROW - 3):
                if 1+i+7*j in num_puted_pos_list and 8+i+7*j in num_puted_pos_list and 15+i+7*j in num_puted_pos_list and 22+i+7*j in num_puted_pos_list:
                    return True # 縦
        return False
        # 1 ,2 ,3 ,4 ,5 ,6 ,7
        # 8 ,9 ,10,11,12,13,14
        # 15,16,17,18,19,20,21
        # 22,23,24,25,26,27,28
        # 29,30,31,32,33,34,35
        # 36,37,38,39,40,41,42
