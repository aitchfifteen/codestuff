class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        possible = sum(gas) - sum(cost)
        diff = gas[:]

        if possible < 0:
            return -1
        
        tank = 0
        min_tank = 0
        min_index = -1

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff

            if tank < min_tank:
                min_tank = tank
                min_index = i
        
        start = (min_index + 1) % len(gas)
        return start







