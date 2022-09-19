Gramaticas (G) = { Et Etn N P }

Et = Alfabeto de simbolos terminales

Et para el efecto practico son los Tokens,
los tokens son de 3 tipos

- Reservados
- Simbolos
  - Identificadores
  - Números

```
if ( a > b ) {
```

| Token     | Lexema |
| --------- | ------ |
| Reservado | if     |
| Simbolo   | (      |
| Id        | a      |
| Simbolo   | >      |
| Id        | b      |
| Simbolo   | )      |
| Reservado | {      |

Otras maneras de expresar gramaticas
recursivas por ambos lados

A -> Ac | B
A -> c*B
A -> B{c}


A -> cA | B
A -> *cB
A -> {c}B

Ejemplo de aplicación:

Secuancia-sent -> Sent;Secuancia-sent | Sent
      A            c        A            B

Secuancia-sent -> {Sent;}Sent
      A             {c}   B

Ejemplo #2:

lexp -> atom | list             // No se puede expresar en bnf
atom -> numero | Identificador  // No se puede expresar en bnf
list (lexp-sec)                 // No se puede expresar en bnf
lexp-sec -> lexp-sec lexp | lexp
   A           A       c     B

  lexp-sec -> lexp{lexp} // Por ende se produce

Ejemplo #3:

E -> E + T | T
A -> A   c   B

  A -> T{+T}

T -> T * f | f
A -> A   c   B

  T -> f{f*}

f -> (E) | id | num


Programa -> Secuancia-sent
Secuancia-sent -> Secuancia-sent ;Sentencia | Sentencia
  //Expresión de EBNF: Secuancia-sent -> Sentencia{;Sentencia}
Sentencia -> sent-if | sent-repeat | sent-assign | sent-read | sent-write
sent-if -> if exp then Secuancia-sent end | if exp then Secuancia-sent else Secuancia-sent end
sent-repeat -> repeat Secuancia-sent until exp
sent-assign -> Identificador := exp
sent-read -> read identificador
sent-write -> write exp
exp -> expre-simple op-comparacion expre-simple | expre-simple
op-comparacion -> < | =
expre-simple -> expre-simple opsuma term | term
  // Expresion de EBNF: expre-simple -> term{opsuma term}
opsuma -> + | -
term -> term op-mult factor | factor
  // Expresion de EBNF: term -> factor{op-mult factor}
op-mult -> * | /
factor -> (exp) | numero | identificador
