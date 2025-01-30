import random
def dibuja_tablero(simbolos:dict):

    print(f'''
        {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
        ---------
        {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
        ---------
        {simbolos['7']} | {simbolos['8']} | {simbolos['9']}         
        ''')
 
    
def ia(simbolos:dict):
    '''estrategia de la computadora'''

    ocupado = True
    while ocupado is True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x]= 'O'
            ocupado = False

def usuario(simbolos:dict):
    '''estrategia del usario'''

    ocupado = True 
    lista_numeros = [str(i) for i in range(1,10)] #del 1 al 9
    while ocupado is True:
        x = input("elija un numero del 1 al 9")
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'X'
            ocupado = False
        else:
            print('esa casilla ya esta ocupada')



    numeros = [str(i) for i in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    dibuja_tablero(dsimbolos)

if __name__=='__main__':
   numeros = [str(i) for i in range(1,10)]
   dsimbolos = {x:x for x in numeros}
   dibuja_tablero(dsimbolos)
   ia(dsimbolos)
   dibuja_tablero(dsimbolos)
   usuario(dsimbolos)
   dibuja_tablero(dsimbolos)

   ''' 
   x = random.choice(numeros)
   dsimbolos[x]='x'
   dibuja_tablero(dsimbolos)
   o = random.choice(numeros)
   numeros.remove(o)
   dsimbolos[o] = 'o'
   dibuja_tablero(dsimbolos)
   print(numeros)
   '''  
