'''
Medidior de vel.:
Vel. max. permitida na rua = 80km, a partir disso, o usuario vai dar uma velocidade, e verificar se ele tomou multa leve, grave, ou gravíssima.
Se estiver abaixo, não tomou multa. 10km acima, multa leve; 11 a 20km acima, multa grave; acima de 20km multa gravíssima.
'''

vel_max = 80

vel_user = float(input('Qual foi a velocidade que o velocimetro mostrou? '))
if vel_user <= vel_max:
    print('Não levou multa alguma')
elif vel_user <= 90:
    print('Levou multa leve.')
elif vel_user > vel_max and vel_user <= 100:
    print('Levou multa grave.')
elif vel_user > 100:
    print('Levou multa gravíssima')