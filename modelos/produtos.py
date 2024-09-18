from modelos.produtos import Produtos

class Produtos:
    produtos = []

    def __init__(self, nome, descricao, preco, local):
        self._nome = nome.upper()
        self._descricao = descricao.title()
        self._preco = preco
        self._local = local.title()
        self._estoque = False
        self._valor = []
        Produtos.produtos.append(self)

    def __str__(self):
        return f'{self._nome} | {self._descricao} | {self._preco} | {self._local} | {self.estoque}'

    @classmethod
    def listar_produtos(cls):
        print('''
██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗████████╗░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔════╝
██████╔╝██████╔╝██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝██████╔╝╚██████╔╝░░░██║░░░╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░
''')
        
        print(f'{"Nome do Produto".ljust(20)} | {"Descrição".ljust(30)} | {"Preço".ljust(10)} | {"Local".ljust(20)} | {"Estoque".ljust(10)} | {"Média de Preço"}')
        print('------------------------------------------------------------------------------------------------------------------------------')
        for produto in cls.produtos:
            print(f'{produto._nome.ljust(20)} | {produto._descricao.ljust(30)} | {produto._preco.ljust(10)} | {produto._local.ljust(20)} | {produto.estoque.ljust(10)} | {produto.media_preco}')
            print('------------------------------------------------------------------------------------------------------------------------------')

    @property
    def estoque(self):
        return '❌ Sem estoque' if self._estoque else '✔️ Em estoque'

    def alterar_estado(self):
        self._estoque = not self._estoque        

    def receber_preco(self, fornecedor, preco):
        preco = Produtos(fornecedor, preco)
        self._valor.append(preco)

    @property
    def media_preco(self):
        if not self._valor:
            return 0 
        soma_dos_precos = sum(valor._preco for valor in self._valor)
        quantidade_fornecedores = len(self._valor)
        media = round(soma_dos_precos / quantidade_fornecedores, 2)
        return media
