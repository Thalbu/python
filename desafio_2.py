import math
Y = input()
y = float(Y)
x = [(y/2)]
cont = 0

while (cont < 32):
    x.append(x[cont]-((pow(x[cont],2)-y)/(2*x[cont])))
    cont = cont + 1
print('Valor fornecido: {0:.2f}'.format(y))
print('Valor da raiz: {0:.6f}'.format(x[cont]))