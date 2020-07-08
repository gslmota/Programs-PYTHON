# função que descobre qual o elemento maior
def maior(* num):
    cont = maior = 0
    for val in num:
        if cont == 0:
            maior = val
        else:
            if val > maior:
                maior = val
            
        




# pragrama principal
maior(0,2)
maior(2,3,4,5,6)
maior(54,344,34342,22)