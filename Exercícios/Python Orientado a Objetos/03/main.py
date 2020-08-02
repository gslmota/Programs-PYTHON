from a import A
# Programa principal
a1 = A()
a2 = A()

# Alterando valor direto na classe
A.var = 000
print(a1.var)
print(a2.var)