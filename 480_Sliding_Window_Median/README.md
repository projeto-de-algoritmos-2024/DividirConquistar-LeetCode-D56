# Sliding Window Median

Dado um array de inteiros (`nums`) e um valor inteiro `k`, existe uma janela deslizante de tamanho `k` que percorre o array da esquerda para a direita. Em cada posição da janela, é possível ver somente os `k` elementos que estão dentro dela. A cada movimentação para a direita, deve-se calcular a mediana dos elementos que estão na janela.

A mediana é definida como:
- Se o número de elementos for ímpar, retorna o valor do elemento do meio após a ordenação.
- Se o número de elementos for par, retorna a média (média aritmética) dos dois elementos do meio.

**Retorne a mediana de cada janela deslizante ao longo do array.** Respostas dentro de 10^-5 do valor real são aceitas.

## Exemplo 1

- **Entrada:** `nums = [1,3,-1,-3,5,3,6,7], k = 3`
- **Saída:** `[1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]`


## Exemplo 2

- **Entrada:** `nums = [1,2], k = 2`
- **Saída:** `[1.50000]`

## Restrições

- `1 <= k <= nums.length <= 10^5`
- Cada valor em `nums` está dentro do intervalo de 32 bits para inteiros.
- Deve-se garantir eficiência na atualização da mediana a cada passo da janela.
