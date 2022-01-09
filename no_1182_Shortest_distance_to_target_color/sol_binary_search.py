class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        hashmap = collections.defaultdict(list) # 1111
        for i, c in enumerate(colors):
            hashmap[c].append(i)
            
        query_results = []
        for i, (target, color) in enumerate(queries):
            if color not in hashmap:
                query_results.append(-1)
                continue
            
            index_list = hashmap[color] # 22222
            insert = bisect.bisect_left(index_list, target)
            
            left_nearest = abs(index_list[max(insert - 1, 0)] - target)
            right_nearest = abs(index_list[min(insert, len(index_list) - 1)] - target)
            query_results.append(min(left_nearest, right_nearest))
        return query_results

#  Input: colors = [1,1,2,1,3,2,2,3,3], 
#     queries = [[1,3],[2,2],[6,1]]
# Output: [3,0,3]       