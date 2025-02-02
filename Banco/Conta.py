class Conta:
    def __init__(self, titular, numero):
        self._saldo = 0.0
        self._numero = numero
        self._titular = titular
     
    @property   
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):    
        if(saldo < 0):
            print("O saldo não pode ser negativo!!")
        else:
            self._saldo = saldo
    
    def deposita(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("Saque realizado com sucesso!!")
        else:
            print("Saque invalido, não possui saldo suficiente!!")
            
    def extrato(self):
        print("Cliente: ", self._titular, " Possui um saldo de: ", self._saldo)