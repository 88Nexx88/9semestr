# data_1_3 = '''
# 1 7,4 2,7 0,1 63,8 -7,4 267,8
# 2 10,1 20,6 1,0 1,6 -7,2 235,2
# 3 12,8 35,0 1,9 -1,7 -7,0 220,9
# 4 15,5 57,8 2,8 -2,8 -6,8 207,7
# 5 18,2 69,8 3,7 -3,4 -6,6 201,6
# 6 20,9 88,6 4,6 -3,8 -6,4 178,1
# 7 23,6 112,2 5,5 -4,0 -6,2 161,2
# 8 26,3 123,7 6,4 -4,2 -6,0 163,1
# 9 29,0 132,3 7,3 -4,4 -5,8 139,6
# 10 31,7 147,4 8,2 -4,5 -5,6 128,2
# 11 34,4 188,2 9,1 -4,5 -5,4 118,1
# 12 37,1 186,5 10,0 -4,6 -5,2 123,5
# 13 39,8 198,5 10,9 -4,7 -5,0 108,7
# 14 42,5 238,5 11,8 -4,7 -4,8 100,2
# 15 45,2 235,8 12,7 -4,7 -4,6 87,7
# 16 47,9 264,3 13,6 -4,8 -4,4 82,3
# 17 50,6 293,7 14,5 -4,8 -4,2 71,0
# 18 53,3 285,4 15,4 -4,9 -4,0 60,6
# 19 56,0 306,8 16,3 -4,9 -3,8 55,2
# 20 58,7 347,5 17,2 -4,9 -3,6 47,8
# 21 61,4 329,4 18,1 -4,9 -3,4 37,4
# 22 64,1 341,7 19,0 -4,9 -3,2 31,5
# 23 66,8 386,2 19,9 -5,0 -3,0 29,5
# 24 69,5 387,2 20,8 -5,0 -2,8 20,8
# 25 72,2 440,2 21,7 -5,0 -2,6 16,7
# 26 74,9 444,1 22,6 -5,0 -2,4 13,4
# 27 77,6 434,6 23,5 -5,0 -2,2 9,6
# 28 80,3 497,7 24,4 -5,0 -2,0 6,6
# 29 83,0 498,0 25,3 -5,0 -1,8 3,0
# 30 85,7 519,2 26,2 -5,0 -1,6 0,6
# '''

data_3var_1_3 = '''
1 6,7 -31,7 -7,2 319,1 0,2 15,1
2 10,3 -13,3 -6,6 291,8 1,2 9,3
3 13,9 5,8 -6,0 239,1 2,2 8,7
4 17,5 24,4 -5,4 190,3 3,2 8,5
5 21,1 40,5 -4,8 162,8 4,2 8,5
6 24,7 63,6 -4,2 130,7 5,2 8,4
7 28,3 80,8 -3,6 98,1 6,2 8,3
8 31,9 104,8 -3,0 64,0 7,2 8,3
9 35,5 112,9 -2,4 45,4 8,2 8,3
10 39,1 131,6 -1,8 26,9 9,2 8,2
11 42,7 156,1 -1,2 10,6 10,2 8,2
12 46,3 167,2 -0,6 0,3 11,2 8,2
13 49,9 195,8 0,0 -6,4 12,2 8,2
14 53,5 200,2 0,6 -9,4 13,2 8,2
15 57,1 231,9 1,2 -8,5 14,2 8,2
16 60,7 257,7 1,8 -3,7 15,2 8,2
17 64,3 253,8 2,4 4,9 16,2 8,2
18 67,9 278,1 3,0 16,3 17,2 8,2
19 71,5 291,7 3,6 35,3 18,2 8,2
20 75,1 330,3 4,2 53,6 19,2 8,2
21 78,7 324,3 4,8 74,9 20,2 8,2
22 82,3 362,6 5,4 105,3 21,2 8,2
23 85,9 353,3 6,0 141,0 22,2 8,2
24 89,5 409,0 6,6 169,8 23,2 8,2
25 93,1 406,0 7,2 197,2 24,2 8,2
26 96,7 418,1 7,8 261,8 25,2 8,1
27 100,3 424,7 8,4 303,4 26,2 8,1
28 103,9 509,9 9,0 329,9 27,2 8,1
29 107,5 470,9 9,6 409,9 28,2 8,1
30 111,1 539,4 10,2 458,8 29,2 8,2
'''

