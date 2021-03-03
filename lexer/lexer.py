# coding: utf-8
'''
Lenguaje BASIC Dartmouth
------------------------

Palabras Reservadas (keywords)

DEF — define funciones de una sola línea
DIM — define el tamaño de los arreglos
END — define el final del programa
STOP — detiene un programa antes del final
FOR/TO/STEP — define los bucles
NEXT — marca el final de los bucles
GOSUB — transfiere control a subrutinas simples
RETURN — retorna el control desde subrutinas simples
GOTO — transfiere el control a otra sentencia
IF/THEN — toma de decisiones
LET/= — asigna los resultados de las fórmulas a una variable
PRINT — salida de resultados
DATA — almacena datos estáticos dentro del programa
READ — entrada de datos almacenados en sentencias DATA
REM — comentario

También implementó variables numéricas y aritmética de punto flotante.
Los nombres de variables fueron limitados de A a Z, A0 a A9, B0 a B9, ... , Z0 a Z9,
dando un máximo de 286 distintas variables posibles.
Los nombres de matrices estaban restringidos a solamente de A a Z. Las matrices
no necesitaban ser definidas, pero en ausencia de una declaración DIM tenían por
defecto 10 elementos, a los que se accedía con un índice desde 1 a 10.

Lista de operadores

Operadores aritméticos	       Operadores relacionales/lógicos
-	Negación (op. unario)	    =	Igual a
+	Adición	                    <>	No igual a
-	Sustracción (op. binario)   <	Menor que
*	Multiplicación	            <=	Menor o igual a
/	División	            >	Mayor que
^	Exponenciación	            >=	Mayor o igual a

Operadores de agrupamiento
( )	Agrupamiento

Lista de funciones
ABS -- Valor absoluto
INT -- Parte entera de un número
RND -- número real al azar entre 0 y 1
SIN -- Seno (argumento en radianes)
COS -- Coseno (argumento en radianes)
TAN -- Tangente (argumento en radianes)
ATN -- Arco tangente (resultado en radianes)
EXP -- Exponencial (e^x)
LOG -- Logaritmo natural
SQR -- raíz cuadrada
'''

from errors import *
import sly

class Lexer(sly.Lexer):
    tokens = {
        # palabras resevadas
        LET, READ, DATA, PRINT, GOTO, IF,
        THEN, FOR, NEXT, TO, STEP, END,
        STOP, DEF, GOSUB, DIM, REM, RETURN,
        RUN, LIST, NEW,
        # matematicas
        ABS, INT, RND, SIN, COS, TAN, ATN,
        EXP, LOG, SQR,
        # operadores de relacion
        LT, LE, GT, GE, NE, EQ,
        # Identificadores
        ID,
        # constantes
        LINENO, NUMBER, STRING,
    }

    # OPERADORES
    literals = '+-*/^()=:,;'

    # IGNORA
    ignore = r' \s+'
    ignore_space = r'\s+'
    ignore_newline = r'\n+'

    # COMENTARIO
    REM = r'REM .*'

    # PALABRAS RESERVADAS
    ID = r'[a-zA-Z][a-zA-Z\-0-9]*'
    ID['LET']    = LET
    ID['READ']   = READ
    ID['DATA']   = DATA
    ID['PRINT']  = PRINT
    ID['GOTO']   = GOTO
    ID['IF']     = IF
    ID['THEN']   = THEN
    ID['FOR']    = FOR
    ID['NEXT']   = NEXT
    ID['TO']     = TO
    ID['STEP']   = STEP
    ID['END']    = END
    ID['STOP']   = STOP
    ID['DEF']    = DEF
    ID['GOSUB']  = GOSUB
    ID['DIM']    = DIM
    ID['RETURN'] = RETURN
    ID['RUN']    = RUN
    ID['LIST']   = LIST
    ID['NEW']    = NEW
    ID['ABS']    = ABS
    ID['INT']    = INT
    ID['RND']    = RND
    ID['SIN']    = SIN
    ID['COS']    = COS
    ID['TAN']    = TAN
    ID['ATN']    = ATN
    ID['EXP']    = EXP
    ID['LOG']    = LOG
    ID['SQR']    = SQR

    # OPERADORES
    LE = r"<="
    LT = r"<"
    EQ = r"=="
    GE = r">="
    GT = r">"
    NE = r"<>"
    LINENO = r'> ^\d+'

    def ignore_newline(self,t):
        self.lineno += t.value.count("\n")

    #r'(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)'
    @_(r'-?(\d+\.?\d*|\d*\.\d+)(E(-+)?\d+)?')
    #@_(r'\d+(\.\d+)?')
    def NUMBER(self,t):
        try:
            t.value = int(t.value)
        except ValueError:
            t.value = float(t.value)
        return t

    #STRING = r'"[^"]*"?'
    #@_(r"'[^']*'")
    @_(r"'[^']*'", r'"[^"]"')
    def STRING(self,t):
        return t

    def error(self,t):
        error('Caracter ilegal %s' % t.value[0], t.lineno)
        self.index += 1

