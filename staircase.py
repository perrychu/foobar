
import math

def memoize(f):
    memo = {}
    def helper(x,y):
        if (x,y) not in memo:            
            memo[(x,y)] = f(x,y)
        return memo[(x,y)]
    return helper

def answer(n):
  if n < 3:
    return 0
  
  #n = (k*(k+1))/2
  max_steps = int(0.5*(math.sqrt(8*n+1)-1))
  print("max_steps:",max_steps)
  
  count = 0
  
  for steps in range(2,max_steps+1):
    #print("steps:", steps)
    bricks_req = steps*(steps+1)/2
    bricks_remain = n - bricks_req
    
    res = do_count(steps, bricks_remain)
    
    print("result for",steps,"steps is:",res)
    
    count += res
  
  return count

@memoize 
def do_count(steps, bricks):
  #print("do_count - steps:",steps,"bricks:",bricks)
  if steps == 1:
    return 1
  
  if bricks == 0:
    return 1
  
  max_lowest = int(bricks / steps) 
  #print("max_lowest:", max_lowest)
  count = 0
  
  for lowest in range(0,max_lowest+1):
    #print("lowest:",lowest)
    bricks_req = lowest * steps
    if steps-1 == 1:
      count+=1
    else:
      count += do_count(steps-1, bricks - bricks_req)
  
  return count

print(answer(200))
