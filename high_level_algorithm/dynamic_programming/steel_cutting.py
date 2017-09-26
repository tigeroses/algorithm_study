#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cut_rod(p, n):
    if n == 0:
        return 0
    q = -1
    for i in xrange(n):
        q = max(q, p[i]+cut_rod(p,n-i-1))
    return q

def memo_cut_rod(p,n):
    r = []
    for i in xrange(n):
        r.append(-1)
    def memo_cut_rod_aux(p,n,r):
        if r[n-1] >= 0:
            return r[n-1]
        if n == 0:
            q = 0
        else:
            q = -1
            for i in xrange(n):
                q = max(q, p[i]+memo_cut_rod_aux(p,n-i-1,r))
        r[n-1] = q
        return q
    return memo_cut_rod_aux(p,n,r)

def extended_botton_up_cut_rod(p, n):
    r = [0] * (n+1)
    s = [0] * (n+1)
    result = []
    for j in xrange(1, n+1):
        q = -1
        for i in xrange(1, j+1):
            if q < p[i-1]+r[j-i]:
                q = p[i-1]+r[j-i]
                s[j] = i
        r[j] = q

    tmp_n = n
    while tmp_n > 0:
        result.append(s[tmp_n])
        tmp_n = tmp_n-s[tmp_n]
    return r[n], result

def botton_up_cut_rod(p, n):
    r = [0] * n
    for j in xrange(n):
        q = -1
        for i in xrange(j+1):
            q = max(q, p[i]+r[j-i-1])
        r[j] = q
    return r[n-1]

if __name__ == '__main__':
    p = [1,5,8,9,10,17,17]
    n = 7
    print cut_rod(p, n)
    print memo_cut_rod(p, n)
    print botton_up_cut_rod(p, n)
    print extended_botton_up_cut_rod(p, n)
