# Con este concepto de parámetros predeterminados en mente, el objetivo de esta asignación es escribir 
    # una sola función, randInt() que tome hasta 2 argumentos.
# Si no se proporcionan argumentos, la función debería devolver un entero aleatorio entre 0 y 100.
# Si solo se proporciona un número máximo, la función debe devolver un número entero aleatorio entre 0 y el número máximo.
# Si solo se proporciona un número mínimo, la función debe devolver un número entero aleatorio entre el número mínimo y 100
# Si se proporcionan un número mínimo y máximo, la función debe devolver un número entero aleatorio entre esos 2 valores.
import random
def randInt(min=0, max=100):
    if min > max:
        return False
    if max  < 0 or min < 0:
        return False
    else:
        #num = random.random()*max +min # Estoy indicando que el rango va desde los 50 a los 150 en el 2do print
        num = random.random()*(max-min) +min # En este caso, el rango va desde los 50 a los 100 (sumo (100-50)+50)
        #if num > max:                        # para el 5to print, el rango va desde 90 a 98 ((98-90) --> (8)+90)
        #   num = (random.random()*max +min) - min
        #if num < min:
        #   num += min ???
    ## Al asignar el mínimo en los parámetros, se está sumando 100 + 50 y el numero aleatorio estaría en un rango 
    ## desde los 50 a los 150, por lo que se le indica que debe restarle el mínimo ingresado si el número aleatorio es 
    ## mayor que el máximo permitido, así este siempre estará dentro del rango
    
    # Depuración 2: Al sumarle el número mínimo, a veces el valor correspondía a un número menor al mínimo,
    # pues siempre estoy restando, se intentó depurar sumando al mínimo, pero posteriormente se optó por modificar 
    # parámetros de random.random para que el rango siempre sea el correcto
    return round(num)
print("#1 Número entre 0 y 100: ",randInt())# debería imprimir un número aleatorio entre 0 a 100
print("#2 Número entre 0 y 50: ",randInt(max=50))# debería imprimir un número aleatorio entre 0 a 50
print("#3 Número entre 50 y 100: ",randInt(min=50))# debería imprimir un número aleatorio entre 50 a 100
print("#4 Número entre 50 y 500: ",randInt(min=50, max=500)) # debería imprimir un número aleatorio entre 50 y 500
print("#5 Rango acotado: ",randInt(95,98))
print("#6 Solo un parámetro, el mínimo: ",randInt(90))
print("#6 Mínimo mayor que máximo, devuelve falso: ",randInt(31,30))
print("#7 Parámetro/s negativo/s, devuelve falso: ",randInt(-30,31))

# Crear una función que juegue al Loto
    # Instrucciones, la función debe elegir al azar 6 números desde al 1 al 41 y devolverlos en una lista ordenada.
def loto (min=1, max=41): 
    lista=[]
    if min > max:
        return False
    if max  < 0 or min < 0:
        return False
    else:
        for i in range (6): #Creará 6 elementos y los introducirá en "lista"
            num = round(random.random()*(max-min) +min)
            lista.append(num)
    lista.sort() # Se ordena la lista, pero qué pasa si me entrega números repetidos?
    for j in range (len(lista)): # Otro ciclo for en el que se compara el número actual con el anterior, si son iguales
        if lista[j] == lista[j-1]: # vuelve a sortear un nuevo número
            lista[j] = round(random.random()*(max-min) +min)
    lista.sort() # Se vuelve a ordenar la lista, ya que el nuevo numero probablemente no quedará dentro del orden anterior
    return lista
print(loto())
# Invocando la función previamente creada
def loto1 ():
    num=[]
    for i in range (6):
        i = randInt(1,41)
        num.append(i)
    num.sort()
    for i in range (len(num)):
        if num[i] == num[i-1]:
            num[i] = randInt(1,41)
    num.sort()
    return num
print(loto1())