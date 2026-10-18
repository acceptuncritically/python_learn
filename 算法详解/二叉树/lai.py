def quick_sort(my_list, start, end):
    if start>=end:
        return
    left = start
    right = end
    st=my_list[start]
    while left<right:
        while my_list[right]>st and left<right:
            right-=1
        my_list[left]=my_list[right]
        while my_list[left]<st and left<right:
            left+=1
        my_list[right]=my_list[left]

    my_list[right]=st
    quick_sort(my_list,start,left-1)
    quick_sort(my_list,right+1,end)
if __name__=="__main__":
    my_list=[1,6,3,5,9]
    quick_sort(my_list,0,len(my_list)-1)
    print(my_list)