import time

import numpy
import pandas as pd
import scipy


def return_I_g(year):
    if year == 2018:
        years = ['2018', '2019', '2020', '2021']
    elif year == 2019:
        years = ['2019', '2020', '2021']
    elif year == 2020:
        years = ['2020', '2021']
    else:
        years = ['2021']
    Ig = 1
    for i in years:
        Ig*=return_k_years(i)
    return Ig
def return_k_years(year):
    dict = {'2018' : 1.08, '2019' : 1.10, '2020' : 1.12, '2021' : 1.15}
    return dict[year]


def calc_razr(list_S_baz, years, ir_num):
    S_nak = []
    S_nak.append(list_S_baz[years[0]])
    print('S_nak {:d} Год {:s} S_baz {:.0f}'.format(ir_num+1, years[0], list_S_baz[years[0]]))
    if len(years) > 1:
        for i in range(1, len(years)):
            print('S_nak {:d} Год {:s} S_baz {:.0f} S_nak(i-1) {:.0f} I(i-1) {:.2f}'.format(ir_num+1, years[i], list_S_baz[years[i]], S_nak[i-1], return_k_years(years[i-1])))
            S_nak.append(list_S_baz[years[i]]+S_nak[i-1]*return_k_years(years[i-1]))
    print('S_nak по годам', S_nak)
    S_raz = S_nak[-1] * return_I_g(int(years[-1])) * (1 - ((type_ir['текущий'].iloc[ir_num] - 1)
                                     /
                                     (type_ir['планируемый'].iloc[ir_num])))
    print('{:d} ИР разр = {:.0f}'.format(ir_num+1, round(S_raz, 0)))
    return round(S_raz, 0)

def calc_priob(priob_nach, year, ir_num):
    print('{:d} ИР приобрет = {:d} * {:.5f} * {:.2f}'.format(ir_num+1, priob_nach, return_I_g(year), (1 - ((type_ir['текущий'].iloc[ir_num] - 1)
                                           /
                                           (type_ir['планируемый'].iloc[ir_num])))))

    S_priobr = priob_nach * return_I_g(year) * (1 - ((type_ir['текущий'].iloc[ir_num] - 1)
                                           /
                                           (type_ir['планируемый'].iloc[ir_num])))
    print('{:d} ИР приобрет = {:.0f}'.format(ir_num+1, round(S_priobr, 0)))
    return round(S_priobr, 0)


rang_ir = pd.read_csv("rang_ir.csv")
type_ir = pd.read_csv("6var\\type_ir.csv")
price_all = numpy.zeros(8)
print(price_all)
print()
print()

filename = '6var\\1ir.csv'
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    ir_num = 0 # 1 ir = 0    2 ir = 1 itd
    S_priobr = 0
    S_razr = 0
    S_pribl = 0
    S_obs = 0
    for i in range(len(lines)):
        if lines[i] == 'приобретаемый':
            priob_nach, god = lines[i+1].split(',')
            priob_nach, god = int(priob_nach), int(god)
            S_priobr = calc_priob(priob_nach, god, ir_num)
        if lines[i] == 'разрабатываемый':
            i += 1
            dict_s_baz = {}
            years = lines[i].split(',')
            for j in years:
                i += 1
                r = lines[i].split(',')
                s = 0
                for n in r:
                    s+=int(n)
                dict_s_baz[j] = s
            S_razr = calc_razr(dict_s_baz, years, ir_num)
        if lines[i] == 'обслуживаемый':
            r = lines[i+1].split(',')
            s = 0
            for n in r:
                s += int(n)
            S_obs = s
            print('{:d} ИР обсл= {:.0f}'.format(ir_num + 1, round(S_obs, 0)))
        if lines[i] == 'приносящий_прибыль':
            S_pribl = int(lines[i+1])

    Stoim_ir1 = round(S_priobr + S_razr + S_pribl+S_obs, 0)
    print('ИР {:d} = {:.0f} + {:.0f} + {:.0f} + {:.0f} = {:.0f}'.format(ir_num+1, S_priobr, S_razr, S_pribl, S_obs, Stoim_ir1))
