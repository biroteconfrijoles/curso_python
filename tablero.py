import random
def dibuja_tablero(simbolos:dict):

    print(f'''
        {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
        ---------
        {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
        ---------
        {simbolos['7']} | {simbolos['8']} | {simbolos['9']}         
        ''')
 

if __name__=='__main__':
   numeros = [str(i) for i in range(1,10)]
   dsimbolos = {x:x for x in numeros}
   dibuja_tablero(dsimbolos)
   x = random.choice(numeros)
   dsimbolos[x]='x'
   dibuja_tablero(dsimbolos)
   o = random.choice(numeros)
   numeros.remove(o)
   dsimbolos[o] = 'o'
   dibuja_tablero(dsimbolos)
   print(numeros)