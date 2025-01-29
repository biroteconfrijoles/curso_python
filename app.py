'''
    archivo prinçipal de linea
'''
import argparse
from sys import float_repr_style
import funciones
import parser

def main(m:float, b:float):
    '''
    funcion principal que calcula las coordenadas de una linea recta recibimos m y b regresa nada
    '''
    X = [x/10.0 for x in range(10,101,5)]
    Y = [funciones.calcular_y(x,m,b) for x in X]
    print(X)
    print(Y)
    coordenadas = list(zip(X,Y))
    print(coordenadas)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='calcula las coordenadas de una linea recta')
    parser.add_argument('-m', type=float,
    help='pendiente de la linea',default=2.0)
    parser.add_argument('-b', type=float,
    help='interseccion en y',default=3.0)  
    args=parser.parse_args()
    main(args.m,args.b)




    #main(m=2,b=3)
