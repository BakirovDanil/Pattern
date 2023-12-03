import math
from tkinter.messagebox import showerror

import numpy as np


def Prior1(matrix_1_1, matrix_2_1, matrix_3_1,
           matrix_1_2, matrix_2_2, matrix_3_2,
           crit1, crit2, crit3,
           res1, res2):
    result1 = matrix_1_1.get() * crit1.get() + matrix_2_1.get() * crit2.get() + matrix_3_1.get() * crit3.get()
    result2 = matrix_1_2.get() * crit1.get() + matrix_2_2.get() * crit2.get() + matrix_3_2.get() * crit3.get()
    res1.set("{:.3f}".format(result1))
    res2.set("{:.3f}".format(result2))


def Raschet1(exp, res1, res2):
    print("Оценка первого эксперта для модели 1: " + str(exp.get() * res1.get()))
    print("Оценка первого эксперта для модели 2: " + str(exp.get() * res2.get()))


def Raschet2(exp, res1, res2):
    print("Оценка второго эксперта для модели 1: " + str(exp.get() * res1.get()))
    print("Оценка второго эксперта для модели 2: " + str(exp.get() * res2.get()))
