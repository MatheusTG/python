class Casa:
    def __init__(self, quarto, sala, cozinha):
        self.quarto = quarto
        self.sala = sala
        self.cozinha = cozinha

    def tamanho(self, comodo):
        if comodo == 'quarto':
            return '10 x 10'

        elif comodo == 'sala':
            return '12 x 12'

        else:
            return '14 x 14'


mansao = Casa(3, 1, 1)
tamanho = mansao.tamanho('sala')
print(tamanho)
