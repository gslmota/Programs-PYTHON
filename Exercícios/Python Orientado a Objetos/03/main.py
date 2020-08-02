from a import A
# Programa principal
a1 = A()
a2 = A()
print(A.var)
# Alterando valor direto na classe
A.var = 000
# novo valor 
print(A.var)
print(a1.var)
print(a2.var)   