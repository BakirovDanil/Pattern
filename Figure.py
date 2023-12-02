from tkinter import ttk
from abc import ABC
from tkinter.messagebox import showerror


def on_key_press(event):
    if event.char.lower() not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                  '\x08']:
        return "break"
    elif event.char == '.' in event.widget.get():
        return "break"


def proverka(m):
    found_invalid_value = False
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j].get() > 1 or m[i][j].get() == 0:
                found_invalid_value = True
                m[i][j].set(0)

    if found_invalid_value:
        showerror(title="Ошибка", message="Введенные данные некорректны. Одно из значений превышает 9 или равно нулю")
        for i in range(len(m)):
            for j in range(len(m[i])):
                if i != j:
                    m[i][j].set(0)
        return False
    else:
        return True


class Figure(ABC):
    def Sozdanie(self, window):
        pass


class Label(Figure):
    def Sozdanie(self, window):
        # Размещение текстовых полей критерий по вертикали
        crit1h = ttk.Label(text="Критерий 1")
        crit2h = ttk.Label(text="Критерий 2")
        crit3h = ttk.Label(text="Критерий 3")
        crit4h = ttk.Label(text="Общая значимость\nкаждого эксперта")
        # Размещение текстовых полей критерий по горизонтали
        crit1v = ttk.Label(text="Приоритетность\nкритериев")
        crit2v = ttk.Label(text="Эксперт 1")
        crit3v = ttk.Label(text="Эксперт 2")
        #
        crit1h.place(x=25, y=40)
        crit2h.place(x=25, y=85)
        crit3h.place(x=25, y=130)
        crit4h.place(x=25, y=175)
        #
        crit1v.place(x=110, y=7)
        crit2v.place(x=210, y=7)
        crit3v.place(x=270, y=7)


class Result1(Figure):
    def __init__(self, res1, res2):
        self.res1 = res1
        self.res2 = res2

    def Sozdanie(self, window):
        res1 = ttk.Entry(width=5, textvariable=self.res1)
        res2 = ttk.Entry(width=5, textvariable=self.res2)
        spisok = [res1, res2]
        for i in spisok:
            i.bind("<Key>", on_key_press)
        res1.place(x=210, y=175)
        res2.place(x=270, y=175)


class Prior1(Figure):
    def __init__(self, criter1, criter2, criter3):
        self.criter1 = criter1
        self.criter2 = criter2
        self.criter3 = criter3

    def Sozdanie(self, window):
        crit1 = ttk.Entry(width=5, textvariable=self.criter1)
        crit2 = ttk.Entry(width=5, textvariable=self.criter2)
        crit3 = ttk.Entry(width=5, textvariable=self.criter3)
        spisok = [crit1, crit2, crit3]
        for i in spisok:
            i.bind("<Key>", on_key_press)
        crit1.place(x=110, y=40)
        crit2.place(x=110, y=85)
        crit3.place(x=110, y=130)


class Matrix1(Figure):
    def __init__(self, matrix_1_1, matrix_1_2,
                 matrix_2_1, matrix_2_2,
                 matrix_3_1, matrix_3_2):
        self.matrix_1_1 = matrix_1_1
        self.matrix_1_2 = matrix_1_2
        self.matrix_2_1 = matrix_2_1
        self.matrix_2_2 = matrix_2_2
        self.matrix_3_1 = matrix_3_1
        self.matrix_3_2 = matrix_3_2

    def Sozdanie(self, window):
        m11 = ttk.Entry(width=5, textvariable=self.matrix_1_1)
        m12 = ttk.Entry(width=5, textvariable=self.matrix_1_2)
        m21 = ttk.Entry(width=5, textvariable=self.matrix_2_1)
        m22 = ttk.Entry(width=5, textvariable=self.matrix_2_2)
        m31 = ttk.Entry(width=5, textvariable=self.matrix_3_1)
        m32 = ttk.Entry(width=5, textvariable=self.matrix_3_2)
        matrix0 = [m11, m12, m21, m22, m31, m32]
        for i in matrix0:
            i.bind("<Key>", on_key_press)
        m11.place(x=210, y=40)
        m12.place(x=270, y=40)
        m21.place(x=210, y=85)
        m22.place(x=270, y=85)
        m31.place(x=210, y=130)
        m32.place(x=270, y=130)
