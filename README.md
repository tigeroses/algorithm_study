algorithm study
---------------

学习基础算法

sorting
-------

学习常用排序算法，python实现；使用matplotlib的animation模块将排序的过程使用动态柱状图展示出来，加深理解

## bubble sort

冒泡排序：最简单的排序。两层for循环，交换元素，实现简单。

时间复杂度O(n^2)

空间复杂度O(1)

## insertion sort

插入排序：假设前i个元素已经排序，第i－1个元素与前i个元素逆序比较，找到一个小于i－1元素的元素，插入它后面。

时间复杂度O(n^2)

空间复杂度O(1)

## quick sort

快速排序：其核心是二分法，即对于一个无序序列，随机挑选一个数作为轴，将序列分成两个，左边的都小于它，右边的都大于它，然后对两个序列递归的进行排序，直到每个序列只有一个元素，则排序完成。

时间复杂度O(nlog(n))

空间复杂度O(1)

## shell sort

希尔排序：分组插入排序，即先将序列按照增量分成若干子序列，对子序列进行直接插入排序，然后减少增量再排序。

时间复杂度O(依赖于gap序列的选取) 最好O(nlog(n))  最差O(n^2)

空间复杂度O(1)


data structure
--------------

常见的数据结构

## list

仿照python的list实现了一个简单的单链表，实现的功能有:

- insert 插入元素,可选择位置
- append 在末尾追加元素
- count 统计某元素出现的次数
- extend 追加入一个列表
- index 查找某元素第一次出现的索引位置
- pop 删除某元素，根据位置查找，默认从列表末位删除
- remove 删除元素，根据值查找
- reverse 反转链表

主要说一下反转一个单链表：
head -> current -> pnext -> prev

反转分三步： 

- current -> prev
- pnext -> current
- head -> pnext

这三步完成之后，链表就变为：
head -> pnext -> current -> prev
也就是反转了current 和 pnext, 然后一直循环就可以。
