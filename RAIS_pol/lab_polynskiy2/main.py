import time
import webbrowser
import numpy
import pandas as pd
import warnings

import View

warnings.filterwarnings("ignore")
pd.options.display.max_columns = 100
pd.options.display.max_rows = 100

var = 'var5'
df1 = pd.read_csv(var+'/1.csv', index_col='id')
print(df1)
df2 = pd.read_csv(var+'/2.csv', index_col='id')
print(df2)
df3 = pd.read_csv(var+'/3.csv', index_col='id')
print(df3)
df4 = pd.read_csv(var+'/4.csv', index_col='id')
print(df4)
df5 = pd.read_csv(var+'/5.csv', index_col='id')
print(df5)

df2_2 = pd.read_csv(var+'/2.2.csv', index_col='id')
print(df2_2)

df2_7 = pd.read_csv(var+'/2.7.csv', delimiter=';', index_col='id')
print(df2_7)

dfcon = pd.read_csv(var+'/con1.csv', delimiter=';', index_col='id')
print(dfcon)

dfvar = pd.read_csv(var+'/variant.csv', delimiter=';')
print(dfvar)

id_uyz = []
znach = []

type_ = []
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
    type_.append(d)
    type_znach.append(r)
id_uyz.append(type_)
znach.append(type_znach)
type_ = []
type_znach = []
for id, row in df2.iterrows():
    d = []
    r = []
    for i in row.dropna().index:
        d.append(str(id) + '.' + str(i))
    for i in row.dropna():
        r.append(i)
    type_.append(d)
    type_znach.append(r)
id_uyz.append(type_)
znach.append(type_znach)
type_ = []
type_znach = []

for id, row in df3.iterrows():
    d = []
    r = []
    for i in row.dropna().index:
        d.append(str(id) + '.' + str(i))
    for i in row.dropna():
        r.append(i)
    type_.append(d)
    type_znach.append(r)
id_uyz.append(type_)
znach.append(type_znach)
type_ = []
type_znach = []
for id, row in df4.iterrows():
    d = []
    r = []
    for i in row.dropna().index:
        d.append(str(id) + '.' + str(i))
    for i in row.dropna():
        r.append(i)
    type_.append(d)
    type_znach.append(r)
id_uyz.append(type_)
znach.append(type_znach)
type_ = []
type_znach = []

for id, row in df5.iterrows():
    d = []
    r = []
    for i in row.dropna().index:
        d.append(str(id) + '.' + str(i))
    for i in row.dropna():
        r.append(i)
    type_.append(d)
    type_znach.append(r)
id_uyz.append(type_)
znach.append(type_znach)
type_ = []
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
            for type_ in range(len(line_str)):
                for id in range(len(line_str[type_])): #если без этго то в столбце тоже по типу
                    l_znach.append(dfvar.loc[(dfvar['типы'] == (l+1)), str(type_+1)].values[0])
            line_znach_var.append(l_znach)


# for i in line_znach_var:
#     print(i)

all_znach = []

for l in range(len(line_str)):
    # for type_L in range(len(line_str)):         #если без 2 этих то по типу в строчке
        for id_L in range(len(line_str[l])): #если без 2 этих то по типу в строчке
            l_znach = []
            for type_ in range(len(line_str)):
                for id in range(len(line_str[type_])): #если без этго то в столбце тоже по типу
                    l_znach.append(dfvar.loc[(dfvar['типы'] == (l+1)), str(type_+1)].values[0])
            all_znach.append(l_znach)

line_one_m = []
for type_ in range(len(line_str)):
    for id in range(len(line_str[type_])):
        line_one_m.append(line_str[type_][id])


gamma_m = pd.DataFrame(data=all_znach, columns=line_one_m, index=line_one_m)
webbrowser.open(View.View(gamma_m, 'gamma_m.html'))
# gamma_m.to_csv('gamma_m.csv')

print('Матрица ПСС по варианту')

pps_m = pd.DataFrame()

