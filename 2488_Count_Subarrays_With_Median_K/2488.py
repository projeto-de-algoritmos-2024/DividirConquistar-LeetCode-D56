from typing import List


def countSubarrays(nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for start in range(n):
            for end in range(start, n):
                arr = sorted(nums[start:end+1])
                length = end - start + 1
                mid_index = length // 2
                
                if length % 2 == 1:
                    # ímpar
                    median = arr[mid_index]
                else:
                    # par
                    median = arr[mid_index - 1]

                if median == k:
                    count += 1

        return count