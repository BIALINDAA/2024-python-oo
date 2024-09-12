class Cliente:
    def __init__(self, nome, servico, horario, pagamento):
        self.nome = nome
        self.servico = servico
        self.horario = horario
        self.pagamento = pagamento

    def __str_(self):
        return f'{self.nome} | {self.servico} | {self.horario} | {self.pagamento}'
    
cliente_Maria = Cliente('Maria', 'Corte de cabelo', '10:00', 'Dinheiro')
cliente_Fernanda = Cliente('Fernanda', 'Manicure', '14:00', 'Cartão')
cliente_Ana = Cliente('Ana', 'Corte de cabelo', '11:00', 'Dinheiro')

clientes = [cliente_Maria, cliente_Fernanda, cliente_Ana]

print(cliente_Maria)
print(cliente_Fernanda)