list_1_3 = data_3var_1_3.replace('\n', ' ').replace(',','.').split(' ')[1:-1]
x1 = list_1_3[1::7].copy()
y1 = list_1_3[2::7].copy()
x2 = list_1_3[3::7].copy()
y2 = list_1_3[4::7].copy()
x3 = list_1_3[5::7].copy()
y3 = list_1_3[6::7].copy()

# data_4 = '''
# 1 1,4 1,0 18 79,6 17,5 35 157,8 20,7
# 2 6,0 7,0 19 84,2 17,4 36 162,4 20,4
# 3 10,6 9,1 20 88,8 17,6 37 167,0 21,0
# 4 15,2 10,7 21 93,4 18,2 38 171,6 20,9
# 5 19,8 11,9 22 98,0 18,2 39 176,2 20,6
# 6 24,4 12,7 23 102,6 18,2 40 180,8 20,7
# 7 29,0 13,5 24 107,2 18,9 41 185,4 21,0
# 8 33,6 14,1 25 111,8 18,9 42 190,0 21,5
# 9 38,2 14,7 26 116,4 18,7 43 194,6 20,8
# 10 42,8 15,0 27 121,0 19,4 44 199,2 21,1
# 11 47,4 15,6 28 125,6 19,2 45 203,8 21,0
# 12 52,0 15,5 29 130,2 19,3 46 208,4 21,3
# 13 56,6 16,0 30 134,8 19,9 47 213,0 21,6
# 14 61,2 16,1 31 139,4 19,8 48 217,6 22,1
# 15 65,8 16,4 32 144,0 20,4 49 222,2 21,3
# 16 70,4 17,2 33 148,6 19,7 50 226,8 21,6
# 17 75,0 17,1 34 153,2 20,2
# '''
data_3var_4 = '''
1 0,6 4,6 18 39,7 0,2 35 78,8 -0,5
2 2,9 3,0 19 42,0 0,2 36 81,1 -0,5
3 5,2 2,4 20 44,3 0,1 37 83,4 -0,6
4 7,5 2,0 21 46,6 0,0 38 85,7 -0,6
5 9,8 1,7 22 48,9 0,0 39 88,0 -0,6
6 12,1 1,5 23 51,2 -0,1 40 90,3 -0,7
7 14,4 1,3 24 53,5 -0,1 41 92,6 -0,7
8 16,7 1,1 25 55,8 -0,2 42 94,9 -0,7
9 19,0 1,0 26 58,1 -0,2 43 97,2 -0,7
10 21,3 0,9 27 60,4 -0,2 44 99,5 -0,7
11 23,6 0,8 28 62,7 -0,3 45 101,8 -0,8
12 25,9 0,7 29 65,0 -0,3 46 104,1 -0,8
13 28,2 0,6 30 67,3 -0,4 47 106,4 -0,8
14 30,5 0,5 31 69,6 -0,4 48 108,7 -0,9
15 32,8 0,4 32 71,9 -0,4 49 111,0 -0,9
16 35,1 0,3 33 74,2 -0,4 50 113,3 -0,9
17 37,4 0,3 34 76,5 -0,5
'''


list_4 = data_3var_4.replace('\n', ' ').replace(',','.').split(' ')[1:-1]
x4 = list_4[1::9].copy() + list_4[4::9].copy() + list_4[7::9].copy()
y4 = list_4[2::9].copy() + list_4[5::9].copy() + list_4[8::9].copy()