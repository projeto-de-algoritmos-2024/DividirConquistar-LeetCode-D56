from typing import List

def medianSlidingWindow( nums: List[int], k: int) -> List[float]:
        result = []

        for i in range(len(nums) - k + 1):
            window = nums[i:i+k]

            # Cálculo da mediana :
            window.sort()
            if k % 2 == 1:
                result.append(window[k // 2])
            else:
                result.append((window[k // 2] + window[k // 2]) / 2)
        
        return result

nums = [1,3,-1,-3,5,3,6,7]
k = 2
print(medianSlidingWindow(nums, k)) #  esperado = [2.0,-2.0,-1.0,1.0,4.0,4.5,6.5]