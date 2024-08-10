altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está com magresa')
elif imc >= 18.5 and  imc <= 24.9:
    print('Normal')
elif imc >= 25 and imc <= 29.9:
    print("Você estar no com sobrepeso")
elif  imc >= 30 and imc <= 39.9:
    print(" Você estar com obsidade")
elif imc >=40:
    print(" Obesidade grave")

