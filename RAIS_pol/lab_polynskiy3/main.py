import math
import time

import numpy
import pandas as pd

pd.set_option('display.max_columns',  1000)

treb = pd.read_csv('treb.csv')

lab3 = pd.read_csv('var6/lab3.csv', delimiter=';', index_col='index')

print(treb)

print(lab3)
print('1___________________________________________')
print('Вычислить дополнения нечётких множеств A и B ,'
      ' и соответственно кардинальные числа этих дополнений.')
step = 'дополнения'
df_dop = pd.DataFrame(index=lab3['x'])
# round(,treb['Точность представления'].loc[treb['Вид показателя'] == step])
df_dop['дополнения A'] = 1 - (lab3['A'])
df_dop['дополнения A'] = df_dop['дополнения A'].round(int(treb['Точность представления'].loc[treb['Вид показателя'] == step].iloc[0]))
df_dop['кард_доп_А'] = df_dop['дополнения A'].sum()

df_dop['дополнения B'] = 1 - (lab3['B'])
df_dop['дополнения B'] = df_dop['дополнения B'].round(int(treb['Точность представления'].loc[treb['Вид показателя'] == step].iloc[0]))
df_dop['кард_доп_B'] = df_dop['дополнения B'].sum()
print(df_dop)
print('2___________________________________________')
print('Вычислить пересечения нечётких множеств A и B'
      '(двумя способами) и соответственно кардинальные числа этих пересечений.')
step = 'пересечения'
df_per = pd.DataFrame(index=lab3['x'])
df_per['пересечение 1'] = (lab3[['A', 'B']].min(axis=1))
df_per['пересечение 1']=df_per['пересечение 1'].round(treb['Точность представления'].loc[treb['Вид показателя'] == step].iloc[0])
df_per['кард_пер_1'] = df_per['пересечение 1'].sum()

df_per['пересечение 2'] = (lab3['A']) * (lab3['B'])
df_per['пересечение 2']=df_per['пересечение 2']
df_per['кард_пер_2'] = df_per['пересечение 2'].sum()

print(df_per)

print('3___________________________________________')
print('Сравнить кардинальные числа по п.2 и объяснить их различия.')
print(round(df_per['кард_пер_1'].iloc[0], 3), ' - ', round(df_per['кард_пер_2'].iloc[0], 3),' = ',
    round(abs(df_per['кард_пер_1'].iloc[0] - df_per['кард_пер_2'].iloc[0]),
    int(treb['Точность представления'].loc[treb['Вид показателя'] == step].iloc[0])))
print('''Первая формула расчёта (то есть 1 значение) даёт при любых значениях степеней
принадлежности элементов в обоих исходных множествах такие значения в результирующем, которые никогда не могут быть меньше, чем
по второй формуле. Т.е. является менее строгим правилом пересечения.''')

print('4___________________________________________')
print('Вычислить объединения нечётких множеств A и B '
      '(двумя способами) и соответственно кардинальные числа этих объединений.')

step = 'объединения'
df_ob = pd.DataFrame(index=lab3['x'])
df_ob['объединение 1'] = lab3[['A', 'B']].max(axis=1)
df_ob['объединение 1']=df_ob['объединение 1'].round(int(treb['Точность представления'].loc[treb['Вид показателя'] == step].iloc[0]))
df_ob['кард_объед_1'] = df_ob['объединение 1'].sum()

df_ob['объединение 2'] = lab3['A'] + lab3['B']
df_ob['объединение 2'].loc[df_ob['объединение 2'] >= 1] = 1
df_ob['объединение 2']=df_ob['объединение 2'].round(int(treb['Точность представления'].loc[treb['Вид показателя'] == step].iloc[0]))
df_ob['кард_объед_2'] = df_ob['объединение 2'].sum().round((int(treb['Точность представления'].loc[treb['Вид показателя'] == step].iloc[0])))

print(df_ob)
print('5___________________________________________')
print('Сравнить кардинальные числа по п.4 и объяснить их различия.')
print(df_ob['кард_объед_1'].iloc[0], ' - ',df_ob['кард_объед_2'].iloc[0],' = ',
    round(abs(df_ob['кард_объед_1'].iloc[0] - df_ob['кард_объед_2'].iloc[0]),
    int(treb['Точность представления'].loc[treb['Вид показателя'] == step].iloc[0])))
print('''
Первая формула расчёта (то есть первое значение) даёт при любых значениях степеней
принадлежности элементов в обоих исходных множествах такие значения в результирующем, которые никогда не могут быть больше, чем
по второй формуле. Т.е. является более строгим правилом объединения.
''')
print('6___________________________________________')
print('''
Построить отображение нечёткого множества A в универсальном множестве Y согласно функции f(x) и вычислить кардинальное число полученного нечёткого множества.
''')
# y = range(int(lab3['y'].iloc[0].split('_')[0]), int(lab3['y'].iloc[0].split('_')[1]))

y = [int(lab3['y'].iloc[0].split('_')[0]), int(lab3['y'].iloc[0].split('_')[1])]
df_fun_Y = pd.DataFrame(index=range(y[0], y[1]+1))
print(f'y=[{y}]')
fx = lab3['fx'].iloc[0].split(' = ')[1]
print(f'fx={fx}')
u_Y = [0 for i in range(0, y[1]+1)]
for x in lab3['x'].values:
    # print(f'{fx} при x={x} = {eval(fx)}')
    if (eval(fx) >= y[0]) and (eval(fx) <= y[-1]):
        u_Y[eval(fx)] = lab3['A'].loc[lab3['x'] == x].values[0]
