from typing import List


def countSubarrays( nums, k):
    def F_brute(nums, x):
        n = len(nums)
        cnt = 0
        for start in range(n):
            for end in range(start, n):
                arr = sorted(nums[start:end+1])
                length = end - start + 1
                mid_index = length // 2
                
                if length % 2 == 1:
                    median = arr[mid_index]
                else:
                    # Para par, o problema define mediana como
                    # o MENOR dos dois do meio
                    median = arr[mid_index - 1]
                
                # Agora, se mediana <= x, incrementa
                if median <= x:
                    cnt += 1
        return cnt
    return F_brute(nums, k) - F_brute(nums, k-1)

nums = [3,2,1,4,5]
k = 4
print(countSubarrays(nums, k)) #  esperado = 3