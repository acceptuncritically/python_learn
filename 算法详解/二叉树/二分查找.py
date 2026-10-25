def binary_search(my_list,number):
    start=0
    end=len(my_list)-1
    while start<=end:
        mid=(start+end)//2
        if my_list[mid]<number:
            start=mid+1
        elif my_list[mid]>number:
            end=mid-1
        else:
            return mid
    return False
if __name__=='__main__':
    my_list=[1,2,4,5,6]
    print(binary_search(my_list,3))
    print(binary_search(my_list,5))