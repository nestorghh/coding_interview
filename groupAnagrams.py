class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        d={}
        
        for current in strs:
            cw = "".join(sorted(current))
            
            if cw in d:
                d[cw].append(current)
            else:
                d[cw]=[current]
                
        return [d[k] for k in d]
        

