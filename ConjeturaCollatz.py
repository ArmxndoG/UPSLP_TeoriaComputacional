#coding=utf-8
def conjeturaCollatz(numero):
    
    if numero % 2 == 0: 
        numero = numero/2
    else: 
        numero = (3*numero) + 1
        
    print(numero)
    if numero != 1: #Volver a llamar la funcion hasta que el numero sea 1
        conjeturaCollatz(numero)
    else:
        return numero
        
numero_entero = int(input("Digita un numero entero: "))
serie = conjeturaCollatz(numero_entero)




    


    
