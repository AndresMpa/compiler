Ejemplo:

Sea la gramatica S -> (S)S | E, utilizar el algoritmo
LL(1) para aceptar la cadena ()

| Pasos | Pila  | Cadena | Acciones          |
| ----- | ----- | ------ | ----------------- |
| 1     | $S    | ()$    | Derivar S -> (S)S |
| 2     | $(S)S | ()$    | Concondar         |
| 3     | $S)S  | )$     | Derivar S -> E    |
| 4     | $)S   | )$     | Concondar         |
| 5     | $S    | $      | Derivar -> E      |
| 6     | $     | $      | Concondar         |

Ejemplo #2:

Sea la gramatica S -> (S)S | E, utilizar el algoritmo
LL(1) para aceptar la cadena (())()

| Pasos | Pila    | Cadena  | Acciones          |
| ----- | ------- | ------- | ----------------- |
| 1     | $S      | (())()$ | Derivar S -> (S)S |
| 2     | $(S)S   | (())()$ | Concondar         |
| 3     | $S)S    | ())()$  | Derivar S -> (S)S |
| 4     | $(S)S)S | ())()$  | Concondar         |
| 5     | $S)S)S  | ))()$   | Derivar S -> E    |
| 6     | $S)S    | )()$    | Concondar         |
| 7     | $S)S    | )()$    | Derivar S -> E    |
| 8     | $S      | ()$     | Concondar         |
| 9     | $S      | ()$     | Derivar S -> (S)S |
| 10    | $(S)S   | ()$     | Concondar         |
| 11    | $S)S    | )$      | Derivar S -> E    |
| 12    | $)S     | )$      | Concondar         |
| 13    | $S      | $       | Derivar -> E      |
| 14    | $       | $       | Concondar         |

Los analizadores decendentes no aceptan gramaticas recursivas por la izquierda

Ejemplo #3:

Sea la gramatica

```
E -> E+T | E-T | T
T -> T\*f | T/f | f
f -> (E) | id | num
```

Utilizar algoritmo ll(1) para aceptar la cadena

id + id \* id

Eliminando la recursividad por la izquierda

> Primera regla

```
E -> E + T | E - T | T
A A c A c B

A -> BA'
A' -> cA' | cA' | ε

E -> TE'
E' -> +TE' | -TE' | ε
```

> Segunda regla

```
T -> T \* f | T / f | f
A A c A c B

A -> BA'
A' -> cA' | cA' | ε

T -> fT'
T' -> \*fT' | /fT' | ε
```

> Tercera regla

```
f -> (E) | id | num
```

> Gramatica justada

```
E -> TE'
E' -> +TE' | -TE' | ε
T -> fT'
T' -> \*fT' | /fT' | ε
f -> (E) | id | num
```

| Pasos | Pila     | Cadena          | Acciones           |
| ----- | -------- | --------------- | ------------------ |
| 1     | $E       | id + id \* id $ | Derivar E -> TE'   |
| 2     | $TE'     | id + id \* id $ | Derivar F -> fT'   |
| 3     | $fT'E'   | id + id \* id $ | Derivar f -> id    |
| 4     | $idT'E'  | id + id \* id $ | Concondar          |
| 5     | $T'E'    | + id \* id $    | Derivar -> T' ε    |
| 6     | $E'      | + id \* id $    | Derivar E' -> +TE' |
| 7     | $+TE'    | + id \* id $    | Concondar          |
| 8     | $TE'     | id \* id $      | Derivar T -> fT'   |
| 9     | $fT'E'   | id \* id $      | Derivar f -> id    |
| 10    | $idT'E'  | id \* id $      | Concondar          |
| 11    | $T'E'    | \* id $         | Derivar T' \*fT'   |
| 12    | $\*fT'E' | \* id $         | Concondar          |
| 13    | $fT'E'   | id $            | Derivar f -> id    |
| 14    | $idT'E'  | id $            | Concondar          |
| 15    | $T'E'    | $               | Derivar T' -> ε    |
| 16    | $E'      | $               | Derivar E' -> ε    |
| 17    | $        | $               | Concondar          |

Ejemplo #4:

Sea la gramatica

```
E -> TE'
E' -> +TE' | -TE' | ε
T -> fT'
T' -> \*fT' | /fT' | ε
f -> (E) | id | num
```

Utilizar algoritmo ll(1) para aceptar la cadena

```
id - id + id + id / id - id
id + id \* id + id / (id - id \* id) + id
```

Eliminando la recursividad por la izquierda

| Pasos | Pila    | Cadena                      | Acciones           |
| ----- | ------- | --------------------------- | ------------------ |
| 1     | $E      | id - id + id + id / id - id | Derivar E -> TE'   |
| 2     | $TE'    | id - id + id + id / id - id | Derivar T -> fT'   |
| 3     | $fT'E'  | id - id + id + id / id - id | Derivar f -> id    |
| 4     | $idT'E' | id - id + id + id / id - id | Concondar          |
| 5     | $T'E'   | - id + id + id / id - id    | Derivar T' -> ε    |
| 6     | $E'     | - id + id + id / id - id    | Derivar E' -> -TE' |
| 7     | $-TE'   | id + id + id / id - id      | Concondar          |
| 8     | $TE'    | id + id + id / id - id      | Derivar T -> fT'   |
| 9     | $fT'E'  | id + id + id / id - id      | Derivar f -> id    |
| 10    | $idT'E' | id + id + id / id - id      | Concondar          |
| 11    | $T'E'   | + id + id / id - id         | Derivar T' -> ε    |
| 12    | $E'     | + id + id / id - id         | Derivar E' -> +TE' |
| 13    | $+TE'   | id + id / id - id           | Concondar          |
| 14    | $TE'    | id + id / id - id           | Derivar T -> fT'   |
| 15    | $fT'E'  | id + id / id - id           | Derivar f -> id    |
| 16    | $idT'E' | id + id / id - id           | Concondar          |
| 17    | $T'E'   | + id / id - id              | Derivar T' -> ε    |
| 18    | $E'     | + id / id - id              | Derivar E' -> +TE' |
| 19    | $+TE'   | + id / id - id              | Concondar          |
| 20    | $TE'    | id / id - id                | Derivar T -> fT'   |
| 21    | $fT'E'  | id / id - id                | Derivar f -> id    |
| 22    | $idT'E' | id / id - id                | Concondar          |
| 23    | $T'E'   | / id - id                   | Derivar T' -> /fT' |
| 24    | $/fT'E' | / id - id                   | Concondar          |
