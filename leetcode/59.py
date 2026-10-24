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
        return mat
    def generateMatrix2(self, n: int) -> list[list[int]]:
        mat = [[0] * n for _ in range(n)]
        count = 1
        top, bottom = 0, n-1
        left, right = 0, n-1
        while top<=bottom and left<=right:
            for j in range(left,right):
                mat[top][j]=count
                count+=1
            for i in range(top,bottom):
                mat[i][right]=count
                count+=1
            for j in range(right,left,-1):
                mat[bottom][j]=count
                count+=1
            for i in range(bottom,top,-1):
                mat[i][left]=count
                count+=1
                #保证在完成所有外部填数后，将边界缩小
            top+=1
            right-=1
            bottom-=1
            left+=1
        if n%2==1:
            mat[n//2][n//2]=count
        return mat