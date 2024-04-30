def pagamento(ckm, dp):
    valor_total = ckm * dp
    return valor_total

def inserir():
    ckm = float(input('Digite o custo do KM rodado: '))
    dp = float(input('Digite a distância percorrida em KM: '))

    valor_total = pagamento(ckm, dp)

    print('O total a pagar é R$', valor_total)

inserir()

