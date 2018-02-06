#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import codecs
import csv
import sys
from common import screen_ocr, methods
from colorama import init, Fore

init(autoreset=True)


def do_it(game_num):
    Start = time.time()
    Que0, Ans = screen_ocr.Baidu_ocr(game_num)
    print('\n识别完毕')
    End = time.time()
    Duration = End - Start
    print('\n识别耗时: {:.2f}s'.format(Duration))
    # Que = '以下哪项不是酸梅汤的主要功效'
    # Ans = ['解酒','减肥','解口']
    print('\n{}\n'.format(Que0))
    Que, temp = methods.judge_false(Que0)
    Que = Que.replace('?', '').replace('《', '').replace('》', '').replace('“', '').replace('”', '').replace('"', '')
    # methods.Open_web(Que)

    S_count, S_sign = methods.S30_count(Que, Ans)
    methods.p_it(Ans, S_count, S_sign)
    W_count, W_sign = methods.Word_count(Que, Ans)
    methods.p_it(Ans, W_count, W_sign)

    F_IDX = methods.Solve_it(Ans, S_count, W_count, temp)
    End = time.time()
    Duration = End - Start
    print('\n总耗时: {:.2f}s'.format(Duration))
    print('--------------------------------\n')
    # methods.open_web(Que_ocr)
    return Que0, Ans, Duration, F_IDX

def check_yn_input(str_input):
    while str_input != 'y' and str_input != 'n' and len(str_input) != 0:
        str_input = input('\n输入错误,请重新输入 y/n[y]: ')
    return str_input

def check_num_input(str_input):
    while str_input not in ['1','2','3','4']:
        str_input = input('\n输入错误,请重新输入 1 or 2 or 3 or 4: ')
    return str_input

def loop():
    print('\n软件序号如下:\n1-简单搜索\n2-花椒视频\n3-冲顶大会\n4-西瓜视频')
    game_num = input('\n请输入你的软件序号: ')
    game_num = check_num_input(game_num)
    file_write = input('\n是否将题目写入题库中? y/n[y]: ')
    file_write = check_yn_input(file_write)
    if file_write == 'y' or len(file_write) == 0:
        print(Fore.GREEN + '\n将追加写入' + Fore.RESET)
    else:
        print(Fore.RED + '\n不会写入' + Fore.RESET)

    start = input('\n回车开始识别 ->')
    while True:
        Q, A, D, F = do_it(game_num)
        if file_write == 'y' or len(file_write) == 0:
            csv_file = codecs.open('tk.csv', 'ab+', encoding='utf_8_sig')
            tk = csv.writer(csv_file)
            Q = str(Q.replace('\"', ''))
            D = round(D, 2)
            # line = [Q,]
            # for ans in A:
            #     line.append(ans)
            # line.append(D)
            # line.append(A[F])
            line = [Q, A, D, A[F]]
            tk.writerow(line)
            # file2read.close()
            csv_file.close()
        go = input('是否继续运行? y/n[y]: ')
        go = check_yn_input(go)
        if go == 'n':
            sys.exit()
            # break
        # print('')


def p_time():
    s = time.time()
    for i in range(10):
        do_it()
    e = time.time()
    print((e - s) / 10)


if __name__ == '__main__':
    # p_time()
    loop()
    # do_it()
