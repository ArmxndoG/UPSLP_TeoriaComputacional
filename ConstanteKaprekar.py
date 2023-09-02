
#coding=utf-8
def constanteKaprekar(numero):
    
    digitos = [int(a) for a in str(numero)]#guardando los digitos en una lista ej: [1,2,3,4]
    #ordenar la lista de digitos de forma descendente y ascendente.
    menor = int(''.join(map(str,sorted(digitos)))) #concatenar los digitos de la lista como cadenas para luego convertir esa cadena a 'enter ej: [1,2,3,4] -> '1234' -> 1234
    mayor = int(''.join(map(str,sorted(digitos,reverse=True)))) #[4,3,2,1] -> '4321' -> 4321
    resta = mayor - menor #Restar el menor al mayor
    print(f"{mayor} - {menor} = {resta}")
    #Volver a llamar a la función hasta que el resultado sea 6174
    if resta == 6174: 
        print(f"Se alcanzó la constante de kaprekar: {resta}")
        return resta
    else:
        constanteKaprekar(resta)
# Verificar que el número sea de 4 digitos   
while(True):
    pedir_numero = input("Digita un número de 4 digitos: ")
    if(len(pedir_numero)<=4):break

numero = constanteKaprekar(int(pedir_numero))


    
    
    
    
    
    
