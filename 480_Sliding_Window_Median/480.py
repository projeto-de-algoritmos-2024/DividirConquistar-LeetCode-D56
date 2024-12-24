from typing import List
from sortedcontainers import SortedList


def medianSlidingWindow( nums: List[int], k: int) -> List[float]:
    sl = SortedList()
    result = []

    for i in range(len(nums)):
        sl.add(nums[i])
        
        # Se exceder o tamanho k, removemos o elemento antigo
        if i >= k:
            sl.remove(nums[i - k])

        # Quando atingimos pelo menos k elementos, calculamos a mediana
        if i >= k - 1:
            if k % 2 == 1:
                result.append(sl[k // 2])
            else:
                mid1 = sl[k // 2 - 1]
                mid2 = sl[k // 2]
                result.append((mid1 + mid2) / 2)

    return result

nums = [1,3,-1,-3,5,3,6,7]
k = 2
print(medianSlidingWindow(nums, k)) #  esperado = [2.0,-2.0,-1.0,1.0,4.0,4.5,6.5]