from random import sample


a = sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
print(a)


def bubble_sort(arr):
    sort_border = len(arr) - 1
    last_exchange_index = 0
    
    for i in range(sort_border):
    
        is_sorted = True
        
        for j in range(sort_border):
        
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                is_sorted = False
                last_exchange_index = j
                
        # 如果数组已经有序则结束排序
        if is_sorted:
            break
    
        # 更新数组的有序边界
        sort_border = last_exchange_index
    
    
bubble_sort(a)
print(a)
