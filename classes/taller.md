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

### 2.2) Elaborar el árbol de cálculo de atributos para los números:

- 987700
- 1004567

### 3.2) Considere la gramatica siguiente para expresiones aritmeticas enteras simples

exp -> exp + term | exp - term | term
term -> term \* factor | factor
factor -> (exp) | numero

### 4.2) Elaborar el árbol de cálculo de atributos para las expresiones

- ( 34 - 3 ) \* 42
- ( 25 + 3 \* 8 ) + 16
