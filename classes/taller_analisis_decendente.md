# Ejercicios Análisis Descendente.

Utilizar el algoritmo básico LL(1) para aceptar las cadenas en entrada planteadas dada una
gramática respectiva.

1. Sea la gramática:

```
exp -> exp + term | exp - term | term
term -> term * factor | term / factor | factor
factor -> (exp) | id | num
```

Resolver las cadenas:

```
id + id / (id - id * id) + id * id + id * (id - id / (id * id)) + id
id - (id + id * id - id * (id + id) - id) + (id - id) - id * id + id
```

2. Sea la gramatica:

```
lexp -> atom | list
atom -> numero | identificador
list -> ( lexp-sec )
lexp-sec -> lexp-sec lexp | lexp
```

Resolver la cadena:

```
(a 23(m))
```

---

## Eliminando la recursión por la izquierda de la primera gramática

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

#### Ejercicio #1

```
id + id / (id - id * id) + id * id + id * (id - id / (id * id)) + id
```

| #   | Pila                                          | Cadena                                                                  | Acciones                          |
| --- | --------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------- |
| 1   | $`exp`                                        | `id + id / (id - id * id) + id * id + id * (id - id / (id * id)) + id`$ | Derivar `exp -> term exp'`        |
| 2   | $`term exp'`                                  | `id + id / (id - id * id) + id * id + id * (id - id / (id * id)) + id`$ | Derivar `term -> factor term'`    |
| 3   | $`factor term exp'`                           | `id + id / (id - id * id) + id * id + id * (id - id / (id * id)) + id`$ | Derivar `factor -> id`            |
| 4   | $`id term' exp'`                              | `id + id / (id - id * id) + id * id + id * (id - id / (id * id)) + id`$ | Concordar                         |
| 5   | $`term' exp'`                                 | `+ id / (id - id * id) + id * id + id * (id - id / (id * id)) + id`$    | Derivar `term' -> ε`              |
| 6   | $`exp'`                                       | `+ id / (id - id * id) + id * id + id * (id - id / (id * id)) + id`$    | Derivar `exp' -> + term exp'`     |
| 7   | $`+ term exp'`                                | `+ id / (id - id * id) + id * id + id * (id - id / (id * id)) + id`$    | Concordar                         |
| 8   | $`term exp'`                                  | `id / (id - id * id) + id * id + id * (id - id / (id * id)) + id`$      | Derivar `term -> factor term'`    |
| 9   | $`factor term' exp'`                          | `id / (id - id * id) + id * id + id * (id - id / (id * id)) + id`$      | Derivar `factor -> id`            |
| 10  | $`id term' exp'`                              | `/ (id - id * id) + id * id + id * (id - id / (id * id)) + id`$         | Concordar                         |
| 11  | $`term' exp'`                                 | `/ (id - id * id) + id * id + id * (id - id / (id * id)) + id`$         | Derivar `term' -> / factor term'` |
| 12  | $`/ factor term' exp'`                        | `/ (id - id * id) + id * id + id * (id - id / (id * id)) + id`$         | Concordar                         |
| 13  | $`factor term' exp'`                          | `(id - id * id) + id * id + id * (id - id / (id * id)) + id`$           | Derivar `factor -> (exp)`         |
| 14  | $`(exp) term' exp'`                           | `(id - id * id) + id * id + id * (id - id / (id * id)) + id`$           | Concordar                         |
| 15  | $`exp) term' exp'`                            | `id - id * id) + id * id + id * (id - id / (id * id)) + id`$            | Derivar `exp -> term exp'`        |
| 16  | $`term exp') term' exp'`                      | `id - id * id) + id * id + id * (id - id / (id * id)) + id`$            | Derivar `term -> factor term'`    |
| 17  | $`factor term' exp') term' exp'`              | `id - id * id) + id * id + id * (id - id / (id * id)) + id`$            | Derivar `factor -> id`            |
| 18  | $`id term' exp') term' exp'`                  | `- id * id) + id * id + id * (id - id / (id * id)) + id`$               | Concordar                         |
| 19  | $`term' exp') term' exp'`                     | `- id * id) + id * id + id * (id - id / (id * id)) + id`$               | Derivar `term' -> ε`              |
| 20  | $`exp') term' exp'`                           | `- id * id) + id * id + id * (id - id / (id * id)) + id`$               | Derivar `exp' -> - term exp'`     |
| 21  | $`- term exp') term' exp'`                    | `- id * id) + id * id + id * (id - id / (id * id)) + id`$               | Concordar                         |
| 22  | $`term exp') term' exp'`                      | `id * id) + id * id + id * (id - id / (id * id)) + id`$                 | Derivar `term -> factor term'`    |
| 23  | $`factor term' exp') term' exp'`              | `id * id) + id * id + id * (id - id / (id * id)) + id`$                 | Derivar `factor -> id`            |
| 24  | $`id term' exp') term' exp'`                  | `id * id) + id * id + id * (id - id / (id * id)) + id`$                 | Concordar                         |
| 25  | $`term' exp') term' exp'`                     | `* id) + id * id + id * (id - id / (id * id)) + id`$                    | Derivar `term' -> * factor term'` |
| 26  | $`* factor term' exp') term' exp'`            | `* id) + id * id + id * (id - id / (id * id)) + id`$                    | Concordar                         |
| 27  | $`factor term' exp') term' exp'`              | `id) + id * id + id * (id - id / (id * id)) + id`$                      | Derivar `factor -> id'`           |
| 28  | $`id term' exp') term' exp'`                  | `id) + id * id + id * (id - id / (id * id)) + id`$                      | Concordar                         |
| 29  | $`term' exp') term' exp'`                     | `) + id * id + id * (id - id / (id * id)) + id`$                        | Derivar `term' -> ε`              |
| 30  | $`exp') term' exp'`                           | `) + id * id + id * (id - id / (id * id)) + id`$                        | Derivar `exp' -> ε`               |
| 31  | $`) term' exp'`                               | `) + id * id + id * (id - id / (id * id)) + id`$                        | Concordar                         |
| 32  | $`term' exp'`                                 | `+ id * id + id * (id - id / (id * id)) + id`$                          | Derivar `term' -> ε`              |
| 33  | $`exp'`                                       | `+ id * id + id * (id - id / (id * id)) + id`$                          | Derivar `exp' -> + term exp'`     |
| 34  | $`+ term exp'`                                | `+ id * id + id * (id - id / (id * id)) + id`$                          | Concordar                         |
| 35  | $`term exp'`                                  | `+ id * id + id * (id - id / (id * id)) + id`$                          | Derivar `term -> factor term'`    |
| 36  | $`factor term' exp'`                          | `id * id + id * (id - id / (id * id)) + id`$                            | Derivar `factor -> id`            |
| 37  | $`id term' exp'`                              | `id * id + id * (id - id / (id * id)) + id`$                            | Concordar                         |
| 38  | $`term' exp'`                                 | `* id + id * (id - id / (id * id)) + id`$                               | Derivar `term' -> * factor term'` |
| 39  | $`* factor term' exp'`                        | `* id + id * (id - id / (id * id)) + id`$                               | Concordar                         |
| 40  | $`factor term' exp'`                          | `id + id * (id - id / (id * id)) + id`$                                 | Derivar `factor -> id`            |
| 41  | $`id term' exp'`                              | `id + id * (id - id / (id * id)) + id`$                                 | Concordar                         |
| 42  | $`term' exp'`                                 | `+ id * (id - id / (id * id)) + id`$                                    | Derivar `term' -> ε`              |
| 43  | $`exp'`                                       | `+ id * (id - id / (id * id)) + id`$                                    | Derivar `exp' -> + term exp'`     |
| 44  | $`+ term exp'`                                | `+ id * (id - id / (id * id)) + id`$                                    | Concordar                         |
| 45  | $`term exp'`                                  | `id * (id - id / (id * id)) + id`$                                      | Derivar `term -> factor term'`    |
| 46  | $`factor term' exp'`                          | `id * (id - id / (id * id)) + id`$                                      | Derivar `factor -> id`            |
| 47  | $`id term' exp'`                              | `* (id - id / (id * id)) + id`$                                         | Concordar                         |
| 48  | $`term' exp'`                                 | `* (id - id / (id * id)) + id`$                                         | Derivar `term' -> * factor term'` |
| 49  | $`* factor term' exp'`                        | `* (id - id / (id * id)) + id`$                                         | Concordar                         |
| 50  | $`factor term' exp'`                          | `(id - id / (id * id)) + id`$                                           | Derivar `factor -> (exp)`         |
| 51  | $`(exp) term' exp'`                           | `(id - id / (id * id)) + id`$                                           | Concordar                         |
| 52  | $`exp) term' exp'`                            | `id - id / (id * id)) + id`$                                            | Derivar `exp -> term exp'`        |
| 53  | $`term exp') term' exp'`                      | `id - id / (id * id)) + id`$                                            | Derivar `term -> factor term'`    |
| 54  | $`factor term' exp') term' exp'`              | `id - id / (id * id)) + id`$                                            | Derivar `factor -> id`            |
| 55  | $`id term' exp') term' exp'`                  | `id - id / (id * id)) + id`$                                            | Concordar                         |
| 56  | $`term' exp') term' exp'`                     | `- id / (id * id)) + id`$                                               | Derivar `term' -> ε`              |
| 57  | $`exp') term' exp'`                           | `- id / (id * id)) + id`$                                               | Derivar `exp' -> - term exp'`     |
| 58  | $`- term exp') term' exp'`                    | `- id / (id * id)) + id`$                                               | Concordar                         |
| 59  | $`term exp') term' exp'`                      | `id / (id * id)) + id`$                                                 | Derivar `term -> factor term'`    |
| 60  | $`factor term' exp') term' exp'`              | `id / (id * id)) + id`$                                                 | Derivar `factor -> id`            |
| 61  | $`id term' exp') term' exp'`                  | `id / (id * id)) + id`$                                                 | Concordar                         |
| 62  | $`term' exp') term' exp'`                     | `/ (id * id)) + id`$                                                    | Derivar `term' -> / factor term'` |
| 63  | $`/ factor term' exp') term' exp'`            | `/ (id * id)) + id`$                                                    | Concordar                         |
| 64  | $`factor term' exp') term' exp'`              | `(id * id)) + id`$                                                      | Derivar `factor -> (exp)`         |
| 65  | $`(exp) term' exp') term' exp'`               | `(id * id)) + id`$                                                      | Concordar                         |
| 66  | $`exp) term' exp') term' exp'`                | `id * id)) + id`$                                                       | Derivar `exp -> term exp'`        |
| 67  | $`term exp') term' exp') term' exp'`          | `id * id)) + id`$                                                       | Derivar `term -> factor term'`    |
| 68  | $`factor term' exp') term' exp') term' exp'`  | `id * id)) + id`$                                                       | Derivar `factor -> id'`           |
| 69  | $`id term' exp') term' exp') term' exp'`      | `id * id)) + id`$                                                       | Concordar                         |
| 70  | $`term' exp') term' exp') term' exp'`         | `* id)) + id`$                                                          | Derivar `term' -> * factor term'` |
| 71  | $`* facto term' exp') term' exp') term' exp'` | `* id)) + id`$                                                          | Concordar                         |
| 72  | $`factor term' exp') term' exp') term' exp'`  | `id)) + id`$                                                            | Derivar `factor -> id`            |
| 73  | $`id term' exp') term' exp') term' exp'`      | `id)) + id`$                                                            | Concordar                         |
| 74  | $`term' exp') term' exp') term' exp'`         | `)) + id`$                                                              | Derivar `term' -> ε`              |
| 75  | $`exp') term' exp') term' exp'`               | `)) + id`$                                                              | Derivar `exp' -> ε`               |
| 76  | $`) term' exp') term' exp'`                   | `)) + id`$                                                              | Concordar                         |
| 77  | $`term' exp') term' exp'`                     | `) + id`$                                                               | Derivar `term' -> ε`              |
| 78  | $`exp') term' exp'`                           | `) + id`$                                                               | Derivar `exp' -> ε`               |
| 79  | $`)term' exp'`                                | `+ id`$                                                                 | Concordar                         |
| 80  | $`term' exp'`                                 | `+ id`$                                                                 | Derivar `term' -> ε`              |
| 81  | $`exp'`                                       | `+ id`$                                                                 | Derivar `exp' -> + term exp'`     |
| 82  | $`+ term exp'`                                | `+ id`$                                                                 | Concordar                         |
| 83  | $`term exp'`                                  | `id`$                                                                   | Derivar `term -> factor term'`    |
| 84  | $`factor term' exp'`                          | `id`$                                                                   | Derivar `factor -> id`            |
| 85  | $`id term' exp'`                              | `id`$                                                                   | Concordar                         |
| 86  | $`term' exp'`                                 | $                                                                       | Derivar `term' -> ε`              |
| 87  | $`exp'`                                       | $                                                                       | Derivar `exp' -> ε`               |
| 88  | $                                             | $                                                                       | Concordar                         |

