import threading
import tkinter as tk
from tkinter import *
from tkinter import ttk

okunan = []
sudoku = []
cozulmemis=[]
cozulmemisloc=[]

satir = 0
satir2 = 0
satir3 = 12
satir4 = 12
satir5 = 6

sutun = 0
sutun2 = 12
sutun3 = 0
sutun4 = 12
sutun5 = 6

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

def geriGel():
    global sutun, satir
    if(sutun == 0 and satir != 0):
        satir -= 1
        sutun = 8
    elif(sutun != 0):
        sutun -= 1
    if type(sudoku[satir][sutun]) is not str:
        if(sudoku[satir][sutun] < 9):
            sudoku[satir][sutun] += 1
        else:
            sudoku[satir][sutun] = 0
            geriGel()
    else:
        geriGel()

def geriGel2():
    global sutun2, satir2
    if(sutun2 == 12 and satir2 != 0):
        satir2 -= 1
        sutun2 = 20
    elif(sutun2 != 12):
        sutun2 -= 1
    if type(sudoku[satir2][sutun2]) is not str:
        if(sudoku[satir2][sutun2] < 9):
            sudoku[satir2][sutun2] += 1
        else:
            sudoku[satir2][sutun2] = 0
            geriGel2()
    else:
        geriGel2()

def geriGel3():
    global sutun3, satir3
    if(sutun3 == 0 and satir3 != 12):
        satir3 -= 1
        sutun3 = 8
    elif(sutun3 != 0):
        sutun3 -= 1
    if type(sudoku[satir3][sutun3]) is not str:
        if(sudoku[satir3][sutun3] < 9):
            sudoku[satir3][sutun3] += 1
        else:
            sudoku[satir3][sutun3] = 0
            geriGel3()
    else:
        geriGel3()

def geriGel4():
    global sutun4, satir4
    if(sutun4 == 12 and satir4 != 12):
        satir4 -= 1
        sutun4 = 20
    elif(sutun4 != 12):
        sutun4 -= 1
    if type(sudoku[satir4][sutun4]) is not str:
        if(sudoku[satir4][sutun4] < 9):
            sudoku[satir4][sutun4] += 1
        else:
            sudoku[satir4][sutun4] = 0
            geriGel4()
    else:
        geriGel4()

def geriGel5():
    global sutun5, satir5
    if(sutun5 == 6 and satir5 != 6):
        satir5 -= 1
        sutun5 = 14
    elif(sutun5 != 6):
        sutun5 -= 1
    if type(sudoku[satir5][sutun5]) is not str:
        if(sudoku[satir5][sutun5] < 9):
            sudoku[satir5][sutun5] += 1
        else:
            sudoku[satir5][sutun5] = 0
            geriGel5()
    else:
        geriGel5()

def ilerle():
    global sutun, satir
    if(sutun == 8 and satir != 8):
        satir += 1
        sutun = 0
    elif(sutun != 8):
        sutun += 1

def ilerle2():
    global sutun2, satir2
    if(sutun2 == 20 and satir2 != 8):
        satir2 += 1
        sutun2 = 12
    elif(sutun2 != 20):
        sutun2 += 1

def ilerle3():
    global sutun3, satir3
    if(sutun3 == 8 and satir3 != 20):
        satir3 += 1
        sutun3 = 0
    elif(sutun3 != 8):
        sutun3 += 1

def ilerle4():
    global sutun4, satir4
    if(sutun4 == 20 and satir4 != 20):
        satir4 += 1
        sutun4 = 12
    elif(sutun4 != 20):
        sutun4 += 1

def ilerle5():
    global sutun5, satir5
    if(sutun5 == 14 and satir5 != 14):
        satir5 += 1
        sutun5 = 6
    elif(sutun5 != 14):
        sutun5 += 1

def basla1():
    while True:
        if type(sudoku[satir][sutun]) is not str:
            if(sudoku[satir][sutun] == 0):
                sudoku[satir][sutun] = 1

            if(kontrol(satir, sutun) == False):
                if(sudoku[satir][sutun] < 9):
                    sudoku[satir][sutun] += 1
                else:
                    sudoku[satir][sutun] = 0
                    geriGel()
            else:
                if(satir == 8 and sutun == 8 and sudoku[satir][sutun] != 0):
                    break
                ilerle()
        else:
            if(satir == 8 and sutun == 8):
                break
            ilerle()

def basla2():
    while True:
        if type(sudoku[satir2][sutun2]) is not str:
            if(sudoku[satir2][sutun2] == 0):
                sudoku[satir2][sutun2] = 1

            if(kontrol2(satir2, sutun2) == False):
                if(sudoku[satir2][sutun2] < 9):
                    sudoku[satir2][sutun2] += 1
                else:
                    sudoku[satir2][sutun2] = 0
                    geriGel2()
            else:
                if(satir2 == 8 and sutun2 == 20 and sudoku[satir2][sutun2] != 0):
                    break
                ilerle2()
        else:
            if(satir2 == 8 and sutun2 == 20):
                break
            ilerle2()

def basla3():
    while True:
        if type(sudoku[satir3][sutun3]) is not str:
            if(sudoku[satir3][sutun3] == 0):
                sudoku[satir3][sutun3] = 1

            if(kontrol3(satir3, sutun3) == False):
                if(sudoku[satir3][sutun3] < 9):
                    sudoku[satir3][sutun3] += 1
                else:
                    sudoku[satir3][sutun3] = 0
                    geriGel3()
            else:
                if(satir3 == 20 and sutun3 == 8 and sudoku[satir3][sutun3] != 0):
                    break
                ilerle3()
        else:
            if(satir3 == 20 and sutun3 == 8):
                break
            ilerle3()

def basla4():
    while True:
        if type(sudoku[satir4][sutun4]) is not str:
            if(sudoku[satir4][sutun4] == 0):
                sudoku[satir4][sutun4] = 1

            if(kontrol4(satir4, sutun4) == False):
                if(sudoku[satir4][sutun4] < 9):
                    sudoku[satir4][sutun4] += 1
                else:
                    sudoku[satir4][sutun4] = 0
                    geriGel4()
            else:
                if(satir4 == 20 and sutun4 == 20 and sudoku[satir4][sutun4] != 0):
                    break
                ilerle4()
        else:
            if(satir4 == 20 and sutun4 == 20):
                break
            ilerle4()

def basla5():
    while True:
        if type(sudoku[satir5][sutun5]) is not str:
            if(sudoku[satir5][sutun5] == 0):
                sudoku[satir5][sutun5] = 1

            if(kontrol5(satir5, sutun5) == False):
                if(sudoku[satir5][sutun5] < 9):
                    sudoku[satir5][sutun5] += 1
                else:
                    sudoku[satir5][sutun5] = 0
                    geriGel5()
            else:
                if(satir5 == 14 and sutun5 == 14 and sudoku[satir5][sutun5] != 0):
                    break
                ilerle5()
        else:
            if(satir5 == 14 and sutun5 == 14):
                break
            ilerle5()

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