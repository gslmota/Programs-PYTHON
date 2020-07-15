# Analisando dicionarios
def notas(*n, sit = False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    
    
# Programa principal
resp = notas(5.5, 3.4, 7, 4.9)
print(resp)