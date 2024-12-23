class Solution:
    def __init__(self):
        self.dp = {}
        self.mod = int(1e9 + 7)

    def solve(self, indice, tamanho, mapa_requisitos, contador):
        if indice == tamanho:
            return 1

        if (indice, contador) in self.dp:
            return self.dp[(indice, contador)]

        total_permutacoes = 0

        for numero in range(contador, contador + indice + 1):
            total_permutacoes = (total_permutacoes + self.solve(indice + 1, tamanho, mapa_requisitos, numero)) % self.mod

        self.dp[(indice, contador)] = total_permutacoes
        return total_permutacoes

    def numberOfPermutations(self, tamanho, requisitos):
        mapa_requisitos = {}
        for requisito in requisitos:
            mapa_requisitos[requisito[0]] = requisito[1]

        return self.solve(1, tamanho, mapa_requisitos, 0)
