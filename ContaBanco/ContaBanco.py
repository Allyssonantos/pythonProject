class Conta:
    def __init__(self, num: int, ag: int, tit: str, saldo: float):
        self.numero = num
        self.agencia = ag
        self.titular = tit
        self.saldo = saldo

    def ver_saldo(self):
        print(f'Seu saldo é {self.saldo}')

    def sacar(self, valor: float):
        if valor > self.saldo:
            print('Saldo Insuficiente')
        else:
            self.saldo = self.saldo - valor # self.saldo -= valor
            self.ver_saldo()

    def depositar(self, valor: float):
        if valor <= 0:
            print('Valor de depósito inválido')
        else:
            self.saldo += valor
            print(f'Você depositou {valor: }')
            self.ver_saldo()

    def transferir(self, destino, valor: float):
        if valor > self.saldo:
            print('Saldo Insuficiente para transferência')
        elif valor <= 0:
            print('Valor de transferência inválido')
        else:
            self.saldo -= valor
            destino.saldo += valor
            print(f'Você transferiu {valor:} para a conta {destino.numero} (Titular: {destino.titular})')
            self.ver_saldo()


conta1 = Conta(12345, 1234, 'Allysson', 100)
conta1.ver_saldo()

conta2 = Conta(12334, 1239, 'Maria', 200)
conta2.ver_saldo()

valor_saque = float(input("Digite o valor a ser sacado de Allysson: "))
conta1.sacar(valor_saque)

valor_deposito = float(input("Digite o valor a ser depositado de Allysson: "))
conta1.depositar(valor_deposito)

valor_transferencia = float(input("Digite o valor a ser transferido de Allysson para a conta de Maria: "))
conta1.transferir(conta2, valor_transferencia)

print(conta1.numero, conta1.agencia, conta1.titular, f'R${conta1.saldo}')
print(conta2.numero, conta2.agencia, conta2.titular, f'R${conta2.saldo}')
