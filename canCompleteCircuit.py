class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        current_gas = 0
        
        for i in range(len(gas)):
            done = True
            for j in range(len(gas)):
                if -cost[(i+j)%len(gas)] + (current_gas + gas[(i+j)%len(gas)])>=0:
                    current_gas +=gas[(i+j)%len(gas)] - cost[(i+j)%len(gas)]
                else:
                    current_gas = 0
                    done = False
                    break
            if done:
                return i
        return -1

a=Solution()
a.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])

