def calcular_y (x,m,b):
    '''
        calcula "y" de acuerdo a la pendiente "m y el punto de interseccion en y "b" retorna el valor de "y" 
    '''
    return (m*x)+b


def test_linea():
    '''comprobamos calcular (y)
    '''
    y = calcular_y(0,2,3)
    return y

if __name__ == "__main__":
    x = 0
    m = 3
    b = 2
    y = calcular_y(x,m,b)
    print(y)

    if y==2:
        print("Prueba exitosa")
    else:
        print("Prueba fallida")
