# Definir una funciòn calcular salario neto

def salario_neto (salario, tasa):

    '''
    Calcula el salario neto descontando la retenciòn en la fuente

    >>> salario_neto(100,2)
    98.0
    >>> salario_neto(200,10)
    180.0
    >>> salario_neto(500,10)
    450.0

    :param salario:  el salario de la persona
    :param tasa:  la retenciòn a ese salario
    :return: salario neto de  la persona
    '''

    salario_n = salario * (100 - tasa)/100
    return salario_n

#llamar la funciòn tres veces

salario1 = salario_neto(float(input("Digite su salario \n")),
                        float(input("Ingrese su tasa")))
salario2 = salario_neto(float(input("Digite su salario \n")),
                        float(input("Ingrese su tasa")))
salario3 = salario_neto(float(input("Digite su salario \n")),
                        float(input("Ingrese su tasa")))

#Calcular el salario neto total

salario_total = salario1+salario2+salario3

print("su salario neto total es: ", salario_total)


