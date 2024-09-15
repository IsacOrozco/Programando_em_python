class Main:
    pass


from Cliente import Cliente

from Conta import Conta


c1 = Cliente("Isac ", "121231231")

conta = Conta(c1.get_nome(), 1222)


conta.deposita(int(input("Quanto gostaria de depositar: ")))

conta.saque(int(input("Quanto gostaria de sacar: ")))

conta.extrato()