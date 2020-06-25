# price for travel
dist = float(input('Digite a distância: '))
if dist < 200:
    price = dist * 0.50
else:
    price = dist * 0.45
print('O preço da viagem é: {:0.2f}'.format(price))