#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# В списке, состоящем из вещественных элементов, вычислить:
# 1) номер минимального элемента списка;
# 2) сумму элементов списка, расположенных между первым и вторым отрицательными
# элементами.
# Преобразовать список таким образом, чтобы сначала располагались все элементы, модуль
# которых не превышает 1, а потом - все остальные.

import sys
#   В списке, состоящем из целых элементов, вычислить номер минимального элемента списка;
if __name__ == '__main__':
    A = list(map(int, input('Введите список ').split()))
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    A_min = A[0]
    A_min = A[0]
    for v, ad in enumerate(A):
        if ad <= A_min:
            v_min, A_min = v, ad
    print('Индекс максимального элемента: ', v_min)
    #   Произведение элементов списка, расположенных между первым и вторым нулевыми элементами.
    for v, ad in enumerate(A):
        if ad == 0:
            A.append(v)
    x = A[0] + 1
    y = A[1]
    m = 1
    for ad in A[x:y]:
        m *= ad
    print("Произведение элементов списка, расположенных между первым и вторым нулевыми элементами равно:", m)
# Преобразовать список таким образом, чтобы сначала располагались все элементы, модуль
# которых не превышает 1, а потом - все остальные.
    c = 1
    for v in A:
        c *= v
    print(c)
    A.sort()
    print(f"2)Cначала идут все элементы, мудуль которых не превышает 1 а потом остальные {A} ")

