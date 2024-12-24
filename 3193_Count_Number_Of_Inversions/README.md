
# Count the Number of Inversions

**Problema disponível no LeetCode:** [Count the Number of Inversions](https://leetcode.com/problems/count-the-number-of-inversions/)

## Descrição

Dado um array `nums` de números inteiros, precisamos contar o número de **inversões** no array.  
Uma inversão é definida como um par de índices \( (i, j) \), onde:

1. \( i < j \)
2. \( nums[i] > nums[j] \)

Nosso objetivo é determinar quantos desses pares existem no array.

### Exemplo:

**Entrada:**
```plaintext
nums = [8, 4, 2, 1]
```

**Saída:**
```plaintext
6
```

**Explicação:**  
As inversões são:
1. (8, 4)
2. (8, 2)
3. (8, 1)
4. (4, 2)
5. (4, 1)
6. (2, 1)

**Explicação:**  
Não há inversões porque o array está ordenado.

### Restrições

- \( 1  <= nums.length  <= 100,000 \)
- \( -10^9  <= nums[i]  <= 10^9 \)

## Solução

Para resolver o problema de forma eficiente, utilizamos uma abordagem baseada no **Merge Sort. Esse algoritmo divide o array em subarrays menores e os ordena, contando as inversões durante o processo de mesclagem.

1. **Condições para uma inversão**:
   - Se um elemento do lado direito do array for menor que um elemento do lado esquerdo, todos os elementos restantes no lado esquerdo formam inversões com ele.

2. **Passos principais**:
   - Dividir o array em subarrays menores usando recursão.
   - Contar as inversões dentro de cada subarray.
   - Contar as inversões entre os subarrays durante o processo de mesclagem.