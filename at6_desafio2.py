from math import *
virus = []

while True:
    n_cultura = input()
    n_celulas = input()
    d_placa = input()
    t_cres = input()
    if (n_cultura == '0') & (n_celulas == '0') & ( d_placa == '0') & (t_cres == '0'): 
        break
    else: 
        entrada = [int(n_cultura), int(n_celulas), int(d_placa), float(t_cres)]
        aux = int(n_celulas)/10
        geracao = 0
        base = 1 + entrada[3]
        while ((aux)<(((entrada[2]*10/2)**2)*pi)):
            geracao += 1
            aux = aux*base
            
            
        entrada.append(geracao)
        virus.append(entrada)        
        
for user in virus:
    print('{0} {1} {2} {3} {4}'.format(int(user[0]),int(user[1]), int(user[2]), float(user[3]), int(user[4])))