#### Ejercicio #2

```
id - (id + id * id - id * (id + id) - id) + (id - id) - id * id + id
```

| #   | Pila                                          | Cadena                                                                  | Acciones                          |
| --- | --------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------- |
| 1   | $`exp`                                        | `id - (id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$ | Derivar `exp -> term exp'`        |
| 2   | $`term exp'`                                  | `id - (id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$ | Derivar `term -> factor term'`    |
| 3   | $`factor term' exp'`                          | `id - (id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$ | Derivar `factor -> id`            |
| 4   | $`id term' exp'`                              | `id - (id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$ | Concordar                         |
| 5   | $`term' exp'`                                 | `- (id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$    | Derivar `term' -> ε`              |
| 6   | $`exp'`                                       | `- (id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$    | Derivar `exp' -> - term exp'`     |
| 7   | $`- term exp'`                                | `- (id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$    | Concordar                         |
| 8   | $`term exp'`                                  | `(id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$      | Derivar `term -> factor term'`    |
| 9   | $`factor term' exp'`                          | `(id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$      | Derivar `factor -> (exp)`         |
| 10  | $`(exp) term' exp'`                           | `(id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$      | Concordar                         |
| 11  | $`exp) term' exp'`                            | `id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$       | Derivar `exp -> term exp'`        |
| 12  | $`term exp') term' exp'`                      | `id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$       | Derivar `term -> factor term'`    |
| 13  | $`factor term' exp') term' exp'`              | `id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$       | Derivar `factor -> id`            |
| 14  | $`id term' exp') term' exp'`                  | `id + id * id - id * (id + id) - id) + (id - id) - id * id + id`$       | Concordar                         |
| 15  | $`term' exp') term' exp'`                     | `+ id * id - id * (id + id) - id) + (id - id) - id * id + id`$          | Derivar `term' -> ε`              |
| 16  | $`exp') term' exp'`                           | `+ id * id - id * (id + id) - id) + (id - id) - id * id + id`$          | Derivar `exp' -> + term exp'`     |
| 17  | $`+ term exp') term' exp'`                    | `+ id * id - id * (id + id) - id) + (id - id) - id * id + id`$          | Concordar                         |
| 18  | $`term exp') term' exp'`                      | `id * id - id * (id + id) - id) + (id - id) - id * id + id`$            | Derivar `term -> factor term'`    |
| 19  | $`factor term' exp') term' exp'`              | `id * id - id * (id + id) - id) + (id - id) - id * id + id`$            | Derivar `factor -> id`            |
| 20  | $`id term' exp') term' exp'`                  | `id * id - id * (id + id) - id) + (id - id) - id * id + id`$            | Concordar                         |
| 21  | $`term' exp') term' exp'`                     | `* id - id * (id + id) - id) + (id - id) - id * id + id`$               | Derivar `term' -> * factor term'` |
| 22  | $`* factor term' exp') term' exp'`            | `* id - id * (id + id) - id) + (id - id) - id * id + id`$               | Concordar                         |
| 23  | $`factor term' exp') term' exp'`              | `id - id * (id + id) - id) + (id - id) - id * id + id`$                 | Derivar `factor -> id`            |
| 24  | $`id term' exp') term' exp'`                  | `- id * (id + id) - id) + (id - id) - id * id + id`$                    | Concordar                         |
| 25  | $`term' exp') term' exp'`                     | `- id * (id + id) - id) + (id - id) - id * id + id`$                    | Derivar `term' -> ε`              |
| 26  | $`exp') term' exp'`                           | `- id * (id + id) - id) + (id - id) - id * id + id`$                    | Derivar `exp' -> - term exp'`     |
| 27  | $`- term exp') term' exp'`                    | `- id * (id + id) - id) + (id - id) - id * id + id`$                    | Concordar                         |
| 28  | $`term exp') term' exp'`                      | `id * (id + id) - id) + (id - id) - id * id + id`$                      | Derivar `term -> factor term'`    |
| 29  | $`factor term' exp') term' exp'`              | `id * (id + id) - id) + (id - id) - id * id + id`$                      | Derivar `factor -> id`            |
| 30  | $`id term' exp') term' exp'`                  | `id * (id + id) - id) + (id - id) - id * id + id`$                      | Concordar                         |
| 31  | $`term' exp') term' exp'`                     | `* (id + id) - id) + (id - id) - id * id + id`$                         | Derivar `term' -> * factor term'` |
| 32  | $`* factor term' exp') term' exp'`            | `* (id + id) - id) + (id - id) - id * id + id`$                         | Concordar                         |
| 33  | $`factor term' exp') term' exp'`              | `(id + id) - id) + (id - id) - id * id + id`$                           | Derivar `factor -> (exp)`         |
| 34  | $`(exp) term' exp') term' exp'`               | `(id + id) - id) + (id - id) - id * id + id`$                           | Concordar                         |
| 35  | $`exp) term' exp') term' exp'`                | `id + id) - id) + (id - id) - id * id + id`$                            | Derivar `exp -> term exp'`        |
| 36  | $`term exp') term' exp') term' exp'`          | `id + id) - id) + (id - id) - id * id + id`$                            | Derivar `term -> factor term'`    |
| 37  | $`factor term' exp') term' exp') term' exp'`  | `id + id) - id) + (id - id) - id * id + id`$                            | Derivar `factor -> id`            |
| 38  | $`id term' exp') term' exp') term' exp'`      | `id + id) - id) + (id - id) - id * id + id`$                            | Concordar                         |
| 39  | $`term' exp') term' exp') term' exp'`         | `+ id) - id) + (id - id) - id * id + id`$                               | Derivar `term' -> + factor term'` |
| 40  | $`+ facto term' exp') term' exp') term' exp'` | `+ id) - id) + (id - id) - id * id + id`$                               | Concordar                         |
| 41  | $`factor term' exp') term' exp') term' exp'`  | `id) - id) + (id - id) - id * id + id`$                                 | Derivar `factor -> id`            |
| 42  | $`id term' exp') term' exp') term' exp'`      | `id) - id) + (id - id) - id * id + id`$                                 | Concordar                         |
| 43  | $`term' exp') term' exp') term' exp'`         | `) - id) + (id - id) - id * id + id`$                                   | Derivar `term' -> ε`              |
| 44  | $`exp') term' exp') term' exp'`               | `) - id) + (id - id) - id * id + id`$                                   | Derivar `exp' -> ε`               |
| 45  | $`) term' exp') term' exp'`                   | `) - id) + (id - id) - id * id + id`$                                   | Concordar                         |
| 46  | $`term' exp') term' exp'`                     | `- id) + (id - id) - id * id + id`$                                     | Derivar `term' -> ε`              |
| 47  | $`exp') term' exp'`                           | `- id) + (id - id) - id * id + id`$                                     | Derivar `exp' -> - term exp'`     |
| 48  | $`- term exp') term' exp'`                    | `- id) + (id - id) - id * id + id`$                                     | Concordar                         |
| 49  | $`term exp') term' exp'`                      | `id) + (id - id) - id * id + id`$                                       | Derivar `term -> factor term'`    |
| 50  | $`factor term' exp') term' exp'`              | `id) + (id - id) - id * id + id`$                                       | Derivar `factor -> id`            |
| 51  | $`id term' exp') term' exp'`                  | `id) + (id - id) - id * id + id`$                                       | Concordar                         |
| 52  | $`term' exp') term' exp'`                     | `) + (id - id) - id * id + id`$                                         | Derivar `term' -> ε`              |
| 53  | $`exp') term' exp'`                           | `) + (id - id) - id * id + id`$                                         | Derivar `exp' -> ε`               |
| 54  | $`) term' exp'`                               | `) + (id - id) - id * id + id`$                                         | Concordar                         |
| 55  | $`term' exp'`                                 | `+ (id - id) - id * id + id`$                                           | Derivar `term' -> ε'`             |
| 56  | $`exp'`                                       | `+ (id - id) - id * id + id`$                                           | Derivar `exp' -> + term exp'`     |
| 57  | $`+ term exp'`                                | `+ (id - id) - id * id + id`$                                           | Concordar                         |
| 58  | $`term exp'`                                  | `(id - id) - id * id + id`$                                             | Derivar `term -> factor term'`    |
| 59  | $`factor term' exp'`                          | `(id - id) - id * id + id`$                                             | Derivar `factor -> (exp)`         |
| 60  | $`(exp) term' exp'`                           | `(id - id) - id * id + id`$                                             | Concordar                         |
| 61  | $`exp) term' exp'`                            | `id - id) - id * id + id`$                                              | Derivar `exp -> term exp'`        |
| 62  | $`term exp') term' exp'`                      | `id - id) - id * id + id`$                                              | Derivar `term -> factor term'`    |
| 63  | $`factor term' exp') term' exp'`              | `id - id) - id * id + id`$                                              | Derivar `factor -> id`            |
| 64  | $`id term' exp') term' exp'`                  | `id - id) - id * id + id`$                                              | Concordar                         |
| 65  | $`term' exp') term' exp'`                     | `- id) - id * id + id`$                                                 | Derivar `term' -> ε`              |
| 66  | $`exp') term' exp'`                           | `- id) - id * id + id`$                                                 | Derivar `exp' -> - term exp'`     |
| 67  | $`- term exp') term' exp'`                    | `- id) - id * id + id`$                                                 | Concordar                         |
| 68  | $`term exp') term' exp'`                      | `id) - id * id + id`$                                                   | Derivar `term -> factor term'`    |
| 69  | $`factor term' exp') term' exp'`              | `id) - id * id + id`$                                                   | Derivar `factor -> id`            |
| 70  | $`id term' exp') term' exp'`                  | `id) - id * id + id`$                                                   | Concordar                         |
| 71  | $`term' exp') term' exp'`                     | `) - id * id + id`$                                                     | Derivar `term' -> ε`              |
| 72  | $`exp') term' exp'`                           | `) - id * id + id`$                                                     | Derivar `exp' -> ε`               |
| 73  | $`) term' exp'`                               | `- id * id + id`$                                                       | Concordar                         |
| 74  | $`term' exp'`                                 | `- id * id + id`$                                                       | Derivar `term' -> ε`              |
| 75  | $`exp'`                                       | `- id * id + id`$                                                       | Derivar `exp' -> - term exp'`     |
| 76  | $`- term exp'`                                | `- id * id + id`$                                                       | Concordar                         |
| 77  | $`term exp'`                                  | `id * id + id`$                                                         | Derivar `term -> factor term'`    |
| 78  | $`factor term' exp'`                          | `id * id + id`$                                                         | Derivar `factor -> id`            |
| 79  | $`id term' exp'`                              | `id * id + id`$                                                         | Concordar                         |
| 80  | $`term' exp'`                                 | `* id + id`$                                                            | Derivar `term' -> * factor term'` |
| 81  | $`* factor term' exp'`                        | `* id + id`$                                                            | Concordar                         |
| 82  | $`factor term' exp'`                          | `id + id`$                                                              | Derivar `factor -> id`            |
| 83  | $`id term' exp'`                              | `id + id`$                                                              | Concordar                         |
| 84  | $`term' exp'`                                 | `+ id`$                                                                 | Derivar `term' -> ε'`             |
| 85  | $`exp'`                                       | `+ id`$                                                                 | Derivar `exp' -> + term exp'`     |
| 86  | $`+ term exp'`                                | `+ id`$                                                                 | Concordar                         |
| 87  | $`term exp'`                                  | `id`$                                                                   | Derivar `term -> factor term'`    |
| 88  | $`factor term' exp'`                          | `id`$                                                                   | Derivar `factor -> id`            |
| 89  | $`id term' exp'`                              | `id`$                                                                   | Concordar                         |
| 90  | $`term' exp'`                                 | $                                                                       | Derivar `term' -> ε`              |
| 91  | $`exp'`                                       | $                                                                       | Derivar `exp' -> ε`               |
| 92  | $                                             | $                                                                       | Concordar                         |

