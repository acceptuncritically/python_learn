nums=[]
cnt=0
    for i in range(0,len(nums)+1):
        if i in nums:
            cnt+=1
            for j in range(i,len(nums)+1):
                if j in nums:
                    cnt+=1
                else:
                    break
    break