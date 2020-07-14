# Exercicio de função
# Ex 101 
# Função para votação
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos, não vota!'
    elif idade < 18:
        return f'Com {idade} anos, o voto é opcionla!'
    else: 
        return f'Com {idade} anos, o voto é obrigatório!'


# Programa principal
anonasc = int(input("Digite o ano de nascimento: "))
print(voto(anonasc))
    