import math
import numpy as np
import scipy.stats
from scipy import interpolate
import pandas as pd


def koef_pr(koef_ir, type_ir, num_ir):
    a = type_ir['начальный'].iloc[num_ir]
    I_g = 1
    for i in range(a, a+type_ir['текущий'].iloc[num_ir]-1):
        I_g *= koef_ir[str(i)]
    return I_g

def s_baz(goda, price):
    print(price, "!!!")
    sum_g = price.sum()
    return sum_g


def custom_sort(arr):
    zero_indexes = [i for i, v in enumerate(arr) if v == 0]
    non_zero_elements = [v for v in arr if v != 0]

    non_zero_elements.sort()

    for index in zero_indexes:
        non_zero_elements.insert(index, 0)

    return non_zero_elements

def pereraschet(rang_price):
    new_rang_price = rang_price.copy()
    break_point = 0
    for i in range(len(rang_price) - 1):
        if rang_price[i] != 0:
            for j in range(i, len(rang_price)):
                if rang_price[j] != 0:
                    if rang_price[i] > rang_price[j]:
                        print('Условие не выполнено перерасчёт')
                        new_rang_price = custom_sort(rang_price)
                        break_point = 1
                        break
            if break_point == 1:
                new_rang_price = pereraschet(new_rang_price)
                break
    return new_rang_price



price_all_ir = [0, 0, 0, 0, 0, 0, 0, 0]


rang_ir = pd.read_csv("rang_ir.csv")
print(rang_ir)
print()
type_ir = pd.read_csv("3var/type_ir.csv")
print(type_ir)
print()
info_1 = pd.read_csv("1ir.csv")
print(info_1)
print()

koef_ir = pd.read_csv("koef.csv")
print(koef_ir)
print()
print()
priob_nach_1 = info_1.iloc[0].to_list()

I_g = koef_pr(koef_ir, type_ir, 0)
print(priob_nach_1[1], '*', I_g, ') * (', "(1-(",(type_ir['текущий'].iloc[0],"-1)",
                                   "/",
                                   (type_ir['планируемый'].iloc[0])))
r = 1.10*1.12*1.15
S_priobr = priob_nach_1[1]*r*(1-((type_ir['текущий'].iloc[0]-1)
                                   /
                                   (type_ir['планируемый'].iloc[0])))
print("S приор к tk году = ",round(S_priobr, 3))

print()
print()

goda = info_1.iloc[2]
price = info_1.iloc[4:10].astype(float)
price_info = pd.DataFrame(columns = goda.to_list(), data = price.values)


S_baz = s_baz(goda, price_info)

S_nak = [S_baz[goda.iloc[0]]]

count = 1

k = [1.10, 1.12, 1.15] # свои
for g in goda.iloc[1:len(goda)]:
    print('S_baz goda', S_baz[g], 's_nak pr ',S_nak[-1], 'k ',k[(count-1)])
    S_nak.append(S_baz[g]+S_nak[-1]*k[(count-1)])
    count+=1
print(S_nak)
print()
# print(S_nak[-1], '\n',koef_pr(koef_ir,type_ir, 0),'\n', (1-((type_ir['текущий'].iloc[0]-1)
#                                    /
#                                    (type_ir['планируемый'].iloc[0]))))
S_raz = S_nak[-1]*1.15 * (1-((type_ir['текущий'].iloc[0]-1)
                                   /
                                   (type_ir['планируемый'].iloc[0])))
print("S разр к tk году = ", round(S_raz, 3))
print()
print(S_priobr, S_raz, info_1['info1'].iloc[-1])
print("1 ИР = ", round(S_priobr + S_raz +  info_1['info1'].iloc[-1],3))
price_all_ir[0] = (round(S_priobr + S_raz +  info_1['info1'].iloc[-1],3))


# ______________________________________________________________
info_2 = pd.read_csv("2ir.csv")
print(info_2)
print()

S_obs = info_2['info'].sum()

print("2 ИР = ", S_obs + info_2['info1'].iloc[0])
price_all_ir[1] = (S_obs+info_2['info1'].iloc[0])


# ______________________________________________________________
info_3 = pd.read_csv("3ir.csv")
print(info_3)
print()

