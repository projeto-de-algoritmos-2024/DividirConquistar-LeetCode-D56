class Solution:
    def __init__(self):  # Corrige o nome do método para __init__
        self.dp = {}  # Dicionário para armazenar os resultados já calculados (memoização)
        self.mod = int(1e9 + 7)  # Constante para realizar operações de módulo

    def solve(self, indice, tamanho, mapa_requisitos, contador):
        # Caso base: se já colocamos todos os números, temos uma permutação válida
        if indice == tamanho:
            return 1

        # Se o contador excede 400, nenhuma permutação válida é possível
        if contador > 400:
            return 0

        # Verifica se o resultado já foi calculado e armazenado
        if (indice, contador) in self.dp:
            return self.dp[(indice, contador)]

        total_permutacoes = 0

        # Tenta posicionar números de contador até contador + indice
        for numero in range(contador, contador + indice + 1):
            # Verifica se o índice atual possui um requisito estrito
            if indice in mapa_requisitos and mapa_requisitos[indice] != numero:
                continue

            # Chamada recursiva para o próximo índice
            total_permutacoes = (total_permutacoes + self.solve(indice + 1, tamanho, mapa_requisitos, numero)) % self.mod

        # Armazena o resultado no dicionário para reutilização
        self.dp[(indice, contador)] = total_permutacoes
        return total_permutacoes

    def numberOfPermutations(self, tamanho, requisitos):
        # Cria um mapeamento para os requisitos
        mapa_requisitos = {}
        for requisito in requisitos:
            mapa_requisitos[requisito[0]] = requisito[1]

        # Se houver um requisito para o índice 0 que não seja zero, é inválido
        if 0 in mapa_requisitos and mapa_requisitos[0] != 0:
            return 0

        # Inicializa a solução recursiva com programação dinâmica
        return self.solve(1, tamanho, mapa_requisitos, 0) 