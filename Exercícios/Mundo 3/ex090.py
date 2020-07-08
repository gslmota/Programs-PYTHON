# função que descobre qual o elemento maior
def maior(* num):
    con = 0
    maior = 0
    for val in num:
        if con == 0:
            maior = val
            con += 1
        else:
            if val > maior:
                maior = val
        con += 1
print(f'Foram informados {con} valores')
print(f'O maior valor é {maior}')
        


# pragrama principal
maior(0,2)
maior(2,3,4,5,6)
maior(54,344,34342,22)