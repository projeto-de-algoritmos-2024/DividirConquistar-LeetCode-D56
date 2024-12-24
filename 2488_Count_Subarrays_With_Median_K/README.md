# Count Subarrays With Median k

Dado um array de inteiros (`nums`) e um inteiro `k`, **conte quantos subarrays** de `nums` possuem mediana igual a `k`.

A mediana de um subarray ordenado é:
- O elemento do meio, caso a quantidade de elementos seja ímpar;
- O **menor** dos dois elementos do meio, caso a quantidade de elementos seja par (conforme especificado no enunciado do problema).

## Exemplo 1

- **Entrada:** `nums = [3, 2, 1, 4, 5], k = 4`
- **Saída:** `1`

Explicação:
- Há apenas um subarray cuja mediana é igual a `4`: `[4]`.

## Exemplo 2

- **Entrada:** `nums = [2, 3, 3, 1, 3, 5, 3], k = 3`
- **Saída:** `5`

Explicação:
- Há 5 subarrays com mediana `3`. Exemplos (não exaustivos):
  - `[2, 3, 3]`
  - `[3, 3]`
  - `[3, 3, 1, 3]`
  - `[3, 1, 3]`
  - `[5, 3]`
  - ... (pode haver mais combinações)

## Restrições

- `1 <= nums.length <= 10^5`
- `1 <= nums[i], k <= 10^5`

**Observações:**
1. É necessário identificar de forma eficiente quando um subarray possui mediana igual a `k`.  
2. Uma estratégia comum envolve transformar os valores para que `k` torne-se um "marco" (por exemplo, substituindo valores maiores que `k` por `1` e valores menores que `k` por `-1`, e utilizando prefix sums para encontrar subarrays elegíveis).
3. A solução exige gerenciamento cuidadoso para lidar com a mediana em subarrays de tamanho par.

> **Nota**: Caso deseje o texto integral ou mais detalhes, consulte a  
> [página do problema no LeetCode](https://leetcode.com/problems/count-subarrays-with-median-k/description/).
