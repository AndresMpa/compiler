1) Si A es la regla inicial entonces $ está en los siguientes de A

2) A -> cB
S(B) = S(A)

3) A -> cBy
S(B) = P(y) - ε
S(B) = P(y) U S(A)

Ejercicio

Encontrar los siguientes y primeros de la gramatica

E -> TE'
E' -> +TE' | -TE' | ε
T -> fT'
T' -> \*fT' | /fT' | ε
f -> (E) | id | num

Los primeros

P(E) = {(, id, num}
P(E') = {+, -, ε}
P(T) = {(, id, num}
P(E') = {+, -, ε}
P(f) = {(, id, num}

Los siguientes

S(E) = {$, )}

// Para la segunda regla se aplica:

A -> cB
E -> TE'

A = E
c = T
B = E'

S(B) = S(A)
S(E') = S(E)

S(E') = {$, )}


// Para la tercera regla se aplica:

A -> c B y
E' -> + T E'

A = E'
c = +
B = T
y = E'

S(B) = P(y) U S(A)
S(T) = P(E') U S(E)

S(T) = {+, -, $, )}

// Para la cuarta regla se aplica:

A -> c B
T -> f T'

A -> T
c = f
B -> T'

S(B) = S(A)
S(T') = S(T)

S(T') = {+, -, $, )}

// Para la cuarta regla se aplica:

A -> c B y
T' -> * f T'

A = T'
c = *
B = f
y = T'

S(B) = P(y) U S(A)
S(f) = P(T') U S(T')

S(f) = {*, /, +, -, $, )}