---

## Eliminando la recursión por la izquierda de la segunda gramática

Las reglasa que tienen recursión por la izquierda de la segunda gramatica son:

```
lexp-sec -> lexp-sec lexp | lexp
```

Para eliminar la recursión por la izquierda se usa la forma general

```
A -> βA'
A' -> cA' | ε
```

Por lo que al aplicarla sobre la regla de esta gramatica se tiene:

| lexp-sec | ->  | lexp-sec | lexp | lexp |
| -------- | --- | -------- | ---- | ---- |
| A        | ->  | A        | c    | β    |

Para lo cual respectivamente se tiene que

- `A` corresponde con `lexp-sec`

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

La #2 gramatica ajustada sería:

```
lexp -> atom | list
atom -> numero | identificador
list -> ( lexp-sec )
lexp-sec -> lexp lexp-sec'
lexp-sec' -> lexp lexp-sec' | ε
```

#### Ejercicio #3

```
(a 23(m))
```

| #   | Pila                                             | Cadena       | Acciones                              |
| --- | ------------------------------------------------ | ------------ | ------------------------------------- |
| 1   | $`lexp-sec`                                      | `(a 23(m))`$ | Derivar `lexp-sec -> lexp lexp-sec'`  |
| 2   | $`lexp lexp-sec'`                                | `(a 23(m))`$ | Derivar `lexp -> list`                |
| 3   | $`list lexp-sec'`                                | `(a 23(m))`$ | Derivar `list -> (lexp-sec)`          |
| 4   | $`(lexp-sec) lexp-sec'`                          | `(a 23(m))`$ | Concordar                             |
| 5   | $`lexp-sec) lexp-sec'`                           | `a 23(m))`$  | Derivar `lexp-sec -> lexp lexp-sec'`  |
| 6   | $`lexp lexp-sec') lexp-sec'`                     | `a 23(m))`$  | Derivar `lexp -> atom`                |
| 7   | $`atom lexp-sec') lexp-sec'`                     | `a 23(m))`$  | Derivar `atom -> identificador`       |
| 8   | $`identificador lexp-sec') lexp-sec'`            | `a 23(m))`$  | Concordar                             |
| 9   | $`lexp-sec') lexp-sec'`                          | `23(m))`$    | Derivar `lexp-sec' -> lexp lexp-sec'` |
| 10  | $`lexp lexp-sec') lexp-sec'`                     | `23(m))`$    | Derivar `lexp -> atom`                |
| 11  | $`atom lexp-sec') lexp-sec'`                     | `23(m))`$    | Derivar `atom -> numero`              |
| 12  | $`numero lexp-sec') lexp-sec'`                   | `23(m))`$    | Concordar                             |
| 13  | $`lexp-sec') lexp-sec'`                          | `3(m))`$     | Derivar `lexp-sec' -> lexp lexp-sec'` |
| 14  | $`lexp lexp-sec') lexp-sec'`                     | `3(m))`$     | Derivar `lexp -> atom`                |
| 15  | $`atom lexp-sec') lexp-sec'`                     | `3(m))`$     | Derivar `atom -> numero`              |
| 16  | $`numero lexp-sec') lexp-sec'`                   | `3(m))`$     | Concordar                             |
| 17  | $`lexp-sec') lexp-sec'`                          | `(m))`$      | Derivar `lexp-sec' -> lexp lexp-sec'` |
| 18  | $`lexp lexp-sec') lexp-sec'`                     | `(m))`$      | Derivar `lexp -> list`                |
| 19  | $`list lexp-sec') lexp-sec'`                     | `(m))`$      | Derivar `list -> (lexp-sec)`          |
| 20  | $`(lexp-sec) lexp-sec') lexp-sec'`               | `(m))`$      | Concordar                             |
| 21  | $`lexp-sec) lexp-sec') lexp-sec'`                | `m))`$       | Derivar `lexp-sec -> lexp lexp-sec'`  |
| 22  | $`lexp lexp-sec') lexp-sec') lexp-sec'`          | `m))`$       | Derivar `lexp -> atom`                |
| 23  | $`atom lexp-sec') lexp-sec') lexp-sec'`          | `m))`$       | Derivar `atom -> identificador`       |
| 24  | $`identificador lexp-sec') lexp-sec') lexp-sec'` | `m))`$       | Concordar                             |
| 25  | $`lexp-sec') lexp-sec') lexp-sec'`               | `))`$        | Derivar `lexp-sec' -> ε`              |
| 26  | $`) lexp-sec') lexp-sec'`                        | `))`$        | Concordar                             |
| 27  | $`lexp-sec') lexp-sec'`                          | `)`$         | Derivar `lexp-sec' -> ε`              |
| 28  | $`) lexp-sec'`                                   | `)`$         | Concordar                             |
| 29  | $`lexp-sec'`                                     | $            | Derivar `lexp-sec' -> ε`              |
| 30  | $                                                | $            | Concordar                             |
