def leiaDinheiro(msg):
    val = False
    while not val:
        entrada = str(input(msg)).replace('.', ',').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro! \"{entrada}\" é um preço inválido!')
        else:
            val = True
            return float(entrada)