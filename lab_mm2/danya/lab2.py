import numpy
import pandas as pd
import scipy

index = ['z1', 'z2', 'z3', 'z4']
down = [9, 11, 25, -11]
up = [24, 28, 39, 0]

df1 = pd.DataFrame({'down' : down, 'up' : up}, index=index)
print(df1)
print()
df2 = pd.read_csv('lab2.csv', index_col='index')
print(df2)


df2_2 = pd.read_csv('lab2.csv', index_col='index')


for i in range(4):
    index = df1.index[i]
    z0a = (df1.iloc[i]['up'] + df1.iloc[i]['down']) / 2
    lymbda0a = (df1.iloc[i]['up'] - df1.iloc[i]['down']) / 2
    df2_2[index] = df2_2[index].replace(to_replace='Н', value=(df1.iloc[i]['down'] - z0a) / lymbda0a)
    df2_2[index] = df2_2[index].replace(to_replace='В', value=(df1.iloc[i]['up'] - z0a) / lymbda0a)
    df2_2.rename(columns={index : str(index).replace('z', 'x')}, inplace=True)

print(df2_2)


print('Рассчитать коэффициенты уравнения регрессии вида (2.5). В уравнении участвуют четыре типа коэффициентов:')
y_ = []

for i, row in df2.iterrows():
    y_.append((row['y1']+row['y2']+row['y3']) / 3)

b0 = sum(y_) * 1/len(y_)
print('b0= ', b0)

b_a = []
for a in range(4):
    xia_y_ = []
    for i, row in df2_2.iterrows():
        xia_y_.append(row['x'+str(a+1)]*(row['y1']+row['y2']+row['y3']) / 3)
    b_a.append(1/len(xia_y_) * sum(xia_y_))
print('b_a= ', b_a)

b_ab = []
for a in range(4):
    for b in range(4):
        xiab_y_ = []
        if a >= b:
            continue
        for i, row in df2_2.iterrows():
            xiab_y_.append(row['x'+str(a+1)]*row['x'+str(b+1)]*(row['y1']+row['y2']+row['y3']) / 3)
        b_ab.append(1/len(xiab_y_) * sum(xiab_y_))
print('b_ab= ', b_ab)

b_aby = []
for a in range(4):
    for b in range(4):
        for yi in range(4):
            xiab_y_ = []
            if a >= b or b>=yi:
                continue
            for i, row in df2_2.iterrows():
                xiab_y_.append(row['x'+str(a+1)]*row['x'+str(b+1)]*row['x'+str(yi+1)]*(row['y1']+row['y2']+row['y3']) / 3)
            b_aby.append(1/len(xiab_y_) * sum(xiab_y_))
print('b_aby= ', b_aby)

b_abyz = []
for a in range(4):
    for b in range(4):
        for yi in range(4):
            for z in range(4):
                xiab_y_ = []
                if a >= b or b>=yi or yi>=z:
                    continue
                for i, row in df2_2.iterrows():
                    xiab_y_.append(row['x'+str(a+1)]*row['x'+str(b+1)]*row['x'+str(yi+1)]*row['x'+str(z+1)]*(row['y1']+row['y2']+row['y3']) / 3)
                b_abyz.append(1/len(xiab_y_) * sum(xiab_y_))
print('b_abyz= ', b_abyz)


all_b = []
all_b.append(b0)
for i in b_a:
    all_b.append(i)
for i in b_ab:
    all_b.append(i)
for i in b_aby:
    all_b.append(i)
for i in b_abyz:
    all_b.append(i)

def check_t_test(b, df_y, df_tt, a = '0.95'):
    n = len(df_y.index)
    m = 3 # количество Y
    sum_ = 0
    for i, row in df_y.iterrows():
        y_ = row[['y1', 'y2', 'y3']].mean()
        sum_ += (row['y1'] - y_)**2
        sum_ += (row['y2'] - y_) ** 2
        sum_ += (row['y3'] - y_) ** 2
    D = (1 / (n*(m-1))) * sum_
    S = (D / n*m)**(1/2)
    step_svob = n*(m-1)
    if step_svob in df_tt.index:
        t_kr = df_tt.iloc[step_svob][a]
    else:
        for i in df_tt.index:
            if step_svob < i:
                t_kr = df_tt.iloc[i][a]
    if numpy.abs(b) > (t_kr * S):
        return 'Значимый!'
    else:
        return 'Не значимый!'


