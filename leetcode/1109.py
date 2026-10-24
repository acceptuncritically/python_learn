class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        dict1={}
        for i in range(1,n+1):
            dict1[i]=0
        for i in range(1,n+1):
            for j in range(0,2):
                dict1[bookings[i-1][j]]=dict1.get(bookings[i-1][j],0)+bookings[i-1][2]
        return [value for key,value in dict1.items()]

    def corpFlightBookings1(self, bookings: list[list[int]], n: int) -> list[int]:
        dict1 = {}
        # 初始化字典，1 到 n 航班号初始值为 0
        for i in range(1, n + 1):
            dict1[i] = 0
        # 遍历每一个订单 (直接遍历 bookings)
        for first, last, seats in bookings:
            # 修复逻辑：要把 first 到 last 之间的所有航班都加上座位
            for flight in range(first, last + 1):
                dict1[flight] = dict1.get(flight, 0) + seats

            # 按 1 到 n 的顺序提取结果返回
        return [dict1[i] for i in range(1, n + 1)]

    def corpFlightBookings2(self, bookings: list[list[int]], n: int) -> list[int]:
        diff=[0]*n
        for first, last, seats in bookings:
            diff[first-1]+=seats
            diff[last]-=seats

        answer=[0]*n
        last_seats=0
        for i in range(n):
            answer[i]=diff[i]+last_seats
            last_seats=answer[i]
        return answer
if __name__=='__main__':
    s=Solution()
    print(s.corpFlightBookings2([[1,2,10],[2,3,20],[2,5,25]],5))