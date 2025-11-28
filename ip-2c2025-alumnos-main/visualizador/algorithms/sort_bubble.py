# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0 #pasada actua
j = 0 #posicion dentro de la pasada

def init(vals):
    global items, n, i, j 
    items = list(vals) #guarda la lista
    n = len(items)
    i = 0 #numero de pasada
    j = 0 #posicion de comparacion

def step():
    global items, n, i, j

    if i >= n - 1:
        return{"done": True}    # Cuando no queden pasos, devolvé {"done": True}. 
    #NO SE PUEDE PONER AL FINAL ESTE CONDICIONAL, PORQUE LOS DEMAS RETURN LO ANULARIAN ANTES.

    # 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).

    a = j
    b = j + 1

    # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.

    swap = False

    if items[a] > items[b]:
        aux = items[a]
        items[a] = items[b]
        items[b] = aux
        swap = True

    # 3) Avanzar punteros (preparar el próximo paso).

    j = j + 1

    # Si llegamos al final de la pasada, reiniciar j y avanzar la pasada i

    if j >= n - 1 - i: #Le resta las posiciones que ya están ordenadas al final, i se usa para ignorar los valores que quedaron al final de la lista en la actual pasada. 
        j = 0
        i = i + 1
    
    # 4) Devolver {"a": a, "b": b, "swap": swap, "done": False}.

    return {"a": a, "b": b, "swap": swap, "done": False}
