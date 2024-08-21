annualInvoice = float(input('\nDigite o valor do seu faturamento anual em reais: '))

planoValido = False
while planoValido == False:
    planType = int(input('\nSelecione abaixo o seu atual plano de assinatura:\n\n [1] Basic | [2] Silver | [3] Gold | [4] Platinum\n\nPlano de assinatura: '))
    if planType == 1:
        paymantPercentage = annualInvoice * 0.30
        planoValido = True
    elif planType == 2:
        paymantPercentage = annualInvoice * 0.20
        planoValido = True
    elif planType == 3:
        paymantPercentage = annualInvoice * 0.10
        planoValido = True
    elif planType == 4:
        paymantPercentage = annualInvoice * 0.05
        planoValido = True
    else:
        print('Essa não é uma opção válida')