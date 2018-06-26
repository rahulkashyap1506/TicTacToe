from tkinter import *
import tkinter.messagebox
from random import randint
from sys import exit

root = Tk()
root.title('Tic Tac Toe')

def bot():
    if(grid_full()):
        tkinter.messagebox.showinfo('Game Over', 'Draw')
        root.destroy()
        exit()

    sum = [0 for i in range(0, 8)]

    for i in range(0, 3):
        for j in range(0, 3):
            sum[i] += grid[i][j]
            sum[3 + i] += grid[j][i]
        sum[6] += grid[i][i]
        sum[7] += grid[2 - i][i]

    for n in range(0, 8):
        if(n < 3 and sum[n] is -2):
            for i in range(0, 3):
                if(grid[n][i] is 0):
                    check(boxes[n][i], n, i)
                    return
        elif(n >= 3 and n < 6 and sum[n] is -2):
            for i in range(0, 3):
                if(grid[i][n - 3] is 0):
                    check(boxes[i][n - 3], i, n - 3)
                    return
        elif(n is 6 and sum[n] is -2):
            for i in range(0, 3):
                if(grid[i][i] is 0):
                    check(boxes[i][i], i, i)
                    return
        elif(n is 7 and sum[n] is -2):
            for i in range(0, 3):
                if(grid[2 - i][i] is 0):
                    check(boxes[2 - i][i], 2-i, i)
                    return

    for i in range(0, 8):
        sum[i] = 0
        
    for i in range(0, 3):
        for j in range(0, 3):
            sum[i] += grid[i][j]
            sum[3 + i] += grid[j][i]
        sum[6] += grid[i][i]
        sum[7] += grid[2 - i][i]

    for n in range(0, 8):
        if(n < 3 and sum[n] is 2):
            for i in range(0, 3):
                if(grid[n][i] is 0):
                    check(boxes[n][i], n, i)
                    return
        elif(n >= 3 and n < 6 and sum[n] is 2):
            for i in range(0, 3):
                if(grid[i][n - 3] is 0):
                    check(boxes[i][n - 3], i, n - 3)
                    return
        elif(n is 6 and sum[n] is 2):
            for i in range(0, 3):
                if(grid[i][i] is 0):
                    check(boxes[i][i], i, i)
                    return
        elif(n is 7 and sum[n] is 2):
            for i in range(0, 3):
                if(grid[2 - i][i] is 0):
                    check(boxes[2 - i][i], 2 - i, i)
                    return

    if(grid[1][1] is 0):
        check(boxes[1][1], 1, 1)
        return

    x = 0
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            if(grid[i][j] is 0):
                x += 1

    if(x is not 0):
        moves = randint(0, x-1)

        x = 0
        for i in range(0, 3, 2):
            for j in range(0, 3, 2):
                if(grid[i][j] is 0):
                    x += 1
                if(x is moves):
                    check(boxes[i][j], i, j)
                    return

    x = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if((i + j) % 2 is not 0 and grid[i][j] is 0):
                x += 1

    if(x is not 0):
        moves = randint(0, x-1)

        x = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if((i + j) % 2 is not 0 and grid[i][j] is 0):
                    x += 1
                if(x is moves):
                    check(boxes[i][j], i, j)
                    return
    
    moves = randint(0, x-1)

    x = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if(grid[i][j] is 0):
                x += 1
            if(x is moves):
                check(boxes[i][j], i, j)
                return

    return


def check(box, x, y, click = False):
    global turn
    if(box['text'] is ' ' and turn is 'P' and click is True):
        box['text'] = 'X'
        grid[x][y] = 1
        turn = 'B'
    elif(box['text'] is ' ' and turn is 'B'):
        box['text'] = 'O'
        grid[x][y] = -1
        turn = 'P'
       
    sum = [0 for i in range(0, 8)]
    for i in range(0, 3):
        for j in range(0, 3):
            sum[i] += grid[i][j]
            sum[3 + i] += grid[j][i]
        sum[6] += grid[i][i]
        sum[7] += grid[2 - i][i]

    print()
    for i in grid:
        for j in i:
            if(j is 1):
                print('X', end=' ')
            elif(j is -1):
                print('O', end=' ')
            else:
                print('-', end=' ')
        print()

    winner = 0
    for i in sum:
        if(abs(i) is 3):
            winner = i//3

    if(winner is 1):
        tkinter.messagebox.showinfo('Game Over', 'Player Won')
        root.destroy()
        exit()
    elif(winner is -1):
        tkinter.messagebox.showinfo('Game Over', 'Bot Won')
        root.destroy()
        exit()

    if(turn is 'B'):
        bot()
        
    return


def grid_full():
    x = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if(grid[i][j] is 0):
                return False

    return True

               
grid = [[0 for i in range(0, 3)] for i in range(0, 3)]

turn = 'P'
boxes = []
for i in range(0, 3):
    boxes.append([])
    for j in range(0, 3):
        boxes[i].append(Button(root, text=' ', font=('Courier 30'), height=3, width=6, command=lambda i=i, j=j:check(boxes[i][j], i, j, True)))
        boxes[i][j].grid(row=i, column=j, sticky=S+N+E+W)

root.mainloop()
