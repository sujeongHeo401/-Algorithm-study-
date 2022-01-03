class Solution(object):
    def minCost(self, costs):

        for n in range(1, len(costs)):
            costs[n][0] += min(costs[n - 1][1], costs[n - 1][2])            # Total cost of painting nth house red.
            costs[n][1] += min(costs[n - 1][0], costs[n - 1][2])            # Total cost of painting nth house green.
            costs[n][2] += min(costs[n - 1][0], costs[n - 1][1])            # Total cost of painting nth house blue.

        if len(costs) == 0: return 0
        return min(costs[len(costs)-1])  