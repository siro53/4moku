#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys
import board
import player

SCREEN_SIZE = (640, 480)
BACK_COLOR = (0, 0, 255)  # ベージュ
LINE_COLOR = (0, 0, 0)  # 白
PLAYER1_COLOR = (255, 0, 0)  # 赤
PLAYER2_COLOR = (255, 255, 0)  # 黄色
BOX_SIZE = 60
COLUMN = 7  # 列
ROW = 6  # 行
RADIUS = 30  # 半径
GOSA = 38  # ピカチュウとイーブイの画像をずらして枠内に入れるための調整用


def main():
    pygame.init()
    statement = 0
    start, play = 0, 1
    screen = pygame.display.set_mode(SCREEN_SIZE)  # スクリーンオブジェクト
    pygame.display.set_caption("Connect 4")  # タイトル

    if statement == start:
        backImg = pygame.image.load("pokeball.jpg")
        font1 = pygame.font.Font("Muller-ExtraBold-DEMO.ttf", 37)
        font2 = pygame.font.Font("Muller-ExtraBold-DEMO.ttf", 57)
        #font1 = pygame.font.SysFont(None, 50)
        #font2 = pygame.font.SysFont(None, 80)
        eevee = pygame.image.load("133_2.png").convert_alpha()
        pikachu = pygame.image.load("025_2.png").convert_alpha()
        introduction = font1.render(
            "PRESS THE SPACE KEY", False, (0, 0, 0))
        connect4 = font2.render("CONNECT 4", False, (0, 0, 0))
        sc = 0
        i = 0
        while True:
            i += 1
            screen.fill((255, 255, 255))
            # テキスト描画
            screen.blit(backImg, (0, 0))
            #screen.blit(introduction, (110, 320))
            screen.blit(connect4, (155, 50))
            screen.blit(eevee, (230, 235))
            screen.blit(pikachu, (335, 235))
            if sc > 15:
                screen.blit(introduction, (110, 340))
            sc += 1
            if sc > 30:
                sc = 0
            transition = False
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        transition = True
            if transition:
                statement += 1
                break

    if statement == play:
        bd = board.Board(screen, LINE_COLOR, 110, 55)  # 盤面のオブジェクト
        #playBackImg = pygame.image.load("backimg.JPG")
        player1 = player.Player(screen, PLAYER1_COLOR, bd, False)
        player2 = player.Player(screen, PLAYER2_COLOR, bd, True)
        puted_pos_list = []  # 既に石を置いた場所を保管しておくlist
        puted_pos_list_1 = []
        puted_pos_list_2 = []
        can_put_dict = bd.can_put_dict()
        sysfont = pygame.font.Font("Muller-ExtraBold-DEMO.ttf", 37)
        eevee = pygame.image.load("133_2.png").convert_alpha()
        pikachu = pygame.image.load("025_2.png").convert_alpha()
        player2_turn = sysfont.render("EEVEE TURN", False, (255, 255, 255))
        player1_turn = sysfont.render("PIKACHU TURN", False, (255, 255, 255))
        player1_win = sysfont.render("EEVEE WIN !!!", False, (255, 200, 0))
        player2_win = sysfont.render("PIKACHU WIN !!!", False, (255, 200, 0))

        while True:
            screen.fill((0, 0, 255))
            bd.draw()  # 盤面を描く
            x, y = 0, 0
            clicked_check = False
            player1_win_check = False
            player2_win_check = False
            for event in pygame.event.get():  # イベント処理
                if event.type == MOUSEBUTTONDOWN and event.button == 1:  # マウスイベント
                    x, y = event.pos
                    if bd.transfer_pos((x, y)) in puted_pos_list or x <= bd.startX or y <= bd.startY or x >= (bd.startX + BOX_SIZE * COLUMN) or y >= (bd.startY + BOX_SIZE * ROW):  # 既にコマを置いてるかどうかのチェック
                        clicked_check = True
                        break
                    player1.turn_check()
                    player2.turn_check()
                if event.type == QUIT:  # 終了イベント
                    pygame.quit()
                    sys.exit()
            if clicked_check:  # 既にコマを置いてるかどうかのチェック
                continue
            for i in range(COLUMN):  # コマ配置
                for j in range(ROW):
                    if bd.transfer_pos((x, y)) == can_put_dict[i][j][0]:
                        if can_put_dict[i][j][1]:
                            player1.put_stone(
                                (x, y), puted_pos_list, puted_pos_list_1)
                            player1_win_check = bd.search_win(puted_pos_list_1)
                            player2.put_stone(
                                (x, y), puted_pos_list, puted_pos_list_2)
                            player2_win_check = bd.search_win(puted_pos_list_2)
                            can_put_dict[i][j - 1][1] = True
                        else:
                            player1.turn_check()
                            player2.turn_check()
                            break

            for pos in puted_pos_list_1:
                screen.blit(eevee, (pos[0] - GOSA, pos[1] - GOSA))

            if player1_win_check:
                player1_turn = player1_win
            if player1.flag == True:
                screen.blit(player1_turn, (190, 10))

            for pos in puted_pos_list_2:
                screen.blit(pikachu, (pos[0] - GOSA, pos[1] - GOSA))

            if player2_win_check:
                player2_turn = player2_win
            if player2.flag == True:
                screen.blit(player2_turn, (210, 10))

            pygame.display.update()


if __name__ == '__main__':
    main()
