Ejercicio #1

Sea la gramatica

A' -> A
A -> (A) | a

### Se saca el conjunto de elementos

```
A' -> .A
A' -> A.

A -> .(A)
A -> (.A)
A -> (A.)
A -> (A).

A -> .a
A -> a.
```

// Ver ilustración

# Ejercicio #2

Sea la gramatica

E' -> E
E -> E+T | E-T | T
T -> T*f | T/f | f
f -> (E) | id | num

### Se saca el conjunto de elementos para la gramatica

```
E' -> .E
E' -> E.

E -> .E+T
E -> E.+T
E -> E+.T
E -> E+T.

E -> .E-T
E -> E.-T
E -> E-.T
E -> E-T.

E -> .T
E -> T.

T -> .T*f
T -> T.*f
T -> T*.f
T -> T*f.

T -> .T/f
T -> T./f
T -> T/.f
T -> T/f.

T -> .f
T -> f.

f -> .(E)
f -> (.E)
f -> (E.)
f -> (E).

f -> .id
f -> id.

f -> .num
f -> num.
```

## Se obtiene el conjunto de elementos inicializadores

```
E' -> .E
E -> .E+T
E -> .E-T
E -> .T
T -> .T*f
T -> .T/f
T -> .f
f -> .(E)
f -> .id
f -> .num
```

