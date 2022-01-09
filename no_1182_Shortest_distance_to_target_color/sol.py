class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        ans =[]
        for idx, nearEle in queries:
            if nearEle not in colors or idx < 0 or idx >= len(colors):
                ans.append(-1)
            else:
                print("colors[idx] : ", colors[idx])
                print("colors.index(nearEle) : ",colors.index(nearEle))
                
        
#  Input: colors = [1,1,2,1,3,2,2,3,3], 
#     queries = [[1,3],[2,2],[6,1]]
# Output: [3,0,3]       