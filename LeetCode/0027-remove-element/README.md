# 27 移除元素

题目链接：[https://leetcode-cn.com/problems/remove-element/](https://leetcode-cn.com/problems/remove-element/)

参考：[代码随想录 (programmercarl.com)](https://programmercarl.com/0027.移除元素.html)

## 暴力破解法

使用嵌套循环，外层循环遍历数组，内层循环进行元素交换。

注意：如果使用Python，外层循环不可使用 For 循环。


## 双指针法

设置两个指针：快指针和慢指针，
当快指针处的值等于目标值时，递增快指针，
当快指针处的值不等于目标值时，将当前位置的值复制到慢指针处，并同时递增快指针和慢指针，直到快指针到达数组尾部，
慢指针的值为数组最终的长度。