for type_ in line_str:
    for id in type_:
        r = dfcon.loc[dfcon[id] == '+', id]
        pps_m = pd.concat([pps_m, r], axis=1, names=[id])

pps_m.replace(to_replace=numpy.nan, value=0, inplace=True)
pps_m.replace(to_replace='+', value=1, inplace=True)
pps_m = pps_m.reset_index()
pps_m.sort_values('index', inplace=True)
pps_m = pps_m.set_index("index")
webbrowser.open(View.View(pps_m, 'pps_m.html'))
# pps_m.to_csv('pps_m.csv')

print('Матрица = М ПСС * М гамма (2.31)')

m = pps_m.dot(gamma_m)
webbrowser.open(View.View(m, 'm.html'))


means = m.sum(axis=1)

# Создаем новый объект pandas
r = []

# Делим значения на соответствующие средние значения
for i in range(len(means)):
    r.append(means.iloc[i])

import numpy as np

m_p = pd.DataFrame({'Сумма по строке': r}, index=m.index)
m_p['Всего'] = np.full(
  shape=len(r),
  fill_value=sum(r),
  dtype=np.float_
)
m_p['Значение'] = m_p['Сумма по строке'] / m_p['Всего']

webbrowser.open(View.View(m_p, 'm_p.html'))
print(m_p)

#матрица расстояний
r = []
for i in range(len(m_p.index)):
    r.append(np.abs(np.full(shape=len(m_p['Значение'].values),fill_value=m_p['Значение'].values[i] ,dtype=np.float_) - m_p['Значение'].values))
m_ugroz = pd.DataFrame(columns=m_p.index, index=m_p.index, data=r)
# for column in m_ugroz.columns:
#     for index in m_ugroz.index:
#         if index == column:
#             m_ugroz.loc[index, column] = np.nan
print(m_ugroz)
webbrowser.open(View.View(m_ugroz, 'm_ugroz.html'))
r = []
for i, row in m_ugroz.iterrows():
    r.append(sum(row) / (len(row)- 1))
m_sred = pd.DataFrame(columns=['Sred_rast'], data=r, index=m_ugroz.index)
print(m_sred)
webbrowser.open(View.View(m_sred, 'm_sred.html'))
list_dict = []

for column in m_ugroz.columns:
    for index in m_ugroz.index:
        if index == column:
            m_ugroz.loc[index, column] = 10000

pred_dict = {}
count = 0
for i, row in m_ugroz.iterrows():
    r = row.loc[(row < m_sred['Sred_rast'].iloc[count]) == True].index
    # print(m_sred['Sred_rast'].iloc[count])
    # print(row < m_sred['Sred_rast'].iloc[count])
    # time.sleep(5)
    count+=1
    pred_dict[i] = r
zad_group = 3
# zad_group = 5
m_pred = pd.DataFrame(data=pred_dict.values(), index=pred_dict.keys())
zad_num = 10
# zad_num = int(round(len(m_pred.index) / zad_group, 0))
# m_pred = m_pred.iloc[0:zad_group+1]
webbrowser.open(View.View(m_pred, 'm_pred.html'))


m_sred_copy = m_sred.copy().to_dict()['Sred_rast']
m_sred_copy = {k: v for k, v in sorted(m_sred_copy.items(), key=lambda item: item[1])}
all_d = {}
for i, row in m_pred.iterrows():
    d = []
    for r in row.values:
        if pd.isna(r):
            continue
        else:
            d.append(m_ugroz.loc[i].loc[r])
    all_d[i] = (d)
m_pred_num = pd.DataFrame(data=all_d.values(), index=all_d.keys())
webbrowser.open(View.View(m_pred_num, 'm_pred_num.html'))


result_pred_up = {}
index_not_use = []
for i, val in m_sred_copy.items():
    index_r = m_pred_num.loc[i].nsmallest(zad_num).index
    index_r = m_pred.loc[i].iloc[index_r].values
    ind_add = []
    if i not in index_not_use:
        for ind in index_r:
            if ind not in index_not_use and not pd.isna(ind):
                index_not_use.append(ind)
                index_not_use.append(i)
                ind_add.append(ind)
        result_pred_up[i] = ind_add

