class Pista:
    def __init__(self, nome_pista, comprimento_pista, n_voltas, consumo, reabastecimentos):
        self.nome_pista = nome_pista
        self.comprimento_pista = comprimento_pista
        self.n_voltas = n_voltas
        self.consumo = consumo
        self.reabastecimentos = reabastecimentos

    def calculo_total_litros(self):
        comprimento_total = (self.comprimento_pista/1000) * self.n_voltas
        n_litros_total = comprimento_total / self.consumo

        return('O numero total de litros para o GP todo em ' + self.nome_pista + ' é de: ' + str(round(n_litros_total, 3)) + 'L')

    def calculo_primeiro_abastecimento(self):

        comprimento_total = (self.comprimento_pista/1000) * self.n_voltas
        n_litros_total = comprimento_total / self.consumo

        primeiro_abastecimento = n_litros_total / (self.reabastecimentos+1)

        return('O numero minimo de litros até o primeiro abastecimento em ' + self.nome_pista + ' é de: ' + str(round(primeiro_abastecimento, 3)) + 'L')

#pistas listadas:
silverstone = Pista('Silverstone', 5891, 59, 4.3, 2)
monaco = Pista('Monaco',3337, 52, 3.6, 1)
bahrein = Pista( 'Bahrein',5412, 63, 4.8, 2)

print(silverstone.calculo_primeiro_abastecimento())
print(monaco.calculo_primeiro_abastecimento())
print(bahrein.calculo_primeiro_abastecimento())
