import os.path

from PIL import Image



class q1:
    def files():
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        print(files)

    def pictures(path1,number, search=-1, w=200, h=300):
        path = 'q1_1/'
        sklad = {1: ['Дайте определение системы m линейных алгебраических уравнений c n неизвестными. Какая СЛАУ называется однородной, неоднородной. Приведите соответствующие примеры. Может ли неоднородная СЛАУ Ax = b быть неопределенной, если столбцы её матрицы линейно независимы (линейно зависимы)? Ответ необходимо обосновать.', 
                    [Image.open(f'{path1}/q1_1/1/{x}') for x in [f for f in os.listdir(f'{path}/1') if os.path.isfile(os.path.join(f'{path}/1', f))]]]}
        if number == -1:
            numbers = []
            for i, j in sklad.items():
                if search in j[0]:
                    numbers.append(i)
            return 'есть в этих номерах: ', numbers
        print(sklad[number][0])
        new_img = []
        for a in sklad[number][1]:
            #while height > 1000:
            #    width /= 1.5
            #    height /= 1.5
            a = a.resize((w, h))
            new_img.append(a)
        return new_img


class q2:
    def pictures(path1,number, search=-1, w=200, h=300):
        path = 'q2_1/'
        sklad = {1: ['Дайте определение комплексного числа в алгебраической форме. Приведите тригонометрическую и показательную формы комплексного числа. Выведите формулу площади параллелограмма с вершинами в точках z1 и z2 комплексной плоскости.', 
                    [Image.open(f'{path1}/{path}/1/{x}') for x in [f for f in os.listdir(f'{path}/1') if os.path.isfile(os.path.join(f'{path}/1', f))]]]}
        if number == -1:
            numbers = []
            for i, j in sklad.items():
                if search in j[0]:
                    numbers.append(i)
            return 'есть в этих номерах: ', numbers
        print(sklad[number][0])
        new_img = []
        for a in sklad[number][1]:
            #while height > 1000:
            #    width /= 1.5
            #    height /= 1.5
            a = a.resize((w, h))
            new_img.append(a)
        return new_img


class q3:
    def pictures(path1,number, search=-1, w=200, h=300):
        path = 'q3_1/'
        sklad = {1: ['Дайте определение линейного пространства и приведите примеры линейных пространств. Является ли линейным пространством V1 = {f ∈ R4[x] : f(5) = 0}, V2 = {f ∈ R4[x] : f(5) = 2}? Ответ необходимо обосновать.', 
                    [Image.open(f'{path1}/{path}/1/{x}') for x in [f for f in os.listdir(f'{path}/1') if os.path.isfile(os.path.join(f'{path}/1', f))]]]}
        if number == -1:
            numbers = []
            for i, j in sklad.items():
                if search in j[0]:
                    numbers.append(i)
            return 'есть в этих номерах: ', numbers
        print(sklad[number][0])
        new_img = []
        for a in sklad[number][1]:
            #while height > 1000:
            #    width /= 1.5
            #    height /= 1.5
            a = a.resize((w, h))
            new_img.append(a)
        return new_img
