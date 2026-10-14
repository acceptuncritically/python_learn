def bubble_sort(lst):
    for i in range(len(lst)-1):
        cnt = 0
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                cnt+=1
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print(f"交换了{cnt}次")
        if cnt==0:
            break
if __name__ == '__main__':
    list1 = [5,3,2,7,6]
    bubble_sort(list1)
    print(list1)