print(result_pred_up)


m_pred_up = pd.DataFrame(data=result_pred_up.values(), index=result_pred_up.keys())
m_pred_up = m_pred_up[(m_pred_up.notna().any(axis=1))]
m_pred_up = m_pred_up.fillna('')
webbrowser.open(View.View(m_pred_up, 'm_pred_up.html'))

m_sred_copy = m_sred.copy().to_dict()['Sred_rast']
m_sred_copy = {k: v for k, v in sorted(m_sred_copy.items(), key=lambda item: item[1], reverse=True)}

result_pred_down = {}
index_not_use = []
for i, val in m_sred_copy.items():
    index_r = m_pred_num.loc[i].nsmallest(zad_num).index
    index_r = m_pred.loc[i].iloc[index_r].values
    ind_add = []
    if i not in index_not_use:
        for ind in index_r:
            if ind not in index_not_use and not pd.isna(ind):
                index_not_use.append(ind)
                index_not_use.append(i)
                ind_add.append(ind)
        result_pred_down[i] = ind_add

print(result_pred_down)
m_pred_down = pd.DataFrame(data=result_pred_down.values(), index=result_pred_down.keys())
m_pred_down = m_pred_down[(m_pred_down.notna().any(axis=1))]
m_pred_down = m_pred_down.fillna('')
webbrowser.open(View.View(m_pred_down, 'm_pred_down.html'))

dict_group_f = {}
list_group_f = []
m_pred_up_list = []

for i, row in m_pred_up.iterrows():
    m_up = []
    m_up.append(i)
    for ii in row:
        if not pd.isna(ii):
            m_up.append(ii)
    m_pred_up_list.append(m_up)
print(m_pred_up_list)
m_pred_down_list = []
for i, row in m_pred_down.iterrows():
    m_down = []
    m_down.append(i)
    for ii in row:
        if not pd.isna(ii):
            m_down.append(ii)
    m_pred_down_list.append(m_down)
print(m_pred_down_list)
max_common_array = {}
for up in m_pred_up_list:
    for down in m_pred_down_list:
        max_array = [x for x in up if x in down]
        max_common_array[f'{up[0]}:{down[0]}'] = (max_array)

groups = {}
used_ = []
count = 1
for i in max_common_array:
    if len(max_common_array[i]) > 1:
        break_ = 0
        for ii in max_common_array[i]:
            if ii in used_:
                break_ = 1
        if break_ == 1:
            continue
        for ii in max_common_array[i]:
            used_.append(ii)
        groups[count] = max_common_array[i]
        print(count, groups[count])
        count+=1

# for i in m_pred_up.index:
#     list_group_f.append(i)
# for i, row in m_pred_up.iterrows():
#         r = (m_pred_down.loc[i] == row).values
#         print(i, row.loc[r].values)
#         dict_group_f[i] = row[r].values
#         for d in row[r].values:
#                 list_group_f.append(d)
#
m_pred_group = pd.DataFrame(data=groups.values(), index=groups.keys())
m_pred_group = m_pred_group.fillna('')
webbrowser.open(View.View(m_pred_group, 'm_pred_group.html'))



for i in m_ugroz.index.values:
    min = 1000
    min_j = 0
    if i not in used_:
        for j in m_pred.index.values:
            if (m_ugroz.loc[i].loc[j] < min):
                for key, value in groups.items():
                    if j in value:
                        min_j = key
                        min = m_ugroz.loc[i].loc[j]
                        break
        print(min_j, i, min)
        groups[min_j] = numpy.append(groups[min_j], i)
m_pred_group = pd.DataFrame(data=groups.values(), index=groups.keys())
print(m_pred_group)
m_pred_group = m_pred_group.fillna('')
webbrowser.open(View.View(m_pred_group, 'm_pred_group2.html'))
