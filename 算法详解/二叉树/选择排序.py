def select_sort(lst):
    n=len(lst)
    for i in range(n-1):
        min_middle=i
        for j in range(i+1,n):
            if lst[min_middle] > lst[j]:
                min_middle=j
        if min_middle!=i:
            lst[i],lst[min_middle]=lst[min_middle],lst[i]
if __name__=='__main__':
    lst=[5,3,2,7,6,9,8,4,5]
    select_sort(lst)
    print(lst)

