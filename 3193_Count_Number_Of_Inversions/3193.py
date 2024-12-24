class Solution:
    def __init__(self):  
        self.dp = {} 
        self.mod = int(1e9 + 7) 

    def solve(self, indice, tamanho, mapa_requisitos, contador):
        if indice == tamanho:
            return 1

        if contador > 400:
            return 0

        # Verifica se o resultado já foi calculado e armazenado
        if (indice, contador) in self.dp:
            return self.dp[(indice, contador)]

        total_permutacoes = 0

        # Para cada número no intervalo [contador, contador + indice + 1]
        for numero in range(contador, contador + indice + 1):

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