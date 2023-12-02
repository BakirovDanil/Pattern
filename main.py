from tkinter import *
from tkinter import ttk

import calculation
import numpy as np

import Figure

# создание главного окна приложения
Frame = Tk()
# значение для первой матрицы (сравнения экспертов)
matrix_1_1 = DoubleVar()
matrix_1_2 = DoubleVar()
matrix_2_1 = DoubleVar()
matrix_2_2 = DoubleVar()
matrix_3_1 = DoubleVar()
matrix_3_2 = DoubleVar()
matrix_1 = [[matrix_1_1, matrix_1_2],
            [matrix_2_1, matrix_2_2],
            [matrix_3_1, matrix_3_2]]
# результат счета для первого столбца
res_matrix_1_1 = DoubleVar()
# результат счета для второго столбца
res_matrix_1_2 = DoubleVar()
# критерии для приоритетности в первой матрице
crit1 = DoubleVar()
crit2 = DoubleVar()
crit3 = DoubleVar()

matrix1_1_1 = DoubleVar()
matrix1_1_2 = DoubleVar()
matrix1_1_3 = DoubleVar()
matrix1_2_1 = DoubleVar()
matrix1_2_2 = DoubleVar()
matrix1_2_3 = DoubleVar()
matrix1_3_1 = DoubleVar()
matrix1_3_2 = DoubleVar()
matrix1_3_3 = DoubleVar()
matrix_2 = [[matrix1_1_1, matrix1_1_2, matrix1_1_3],
            [matrix1_2_1, matrix1_2_2, matrix1_2_3],
            [matrix1_3_1, matrix1_3_2, matrix1_3_3]]
# результат счета для первого столбца
res_matrix_2_1 = DoubleVar()
# результат счета для второго столбца
res_matrix_2_2 = DoubleVar()
# результат счета для третьего столбца
res_matrix_2_3 = DoubleVar()

matrix2_1_1 = DoubleVar()
matrix2_1_2 = DoubleVar()
matrix2_1_3 = DoubleVar()
matrix2_2_1 = DoubleVar()
matrix2_2_2 = DoubleVar()
matrix2_2_3 = DoubleVar()
matrix2_3_1 = DoubleVar()
matrix2_3_2 = DoubleVar()
matrix2_3_3 = DoubleVar()
matrix_3 = [[matrix2_1_1, matrix2_1_2, matrix2_1_3],
            [matrix2_2_1, matrix2_2_2, matrix2_2_3],
            [matrix2_3_1, matrix2_3_2, matrix2_3_3]]


def Finish():
    Frame.destroy()
    print("Приложение закрыто")


def MainForm(window):
    window.title("Бакиров Данил, Валеев Марат, Баембитов Гата, Богомолов Валентин. Метод Pattern")
    window.geometry("800x750+400+200")
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", Finish)
    label = Figure.Label()
    label.Sozdanie(window)
    entry1 = Figure.Matrix1(matrix_1_1, matrix_1_2,
                            matrix_2_1, matrix_2_2,
                            matrix_3_1, matrix_3_2)
    entry1.Sozdanie(window)
    prior = Figure.Prior1(crit1, crit2, crit3)
    prior.Sozdanie(window)
    res = Figure.Result1(res_matrix_1_1, res_matrix_1_2)
    res.Sozdanie(window)
    window.mainloop()


button = ttk.Button(text="Произвести расчет", command=calculation.Prior1(matrix_1_1, matrix_2_1, matrix_3_1,
                                                                         matrix_1_2, matrix_2_2, matrix_3_2,
                                                                         crit1, crit2, crit3,
                                                                         res_matrix_1_1, res_matrix_1_2))
button.place(x=400, y=25)
MainForm(Frame)
