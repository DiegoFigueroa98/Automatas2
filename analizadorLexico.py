#------------------------------------------------------------------
# Nombre: analizadorLexico.py
# Objetivo: crear un analizador léxico para printf
# Autor: Diego Aaron Figueroa Campos
# Fecha: 04/07/2019
#------------------------------------------------------------------

import ply.lex as lex

# resultado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
    'PRINTF',
)
tokens = reservada + (
    'PARENTESIS_APERTURA',
    'PARENTESIS_CERRADURA',
    'CADENA',
    'IDENTIFICADOR',
    'PUNTO_COMA',
)

# Reglas de Expresiones Regulares para token de Contexto simple

t_PUNTO_COMA = r';'
t_PARENTESIS_APERTURA = r'\('
t_PARENTESIS_CERRADURA = r'\)'

def t_PRINTF(t):
    r'printf'
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_CADENA(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_error(t):
    print("\nCaracter no valido :"+t.value[0])
    t.lexer.skip(1)
   
# Prueba de ingreso
def main():
    print("*** Análisis léxico de la sentencia printf ***")
    # instanciamos el analizador lexico
    analizador = lex.lex()
    while True:
        data = input("\nIngrese la sentencia a analizar: ")
        analizador.input(data)

        while True:
            tok = analizador.token()
            if not tok:
                break
            print("Token--> ",tok)

# Inicia programa principal
if __name__ == "__main__" :
    main()