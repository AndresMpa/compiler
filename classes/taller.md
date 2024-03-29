# Taller

Completar los siguientes ejercicios

### 1.1) Sea la gramática

```
S -> (S) S | e
```

#### Primer conjunto de elementos

Conjunto de elementos

```
✔ S' -> .S
S' -> S.

✔ S -> .(S) S
S -> (.S) S
S -> (S.) S
S -> (S) .S
S -> (S) S.
```

- AFD LR(0) correspondiente a esta gramática
- Muestre las acciones de análisis sintáctico para la entrada: ((())(()()))

![Punto_1_AFD_LR(0)](<./Taller-AFD%20LR(0)%20-%20Punto%201.png>)

| #   | Pila                       | Cadena        | Acciones          |
| --- | -------------------------- | ------------- | ----------------- |
| 1   | $0                         | ((())(()()))$ | Desplazar         |
| 2   | $0(2                       | (())(()()))$  | Desplazar         |
| 3   | $0(2(2                     | ())(()()))$   | Desplazar         |
| 4   | $0(2(2(2                   | ))(()()))$    | Reducir S -> e    |
| 5   | $0(2(2(2S3                 | ))(()()))$    | Desplazar         |
| 6   | $0(2(2(2S3)4               | )(()()))$     | Reducir S -> e    |
| 7   | $0(2(2(2S3)4S5             | )(()()))$     | Reducir S -> (S)S |
| 8   | $0(2(2S3                   | )(()()))$     | Desplazar         |
| 9   | $0(2(2S3)4                 | (()()))$      | Desplazar         |
| 10  | $0(2(2S3)4(2               | ()()))$       | Desplazar         |
| 11  | $0(2(2S3)4(2(2             | )()))$        | Reducir S -> e    |
| 12  | $0(2(2S3)4(2(2S3           | )()))$        | Desplazar         |
| 13  | $0(2(2S3)4(2(2S3)4         | ()))$         | Desplazar         |
| 14  | $0(2(2S3)4(2(2S3)4(2       | )))$          | Reducir S -> e    |
| 15  | $0(2(2S3)4(2(2S3)4(2S3     | )))$          | Desplazar         |
| 16  | $0(2(2S3)4(2(2S3)4(2S3)4   | ))$           | Reducir S -> e    |
| 17  | $0(2(2S3)4(2(2S3)4(2S3)4S5 | ))$           | Reducir S -> (S)S |
| 18  | $0(2(2S3)4(2(2S3)4S5       | ))$           | Reducir S -> (S)S |
| 19  | $0(2(2S3)4(2(2S3           | ))$           | Desplazar         |
| 20  | $0(2(2S3)4(2(2S3)4S5       | )$            | Reducir S -> e    |
| 21  | $0(2(2S3)4(2S3             | )$            | Desplazar         |
| 22  | $0(2(2S3)4(2S3)4           | )$            | Reducir S -> e    |
| 23  | $0(2(2S3)4(2S3)4S          | )$            | Reducir S -> (S)  |
| 24  | $0(2(2S3)4S5               | )$            | Reducir S -> (S)  |
| 25  | $0(2S3                     | )$            | Desplazar         |
| 26  | $0(2S3)4                   | $             | Reducir S -> e    |
| 27  | $0(2S3)4S5                 | $             | Reducir S -> (S)S |
| 28  | $0S1                       | $             | Aceptar           |

### 2.1) Sea la gramática

```
E -> E + T | E - T | T
T -> T * F | T / F | F
F -> (E) | id | num
```

- Contruya el AFD de elementos LR(0) correspondiente
- Muestre las acciones de análisis sintactico para la entrada: id + id \* id + ( id + id )

### 3.1) Considerar la siguiente gramática

```
lexp -> atom | list
atom -> numero | identificador
list -> ( lexp-seq )
lexp-seq -> lexp-seq lexp | lexp
```

- Muestre las acciones del analizador sintactico descendente para las cadenas de entrada: (a(b(2))(c(4)))

#### Eliminando la recursión por la izquierda de la gramatica 3.1

Las reglasa que tienen recursión por la izquierda de la primera gramatica son:

```
lexp-seq -> lexp-seq lexp | lexp
```

Para eliminar la recursión por la izquierda se usa la forma general

```
A -> βA'
A' -> cA' | ε
```

| lexp-seq | ->  | lexp-seq | lexp | lexp |
| -------- | --- | -------- | ---- | ---- |
| A        | ->  | A        | c    | β    |

Para lo cual respectivamente se tiene que

- `A` corresponde con `lexp-seq`

- `c` corresponde con `lexp`

- `β` corresponde con `lexp`

Aplicando la forma

```
A -> βA'
A' -> cA' | ε
```

La primera regla se re ordena como:

```
lexp-sec -> lexp lexp-sec'
lexp-sec' -> lexp lexp-sec' | ε
```

La gramatica ajustada del punto 3.1 sería:

```
lexp-sec -> lexp lexp-sec'
lexp-sec' -> lexp lexp-sec' | ε
lexp -> atom | list
atom -> numero | identificador
list -> ( lexp-sec )
```

Analizador sintactico descendente

| #   | Pila            | Cadena           | Acciones                           |
| --- | --------------- | ---------------- | ---------------------------------- |
| 1   | $lexp-sec       | (a(b(2))(c(4)))$ | Derivar lexp-sec -> lexp lexp-sec' |
| 2   | $lexp lexp-sec' | (a(b(2))(c(4)))$ | Derivar lexp-sec' -> ε             |
| 3   | $lexp           | (a(b(2))(c(4)))$ | Derivar lexp -> list               |

### 4.1) Considerar la siguiente gramática

```
exp -> exp + term | exp - term | term
term -> term * factor | exp / factor | factor
factor -> (exp) | id | num
```

- Construya la tabla de análisis sintactico
- Muestre las acciones del analizador sintactico descendente para la cadena de entrada: 3 - 5 ( 3 + 4 \* 3 ) + 6
- ¿La gramatica resultante es LL? Justifique su respuesta

#### Eliminando la recursividad por la izquierda de la gramatica 4.1

Las reglasa que tienen recursión por la izquierda de la primera gramatica son:

```
exp -> exp + term | exp - term | term
term -> term * factor | term / factor | factor
```

Para eliminar la recursión por la izquierda se usa la forma general

```
A -> βA'
A' -> cA' | ε
```

Por lo que al aplicarla sobre las reglas de primera gramatica se tiene:

### Para la primera regla

```
exp -> exp + term | exp - term | term
```

| exp | ->  | exp | + term | exp | - term | term |
| --- | --- | --- | ------ | --- | ------ | ---- |
| A   | ->  | A   | c      | A   | c      | β    |

Para lo cual respectivamente se tiene que

- `A` corresponde con `exp`

- `c` corresponde con `+ term` y `- term`

- `β` corresponde con `term`

Aplicando la forma

```
A -> βA'
A' -> cA' | ε
```

La primera regla se re ordena como:

```
exp -> term exp'
exp' -> + term exp' | - term exp' | ε
```

### Para la segunda regla

```
term -> term * factor | term / factor | factor
```

| term | ->  | term | \* factor | term | / factor | factor |
| ---- | --- | ---- | --------- | ---- | -------- | ------ |
| A    | ->  | A    | c         | A    | c        | β      |

Para lo cual respectivamente se tiene que

- `A` corresponde con `term`

- `c` corresponde con `* factor` y `/ factor`

- `β` corresponde con `factor`

Aplicando la forma

```
A -> βA'
A' -> cA' | ε
```

La segunda regla se re ordena como:

```
term -> factor term'
term' -> * factor term' | / factor term' | ε
```

La #1 gramatica ajustada sería:

```
exp -> term exp'
exp' -> + term exp' | - term exp' | ε
term -> factor term'
term' -> * factor term' | / factor term' | ε
factor -> (exp) | id | num
```

Los primeros

```
P(exp) = {(, id, num}
P(exp') = {+, -, ε}
P(term) = {(, id, num}
P(term') = {*, /, ε}
P(factor) = {(, id, num}
```

Los siguientes

Para la regla inicial

```
exp -> term exp'

S(exp) = {$, )}
```

Para los siguientes de exp'

```
exp -> term exp'
A   ->  c   B

B = exp'
c = term
A = exp

S(B) = S(A)
S(exp') = {$, )}
```

Para los siguientes de term

```
exp' -> + term exp'
A    -> c  B    y

A = exp'
c = +
B = term
y = exp'

S(B) = P(y) U S(A)
S(term) = P(exp') U S(exp')

S(term) = {$, ), +, -, ε}
```

Para los siguientes de term'

```
term -> factor term'
A    ->   c     B

A = term
c = factor
B = term'

S(B) = S(A)
S(term') = {$, ), +, -, ε}
```

Para los siguientes de factor

```
term' -> * factor term'
A     -> c   B      y

A = term'
c = *
B = factor
y = term'

S(B) = P(y) U S(A)
S(factor) = P(term') U S(term')

S(factor) = {+, -, *, /, ), $, ε}
```

Los primeros

```
P(exp) = {(, id, num}
P(exp') = {+, -, ε}
P(term) = {(, id, num}
P(term') = {*, /, ε}
P(factor) = {(, id, num}
```

De manera que los siguiente serían

```
S(exp) = {$, )}
S(exp') = {$, )}
S(term) = {$, ), +, -, ε}
S(term') = {$, ), +, -, ε}
S(factor) = {+, -, *, /, ), $, ε}
```

Gramatica

```
exp -> term exp'
exp' -> + term exp' | - term exp' | ε
term -> factor term'
term' -> * factor term' | / factor term' | ε
factor -> (exp) | id | num
```

#### Tabla de analisis sintactico ll1

| Regla/Simbolo | +           | -           | /              | \*            | id           | num          | (            | )   | $   |
| ------------- | ----------- | ----------- | -------------- | ------------- | ------------ | ------------ | ------------ | --- | --- |
| exp           |             |             |                |               | term exp'    | term exp'    | term exp'    |     |     |
| exp'          | + term exp' | - term exp' |                |               |              |              |              | ε   | ε   |
| term          |             |             |                |               | factor term' | factor term' | factor term' |     |     |
| term'         | ε           | ε           | \*factor term' | /factor term' |              |              |              | ε   | ε   |
| factor        |             |             |                |               | id           | num          | (exp)        |     |     |

### 5.1) Dada la gramática

```

S -> I | otro
I -> if S | if S else S

```

- Construir el automata finito de elementos LR(0)

#### Conjunto de elementos

```

✔ S' -> .S
S' -> S.

✔ S -> .I
S -> I.

✔ S -> .otro
S -> otro.

✔ I -> .if S
I -> if .S
I -> if S.

✔ I -> .if S else S
I -> if .S else S
I -> if S .else
I -> if S else .S

```

Automata finito LR(0)

![Punto_5_AFD_LR(0)](<./Taller-AFD%20LR(0)%20-%20Punto%205.png>)

# Ejercicios de calculo de atributos

### 1.2) Sea la gramatica

```

número -> número digito | digito
digito -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

Elaborar el árbol de cálculo de atributos para los números:

- 987700
- 1004567

Para el número: 987700

```
numero -> numero digito
numero -> numero digito digito
numero -> numero digito digito digito
numero -> numero digito digito digito digito
numero -> numero digito digito digito digito digito
numero -> digito digito digito digito digito digito
digito -> 9 digito digito digito digito digito
digito -> 9 8 digito digito digito digito
digito -> 9 8 7 digito digito digito
digito -> 9 8 7 7 digito digito
digito -> 9 8 7 7 0 digito
digito -> 9 8 7 7 0 0
```

| Regla gramatical                                    | Reglas semánticas                                                                                                                         |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| numero -> numero digito digito digito digito digito | numero.val = numero5.val \* 10^5 + digito.val \* 10^4 + digito.val \* 10^3 + digito.val \* 10^2 + digito.val \* 10^1 + digito.val \* 10^0 |
| numero -> digito                                    | numero.val = digito.val                                                                                                                   |
| digito -> 0                                         | digito.val = 0                                                                                                                            |
| digito -> 1                                         | digito.val = 1                                                                                                                            |
| digito -> 2                                         | digito.val = 2                                                                                                                            |
| digito -> 3                                         | digito.val = 3                                                                                                                            |
| digito -> 4                                         | digito.val = 4                                                                                                                            |
| digito -> 5                                         | digito.val = 5                                                                                                                            |
| digito -> 6                                         | digito.val = 6                                                                                                                            |
| digito -> 7                                         | digito.val = 7                                                                                                                            |
| digito -> 8                                         | digito.val = 8                                                                                                                            |
| digito -> 9                                         | digito.val = 9                                                                                                                            |

#### Arbol para: 987700

![987700](./Taller-%C3%81rbol%20gramatical_987700.png)

Para el número: 1004567

```
numero -> numero digito
numero -> numero digito digito
numero -> numero digito digito digito
numero -> numero digito digito digito digito
numero -> numero digito digito digito digito digito
numero -> numero digito digito digito digito digito digito
numero -> digito digito digito digito digito digito digito
digito -> 1 digito digito digito digito digito digito
digito -> 1 0 digito digito digito digito digito
digito -> 1 0 0 digito digito digito digito
digito -> 1 0 0 4 digito digito digito
digito -> 1 0 0 4 5 digito digito
digito -> 1 0 0 4 5 6 digito
digito -> 1 0 0 4 5 6 7
```

| Regla gramatical                                           | Reglas semánticas                                                                                                                                              |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| numero -> numero digito digito digito digito digito digito | numero.val = numero6.val \* 10^6 + digito.val \* 10^5 + digito.val \* 10^4 + digito.val \* 10^3 + digito.val \* 10^2 + digito.val \* 10^1 + digito.val \* 10^0 |
| numero -> digito                                           | numero.val = digito.val                                                                                                                                        |
| digito -> 0                                                | digito.val = 0                                                                                                                                                 |
| digito -> 1                                                | digito.val = 1                                                                                                                                                 |
| digito -> 2                                                | digito.val = 2                                                                                                                                                 |
| digito -> 3                                                | digito.val = 3                                                                                                                                                 |
| digito -> 4                                                | digito.val = 4                                                                                                                                                 |
| digito -> 5                                                | digito.val = 5                                                                                                                                                 |
| digito -> 6                                                | digito.val = 6                                                                                                                                                 |
| digito -> 7                                                | digito.val = 7                                                                                                                                                 |
| digito -> 8                                                | digito.val = 8                                                                                                                                                 |
| digito -> 9                                                | digito.val = 9                                                                                                                                                 |

#### Arbol para: 1004567

![1004567](./Taller-%C3%81rbol%20gramatical_1004567.png)

### 2.2) Considere la gramatica siguiente para expresiones aritmeticas enteras simples

```
exp -> exp + term | exp - term | term
term -> term * factor | factor
factor -> (exp) | numero
```

Elaborar el árbol de cálculo de atributos para las expresiones

- ( 34 - 3 ) \* 42
- ( 25 + 3 \* 8 ) + 16

#### Arbol para: ( 34 - 3 ) \* 42

```
exp     -> term
term    -> term * factor
term    -> factor * factor
factor  -> (exp) * factor
exp     -> (exp - term) * factor
exp     -> (term - term) * factor
term    -> (factor - term) * factor
term    -> (factor - factor) * factor
factor  -> (numero - factor) * factor
factor  -> (numero - numero) * factor
factor  -> (numero - numero) * numero
numero  -> (32 - numero) * numero
numero  -> (32 - 3) * numero
numero  -> (32 - 3) * 42
```

| Regla gramatical              | Reglas semánticas                            |
| ----------------------------- | -------------------------------------------- |
| exp -> (exp - term) \* factor | exp.val = (exp.val - term.val) \* factor.val |
| exp -> term                   | exp.val = term                               |
| term -> factor                | term.val = factor                            |
| factor -> numero              | factor.val = numero                          |

![(34-3)*42](./Taller-%C3%81rbol%20gramatical__34-3_42.png)

#### Arbol para: ( 25 + 3 \* 8 ) + 16

```
exp     -> exp + term
exp     -> term + term
term    -> factor + term
factor  -> (exp) + term
exp     -> (exp + term) + term
term    -> (exp + term * factor) + term
exp     -> (term + term * factor) + term
term    -> (factor + term * factor) + term
term    -> (factor + factor * factor) + term
term    -> (factor + factor * factor) + factor
factor  -> (numero + factor * factor) + factor
factor  -> (numero + numero * factor) + factor
factor  -> (numero + numero * numero) + factor
factor  -> (numero + numero * numero) + numero
numero  -> (25 + numero * numero) + numero
numero  -> (25 + 3 * numero) + numero
numero  -> (25 + 3 * 8) + numero
numero  -> (25 + 3 * 8) + 16
```

| Regla gramatical              | Reglas semánticas                          |
| ----------------------------- | ------------------------------------------ |
| exp -> (exp - term) \* factor | exp.val = (exp + term \* factor) \* factor |
| exp -> term                   | exp.val = term                             |
| term -> factor                | term.val = factor                          |
| factor -> numero              | factor.val = numero                        |

![(25+3*8)+16](./Taller-%C3%81rbol%20gramatical__25_3_8__16.png)