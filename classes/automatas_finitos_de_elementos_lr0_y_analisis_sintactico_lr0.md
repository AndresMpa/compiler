De manera general:

1. Se encientra el conjunto de elementos
2. Se encuentra la regla inicial y se encuentran los inicializadores
3. Redibujar los elementos del punto #2 como estados
4. Se hacen ε las transiciones necesarias entre estados (Esto genera estados, representados en una buburja)
5. Hacer X transiciones entre los estados (Esto genera un automata cuyas transiciones son las partes de la gramatica)
6. En caso de encontrar un elemento del tipo ".A" se han de realizar N transiciones a los estados inicializadores

## Para el caso de los AFND

## Ejemplo #1 (AFND)

Sea la gramatica

```
S' -> S
S -> (S)S | ε
```

### Se saca el conjunto de elementos

```
S' -> .S
S' -> S.

S -> .(S)S
S -> (.S)S
S -> (S.)S
S -> (S).S
S -> (S)S.
S -> .
```

numeroDeElementos = 8

### Se identifican los inicializadores

```
S -> .(S)S
S' -> .S
```

### Se dibujan el conjunto de elementos

Nota: numeroDeElementos === "numero de estados en el automata"

### Se dibuja el automata

### En caso de encotrar ".A" se generan transiciones a los inicializadores

--

## Ejemplo #2 (AFND)

Sea la gramatica

```
E' -> E
E -> E+n | n
```

### Se saca el conjunto de elementos para la gramatica #2

```
E' -> .E
E' -> E.

E -> .E+n
E -> E.+n
E -> E+.n
E -> E+n.

E -> .n
E -> n.
```

### Se obtienen los inicializadores

```
E' -> .E
E -> .E+n
E -> .n
```

### Se dibuja el conjunto de elementos como estados

```
1. E' -> .E
2. E -> .n
3. E -> .E+n // Este estado genera transiciones a 1, 2 y 3
```

(Estos serían los primeros que se dibujan)

```
4. E' -> E.
5. E -> n.
6. E -> E.+n
7. E -> E+.n
8. E -> E+n.
```

## Para el caso de los AFD

### Ejemplo #1 (AFD)

Sea la gramatica

```
S' -> S
S -> (S)S | ε
```

### Se saca el conjunto de elementos (Igual que antes)

```
S' -> .S
S' -> S.

S -> .(S)S
S -> (.S)S
S -> (S.)S
S -> (S).S
S -> (S)S.
S -> .
```

numeroDeElementos = 8

### Se identifican los inicializadores (Igual que antes)

```
S' -> .S
S -> .(S)S
S' -> .S
```

### Al graficar se altera un poco

Revisar ilustración

### Al presentarse el caso de ".A" se genera un ciclo

--

## Ejemplo #2 (AFD)

Sea la gramatica

```
E' -> E
E -> E+n | n
```

### Se saca el conjunto de elementos para la gramatica

```
E' -> .E
E' -> E.

E -> .E+n
E -> E.+n
E -> E+.n
E -> E+n.

E -> .n
E -> n.
```

### Se obtienen los inicializadores del conjunto de elementos

```
E' -> .E
E -> .E+n
E -> .n
```

### Al graficar se altera un poco debido a que

```
E' -> .E
E -> .E+n
```

Representa 2 transiciones con un mismo estado, por ende esto se lleva como un bloque

// Revisar ilustración

### Debido al caso anterior se reducen bastante el número de estados

// Revisar ilustración
