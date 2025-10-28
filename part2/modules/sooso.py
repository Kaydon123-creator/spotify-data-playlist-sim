import random 
from collections import deque
def perrin(nb_elements):
    derniers_elems = deque([3, 0, 2])
 
    #for i in range(min(3, nb_elements)):
       # yield derniers_elems[i]
 
    for i in range(3, nb_elements):
        n = derniers_elems[-2] + derniers_elems[-3]
        derniers_elems.popleft()
        derniers_elems.append(n)
        yield n 


print(len(perrin(2)))