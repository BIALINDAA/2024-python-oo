class Cliente:
    clientes = []

    def __init__(self, nome, serviço, horário, pagamento):
        self.nome = nome
        self.serviço = serviço
        self.horário = horário
        self._pagamento = False
        Cliente.clientes.append(self)

    def __str_(self):
        return f'{self.nome} | {self.serviço} | {self.horário} | {self.pagamento}'

    def listar_cliente():
        print('''
█▀▀ █░░ █ █▀▀ █▄░█ ▀█▀ █▀▀ █▀   █▀▄ ▄▀█   █░░ █▀█ ░░█ ▄▀█   █▀▄ ▄▀█   █▄▄ █ ▄▀█
█▄▄ █▄▄ █ ██▄ █░▀█ ░█░ ██▄ ▄█   █▄▀ █▀█   █▄▄ █▄█ █▄█ █▀█   █▄▀ █▀█   █▄█ █ █▀█''')
        
        print(f'{'Nome do Cliente'.ljust(25)} | {'serviço'.ljust(25)} | {'horário'.ljust(25)} | {'pagamento'.ljust(25)}')
        for cliente in Cliente.clientes:
            print(f'{cliente.nome} | {cliente.servio} | {cliente.horário} | {cliente.pagamento}')
            
    @property
    def exrtinta(self):
        return '❌ não pago' if self._pagamento else '✔️ pago'
    
cliente_Maria = Cliente('Maria', 'Corte de cabelo', '10:00', 'Dinheiro')
cliente_Fernanda = Cliente('Fernanda', 'Manicure', '14:00', 'Cartão')
cliente_Ana = Cliente('Ana', 'Corte de cabelo', '11:00', 'Dinheiro')

Cliente.listar_cliente()