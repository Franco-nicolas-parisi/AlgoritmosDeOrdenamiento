# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # donde inicia la parte desordenada de la lista
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0 #se inicia al principio # es la posición donde quiero colocar el número más chico de esta pasada.
    j = i + 1 # arranca desde el siguiente
    min_idx = i #se supone que el primer valor es el mas chico
    fase = "buscar" #para arrancar buscando el minimo y la cambiamos a swap cuando sea necesaro intercambiar

def step():
    global items, n, i, j, min_idx, fase

    if i >= n - 1:
        return {"done": True}

    # - Fase "buscar":  
    if fase == 'buscar':
        if j < n:
            if items[j] < items[min_idx]: #comparar j con min_idx, 
                min_idx = j #actualizar min_idx,
            j = j + 1 #avanzar j.

    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
            return{"a": min_idx, "b": j-1, "swap": False, "done": False}
        
        else:
            fase = 'swap'
            return {"a": i, "b": min_idx, "swap": False, "done": False}
        
    #   Al terminar el barrido, pasar a fase "swap".

    if fase == 'swap':  # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
        a = i
        b = min_idx # Tuve que agregar estas variables porque no se me ocurrio como retornar los valores necesario de i e min_idx en el return porque antes los modificaba en el if y luego fuera de el.

        swap = False
        if min_idx != i:
            aux = items[i]
            items[i] = items[min_idx]
            items[min_idx] = aux
            swap = True

        #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".

        i = i + 1 #sumamos para seguir con la siguiente pasada
        j = i + 1
        min_idx = i
        fase = 'buscar'

        return {"a": a, "b": b, "swap": swap, "done": False}




