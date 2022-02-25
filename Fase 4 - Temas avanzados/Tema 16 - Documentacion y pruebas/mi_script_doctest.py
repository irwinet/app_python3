# Doctest: Pruebas en la documentacion

def suma(a,b):
    """
    La funcion suma(a,b) recibe dos parametros a y b.
    Devuelve la suma de ambos
    
    Pueden ser numeros:
    >>> suma(5,10)
    15
    
    >>> suma(0,0)
    0

    >>> suma(-5,7)
    2

    Cadenas de texto:
    >>> suma('aa','bb')    
    'aabb'

    o listas:
    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> suma(a,b)
    [1, 2, 3, 4, 5, 6]

    Sumar distintos tipos:

    >>> suma(10,"hola")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

    """
    return a+b


# def palindromo(palabra):
#     """
#     La funcion palindromo(palabra) recibe una palabra
#     Si la palabra es un palindromo devuelve True, sino False

#     Un palindromo es una palabra o frase que se lee igual
#     tanto de izquierda a derecha como de derecha a izquierda

#     >>> palindromo("radar")
#     True

#     >>> palindromo("somos")
#     True

#     >>> palindromo("holah")
#     False

#     >>> palindromo("Ana")
#     True

#     >>> palindromo("Atar a la rata")
#     True

#     """
#     if palabra.lower().replace(" ","") == palabra[::-1].lower().replace(" ",""):
#         return True
#     else:
#         return False


# def doblar(lista):
#     """
#     Dobla el valor de los elementos de una lista

#     >>> l = [1, 2, 3, 4, 5]
#     >>> doblar(l)
#     [2, 4, 6, 8, 10]

#     >>> l = []
#     >>> for i in range(10):
#     ...     l.append(i)
#     >>> doblar(l)
#     [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#     """
#     return [n*2 for n in lista]

if __name__ == "__main__":
    import doctest
    doctest.testmod()


# python .\mi_script.py -v