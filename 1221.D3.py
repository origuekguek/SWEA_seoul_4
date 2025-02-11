# GNS

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    case_num, case_length = input().split()
    lst = list(input().split())
    
    mapping_dct = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    mapping_lst = [mapping_dct[word] for word in lst]
    