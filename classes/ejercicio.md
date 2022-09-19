# Ejercicio

Sea la gramatica

Exp -> Exp + Term | Exp - Term | Term
Term -> Term \* factor | Term / factor | factor
factor -> (Exp) | id | numero

Eliminando la recursividad por la izquierda

> Primera regla

Exp -> Exp + Term | Exp - Term | Term
A A c A c B

A -> BA'
A' -> cA' | cA' | ε

Exp -> Term Exp'
Exp' -> + Term Exp' | - Term Exp' | ε

> Segunda regla

Term -> Term \* factor | Term / factor | factor
A A c A c B

A -> BA'
A' -> cA' | cA' | ε

Term -> factor Term'
Term' -> \* factor Term' | / factor Term' | ε

> Tercera regla

factor -> (Exp) | id | numero

> Gramatica justada

Exp -> Term Exp'
Exp' -> + Term Exp' | - Term Exp' | ε
Term -> factor Term'
Term' -> \* factor Term' | / factor Term' | ε
factor -> (E) | id | numero

## Los primeros

```
P(Exp) = {(, id, numero}
P(Exp') = {+, -, ε}
P(Term) = {(, id, numero}
P(Term') = {+, -, ε}
P(factor) = {(, id, numero}
```

## Los siguientes

S(Exp) = {$, )}

### Para la segunda regla se aplica:

A -> cB
Exp -> Term Exp'

A = Exp
c = Term
B = Exp'

S(B) = S(A)
S(Exp') = S(Exp)

S(Exp') = {$, )}

### Para la tercera regla se aplica:

A -> c B y
Exp' -> + Term Exp'

A = Exp'
c = +
B = Term
y = Exp'

S(B) = P(y) U S(A)
S(Twem) = P(Exp') U S(Exp)

S(Term) = {+, -, $, )}

### Para la cuarta regla se aplica:

A -> c B
Term -> factor Term'

A -> Term
c = factor
B -> Term'

S(B) = S(A)
S(Term') = S(Term)

S(Term') = {+, -, $, )}

### Para la cuarta regla se aplica:

A -> c B y
Term' -> \* factor Term'

A = Term'
c = \*
B = factor
y = Term'

S(B) = P(y) U S(A)
S(factor) = P(Term') U S(Term')

S(factor) = {\*, /, +, -, $, )}

## Los segundos

```
S(Exp) = {$, )}
S(Exp') = {$, )}
S(Term) = {+, -, $, )}
S(Term') = {+, -, $, )}
S(factor) = {/*, /, +, -, $, )}
```

# Tabla de analisis sintactico


| Regla/Simbolo | +           | -           | /               | \*             | id           | numero       | (            | )   | $   |
| ------------- | ----------- | ----------- | --------------- | -------------- | ------------ | ------------ | ------------ | --- | --- |
| Exp           |             |             |                 |                | Term Exp'    | Term Exp'    | Term Exp'    |     |     |
| Exp'          | + Term Exp' | - Term Exp' |                 |                |              |              |              | ε   | ε   |
| Term          |             |             |                 |                | factor Term' | factor Term' | factor Term' |     |     |
| Term'         | ε           | ε           | \* factor Term' | / factor Term' |              |              |              | ε   | ε   |
| factor        |             |             |                 |                | id           | numero       | (Exp)        |     |     |
