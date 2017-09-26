
动态规划之钢条切割问题
----------------------

问题描述：有一根钢条，切割出售，不同长度价格也不相同，其长度和价格对应关系如下，求如何切割使得收益最大。

长度i   1   2   3   4   5   6   7   

价格pi  1   5   8   9   10  17  17

## 分析

问题分析：

假如长度为1，则无法切割，收益就是p1=1
假如长度为2，有两种方法，不切割则收益是p2=5;或者分成两个长度1则p2=p1+p1=1+1=2
假如长度为3，则三种方法，不切割p3=8;切成p2+p1;或者p1+p1+p1

可以看到，随着长度的增加，切割方法会成倍的增加;有一个规律就是长度i是与长度i－1的方法有关系的，比如长度为3的切割方法可以转化为长度为2的方法加上长度为1

## 递归方法

此问题的递归求解方法为：将钢条从左边切下长度为i的一段，只对右边长度为n－i的一段进行继续切割。

自顶向下递归实现的伪代码：

```
CUT-ROD(p,n)
if n == 0
    return 0
q=-∞
for i=1 to n
    q=max(q, p[i]+CUT-ROD(p,n-i))
return q,
```

过程CUT-ROD以价格数组p[1..n]和整数n作为输入，返回长度为n的钢条的最大收益。

递归的方法可以很简洁的实现要求，但是当n太大时，求解时间也大大增加；此算法的时间复杂度时O(2^n),指数函数

## 动态规划方法

递归求解慢是因为重复求解相同的子问题；动态规划方法是仔细安排求解顺序，对每个子问题只求解一遍，并将结果保存，这样下次再遇到相同子问题，不用重复求解，只要查找保存的结果即可。

因此动态规划是付出额外的内存空间来节省计算时间，是典型的时空权衡的例子;时间上，将指数级的解转化为多项式时间的解。

带备忘的自顶向下法：
```
MEMORIZED-CUT-ROD(p,n)
let r[0..n] be a new array
for i=0 to n
    r[i]=-∞
return MEMORIZED-CUT-ROD-AUX(p,n,r)

MEMORIZED-CUT-ROD-AUX(p,n,r)
if r[n]>=0
    return r[n]
if n==0
    q=0
else
    q=-∞
    for i=1 to n:
        q=max(q,p[i]+MEMORIZED-CUT-ROD-AUX(p,n-i,r))
r[n] = q
return q
```

自底向上法：
```
BOTTOM-UP-CUT-ROD(p,n)
let r[0..n] be a new array
r[0]=0
for j=1 to n
    q=-∞
    for i=1 to j
        q=max(q,p[i]+r[j-i])
    r[j]=q
return r[n]
```

## 重解构

上面的动态规划只给出了最高的收益，并没有给出切割方案；拓展动态规划算法，给出切割方案。

```
EXTENDED-BOTTOM-UP-CUT-ROD(p,n)
let r[0..n] and s[0..n] be new arrays
r[0]=0
for j=1 to n
    q=-∞
    for i=1 to j
        if q<p[i]+r[j-i]
            q=p[i]+r[j-i]
            s[j]=i
    r[j]=q
return r and s

```

s[i]保存的是长度j的第一段钢条的最优切割长度。

