# Aula de Modularização
# Voce tera mais organização, facil manutenção, ocultar codigo, reutilização
# Arquivo de Modulos : Uteis
import uteis
# Programa principal
num =  int(input("Digite um numero: "))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}!')
print(f'O dobro de {num} é {uteis.dobro(num)}!')
print(f'O triplo de {num} é {uteis.triplo(num)}!')
