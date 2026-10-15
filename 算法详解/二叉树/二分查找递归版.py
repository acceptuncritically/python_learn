# 在列表是有序的前提下
#相对效率高 时间复杂度为o(n)
def binary_search(my_list,number):
    n=len(my_list)
    #判断列表为空
    if n==0:
        return False
    mid=(n-1)//2
    # 比较要查找的元素和中值
    if my_list[mid]<number:
        return binary_search(my_list[mid+1:n+1],number)
    elif my_list[mid]>number:
        return binary_search(my_list[:mid],number)
    else:
        return True
if __name__ == '__main__':
    print(binary_search([1,2,4,5,6],3))
    print(binary_search([1,2,4,5,6],4))