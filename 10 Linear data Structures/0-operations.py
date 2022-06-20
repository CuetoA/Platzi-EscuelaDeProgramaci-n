from re import A


l = []


# (C) Insert
l.append('Scarlette')
l.insert(0, 'Boni')
# (R) Acceder
print(l)
print(l[0])
# (U) Remplazar
l[1] = "Ceres"
print(l)
# (D) Remover
l.pop(1)
print(l)
# Concatenar
a = ['Scarlette']
l = l + a
print(l)
# Convertir
string = ' '.join(l)
print(string)