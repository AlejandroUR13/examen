def burbuja(array,n): #definimos nuestra funcion con el arreglo que usaremos 
#Ordenamiento burbuja de manera iterativa    
#Para que el algoritmo funcione de dicha manera por favor comente el algoritmo de abajo
    n=len(array) #calcula la longitud de array y la guarda en la variable n
    for i in range (n-1): #Con el for controlamos la cantidad de veces que pasa por el arreglo 
        for j in range (0, n-1-i): #Aqui es donde se itera por cada elemento del arreglo excepto por aquellos que ya fueron ordenados
            if array[j]>array[j+1]: #verifica que el elemento actual en [j] sea mayor que el siguiebte en [j+1] de ser asi se intercambian los elementos 
                array[j], array[j+1]=array[j+1], array[j] #luego de que el bucle de adentro complete una vuelta el elemento mas genade del arreglo se encuentra hasta el final termonara
f=[5,3,8,4,6] #Hola yo soy el arreglo 
burbuja(f) #Hola yo mando a llamar la funcion para ordenar el arreglo
print('La lista de manera ordenada es:\t', f)*/ #Hola yo me dirijo a la termonal de salida con el arreglo ordenado

#Ordenamiento burbuja de manera recursiva
#Para que el algoritmo funcione de dicha manera por favor comente el algoritmo de arriba
    if n<= 1: #Esta condicion dicta que si el arreglo es menor o igual a 1 
        return# Retornara sin hacer nada ya que solamnete sera un arreglo de un elemento o cero elementos
    for i in range (n-1): #Con el for controlamos la cantidad de veces que pasa por el arreglo 
        array[i], array[i+1]=array[i+1], array[i] # Se hace el intercambio de valores entre [i] y [i+1] si se necesita obtener los elementos
    burbuja(array, n-1) # Mandamos llamar la funcion con n-1 para que no considere contar los elementos ordenados 
f=[5,3,8,4,6] #Hola yo soy el arreglo 
print('La lista original es:\t',f) #Yo imprimo el arreglo sin ordenar
burbuja(f, len(f)) #Se manda a llamar la funcion completa para que termine de ordenar todo el arreglo 
print('La lista ordenada es:\t', f) #Yo imprimo el arreglo ya ordenado 