S_obs = info_3['info'].sum()

print("3 ИР = ", S_obs)
price_all_ir[2] = (S_obs)
# _____________________________________________________________
info_4 = pd.read_csv("4ir.csv")
print(info_4)
print()

S_baz = info_4['info'].sum()
S_raz = (S_baz*koef_pr(koef_ir, type_ir, 3) * (1-((type_ir['текущий'].iloc[3]-1)
                                   /
                                   (type_ir['планируемый'].iloc[3]))))


print("S разр к tk году = ", round(S_raz.values[0], 3))


print("4 ИР = ", round(S_raz.values[0] +  info_4['info1'].iloc[0]))
price_all_ir[3] = (S_raz.values[0] +  info_4['info1'].iloc[0])
# ______________________________________________________________
info_5 = pd.read_csv("5ir.csv")
print(info_5)
print()

S_baz = info_5['info'].sum()
S_raz = (S_baz*koef_pr(koef_ir, type_ir, 4) * (1-((type_ir['текущий'].iloc[4]-1)
                                   /
                                   (type_ir['планируемый'].iloc[4]))))


print("S разр к tk году = ", round(S_raz.values[0], 3))

S_obs = info_5['info1'].sum()

print("5 ИР = ", S_obs+S_raz.values[0])
price_all_ir[4] = (S_obs+S_raz.values[0])

print("_________________________________________________")

info_ir = pd.DataFrame(columns=['price'], data=price_all_ir)
print(info_ir)
print("_________________________________________________")

print("_________________________________________________")

info_ir = pd.DataFrame(columns=['price'], data=price_all_ir)
info_ir['rang'] = rang_ir['Ранг']
print(info_ir)
print("_________________________________________________")
print("_________________________________________________")
rang_price = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1, 9):
    rang_price[i] = info_ir['price'].loc[info_ir['rang'] == i].mean()

for i in range(len(rang_price)):
    if pd.isna(rang_price[i]):
        rang_price[i] = 0

print('Значение по рангам')
print(rang_price)
print("_________________________________________________")
print("Проверим условие 1.11")

test = pereraschet(rang_price)
print('Значение после перерасчёта')
print(test)
print('Результаты проверки условий ранжирования ИР')


rang_first = []
rang_last = []
dEk = []
for i in range(len(test)-1):
    if test[i] != 0:
        for j in range(i+1, len(test)):
            if test[j] != 0:
                a = round((test[j] / test[i])**(1/(j-i)), 3)
                rang_first.append(i)
                rang_last.append(j)
                dEk.append(a)

stup_rosta = pd.DataFrame({'first': rang_first, 'last':rang_last, 'dEk':dEk})
print(stup_rosta)
# dEk_rang_test =  [round(scipy.stats.gmean(stup_rosta['dEk'].loc[stup_rosta['first'] == f]), 3) for f in stup_rosta['first'].unique()]
# print(dEk_rang_test)
# print(round(scipy.stats.gmean(dEk_rang_test), 3))
print('____________________________________________')
dEk_test2 = [stup_rosta['dEk'].loc[stup_rosta['first'] == i].values[0] for i in stup_rosta['first'].unique()]
print(dEk_test2)
print(round(scipy.stats.gmean(dEk_test2), 3))
delta_dEk = round(scipy.stats.gmean(dEk_test2), 3)
uslovie_1_15 = []
for i in dEk_test2:
    if i > delta_dEk:
        print(i, " > ", delta_dEk, 'условие 1.11 удов')
    else:
        print(i, " < ", delta_dEk, 'условие 1.11 не удов')
        uslovie_1_15.append(i)

if len(uslovie_1_15) != 0:
    print('Условие 1.11 не удов, проверка условия 1.15')
    for i in range(len(uslovie_1_15)-1):
        for j in range(i, len(uslovie_1_15)):
            if uslovie_1_15[i] == uslovie_1_15[j]:
                continue
            if uslovie_1_15[i] < uslovie_1_15[j]:
                if uslovie_1_15[i] < delta_dEk and uslovie_1_15[j] < delta_dEk:
                    print('Условие 1.15 выполнено для ', uslovie_1_15[i], uslovie_1_15[j])
                else: print('Условие 1.15 не выполнено, перерасчёт, вторая часть', uslovie_1_15[i], uslovie_1_15[j])
            else: print('Условие 1.15 не выполнено, перерасчёт, первая часть', uslovie_1_15[i], uslovie_1_15[j])