df_tt = pd.read_csv('tt.csv', delimiter=';')
znach = {}
count_1 = 0
for b in all_b:
    znach[b] = check_t_test(b, df2, df_tt, '0.95')
    if znach[b] == 'Значимый!':
        count_1+=1
    print(b,' -> ',znach[b])

print('Всего = ', len(znach), ' значимые = ', count_1)

count = 0
for i in all_b:
    if znach[i] == 'Не значимый!':
        all_b[all_b.index(i)] = 0
        # if count == 1:
        #     break
        # count += 1

print(all_b)

b_0 = all_b[0]

b_1 = all_b[1:5]

b_2 = all_b[5:11]

b_3 = all_b[11:15]

b_4 = all_b[15]

print(b_0, b_1, b_2, b_3, b_4)

dfft = pd.read_csv('ft.csv', delimiter=';', index_col='k1 / k2')
print(df2_2)


def krit_fishera(df_y, df_tt, dfft, a, all_b, dfx):
    n = len(df_y.index)
    m = 3  # количество Y
    sum_ = 0
    for i, row in df_y.iterrows():
        y_ = row[['y1', 'y2', 'y3']].mean()
        sum_ += (row['y1'] - y_) ** 2
        sum_ += (row['y2'] - y_) ** 2
        sum_ += (row['y3'] - y_) ** 2
    D = (1 / (n * (m - 1))) * sum_
    S = (D / n * m) ** (1 / 2)

    r = 0
    for i in all_b:
        if i != 0:
            r+=1

    sum_ = 0
    for i, row in dfx.iterrows():
        print('_________', i, '_____________')
        y_ = row[['y1', 'y2', 'y3']].mean()
        # b0
        count = 0
        y_shtr = all_b[count]
        count += 1


        #b1
        sum_1 = 0
        for a in range(4):

            sum_1 += all_b[count] * row['x' + str(a + 1)]
            count+=1

        # b2
        sum_2 = 0
        for a in range(4):
            for b in range(4):
                if a >= b:
                    continue

                sum_2 += all_b[count] * row['x' + str(a + 1)] * row['x' + str(b + 1)]
                count += 1


        # b3
        sum_3 = 0
        for a in range(4):
            for b in range(4):
                for y in range(4):
                    if (a >= b) or (b >= y):
                        continue
                    sum_3 += all_b[count] * row['x' + str(a + 1)] * row['x' + str(b + 1)] * row['x' + str(y + 1)]
                    count += 1

        # b4
        sum_4 = 0
        for a in range(4):
            for b in range(4):
                for y in range(4):
                    for z in range(4):
                        if a >= b or b >= y or y >= z:
                            continue
                        sum_4 += all_b[count] * row['x' + str(a + 1)] * row['x' + str(b + 1)] * row['x' + str(y + 1)] * row['x' + str(z + 1)]
                        count += 1

        print('Все компоненты y\'', sum_1, sum_2, sum_3, sum_4)
        y_shtr = sum_1+sum_2+sum_3+sum_4
        print('y\'', y_shtr)
        print('y_', y_)
        sum_+= (y_shtr - y_)**2
    print('______________________')
    S_ost = (m / (n - r)) * sum_

    F_rasch = S_ost / S
    print('F_расч',F_rasch)

    k1 = n - r
    k2 = n*(m-1)
    print(k1, k2)
    for i in dfft.index:
        if i == 'k1 \ k2':
            continue
        if k2 > i:
            k2 = i
    print('F_табл', dfft.iloc[k2][str(k1)])
    return (F_rasch < float(dfft.iloc[k2][str(k1)]))


print('Адекватно!' if (krit_fishera(df2, df_tt, dfft, '0.05', all_b, df2_2)) else 'Не адекватно!')