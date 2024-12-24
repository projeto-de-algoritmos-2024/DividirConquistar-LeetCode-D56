from sortedcontainers import SortedList

def countSubarrays(nums, k):
    def count_med(nums, x):
        # Passo 1: Transformar cada elemento em +1 (se <= x) ou -1 (se > x)
        arr = [1 if val <= x else -1 for val in nums]
        
        prefix_sum = 0
        # Usamos SortedList para armazenar prefix sums e
        # facilitar a contagem de quantos prefix sums são <= prefix_sum atual
        sl = SortedList([0])
        
        count = 0
        # Percorremos cada valor transformado
        for num in arr:
            # Atualiza o prefix sum
            prefix_sum += num
            
            # Quantos prefix sums anteriores são <= prefix_sum?
            idx = sl.bisect_right(prefix_sum)
            count += idx
            
            # Adiciona o prefix_sum atual na estrutura
            sl.add(prefix_sum)
        
        return count
    
    # Subarrays com mediana = k => F(k) - F(k - 1), onde F(x) conta
    # quantos subarrays têm mediana <= x
    return count_med(nums, k) - count_med(nums, k-1)

# Exemplo de teste
nums = [3, 2, 1, 4, 5]
k = 4
print(countSubarrays(nums, k))  # Esperado = 3
