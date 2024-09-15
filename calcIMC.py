print('\tCalculo de IMC')
print('')
nome=input('Seu nome: ')
peso= float(input('Informe seu peso: '))
altura= float(input('Informe sua altura: '))
print('')
print('CALCULANDO IMC...')
print('')

imc= peso/(altura*altura)

print(f'IMC:{imc:.2f}')

if imc <18.5:
    print(f'{nome} seu IMC é:{imc:.2f} voce esta abaixo do peso. Cuidado!')
elif imc >=18.5 and imc <=24.9:
    print(f'{nome} seu peso esta normal seu IMC é:{imc:.2f} .')
elif imc >=25 and imc <=29.9:
    print(f'{nome}, seu IMC é:{imc:.2f} cuidado voce esta com excesso de peso.')
elif imc >30:
    print(f'{nome} seu IMC é:{imc:.2f} voce esta com obesidade')
elif imc <35:
    print(f'seu IMC é:{imc:.2f} voce esta com obesidade EXTREMA')
else:
    print('Voce esta morrendo')

