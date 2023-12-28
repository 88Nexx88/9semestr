import numpy
import numpy as np

from tools.AllModelCalc import AllModelCalc
from tools.LogarithmicCalc import LogarithmicCalc
from data_parse import *

print('''
1 выборка
''')
print('X: ', x1)
print('Y: ', y1)
print()
AC = AllModelCalc(x1, y1)
AC.show()
AC.graphic('Первая')

print('''
2 выборка
''')
print('X: ', x2)
print('Y: ', y2)
print()
AC = AllModelCalc(x2, y2)
AC.show()
AC.graphic('Вторая')

print('''
3 выборка
''')
print('X: ', *x3)
print('Y: ', *y3)
print()
AC = AllModelCalc(x3, y3)
AC.show()
AC.graphic('Третья')

print('''
4 выборка
''')
print('X: ', *x4)
print('Y: ', *y4)
print()
LC = LogarithmicCalc(x4, y4)
LC.show()
LC.graphic('Четвертая')
