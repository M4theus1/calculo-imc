peso = float(input('Informe seu peso: '))
altura = float(input('Agora, sua altura: '))

imc = peso / (altura **2)

if imc < 18.5:
    print('Pesando {}Kg, medindo {}m e com o IMC de {:.2f}, você '
          'está classificado como ABAIXO DO PESO'.format(peso, altura, imc))
elif imc >= 18.5 and imc < 25:
    print('Pesando {}Kg, medindo {}m e com o IMC de {:.2f}, você '
          'está classificado como PESO IDEAL'.format(peso, altura, imc))
elif imc >= 25 and imc < 30:
    print('Pesando {}Kg e medindo {}m e com o IMC de {:.2f}, você '
          'está classificado como SOBREPESO'.format(peso, altura, imc))
elif imc >=30 and imc < 40:
    print('Pesando {}Kg e medindo {}m e com o IMC de {:.2f}, você '
          'está classificado como OBESIDADE'.format(peso, altura, imc))
else:
    print('Pesando {}Kg e medindo {}m e com o IMC de {:.2f}, você '
          'está classificado como OBESIDADE MÓRBIDA'.format(peso, altura, imc))