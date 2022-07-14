import threading
import tkinter as tk
from tkinter import *
from tkinter import ttk

okunan = []
sudoku = []
cozulmemis=[]
cozulmemisloc=[]

satir11 = 0
satir12 = 8
satir21 = 0
satir22 = 8
satir31 = 12
satir32 = 20
satir41 = 12
satir42 = 20
satir51 = 6
satir52 = 14

sutun11 = 0
sutun12 = 8
sutun21 = 12
sutun22 = 20
sutun31 = 0
sutun32 = 8
sutun41 = 12
sutun42 = 20
sutun51 = 6
sutun52 = 14

pencere = tk.Tk()
canvas = Canvas(pencere, width=1029, height=1029)
canvas.pack()

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()

with open('readme.txt') as f:
    for line in f:
        temp = []
        for harf in line:
            if(harf != "\n"):
                if(harf != "*"):
                    temp.append(harf)
                else:
                    temp.append(0)
        okunan.append(temp)

def olustur():
    global cozulmemis
    for i in range(len(okunan)):
        if(len(okunan[i]) == 18):
            temp = []
            for j in range(len(okunan[i])):
                if(j != 9):
                    temp.append(okunan[i][j])
                else:
                    temp.append('*')
                    temp.append('*')
                    temp.append('*')
                    temp.append(okunan[i][j])
            sudoku.append(temp)
        elif(len(okunan[i]) == 9):
            temp = []
            for j in range(len(okunan[i])):
                if(j == 0):
                    temp.append('*')
                    temp.append('*')
                    temp.append('*')
                    temp.append('*')
                    temp.append('*')
                    temp.append('*')
                    temp.append(okunan[i][j])
                elif(j == 8):
                    temp.append(okunan[i][j])
                    temp.append('*')
                    temp.append('*')
                    temp.append('*')
                    temp.append('*')
                    temp.append('*')
                    temp.append('*')
                else:
                    temp.append(okunan[i][j])
            sudoku.append(temp)
        else:
            temp = []
            for j in range(len(okunan[i])):
                temp.append(okunan[i][j])
            sudoku.append(temp)
    cozulmemis = sudoku

def bastır():
    for i in range(len(cozulmemis)):
     for j in range(len(cozulmemis)):
        if (cozulmemis[i][j] != 0 and cozulmemis[i][j] != '*'):
            canvas.create_text(i * 49+20, j * 49+20, fill="darkblue",font="Times 20 italic bold",text=cozulmemis[j][i])
            canvas.update()

