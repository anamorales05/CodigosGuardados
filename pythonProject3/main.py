textoEntrada = """(
    <
    [precio] = 45.09,
    [descripcion] = "adios mundo",
    [disponible] = false
    >,
    <
    [precio] = 4.3,
    [descripcion] = "adios mundo",
    [disponible] = false
    >,
    <
    [precio] = -56.4,
    [descripcion] =  "este es el otro ejemplo las cadenas pueden ser muy largas",
    [disponible] = false
    >,
    <
    [precio] = 100,
    [descripcion] =  "valio madres",
    [disponible] = true
    >
)"""
textoEntrada2 = """(
    <
        [atributo_numerico] = 45.09,
        [atributo_cadena] = "hola mundo",
        [atributo_booleano] = true
    >,
    <
        [atributo_numerico] = 4,
        [atributo_cadena] = "adios mundo",
        [atributo_booleano] = false
    >,
    <
        [atributo_numerico] = -56.4,
        [atributo_cadena] = "este es otro ejemplo las cadenas pueden ser muy largas",
        [atributo_booleano] = false
    >
)"""
f = open('D:\Descargas\Archivo1.aon', 'r')
ArchivoTexto = f.read()

texto2 = textoEntrada.replace("", "")
text3 = texto2.replace("\n", "")
text4 = text3.replace(" ", "")
print(text4)


def AFD(cadena):
    palabra = ""
    palabra2 = ""
    numero = ''
    estado = 0
    j = 0;
    diccionario = {}
    total = []
    for i in range(len(textoEntrada)):
        if estado == 0:
            if cadena[i] == "(":
                print(cadena[i] + " =Token_parentesis")
                estado = 1
        if estado == 1:
            if cadena[i] == "<":
                print(cadena[i] + " =token_menorque")
                estado = 2
        if estado == 2:
            if cadena[i] == "[":
                print(cadena[i] + " =token_corchete")
                estado = 3
        if estado == 3:
            if cadena[i].isalpha() or cadena[i] == "_":
                palabra = palabra + cadena[i]
            elif cadena[i] == "]":
                print(palabra + " =token_palabra")
                print(cadena[i] + " =token_corchete")
                estado = 4
        if estado == 4:
            if cadena[i] == "=":
                print(cadena[i] + " =token_igual")
                estado = 5
        if estado == 5:
            if cadena[i].isdigit() or cadena[i] == "." or cadena[i] == "-":
                numero = numero + cadena[i]
            elif cadena[i].isalpha() :
                palabra2 = palabra2 + cadena[i]
            elif cadena[i] == ",":
                if numero != "":
                    print(numero + " =token_numero")
                    print(cadena[i] + " =token_coma")
                    diccionario[palabra] = numero
                    numero = ''
                    palabra = ""
                    estado = 2
                elif palabra2 != "":
                    print(palabra2 + " =token_palabra")
                    diccionario[palabra] = palabra2
                    print(cadena[i] + " =token_coma")
                    palabra2 = ''
                    palabra = ""
                    estado = 2
            elif cadena[i] == ">":
                print(palabra2 + ' =token_palabra')
                diccionario[palabra] = palabra2
                palabra2 = ''
                palabra = ""
                print(cadena[i] + " =token_mayorque")
                estado = 6
                total.append(diccionario)
                diccionario = {}
        if estado == 6:
            if cadena[i] == ",":
                print(cadena[i] + " =token_coma")
                estado = 1
            elif cadena[i] == ")":
                print(cadena[i] + " =token_parentesis")

                print(total)
                f.close()


try:
    AFD(text4)

except:
    print("")