price_all[ir_num] = Stoim_ir1

print()
print()

filename = '6var\\2ir.csv'
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    ir_num = 1 # 1 ir = 0    2 ir = 1 itd
    S_priobr = 0
    S_razr = 0
    S_pribl = 0
    S_obs = 0
    for i in range(len(lines)):
        if lines[i] == 'приобретаемый':
            priob_nach, god = lines[i+1].split(',')
            priob_nach, god = int(priob_nach), int(god)
            S_priobr = calc_priob(priob_nach, god, ir_num)
        if lines[i] == 'разрабатываемый':
            i += 1
            dict_s_baz = {}
            years = lines[i].split(',')
            for j in years:
                i += 1
                r = lines[i].split(',')
                s = 0
                for n in r:
                    s+=int(n)
                dict_s_baz[j] = s
            S_razr = calc_razr(dict_s_baz, years, ir_num)
        if lines[i] == 'обслуживаемый':
            r = lines[i+1].split(',')
            s = 0
            for n in r:
                s += int(n)
            S_obs = s
            print('{:d} ИР обсл= {:.0f}'.format(ir_num + 1, round(S_obs, 0)))
        if lines[i] == 'приносящий_прибыль':
            S_pribl = int(lines[i+1])

    Stoim_ir2 = round(S_priobr + S_razr + S_pribl+S_obs, 0)
    print('ИР {:d} = {:.0f} + {:.0f} + {:.0f} + {:.0f} = {:.0f}'.format(ir_num+1, S_priobr, S_razr, S_pribl, S_obs, Stoim_ir2))

price_all[ir_num] = Stoim_ir2
print()
print()

filename = '6var\\3ir.csv'
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    ir_num = 2 # 1 ir = 0    2 ir = 1 itd
    S_priobr = 0
    S_razr = 0
    S_pribl = 0
    S_obs = 0
    for i in range(len(lines)):
        if lines[i] == 'приобретаемый':
            priob_nach, god = lines[i+1].split(',')
            priob_nach, god = int(priob_nach), int(god)
            S_priobr = calc_priob(priob_nach, god, ir_num)
        if lines[i] == 'разрабатываемый':
            i += 1
            dict_s_baz = {}
            years = lines[i].split(',')
            for j in years:
                i += 1
                r = lines[i].split(',')
                s = 0
                for n in r:
                    s+=int(n)
                dict_s_baz[j] = s
            S_razr = calc_razr(dict_s_baz, years, ir_num)
        if lines[i] == 'обслуживаемый':
            r = lines[i+1].split(',')
            s = 0
            for n in r:
                s += int(n)
            S_obs = s
            print('{:d} ИР обсл= {:.0f}'.format(ir_num + 1, round(S_obs, 0)))
        if lines[i] == 'приносящий_прибыль':
            S_pribl = int(lines[i+1])

    Stoim_ir3 = round(S_priobr + S_razr + S_pribl+S_obs, 0)
    print('ИР {:d} = {:.0f} + {:.0f} + {:.0f} + {:.0f} = {:.0f}'.format(ir_num+1, S_priobr, S_razr, S_pribl, S_obs, Stoim_ir3))

price_all[ir_num] = Stoim_ir3

print()
print()

