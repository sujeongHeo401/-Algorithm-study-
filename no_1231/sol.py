class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        low = 1 #초기화 
        print("sum(sweetness): ", sum(sweetness))
        print("k + 1: ", k + 1)
        high = int(sum(sweetness) / (k+1)) # 초기화
        print("low : ", low)
        print("high: ", high)
        while low < high:
            mid = math.floor((high + low + 1) / 2)
            if self.can_split(sweetness, k, mid):
                low = mid
            else:
                high = mid - 1
        return low
        
    def can_split(self, sweetness: List[int], k: int, mid: int) -> bool:
        temp_sum = 0
        chunks = 0
        for element in sweetness:
            temp_sum += element
            if temp_sum >= mid:
                chunks += 1
                temp_sum = 0
        return chunks >= k + 1      

                
                