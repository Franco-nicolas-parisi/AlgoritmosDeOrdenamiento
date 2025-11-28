# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar) # arranca en NONE Porque al principio del paso, todavía NO estamos desplazando nada.

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento (la primer posicion ya arranca ordenada). I es el elemento que quiero ordenar
    j = None

def step():
    global items, n, i, j

    # - Si i >= n: devolver {"done": True}.
    if i >= n:
        return{'done': True} #NO SE PUEDE PONER AL FINAL ESTE CONDICIONAL, PORQUE LOS DEMAS RETURN LO ANULARIAN ANTES.

    
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    if j == None:
        j = i #(porque si j fuera 0, no hay nada a la izquierda para comparar)
        return{"a": j-1, "b": j, "swap": False, "done": False} #estoy viendo estos valores, pero que aun no hice ningun intercambio”
    
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.

    if j > 0 and items[j-1] > items[j]: #Si j es mayor a 0, es porque hay un elemento a la izquierda para poder comparar.
        aux = items[ j - 1]
        items[ j - 1] = items[j]
        items[j] = aux
        j = j - 1 #Movemos j a una posicion mas a la izquierda
        return{'a': j, 'b': j + 1, 'swap': True, 'done': False} #a y b contiene el valor de las posiciones en ese momento. Le aviso al visualiador que cambiaron.
        # COMO A J SE LE RESTA UNO ANTES DEL RETURN, ES NECESARIO SUMARLE +1 CUANDO SE LE DICE AL VISUALIZADOR QUE VALORES ACABAMOS DE COMPARAR PARA QUE VEA AL CORRECTO. 

    # - Si ya no hay que desplazar: avanzar i y setear j=None.
    
    i = i + 1
    j = None

    return {"a": 0, "b": 0, "swap": False, "done": False} #NO se compara nada, por eso las variables estan con valor 0. Y aun debe seguir el algoritmo, por ello dice done False.
    #Es necesario retornar algo porque mas que este vacio, sino el visualizador no sirve.


   