#Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

#Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

import heapq
import statistics
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students={}
        
        for i in items:
            if i[0] not in students:
                students[i[0]]=[i[1]]
            else:
                heapq.heappush(students[i[0]],i[1])
            
        out=[]
        for s in students:
              out.append([s,sum(heapq.nlargest(5,students[s]))//5])
        return out
                