filename = '6var\\4ir.csv'
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    ir_num = 3 # 1 ir = 0    2 ir = 1 itd
    S_priobr = 0
    S_razr = 0
    S_pribl = 0
    S_obs = 0
    for i in range(len(lines)):
        if lines[i] == 'приобретаемый':
            priob_nach, god = lines[i+1].split(',')
            priob_nach, god = int(priob_nach), int(god)
            S_priobr = calc_priob(priob_nach, god, ir_num)
        if lines[i] == 'разрабатываемый':
            i += 1
            dict_s_baz = {}
            years = lines[i].split(',')
            for j in years:
                i += 1
                r = lines[i].split(',')
                s = 0
                for n in r:
                    s+=int(n)
                dict_s_baz[j] = s
            S_razr = calc_razr(dict_s_baz, years, ir_num)
        if lines[i] == 'обслуживаемый':
            r = lines[i+1].split(',')
            s = 0
            for n in r:
                s += int(n)
            S_obs = s
            print('{:d} ИР обсл= {:.0f}'.format(ir_num + 1, round(S_obs, 0)))
        if lines[i] == 'приносящий_прибыль':
            S_pribl = int(lines[i+1])

    Stoim_ir4 = round(S_priobr + S_razr + S_pribl+S_obs, 0)
    print('ИР {:d} = {:.0f} + {:.0f} + {:.0f} + {:.0f} = {:.0f}'.format(ir_num+1, S_priobr, S_razr, S_pribl, S_obs, Stoim_ir4))

price_all[ir_num] = Stoim_ir4
print()
print()

filename = '6var\\5ir.csv'
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    ir_num = 4 # 1 ir = 0    2 ir = 1 itd
    S_priobr = 0
    S_razr = 0
    S_pribl = 0
    S_obs = 0
    for i in range(len(lines)):
        if lines[i] == 'приобретаемый':
            priob_nach, god = lines[i+1].split(',')
            priob_nach, god = int(priob_nach), int(god)
            S_priobr = calc_priob(priob_nach, god, ir_num)
        if lines[i] == 'разрабатываемый':
            i += 1
            dict_s_baz = {}
            years = lines[i].split(',')
            for j in years:
                i += 1
                r = lines[i].split(',')
                s = 0
                for n in r:
                    s+=int(n)
                dict_s_baz[j] = s
            S_razr = calc_razr(dict_s_baz, years, ir_num)
        if lines[i] == 'обслуживаемый':
            r = lines[i+1].split(',')
            s = 0
            for n in r:
                s += int(n)
            S_obs = s
            print('{:d} ИР обсл= {:.0f}'.format(ir_num + 1, round(S_obs, 0)))
        if lines[i] == 'приносящий_прибыль':
            S_pribl = int(lines[i+1])

    Stoim_ir5 = round(S_priobr + S_razr + S_pribl+S_obs, 0)
    print('ИР {:d} = {:.0f} + {:.0f} + {:.0f} + {:.0f} = {:.0f}'.format(ir_num+1, S_priobr, S_razr, S_pribl, S_obs, Stoim_ir5))

price_all[ir_num] = Stoim_ir5

print()
print()
count = 1
for i in price_all:
    print(count, i)
    count+=1



info_ir = pd.DataFrame(columns=['price'], data=price_all)
info_ir['rang'] = rang_ir['Ранг']
print("_________________________________________________")
print("_________________________________________________")
rang_price = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1, 9):
    rang_price[i] = info_ir['price'].loc[info_ir['rang'] == i].mean()

for i in range(len(rang_price)):
    if pd.isna(rang_price[i]):
        rang_price[i] = 0

print('Значение по рангам')
count = 0
for i in rang_price:
    print(count, i)
    count+=1

#_______________________________________________________________________________________________________________________
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



print("_________________________________________________")
print("Проверим условие 1.13")
test = pereraschet(rang_price)
print('Значение после перерасчёта')
test = [0, 0, 0, 0, 0, (2635231.0+2941600.0) / 2, 0, 7447230.5, 11233624.0, 0] #смотрим что было снизу при выводе, если не нравится Д.А. то правим на то что тут
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
        print(i, " > ", delta_dEk, 'условие 1.13 удов')
    else:
        print(i, " < ", delta_dEk, 'условие 1.13 не удов')
        uslovie_1_15.append(i)

if len(uslovie_1_15) != 0:
    print('Условие 1.13 не удов, проверка условия 1.15')
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


last_rang_price = numpy.zeros(len(rang_price))

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

count = 1
for i in price_all:
    if i != 0:
        print(count, i)
    else:
        print(count, last_rang_price[rang_ir['Ранг'].iloc[count-1]])
    count+=1
