class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        mat=[[0]*n for _ in range(n)]
        count=1
        start_index=0#标记当前循环的初始化位置
        while not count==n**2+1:
            for j in range(start_index,n-1-start_index):
                mat[start_index][j]=count
                count+=1
            for i in range(start_index,n-1-start_index):
                mat[i][n-1-start_index]=count
                count+=1
            for j in range(n-1-start_index,start_index,-1):
                mat[n-1-start_index][j]=count
                count+=1
            for i in range(n-1-start_index,start_index,-1):
                mat[i][start_index]=count
                count+=1
            start_index+=1