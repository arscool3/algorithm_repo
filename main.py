# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
from collections import deque

def analyse(programms):
    k = 0
    t = 0
    pos = {}
    ans = 0
    li = []
    for programm in programms:
        if programm[0] == 'выгрузить':
            t += 1
            pos[programm[1]] = t

    for programm in programms :
        if programm[0] == 'выгрузить':
            ans += (len(li) - li.index(programm[1]) - 1) * 2 + 1
            li.remove(programm[1])
            k += 1
            t -= 1
        else:
            if programm[1] not in pos.keys():
                li.insert(0, programm[1])
                ans += 1
            elif pos[programm[1]] -k  <= math.ceil(t / 2):
                li.append(programm[1])
                ans += 1
            else:
                li.insert(0, programm[1])
                ans += 1
    return ans


def calculate(m, n, p) :
    mx = 0
    pr = []
    for i in range(n) :
        if i == 0 :
            pr.append(p[i])
            continue
        pr.append(pr[-1] + p[i])
    for i in range(n):
        mult = math.floor(m / (i + 2))
        ost = m - mult * (i + 2)
        if ost <= 0 :
            mx = max(pr[i] * mult, mx)
            continue
        mx = max(pr[i] * mult + pr[ost - 1], mx)
    return mx