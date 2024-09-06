class Cliente:
    def __init__(self, nome, servico, horario, pagamento):
        self.nome = nome
        self.servico = servico
        self.horario = horario
        self.pagamento = pagamento

cliente_Maria = Cliente(nome="Maria", servico="Corte de cabelo", horario="10:00", pagamento="Dinheiro")
cliente_Fernanda = Cliente(nome="Fernanda", servico="Manicure", horario="14:00", pagamento="Cartão")

clientes = [cliente_Maria, cliente_Fernanda]
