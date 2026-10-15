def insert_sort(my_list):
    n=len(my_list)
    for i in range(1,n):
        for j in range(i,0,-1):
            if my_list[j]<my_list[j-1]:
                my_list[j],my_list[j-1]=my_list[j-1],my_list[j]
            else:
                break
    return my_list
# 最坏o(n²) 最优o(n)
my_list=[5,3,4,1]
print(insert_sort(my_list))