def kontrol(satir, sutun):
    for i in range(0, 9):
        if(i != sutun and int(sudoku[satir][i]) == sudoku[satir][sutun]):
            return False

        if(i != satir and int(sudoku[i][sutun]) == sudoku[satir][sutun]):
            return False
        
    startRow = (satir // 3) * 3
    startCol = (sutun // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if startRow+i != satir and startCol+j != sutun and sudoku[startRow+i][startCol+j] == sudoku[satir][sutun]:
                return False

    if(satir > 5 and sutun > 5):
        if(kontrol5(satir, sutun) == False):
            return False
    
    return True

def kontrol2(satir, sutun):
    for i in range(12, 21):
        if(i != sutun and int(sudoku[satir][i]) == sudoku[satir][sutun]):
            return False

        if(i%12 != satir and int(sudoku[i%12][sutun]) == sudoku[satir][sutun]):
            return False

    startRow = (satir // 3) * 3
    startCol = (sutun // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if startRow+i != satir and startCol+j != sutun and sudoku[startRow+i][startCol+j] == sudoku[satir][sutun]:
                return False

    if(satir > 5 and sutun < 15):
        if(kontrol5(satir, sutun) == False):
            return False

    return True

def kontrol3(satir, sutun):
    for i in range(12, 21):
        if(i%12 != sutun and int(sudoku[satir][i%12]) == sudoku[satir][sutun]):
            return False

        if(i != satir and int(sudoku[i][sutun]) == sudoku[satir][sutun]):
            return False

    startRow = (satir // 3) * 3
    startCol = (sutun // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if startRow+i != satir and startCol+j != sutun and sudoku[startRow+i][startCol+j] == sudoku[satir][sutun]:
                return False

    if(satir < 15 and sutun > 5):
        if(kontrol5(satir, sutun) == False):
            return False

    return True

def kontrol4(satir, sutun):
    for i in range(12, 21):
        if(i != sutun and int(sudoku[satir][i]) == sudoku[satir][sutun]):
            return False

        if(i != satir and int(sudoku[i][sutun]) == sudoku[satir][sutun]):
            return False
        
    startRow = (satir // 3) * 3
    startCol = (sutun // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if startRow+i != satir and startCol+j != sutun and sudoku[startRow+i][startCol+j] == sudoku[satir][sutun]:
                return False

    if(satir < 15 and sutun < 15):
        if(kontrol5(satir, sutun) == False):
            return False

    return True

def kontrol5(satir, sutun):
    for i in range(6, 15):
        if(i != sutun and int(sudoku[satir][i]) == sudoku[satir][sutun]):
            return False

        if(i != satir and int(sudoku[i][sutun]) == sudoku[satir][sutun]):
            return False
        
    startRow = (satir // 3) * 3
    startCol = (sutun // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if startRow+i != satir and startCol+j != sutun and sudoku[startRow+i][startCol+j] == sudoku[satir][sutun]:
                return False

    """if(satir > 5 and sutun > 5):
        if(kontrol(satir, sutun) == False):
            return False
    elif(satir > 5 and sutun < 15):
        if(kontrol2(satir, sutun) == False):
            return False
    elif(satir < 15 and sutun > 5):
        if(kontrol3(satir, sutun) == False):
            return False
    elif(satir < 15 and sutun < 15):
        if(kontrol4(satir, sutun) == False):
            return False"""

def geriGel11():
    global sutun11, satir11
    if(sutun11 == 0 and satir11 != 0):
        satir11 -= 1
        sutun11 = 8
    elif(sutun11 != 0):
        sutun11 -= 1
    if type(sudoku[satir11][sutun11]) is not str:
        if(sudoku[satir11][sutun11] < 9):
            sudoku[satir11][sutun11] += 1
        else:
            sudoku[satir11][sutun11] = 0
            geriGel11()
    else:
        geriGel11()

def geriGel12():
    global sutun12, satir12
    if(sutun12 == 8 and satir12 != 8):
        satir12 += 1
        sutun12 = 0
    elif(sutun12 != 8):
        sutun12 += 1
    if type(sudoku[satir12][sutun12]) is not str:
        if(sudoku[satir12][sutun12] < 9):
            sudoku[satir12][sutun12] += 1
        else:
            sudoku[satir12][sutun12] = 0
            geriGel12()
    else:
        geriGel12()

def geriGel21():
    global sutun21, satir21
    if(sutun21 == 12 and satir21 != 0):
        satir21 -= 1
        sutun21 = 20
    elif(sutun21 != 12):
        sutun21 -= 1
    if type(sudoku[satir21][sutun21]) is not str:
        if(sudoku[satir21][sutun21] < 9):
            sudoku[satir21][sutun21] += 1
        else:
            sudoku[satir21][sutun21] = 0
            geriGel21()
    else:
        geriGel21()

def geriGel22():
    global sutun22, satir22
    if(sutun22 == 20 and satir22 != 8):
        satir22 += 1
        sutun22 = 12
    elif(sutun22 != 20):
        sutun22 += 1
    if type(sudoku[satir22][sutun22]) is not str:
        if(sudoku[satir22][sutun22] < 9):
            sudoku[satir22][sutun22] += 1
        else:
            sudoku[satir22][sutun22] = 0
            geriGel22()
    else:
        geriGel22()

def geriGel31():
    global sutun31, satir31
    if(sutun31 == 0 and satir31 != 12):
        satir31 -= 1
        sutun31 = 8
    elif(sutun31 != 0):
        sutun31 -= 1
    if type(sudoku[satir31][sutun31]) is not str:
        if(sudoku[satir31][sutun31] < 9):
            sudoku[satir31][sutun31] += 1
        else:
            sudoku[satir31][sutun31] = 0
            geriGel31()
    else:
        geriGel31()

def geriGel32():
    global sutun32, satir32
    if(sutun32 == 8 and satir32 != 20):
        satir32 += 1
        sutun32 = 0
    elif(sutun32 != 8):
        sutun32 += 1
    if type(sudoku[satir32][sutun32]) is not str:
        if(sudoku[satir32][sutun32] < 9):
            sudoku[satir32][sutun32] += 1
        else:
            sudoku[satir32][sutun32] = 0
            geriGel32()
    else:
        geriGel32()

def geriGel41():
    global sutun41, satir41
    if(sutun41 == 12 and satir41 != 12):
        satir41 -= 1
        sutun41 = 20
    elif(sutun41 != 12):
        sutun41 -= 1
    if type(sudoku[satir41][sutun41]) is not str:
        if(sudoku[satir41][sutun41] < 9):
            sudoku[satir41][sutun41] += 1
        else:
            sudoku[satir41][sutun41] = 0
            geriGel41()
    else:
        geriGel41()

def geriGel42():
    global sutun42, satir42
    if(sutun42 == 20 and satir42 != 20):
        satir42 += 1
        sutun42 = 12
    elif(sutun42 != 20):
        sutun42 += 1
    if type(sudoku[satir42][sutun42]) is not str:
        if(sudoku[satir42][sutun42] < 9):
            sudoku[satir42][sutun42] += 1
        else:
            sudoku[satir42][sutun42] = 0
            geriGel42()
    else:
        geriGel42()

def geriGel51():
    global sutun51, satir51
    if(sutun51 == 6 and satir51 != 6):
        satir51 -= 1
        sutun51 = 14
    elif(sutun51 != 6):
        sutun51 -= 1
    if type(sudoku[satir51][sutun51]) is not str:
        if(sudoku[satir51][sutun51] < 9):
            sudoku[satir51][sutun51] += 1
        else:
            sudoku[satir51][sutun51] = 0
            geriGel51()
    else:
        geriGel51()

def geriGel52():
    global sutun52, satir52
    if(sutun52 == 14 and satir52 != 14):
        satir52 += 1
        sutun52 = 6
    elif(sutun52 != 14):
        sutun52 += 1
    if type(sudoku[satir52][sutun52]) is not str:
        if(sudoku[satir52][sutun52] < 9):
            sudoku[satir52][sutun52] += 1
        else:
            sudoku[satir52][sutun52] = 0
            geriGel52()
    else:
        geriGel52()

def ilerle11():
    global sutun11, satir11
    if(sutun11 == 8 and satir11 != 8):
        satir11 += 1
        sutun11 = 0
    elif(sutun11 != 8):
        sutun11 += 1

def ilerle12():
    global sutun12, satir12
    if(sutun12 == 0 and satir12 != 0):
        satir12 -= 1
        sutun12 = 8
    elif(sutun12 != 0):
        sutun12 -= 1

def ilerle21():
    global sutun21, satir21
    if(sutun21 == 20 and satir21 != 8):
        satir21 += 1
        sutun21 = 12
    elif(sutun21 != 20):
        sutun21 += 1

def ilerle22():
    global sutun22, satir22
    if(sutun22 == 12 and satir22 != 0):
        satir22 -= 1
        sutun22 = 20
    elif(sutun22 != 12):
        sutun22 -= 1

def ilerle31():
    global sutun31, satir31
    if(sutun31 == 8 and satir31 != 20):
        satir31 += 1
        sutun31 = 0
    elif(sutun31 != 8):
        sutun31 += 1

def ilerle32():
    global sutun32, satir32
    if(sutun32 == 0 and satir32 != 12):
        satir32 -= 1
        sutun32 = 8
    elif(sutun32 != 0):
        sutun32 -= 1

def ilerle41():
    global sutun41, satir41
    if(sutun41 == 20 and satir41 != 20):
        satir41 += 1
        sutun41 = 12
    elif(sutun41 != 20):
        sutun41 += 1

def ilerle42():
    global sutun42, satir42
    if(sutun42 == 12 and satir42 != 12):
        satir42 -= 1
        sutun42 = 20
    elif(sutun42 != 12):
        sutun42 -= 1

def ilerle51():
    global sutun51, satir51
    if(sutun51 == 14 and satir51 != 14):
        satir51 += 1
        sutun51 = 6
    elif(sutun51 != 14):
        sutun51 += 1

def ilerle52():
    global sutun52, satir52
    if(sutun52 == 6 and satir52 != 6):
        satir52 -= 1
        sutun52 = 14 
    elif(sutun52 != 6):
        sutun52 -= 1

def basla11():
    while True:
        if type(sudoku[satir11][sutun11]) is not str:
            if(sudoku[satir11][sutun11] == 0):
                sudoku[satir11][sutun11] = 1

            if(kontrol(satir11, sutun11) == False):
                if(sudoku[satir11][sutun11] < 9):
                    sudoku[satir11][sutun11] += 1
                else:
                    sudoku[satir11][sutun11] = 0
                    geriGel11()
            else:
                if(satir11 == 8 and sutun11 == 8 and sudoku[satir11][sutun11] != 0):
                    break
                ilerle11()
        else:
            if(satir11 == 8 and sutun11 == 8):
                break
            ilerle11()

def basla12():
    while True:
        if type(sudoku[satir12][sutun12]) is not str:
            if(sudoku[satir12][sutun12] == 0):
                sudoku[satir12][sutun12] = 1

            if(kontrol(satir12, sutun12) == False):
                if(sudoku[satir12][sutun12] < 9):
                    sudoku[satir12][sutun12] += 1
                else:
                    sudoku[satir12][sutun12] = 0
                    geriGel12()
            else:
                if(satir12 == 0 and sutun12 == 0 and sudoku[satir12][sutun12] != 0):
                    break
                ilerle12()
        else:
            if(satir12 == 0 and sutun12 == 0):
                break
            ilerle12()

def basla21():
    while True:
        if type(sudoku[satir21][sutun21]) is not str:
            if(sudoku[satir21][sutun21] == 0):
                sudoku[satir21][sutun21] = 1

            if(kontrol2(satir21, sutun21) == False):
                if(sudoku[satir21][sutun21] < 9):
                    sudoku[satir21][sutun21] += 1
                else:
                    sudoku[satir21][sutun21] = 0
                    geriGel21()
            else:
                if(satir21 == 8 and sutun21 == 20 and sudoku[satir21][sutun21] != 0):
                    break
                ilerle21()
        else:
            if(satir21 == 8 and sutun21 == 20):
                break
            ilerle21()

def basla22():
    while True:
        if type(sudoku[satir22][sutun22]) is not str:
            if(sudoku[satir22][sutun22] == 0):
                sudoku[satir22][sutun22] = 1

            if(kontrol2(satir22, sutun22) == False):
                if(sudoku[satir22][sutun22] < 9):
                    sudoku[satir22][sutun22] += 1
                else:
                    sudoku[satir22][sutun22] = 0
                    geriGel22()
            else:
                if(satir22 == 0 and sutun22 == 12 and sudoku[satir22][sutun22] != 0):
                    break
                ilerle22()
        else:
            if(satir22 == 0 and sutun22 == 12):
                break
            ilerle22()

def basla31():
    while True:
        if type(sudoku[satir31][sutun31]) is not str:
            if(sudoku[satir31][sutun31] == 0):
                sudoku[satir31][sutun31] = 1

            if(kontrol3(satir31, sutun31) == False):
                if(sudoku[satir31][sutun31] < 9):
                    sudoku[satir31][sutun31] += 1
                else:
                    sudoku[satir31][sutun31] = 0
                    geriGel31()
            else:
                if(satir31 == 20 and sutun31 == 8 and sudoku[satir31][sutun31] != 0):
                    break
                ilerle31()
        else:
            if(satir31 == 20 and sutun31 == 8):
                break
            ilerle31()

def basla32():
    while True:
        if type(sudoku[satir32][sutun32]) is not str:
            if(sudoku[satir32][sutun32] == 0):
                sudoku[satir32][sutun32] = 1

            if(kontrol3(satir32, sutun32) == False):
                if(sudoku[satir32][sutun32] < 9):
                    sudoku[satir32][sutun32] += 1
                else:
                    sudoku[satir32][sutun32] = 0
                    geriGel32()
            else:
                if(satir32 == 12 and sutun32 == 0 and sudoku[satir32][sutun32] != 0):
                    break
                ilerle32()
        else:
            if(satir32 == 12 and sutun32 == 0):
                break
            ilerle32()

def basla41():
    while True:
        if type(sudoku[satir41][sutun41]) is not str:
            if(sudoku[satir41][sutun41] == 0):
                sudoku[satir41][sutun41] = 1

            if(kontrol4(satir41, sutun41) == False):
                if(sudoku[satir41][sutun41] < 9):
                    sudoku[satir41][sutun41] += 1
                else:
                    sudoku[satir41][sutun41] = 0
                    geriGel41()
            else:
                if(satir41 == 20 and sutun41 == 20 and sudoku[satir41][sutun41] != 0):
                    break
                ilerle41()
        else:
            if(satir41 == 20 and sutun41 == 20):
                break
            ilerle41()

def basla42():
    while True:
        if type(sudoku[satir42][sutun42]) is not str:
            if(sudoku[satir42][sutun42] == 0):
                sudoku[satir42][sutun42] = 1

            if(kontrol4(satir42, sutun42) == False):
                if(sudoku[satir42][sutun42] < 9):
                    sudoku[satir42][sutun42] += 1
                else:
                    sudoku[satir42][sutun42] = 0
                    geriGel42()
            else:
                if(satir42 == 12 and sutun42 == 12 and sudoku[satir42][sutun42] != 0):
                    break
                ilerle42()
        else:
            if(satir42 == 12 and sutun42 == 12):
                break
            ilerle42()

def basla51():
    while True:
        if type(sudoku[satir51][sutun51]) is not str:
            if(sudoku[satir51][sutun51] == 0):
                sudoku[satir51][sutun51] = 1

            if(kontrol5(satir51, sutun51) == False):
                if(sudoku[satir51][sutun51] < 9):
                    sudoku[satir51][sutun51] += 1
                else:
                    sudoku[satir51][sutun51] = 0
                    geriGel51()
            else:
                if(satir51 == 14 and sutun51 == 14 and sudoku[satir51][sutun51] != 0):
                    break
                ilerle51()
        else:
            if(satir51 == 14 and sutun51 == 14):
                break
            ilerle51()

def basla52():
    while True:
        if type(sudoku[satir52][sutun52]) is not str:
            if(sudoku[satir52][sutun52] == 0):
                sudoku[satir52][sutun52] = 1

            if(kontrol5(satir52, sutun52) == False):
                if(sudoku[satir52][sutun52] < 9):
                    sudoku[satir52][sutun52] += 1
                else:
                    sudoku[satir52][sutun52] = 0
                    geriGel52()
            else:
                if(satir52 == 6 and sutun52 == 6 and sudoku[satir52][sutun52] != 0):
                    break
                ilerle52()
        else:
            if(satir52 == 6 and sutun52 == 6):
                break
            ilerle52()

def basla1():
    t11 = threading.Thread(target=basla11)
    t12 = threading.Thread(target=basla12)
    
    t11.start()
    t12.start()
    t11.join()
    t12.join()

def basla2():
    t21 = threading.Thread(target=basla21)
    t22 = threading.Thread(target=basla22)
    
    t21.start()
    t22.start()
    t21.join()
    t22.join()

def basla3():
    t31 = threading.Thread(target=basla31)
    t32 = threading.Thread(target=basla32)
    
    t31.start()
    t32.start()
    t31.join()
    t32.join()

def basla4():
    t41 = threading.Thread(target=basla41)
    t42 = threading.Thread(target=basla42)
    
    t41.start()
    t42.start()
    t41.join()
    t42.join()

def basla5():
    t51 = threading.Thread(target=basla51)
    #t52 = threading.Thread(target=basla52)
    
    t51.start()
    #t52.start()
    t51.join()
    #t52.join()

olustur()
t1 = threading.Thread(target=basla1)
t2 = threading.Thread(target=basla2)
t3 = threading.Thread(target=basla3)
t4 = threading.Thread(target=basla4)
t5 = threading.Thread(target=basla5)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

t5.start()
t5.join()

printBoard(sudoku)

pencere.title("Samuray Sudoku")
pencere.geometry("1029x1029+350-20")

canvas.create_line(0,0,0,441, fill="green", width=14)
canvas.create_line(0,588,0,1029, fill="green", width=14)
canvas.create_line(147,0,147,441, fill="green", width=5)
canvas.create_line(147,588,147,1029, fill="green", width=5)
canvas.create_line(294,0,294,1029, fill="green", width=5)
canvas.create_line(441,0,441,1029, fill="green", width=5)
canvas.create_line(588,0,588,1029, fill="green", width=5)
canvas.create_line(735,0,735,1029, fill="green", width=5)
canvas.create_line(882,0,882,441, fill="green", width=5)
canvas.create_line(882,588,882,1029, fill="green", width=5)
canvas.create_line(1029,0,1029,441, fill="green", width=14)
canvas.create_line(1029,588,1029,1029, fill="green", width=14)
canvas.create_line(0,0,441,0, fill="green", width=14)
canvas.create_line(588,0,1029,0, fill="green", width=14)
canvas.create_line(0,147,441,147, fill="green", width=5)
canvas.create_line(588,147,1029,147, fill="green", width=5)
canvas.create_line(0,294,1029,294, fill="green", width=5)
canvas.create_line(0,441,1029,441, fill="green", width=5)
canvas.create_line(0,588,1029,588, fill="green", width=5)
canvas.create_line(0,735,1029,735, fill="green", width=5)
canvas.create_line(0,882,441,882, fill="green", width=5)
canvas.create_line(588,882,1029,882, fill="green", width=5)
canvas.create_line(0,1029,441,1029, fill="green", width=14)
canvas.create_line(588,1029,1029,1029, fill="green", width=14)
canvas.create_line(49,0,49,441, fill="red", width=2)
canvas.create_line(49,588,49,1029, fill="red", width=2)
canvas.create_line(98,0,98,441, fill="red", width=2)
canvas.create_line(98,588,98,1029, fill="red", width=2)
canvas.create_line(196,0,196,441, fill="red", width=2)
canvas.create_line(196,588,196,1029, fill="red", width=2)
canvas.create_line(245,0,245,441, fill="red", width=2)
canvas.create_line(245,588,245,1029, fill="red", width=2)
canvas.create_line(343,0,343,1029, fill="red", width=2)
canvas.create_line(392,0,392,1029, fill="red", width=2)
canvas.create_line(490,294,490,735, fill="red", width=2)
canvas.create_line(539,294,539,735, fill="red", width=2)
canvas.create_line(637,0,637,1029, fill="red", width=2)
canvas.create_line(686,0,686,1029, fill="red", width=2)
canvas.create_line(784,0,784,441, fill="red", width=2)
canvas.create_line(784,588,784,1029, fill="red", width=2)
canvas.create_line(833,0,833,441, fill="red", width=2)
canvas.create_line(833,588,833,1029, fill="red", width=2)
canvas.create_line(931,0,931,441, fill="red", width=2)
canvas.create_line(931,588,931,1029, fill="red", width=2)
canvas.create_line(980,0,980,441, fill="red", width=2)
canvas.create_line(980,588,980,1029, fill="red", width=2)
canvas.create_line(0,49,441,49, fill="red", width=2)
canvas.create_line(588,49,1029,49, fill="red", width=2)
canvas.create_line(0,98,441,98, fill="red", width=2)
canvas.create_line(588,98,1029,98, fill="red", width=2)
canvas.create_line(0,196,441,196, fill="red", width=2)
canvas.create_line(588,196,1029,196, fill="red", width=2)
canvas.create_line(0,245,441,245, fill="red", width=2)
canvas.create_line(588,245,1029,245, fill="red", width=2)
canvas.create_line(0,343,1029,343, fill="red", width=2)
canvas.create_line(0,392,1029,392, fill="red", width=2)
canvas.create_line(294,490,735,490, fill="red", width=2)
canvas.create_line(294,539,735,539, fill="red", width=2)
canvas.create_line(0,637,1029,637, fill="red", width=2)
canvas.create_line(0,686,1029,686, fill="red", width=2)
canvas.create_line(0,784,441,784, fill="red", width=2)
canvas.create_line(588,784,1029,784, fill="red", width=2)
canvas.create_line(0,833,441,833, fill="red", width=2)
canvas.create_line(588,833,1029,833, fill="red", width=2)
canvas.create_line(0,931,441,931, fill="red", width=2)
canvas.create_line(588,931,1029,931, fill="red", width=2)
canvas.create_line(0,980,441,980, fill="red", width=2)
canvas.create_line(588,980,1029,980, fill="red", width=2)

bastır()
pencere.mainloop()
