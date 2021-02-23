def funcao_fx(x,n,Y):
    funcao = x**n-Y
    return funcao
def derivada_fx(x,n):
    derivada = n*(x**(n-1))
    return derivada
def raiz(x,n,Y,epsilon):
    
    if (x**n-Y >= (-epsilon)) & (x**n-Y <= epsilon):
        return x 
    else:
        x = x - (funcao_fx(x,n,Y)/derivada_fx(x,n))
        return raiz(x,n,Y,epsilon) 

n = int(input(''))
L = range(1,11)
epsilon = 10**(-5)

print('Tabela de raiz de ordem {0}'.format(n))
print('Número  Raiz')
for Y in L:
    Xo = Y/2
    x = raiz(Xo,n,Y,epsilon)
    print('{0}      {1: .4f}'.format(Y,x))