class Conta:
    def __init__(self, num: int, ag: int, tit: str, saldo: float):
        self.numero = num
        self.agencia = ag
        self.titular = tit
        self.saldo = saldo

conta1 = Conta(12344, 1234, "Allysson", 2500.50)
print(conta1.numero, conta1.agencia, conta1.titular, conta1.saldo)