df_fun_Y['Y'] = u_Y[y[0]:]
df_fun_Y['Y'] = df_fun_Y['Y']
df_fun_Y['кард_Y'] = df_fun_Y['Y'].sum()
print(df_fun_Y)
print('7___________________________________________')
print('''
Вычислить меры энтропии нечётких множеств A и B
(аксиоматически и метрически для расстояний Хэмминга и Евклида).
''')
df_aks = pd.DataFrame(index=lab3['x'])
df_aks['A'] = lab3['A']
df_aks['A_'] = df_aks['A'].apply(lambda x: 1 if x >= 0.5 else 0)
S_y = []
for y in df_aks['A'].values:
    if y == 0 or y == 1:
        S_y.append(0)
    else:
        S_y.append(-y*(math.log(y, math.e))-(1-y)*math.log(1-y, math.e))
df_aks['d(A)лог'] = 1/len(S_y) * sum(S_y)
df_aks['d(A)лог'] = df_aks['d(A)лог'].round(4)
S_y = []
for i, row in df_aks.iterrows():
    # S_y.append((1-numpy.abs(2*row['A']-1))**2)
    S_y.append((row['A'] - row['A_'])**(2)) #2variant
# df_aks['d(A)евкл'] = 1/(len(S_y)**(1/2)) * sum(S_y)**(1/2)
df_aks['d(A)евкл'] = 2/(len(S_y)**(1/2)) * sum(S_y)**(1/2) #2variant
df_aks['d(A)евкл'] = df_aks['d(A)евкл'].round(4)


S_y = []
for i, row in df_aks.iterrows():
    S_y.append((numpy.abs(row['A'] - row['A_'])))

df_aks['d(A)хэм'] = 2/(len(S_y)) * sum(S_y)
df_aks['d(A)хэм'] = df_aks['d(A)хэм'].round(4)
df_aks['B'] = lab3['B']
df_aks['B_'] = df_aks['B'].apply(lambda x: 1 if x >= 0.5 else 0)

S_y = []
for y in df_aks['B'].values:
    if y == 0 or y == 1:
        S_y.append(0)
    else:
        S_y.append(-y*(math.log(y, math.e))-(1-y)*math.log(1-y, math.e))
df_aks['d(B)лог'] = 1/len(S_y) * sum(S_y)
df_aks['d(B)лог'] = df_aks['d(B)лог'].round(4)
S_y = []
for i, row in df_aks.iterrows():
    # S_y.append((1-numpy.abs(2*row['B']-1))**2)
    S_y.append((row['B'] - row['B_'])**(2)) #2variant
# df_aks['d(B)евкл'] = 1/(len(S_y)**(1/2)) * sum(S_y)**(1/2)
df_aks['d(B)евкл'] = 2/(len(S_y)**(1/2)) * sum(S_y)**(1/2) #2variant
df_aks['d(B)евкл'] = df_aks['d(B)евкл'].round(4)


S_y = []
for i, row in df_aks.iterrows():
    S_y.append((numpy.abs(row['B'] - row['B_'])))

df_aks['d(B)хэм'] = 2/(len(S_y)) * sum(S_y)
df_aks['d(B)хэм'] = df_aks['d(B)хэм'].round(4)
print(df_aks)
print('9___________________________________________')
print('''
Вычислить функции доверия нечётким множествам A и B (для расстояний Хэмминга и Евклида)
''')

df_dov = pd.DataFrame(index=lab3['x'])
df_dov['A'] = lab3['A']
u_A_sr = 1 / len(df_dov['A']) * sum(df_dov['A'])

S_y = []
S_y_2 = []
for y in df_aks['A'].values:
        S_y.append(numpy.abs(y - u_A_sr))
        S_y_2.append((y - u_A_sr)**2)
df_dov['d(A)евкл'] = 1 - (2/(len(S_y_2)**(1/2)) * sum(S_y_2)**(1/2))
df_dov['d(A)евкл'] = df_dov['d(A)евкл'].round(4)
df_dov['d(A)хэм'] = 1 - (2/len(S_y) * sum(S_y))
df_dov['d(A)хэм'] = df_dov['d(A)хэм'].round(4)
df_dov['uA_СР'] = u_A_sr

df_dov['B'] = lab3['B']
u_B_sr = 1 / len(df_dov['B']) * sum(df_dov['B'])

S_y = []
S_y_2 = []
for y in df_aks['B'].values:
        S_y.append(numpy.abs(y - u_B_sr))
        S_y_2.append((y - u_B_sr)**2)
df_dov['d(B)евкл'] = 1 - (2/(len(S_y_2)**(1/2)) * sum(S_y_2)**(1/2))
df_dov['d(B)евкл'] = df_dov['d(B)евкл'].round(4)
df_dov['d(B)хэм'] = 1 - (2/len(S_y) * sum(S_y))
df_dov['d(B)хэм'] = df_dov['d(B)хэм'].round(4)
df_dov['uB_СР'] = u_B_sr

print(df_dov)