print("_________________________________________________")


print('Результаты расчёта ступеней роста стоимости ИР')

print(stup_rosta)

dEk_mean = round(scipy.stats.gmean(stup_rosta['dEk']), 3)
print('Средне геом: ',dEk_mean)

print("_________________________________________________")
rang_price = test

def a_(Er1, dE, X):
    return Er1*(dE**X)

def b_(Er2, dE, Y):
    return  Er2 / (dE**Y)

def interpol(rang_price, dE, index, index_left, index_right):
    a = a_(rang_price[index_left], dE, index - index_left)
    b = b_(rang_price[index_right], dE, index_right - index)
    return round(((a + b) / 2), 3)


def extrapol(rang_price, dE, index, index_near):
    if index < index_near:
        return round(b_(rang_price[index_near], dE, index_near-index),3)
    else:
        return round(a_(rang_price[index_near], dE, index - index_near),3)


def find_left(rang_price, index):
    index_left = -1
    for i in range(index):
        if rang_price[i] != 0:
            index_left = i
            break

    return index_left


def find_right(rang_price, index):
    index_right = -1
    for i in range(index, len(rang_price)):
        if rang_price[i] != 0:
            index_right = i
            break

    return index_right


last_rang_price = np.zeros(len(rang_price))

for i in rang_ir['Ранг']:
    if rang_price[i] == 0:
        print('Ранг ', i, 'не рассчитан')
        right = find_right(rang_price, i)
        left = find_left(rang_price, i)
        if left == -1:
            print('Находим данный ранг с помощью экстраполяции с помощью известного самого близкого справа')
            Er = extrapol(rang_price, dEk_mean, i, right)
            print('Ранг ', i, 'рассчитан, ИР с этим рангом имеет стоимость = ', Er)
            last_rang_price[i] = Er
        elif right == -1:
            print('Находим данный ранг с помощью экстраполяции с помощью известного самого близкого слева')
            Er = extrapol(rang_price, dEk_mean, i, left)
            print('Ранг ', i, 'рассчитан, ИР с этим рангом имеет стоимость = ', Er)
            last_rang_price[i] = Er
        else:
            print('Находим данный ранг с помощью интерполяции')
            Er = interpol(rang_price, dEk_mean, i, left, right)
            print('Ранг ', i, 'рассчитан, ИР с этим рангом имеет стоимость = ', Er)
            last_rang_price[i] = Er

    else:
        print('Ранг ', i, 'рассчитан, ИР с этим рангом имеет стоимость = ', rang_price[i])
        last_rang_price[i] = rang_price[i]

print()
print("_________________________________________________")
index = 0
for i in last_rang_price:
    print('Ранг ',index, 'Стоимость ', i)
    index += 1

count = [8, 7, 6, 6, 4, 9, 5, 2]
index = [2, 3, 4, 5, 6, 7, 8, 9]
print()
c = 1
for i in range(len(index)):
    if i == 2:
        print('ИР', index[i]-1, 'Стоимость', round(price_all_ir[i]), 'Ранг ', count[i])
    elif i == 3:
        print('ИР', index[i]-1, 'Стоимость', round(price_all_ir[i]), 'Ранг ', count[i])
    else:
        print('ИР', index[i]-1, 'Стоимость', round(last_rang_price[count[i]], 0), 'Ранг ', count[i])

#  0   9   0    3         8     6           4,5        2          7
#  0   9   0    6         8     4,5           3        2          7
#  1   2   3    4         5     6           7          8          9
# [0, 0.0, 0, 6235400.0, 0.0, 4080187.2, 5970590.0, 10852948.363, 0]
# [0, 0, 0, 4080187.2, 0, 5970590.0, 6235400.0, 10852948.363, 0]

# 1 10324787.0
# 2 6235400.0
# 3 1076800.0
# 4 10864380.0
# 5 4080187.0
# 6 12957845.379
# 7 4939799.556
# 8 2570034.643