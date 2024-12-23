class Solution:
    def solve(self, indice, tamanho, mapa_requisitos, contador):
        if indice == tamanho:
            return 1

        total_permutacoes = 0

        for numero in range(contador, contador + indice + 1):
            total_permutacoes += self.solve(indice + 1, tamanho, mapa_requisitos, numero)

        return total_permutacoes

    def numberOfPermutations(self, tamanho, requisitos):
        return self.solve(1, tamanho, {}, 0)
