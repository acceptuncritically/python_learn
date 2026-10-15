def inseret_sort(my_list):
    n=len(my_list)
    for i in range(1,n):
        for j in range(i,0,-1):
            if my_list[j]<my_list[j-1]:
                my_list[j],my_list[j-1]=my_list[j-1],my_list[j]
            else:
                break
    return my_list
my_list=[5,3,4,1]
print(inseret_sort(my_list))