usuarios = []
maior_c = 0
menor_c = 0
media_1 = 0
media_2 = 0
media_3 = 0
total_1 = 0
total_2 = 0
total_3 = 0
cont_1 = 0
cont_2 = 0
cont_3 = 0

while True:
    user_in = input()
    classe = input()
    kwh = input()
    preco = input()
    if (user_in == '0') & (classe == '0') & (kwh == '0') & (preco == '0'): 
        break
    else: 
        usuario = [int(user_in), int(classe), int(kwh), float(preco)]
        usuario.append((float(kwh)*float(preco) + 27.32))
        usuarios.append(usuario)        
        
      

for user in usuarios:
    print('{0} {1} {2:.2f}'.format(int(user[0]),int(user[2]), float(user[4])))
    if ((maior_c <= int(user[2])) or (maior_c == 0)):
        maior_c = int(user[2])
    if (menor_c >= int(user[2]) or menor_c == 0):
        menor_c = int(user[2])
    if (int(user[1]) == 1):
        total_1 = total_1 + int(user[2])
        cont_1 = cont_1 + 1
    if (int(user[1]) == 2):
        total_2 = total_2 + int(user[2])
        cont_2 = cont_2 + 1
    if (int(user[1]) == 3):
        total_3 = total_3 + int(user[2])
        cont_3 = cont_3 + 1
        
media_1 = total_1/cont_1
media_2 = total_2/cont_2
media_3 = total_3/cont_3

print('{0} {1}'.format(maior_c, menor_c))

print('{0} {1} {2:.2f}'.format('1',total_1, media_1))
print('{0} {1} {2:.2f}'.format('2',total_2, media_2))
print('{0} {1} {2:.2f}'.format('3',total_3, media_3))
