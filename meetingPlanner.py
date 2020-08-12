def meeting_planner(slotsA, slotsB, dur):
  
  def overlap(intervalA,intervalB):
    if intervalA[1]<intervalB[0]:
      return False
    else:
      return [max(intervalA[0],intervalB[0]),min(intervalA[1],intervalB[1])]
      
  i, j = 0,0
  
  while i<len(slotsA) and j<len(slotsB):
    # how do we check that two intervals overlap:
    
    if overlap(slotsA[i],slotsB[j]):
      interval=overlap(slotsA[i],slotsB[j])
      if interval[1]-interval[0]>=dur:
        return [interval[0],interval[0]+dur]
    if slotsA[i][1] <slotsB[j][1]:
      i+=1
    elif slotsA[i][1] >slotsB[j][1] :
      j+=1
    else:
      i+=1
      j+=1
        
  return []
