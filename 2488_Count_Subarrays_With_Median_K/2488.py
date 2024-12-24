from collections import defaultdict


def countSubarrays( nums, k):
    def count_med(nums, x):
        arr = [1 if val <= x else -1 for val in nums]

        prefix_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # prefix sum antes de começar
        
        #Um subarray  tem mediana ≤ 𝑥 se ao menos metade dos elementos são ≤ 𝑥
        
        count = 0
        for num in arr:
            prefix_sum += num

            c = 0
            for ps_val, how_many in prefix_counts.items():
                if ps_val <= prefix_sum:
                    c += how_many
            count += c
            prefix_counts[prefix_sum] += 1
        
        return count
    return count_med(nums, k) - count_med(nums, k-1)

nums = [3,2,1,4,5]
k = 4
print(countSubarrays(nums, k)) #  esperado = 3