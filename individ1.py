##!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти произведение положительных элементов кратных 3,
# их количество и вывести результаты на экран.



import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    s = 1
    for ad in A:
        if ad%3==0:
          if ad > 0:
            s *= ad
    print(s)
