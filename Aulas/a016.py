# Aula de Modularização
# Voce tera mais organização, facil manutenção, ocultar codigo, reutilização
# Arquivo de Modulos : Uteis
import Aulas.uteis.funcao

# Programa principal
num =  int(input("Digite um numero: "))
fat = Aulas.uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}!')
print(f'O dobro de {num} é {Aulas.uteis.dobro(num)}!')
print(f'O triplo de {num} é {Aulas.uteis.triplo(num)}!')
print(f'A soma de 2 e 3 é {Aulas.uteis.funcao.soma(2, 3)}')
