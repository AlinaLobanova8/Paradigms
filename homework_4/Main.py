'''
Ваша задача
Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь.
'''

import math
from functools import reduce

# Первый вариант решения
def Pearson_correlation_1(array_1, array_2):
    if len(array_1) != len(array_2) or len(array_1) == 0:
        return None
    
    srednee_x = sum(array_1)/len(array_1)
    srednee_y = sum(array_2)/len(array_2)
    
    sum_chisl = 0
    sum_znam_1 = 0
    sum_znam_2 = 0
    
    for i in range(len(array_1)):
        chisl = (array_1[i] - srednee_x) * (array_2[i] - srednee_y)
        sum_chisl += chisl
        sum_znam_1 += (array_1[i] - srednee_x) ** 2
        sum_znam_2 += (array_2[i] - srednee_y) ** 2
    
    znam = math.sqrt(sum_znam_1 * sum_znam_2)
    if znam == 0:
        return None
    
    return sum_chisl / znam

print(Pearson_correlation_1([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]))