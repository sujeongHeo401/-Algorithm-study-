class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # common slot : [max(start1, start2), min(end1, end2)]
        slots1.sort()
        slots2.sort()
        pointer1 = pointer2 = 0
        while pointer1 < len(slots1) and pointer2 < len(slots2):
            # find the boundaries of the intersection, or the common slot
            intersect_start = max(slots1[pointer1][0], slots2[pointer2][0])
            intersect_end = min(slots1[pointer1][1], slots2[pointer2][1])
            
            if intersect_end - intersect_start >= duration:
                return [intersect_start, intersect_start + duration]
            
            #always move the one that ends earlier
            if slots1[pointer1][1] < slots2[pointer2][1]:
                pointer1 += 1
            else:
                pointer2 += 1
        return []
                

            
