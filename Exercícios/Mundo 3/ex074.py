# Verifica parênteses
lista = []
exp = str(input('Digite a expressão: '))
for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
          lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')