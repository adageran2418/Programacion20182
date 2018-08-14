print("Bienvenido, vamos a calcular su ingreso neto del salario \n")

salario1 = float(input("Ingrese por favor el valor de su salario numero 1: \n"))

retefuente1 = float(input("Ingrese el valor de la tasa de retencion en la fuente: \n"))

salario_neto_1 =  salario1 * (100 - retefuente1) / 100

salario2 = int(input("Ingrese por favor el valor de su salario numero 2: \n"))

retefuente2 = int(input("Ingrese el valor de la tasa de retencion en la fuente: \n"))

salario_neto_2 =  salario2 * (100 - retefuente2) / 100


salario3 = int(input("Ingrese por favor el valor de su salario numero 3: \n"))

retefuente3 = int(input("Ingrese el valor de la tasa de retencion en la fuente: \n"))

salario_neto_3 =  salario3 * (100 - retefuente3) / 100


print("Su salario neto es: ", salario_neto_1+salario_neto_2+salario_neto_3 )


