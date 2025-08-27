texto = "Hola Marcos "
resul = texto[3]
resul2= texto[-3]

print(resul + "-->"  +resul2)

resul_index = texto.index("l")

print(resul_index)

#busca de izquierda a derecha
resul_index_prt = texto.index("l", 0)
print(resul_index_prt)

#busca de derecha a izquierda
resul_rindex_prt = texto.rindex("M", 0,8)
print(resul_rindex_prt)
