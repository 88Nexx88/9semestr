import time
import webbrowser
import numpy
import pandas as pd
import warnings

import View

warnings.filterwarnings("ignore")
pd.options.display.max_columns = 100
pd.options.display.max_rows = 100


df1 = pd.read_csv('1.csv', index_col='id')
print(df1)
df2 = pd.read_csv('2.csv', index_col='id')
print(df2)
df3 = pd.read_csv('3.csv', index_col='id')
print(df3)
df4 = pd.read_csv('4.csv', index_col='id')
print(df4)
df5 = pd.read_csv('5.csv', index_col='id')
print(df5)

df2_2 = pd.read_csv('2.2.csv', index_col='id')
print(df2_2)

df2_7 = pd.read_csv('2.7.csv', delimiter=';', index_col='id')
print(df2_7)

dfcon = pd.read_csv('con1.csv', delimiter=';', index_col='id')
print(dfcon)

dfvar = pd.read_csv('variant.csv', delimiter=';')
print(dfvar)

id_uyz = []
znach = []

type = []
type_znach = []
print('Преобразование матрицы по формуле 2.23 (гамма >= 0 /// гаммма < 0)')

for col in ['1', '2', '3', '4', '5']:
    dfvar[col] = dfvar[col].apply(float)
for col in ['1', '2', '3', '4', '5']:
    dfvar[col][dfvar[col] >= 0] += 1
for col in ['1', '2', '3', '4', '5']:
    dfvar.loc[dfvar[col] < 0, col] = 1 / (1 - dfvar[col])

print(dfvar)

for id, row in df1.iterrows():
    d = []
    r = []
    for i in row.dropna().index:
        d.append(str(id)+'.'+str(i))
    for i in row.dropna():
        r.append(i)
    type.append(d)
    type_znach.append(r)
id_uyz.append(type)
znach.append(type_znach)
type = []
type_znach = []
for id, row in df2.iterrows():
    d = []
    r = []
    for i in row.dropna().index:
        d.append(str(id) + '.' + str(i))
    for i in row.dropna():
        r.append(i)
    type.append(d)
    type_znach.append(r)
id_uyz.append(type)
znach.append(type_znach)
type = []
type_znach = []

for id, row in df3.iterrows():
    d = []
    r = []
    for i in row.dropna().index:
        d.append(str(id) + '.' + str(i))
    for i in row.dropna():
        r.append(i)
    type.append(d)
    type_znach.append(r)
id_uyz.append(type)
znach.append(type_znach)
type = []
type_znach = []
for id, row in df4.iterrows():
    d = []
    r = []
    for i in row.dropna().index:
        d.append(str(id) + '.' + str(i))
    for i in row.dropna():
        r.append(i)
    type.append(d)
    type_znach.append(r)
id_uyz.append(type)
znach.append(type_znach)
type = []
type_znach = []

for id, row in df5.iterrows():
    d = []
    r = []
    for i in row.dropna().index:
        d.append(str(id) + '.' + str(i))
    for i in row.dropna():
        r.append(i)
    type.append(d)
    type_znach.append(r)
id_uyz.append(type)
znach.append(type_znach)
type = []
type_znach = []

print('все уязвимости')
print(id_uyz)
print('все уязвимости + - по варианту')
print(znach)
all_line = []
# line_znach = []
# for line in range(len(id_uyz)):
#     for type in range(len(id_uyz)):
#         for id in range(len(id_uyz[type])):
#             if line == type:
#                 line_znach.append(0)
#             else:
#                 line_znach.append(dfvar.loc[(dfvar['типы'] == (line+1)), str(type+1)].values[0])
#     all_line.append(line_znach)
#     line_znach = []
# for i in all_line:
#     print(i)

print('все уязвимости по варианту')
line_str = []
for type_zn in range(len(znach)):
    line = []
    for id in range(len(znach[type_zn])):
        for i in range(len(znach[type_zn][id])):
            if znach[type_zn][id][i] == '+':
                line.append(id_uyz[type_zn][id][i])
    line_str.append(line)
print(line_str)

line_znach_var = []
for l in range(len(line_str)):
    # for type_L in range(len(line_str)):         #если без 2 этих то по типу в строчке
    #     for id_L in range(len(line_str[type_L])): #если без 2 этих то по типу в строчке
            l_znach = []
            for type in range(len(line_str)):
                for id in range(len(line_str[type])): #если без этго то в столбце тоже по типу
                    l_znach.append(dfvar.loc[(dfvar['типы'] == (l+1)), str(type+1)].values[0])
            line_znach_var.append(l_znach)


# for i in line_znach_var:
#     print(i)

print('Таблица M  (гамма) из противоположно симметричной в обратно симметричную по формуле 2.23')


file_info = []
r = []
for i in line_str:
    for j in i:
        r.append(j)

line = []
s = '{:^5} |'.format('')
for i in line_str:
    for j in i:
        s+=str((' {:^5} |'.format(j)))
line.append(s)


count = 0
for i in line_str:
    for j in i:
        s=str(('{:^5} |'.format(j)))
        for j_uyz in line_znach_var[count]:
            s += str(('{:^.5f}|'.format(j_uyz)))
        line.append(s)
    count += 1
for i in line:
    print(i)

with open('гамма.txt', 'w') as file:
    for i in line:
        file.write(i)
        file.write('\n')
    file.close()

print()
print()
all_znach = []

for l in range(len(line_str)):
    # for type_L in range(len(line_str)):         #если без 2 этих то по типу в строчке
        for id_L in range(len(line_str[l])): #если без 2 этих то по типу в строчке
            l_znach = []
            for type in range(len(line_str)):
                for id in range(len(line_str[type])): #если без этго то в столбце тоже по типу
                    l_znach.append(dfvar.loc[(dfvar['типы'] == (l+1)), str(type+1)].values[0])
            all_znach.append(l_znach)

line_one_m = []
for type in range(len(line_str)):
    for id in range(len(line_str[type])):
        line_one_m.append(line_str[type][id])


gamma_m = pd.DataFrame(data=all_znach, columns=line_one_m, index=line_one_m)
webbrowser.open(View.View(gamma_m, 'gamma_m.html'))
# gamma_m.to_csv('gamma_m.csv')

print('Матрица ПСС по варианту')

pps_m = pd.DataFrame()

for type in line_str:
    for id in type:
        r = dfcon.loc[dfcon[id] == '+', id]
        pps_m = pd.concat([pps_m, r], axis=1, names=[id])

pps_m.replace(to_replace=numpy.nan, value=0, inplace=True)
pps_m.replace(to_replace='+', value=1, inplace=True)
webbrowser.open(View.View(pps_m, 'pps_m.html'))
# pps_m.to_csv('pps_m.csv')

print('Матрица = М ПСС * М гамма (2.31)')

m = pps_m.dot(gamma_m)
webbrowser.open(View.View(m, 'm.html'))


means = m.mean(axis=1)

# Создаем новый объект pandas
m_p = m.copy()
# Делим значения на соответствующие средние значения
for i in range(len(means)):
    m_p.iloc[i, :] = m.iloc[i, :] / means.iloc[i]

webbrowser.open(View.View(m_p, 'm_p.html'))




