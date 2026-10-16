def quick_sort(my_list, start, end):
    if start >= end:
        return
    left= start
    right= end
    #定义变量mid 表示分界值，假设列表的起始值为分界值
    mid=my_list[start]
    #具体的查找过程 只要left比right小就一直找
    while left < right:
        #必须先左再右，左边已经有一个坑了 要从右边先找把坑填上
        while my_list[right] >= mid and left < right:
            right-=1
        #走到这里说明my_list[right]比分界值小，放左侧
        my_list[left] = my_list[right]
        while my_list[left] <= mid and left < right:
            left += 1
        my_list[right] = my_list[left]
    my_list[right] = mid
    #分界值的位置已经找到
    #在进行递归
    quick_sort(my_list, start, left-1)
    quick_sort(my_list, right+1, end)

if __name__=="__main__":
    my_list=[1,6,3,5,9]
    quick_sort(my_list,0,len(my_list)-1)
    print(my_list)