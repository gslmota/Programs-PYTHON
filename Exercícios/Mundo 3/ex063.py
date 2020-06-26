# Tupla de 0 até 10
nextensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    n = int(input('Digite um número: '))
    if n >= 0 and n <= 10:
        break
print(f'O numero {n} por extenso é {nextensos[n]}')
