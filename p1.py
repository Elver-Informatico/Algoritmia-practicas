import time # Para la función time_measure. Entender código dado.
import matplotlib.pyplot as plt # Para imprimir gráficas. Entender código dado.
import random # Puede usarse random.randint(n, m) para generar listas aleatorias de enteros en las funciones dataprep.
import numpy as np

# I.A.1 Medición de tiempos de ejecución
def time_measure(f, dataprep, Nlist, Nrep=1000, Nstat=100):
    """Mide la media y varianza del tiempo de ejecución de la función f
    para cada tamaño n presente en Nlist.
    """
    res = []
    for n in Nlist:
        partial = []
        for _ in range(Nstat):
            data = dataprep(n)
            t1 = time.perf_counter()
            for _ in range(Nrep):
                f(data)
            t2 = time.perf_counter()
            t_elem = (t2 - t1) / float(Nrep)
            partial.append(t_elem)

        mean_val = sum(partial) / float(Nstat)
        var_val = sum((x - mean_val) ** 2 for x in partial) / float(Nstat)
        res.append((mean_val, var_val))
    return res

def dataprep_sum_pair_hit(n):
    """Genera un caso donde SÍ existe un par que suma target.
    Devuelve una tupla (lista, target)
    """
    lst = [random.randint(0, 80) for _ in range(n-2)]
    lst.append(30)
    lst.append(50)
    random.shuffle(lst)
    target = 80
    return (lst, target)

def dataprep_sum_pair_miss(n):
    """Genera un caso donde NO existe ningún par (Caso peor).
    Devuelve una tupla (lista, target)
    """
    lst = [random.randrange(0, 20, 2) for _ in range(n)] # numeros pares
    target = random.randrange(0, 40, 2) + 1              # numero impar
    return (lst, target)


def dataprep_rle(n):
    """Genera una lista con rachas repetidas de dimensión n.
    Devuelve una lista.
    """
    lst = [random.randint(0, 2) for _ in range(n)]
    return lst
    

# I.A.2 Búsqueda de duplicados manteniendo orden de aparición
def find_duplicates(lst):
    list_set = set()
    duplicates = []

    for element in lst:
        if element in list_set and element not in duplicates:
            duplicates.append(element)
        else:
            list_set.add(element)

    return duplicates

# I.A.3 Búsqueda de par que suma target con complejidad O(n)
def has_sum_pair(par):
    """Dada una tupla (lst, target), devuelve True si existen dos elementos
    distintos en lst que sumen target; de lo contrario devuelve False.
    """
    lst, target = par

    checked = set()

    for n in lst:
        num = target - n
        if num in checked:
            return True
        checked.add(n)

    return False

# I.B.1 RLE Naive / Ingenuo
def rle_encode_naive(lst):
    """Codificación RLE utilizando operador + concatenador de listas."""
    resultado = []
    if len(lst) == 0:
        return resultado

    elem_actual = lst[0]
    contador = 1

    for i in range (1, len(lst)):
        if lst[i] == elem_actual:
            contador +=1
        else:
            resultado =resultado + [(elem_actual,contador)]

            elem_actual = lst[i]
            contador = 1

    resultado = resultado + [(elem_actual,contador)]
    return resultado


# I.B.2 RLE Optimized / Óptimo
def rle_encode_optimized(lst):
    """Codificación RLE optimizada usando append in-place."""
    current_elem = lst[0]
    lst_out = []
    count = 1

    for elem in lst[1:]:
        if elem == current_elem:
            count += 1
        else:
            lst_out.append([current_elem, count])
            current_elem = elem
            count = 1

    lst_out.append([current_elem, count])
        
    return lst_out


# Función auxiliar para generar una gráfica de una serie de datos.
def plot_single_curve(
    x,
    y,
    title="Gráfica de Datos",
    xlabel="Eje X",
    ylabel="Eje Y",
    label=None,
    style="o-",
    color="b",
    grid=True,
    filename=None,
    figsize=(8, 5),
):
    """Genera y muestra/guarda una gráfica limpia para una única serie de datos."""
    plt.figure(figsize=figsize)  # Crea la figura con el tamaño indicado

    # Dibuja la curva
    plt.plot(x, y, style, color=color, label=label)

    # Personalización básica de ejes y título
    plt.title(title)  # Asigna el título
    plt.xlabel(xlabel)  # Etiqueta X
    plt.ylabel(ylabel)  # Etiqueta Y

    if grid:
        plt.grid(True, linestyle="--", alpha=0.6)

    if label:
        plt.legend(
            loc="best"
        )  # Muestra la leyenda si se definió una etiqueta

    plt.tight_layout()

    # Guarda la gráfica en un fichero si se especifica un nombre
    if filename:
        plt.savefig(
            filename, format=filename.split(".")[-1], dpi=300
        )  #

    plt.show()  # Muestra la figura

def init_cd(n: int)-> np.ndarray:
# que devuelve un array con valores -1 en las posiciones {0, 1, ..., n-1}.
    pass

def union(rep_1: int, rep_2: int, p_cd: np.ndarray)-> int:
# que devuelve el representante del conjunto obtenido como la unión por rangos de los representados 
# por los índicesrep_1, rep_2 en el CD almacenado en el array p_cd.
    pass

def find(ind: int, p_cd: np.ndarray)-> int:
# que devuelve el representante del índice ind en el CD almacenado en p_cd realizando compresión de caminos.
    pass

def cd_2_dict(p_cd: np.ndarray)-> dict:
# que reciba un CD en el array p_cd y devuelva un diccionario cuyas claves sean los representantes de los
# subconjuntos del CD y donde el valor de la clave u del dict sea una lista con los miembros del subconjunto
# representado por u , incluyendo, por supuesto el propio u
    pass

def ccs(n: int, l: list)-> dict:
# que nos devuelva las componentes conexas de un tal grafo. Para ello la función inicializará un CD vacío, 
# examinará las ramas del grafo contenidas en la lista l y si los dos nodos de la rama pertenecen a subconjuntos distintos, 
# unirá estos. Cuando se procesen todas las ramas la función convertirá la tabla que contenga el CD en un dict 
# y devolverá éste
    pass