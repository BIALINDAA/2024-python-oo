class Preços:
    def __init__(self, nome, descricao, preco, local):
        self._nome = nome
        self._descricao = descricao
        self._preco = float(preco)  # Converta para float
        self._local = local
        self._estoque = False

    def __str__(self):
        return f'{self._nome} | {self._descricao} | {self._preco} | {self._local} | {self.estoque}'

    def alterar_estado(self):
        self._estoque = not self._estoque
