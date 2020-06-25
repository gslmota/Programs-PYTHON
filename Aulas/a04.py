# Estruturas de Decisão
nome = str(input('Digite o seu nome: ')).strip()
'''
if nome == 'Gabriel':
    print('Prazer Gabriel!')
else:
    print('Prazer!')
'''
#print('Prazer Gabriel!' if nome == 'gabriel' else 'Prazer')
# ^ é um if resumido

# Estrutura Aninhada
# usando o nome coletado anteriormente
if nome == 'Gabriel':{
    print('Que nome legal!')} 
elif nome == 'Joao' or nome == 'Pedro':{
    print('Nome comum no brasil')}
else:{
    print('Seu nome é bem normal!')
}