from modelos.preços import Preços

produto_shampoo = Preços('Shampoo Hidratante', 'Shampoo com óleo de argan', '30', 'Prateleira A')
produto_condicionador = Preços('Condicionador Nutritivo', 'Condicionador com aloe vera', '35', 'Prateleira B')
produto_mascara = Preços('Máscara de Hidratação', 'Máscara para todos os tipos de cabelo', '50', 'Prateleira C')

produto_shampoo.alterar_estado()

produto_mascara.receber_preço('Fornecedora A', '50')
produto_mascara.receber_preço('Fornecedora B', '55')
produto_mascara.receber_preço('Fornecedora C', '48')

def main():
    Preços.listar_produtos()

if __name__ == '__main__':
    main()
