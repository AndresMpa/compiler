Dada la gramatica

```
E' -> E
E -> E + T | E - T | T
T -> T \* F | T / F | F
F -> (E) | num | id
```

Utilizar el algoritmo básico ascendente para aceptar las siguientes cadenas de entrada:

```
id - id / id + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5

(5 + 16 \* 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2
```

> Nota: Tanto el id como también un número, por ejemplo 5 o 16 se reducen con F

Ejercicio #1

| #   | Pila              | Cadena                                                                            | Acciones            |
| --- | ----------------- | --------------------------------------------------------------------------------- | ------------------- |
| 1   | $                 | id - id / id + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$ | Desplazar           |
| 2   | $id               | - id / id + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$    | Reducir F -> id     |
| 3   | $F                | - id / id + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$    | Reducir F -> T      |
| 4   | $T                | - id / id + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$    | Reducir T -> E      |
| 5   | $E                | - id / id + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$    | Desplazar           |
| 6   | $E -              | id / id + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$      | Desplazar           |
| 7   | $E - id           | / id + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$         | Desplazar           |
| 8   | $E - F            | / id + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$         | Reducir F -> id     |
| 9   | $E - T            | / id + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$         | Reducir T -> F      |
| 10  | $E - T /          | id + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$           | Desplazar           |
| 11  | $E - T / id       | + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$              | Desplazar           |
| 12  | $E - T / F        | + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$              | Reducir F -> id     |
| 13  | $E - T            | + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$              | Reducir T -> T / F  |
| 14  | $E                | + id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$              | Reducir E -> E - T  |
| 15  | $E +              | id / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$                | Desplazar           |
| 16  | $E + id           | / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$                   | Reducir F -> id     |
| 17  | $E + F            | / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$                   | Reducir T -> F      |
| 18  | $E + T            | / (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$                   | Desplazar           |
| 19  | $E + T /          | (id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$                     | Desplazar           |
| 20  | $E + T / (        | id \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$                      | Desplazar           |
| 21  | $E + T / (id      | \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$                         | Reducir F -> id     |
| 22  | $E + T / (F       | \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$                         | Reducir T -> F      |
| 23  | $E + T / (T       | \* id + id) - id \* id + (id + id) - id + (id + id) \* 5$                         | Desplazar           |
| 24  | $E + T / (T \*    | id + id) - id \* id + (id + id) - id + (id + id) \* 5$                            | Desplazar           |
| 25  | $E + T / (T \* id | + id) - id \* id + (id + id) - id + (id + id) \* 5$                               | Reducir F -> id     |
| 26  | $E + T / (T \* F  | + id) - id \* id + (id + id) - id + (id + id) \* 5$                               | Reducir T -> T \* F |
| 27  | $E + T / (T       | + id) - id \* id + (id + id) - id + (id + id) \* 5$                               | Reducir E -> T      |
| 28  | $E + T / (E       | + id) - id \* id + (id + id) - id + (id + id) \* 5$                               | Desplazar           |
| 29  | $E + T / (E +     | id) - id \* id + (id + id) - id + (id + id) \* 5$                                 | Desplazar           |
| 30  | $E + T / (E + id  | ) - id \* id + (id + id) - id + (id + id) \* 5$                                   | Desplazar           |
| 31  | $E + T / (E + F   | ) - id \* id + (id + id) - id + (id + id) \* 5$                                   | Reducir F -> id     |
| 32  | $E + T / (E + T   | ) - id \* id + (id + id) - id + (id + id) \* 5$                                   | Reducir T -> F      |
| 33  | $E + T / (E       | ) - id \* id + (id + id) - id + (id + id) \* 5$                                   | Reducir E -> E + T  |
| 34  | $E + T / (E)      | - id \* id + (id + id) - id + (id + id) \* 5$                                     | Desplazar           |
| 35  | $E + T / F        | - id \* id + (id + id) - id + (id + id) \* 5$                                     | Reducir F -> (E)    |
| 36  | $E + T            | - id \* id + (id + id) - id + (id + id) \* 5$                                     | Reducir T -> T / F  |
| 37  | $E                | - id \* id + (id + id) - id + (id + id) \* 5$                                     | Reducir E -> E + T  |
| 38  | $E -              | id \* id + (id + id) - id + (id + id) \* 5$                                       | Desplazar           |
| 39  | $E - id           | \* id + (id + id) - id + (id + id) \* 5$                                          | Desplazar           |
| 40  | $E - F            | \* id + (id + id) - id + (id + id) \* 5$                                          | Reducir F -> id     |
| 41  | $E - T            | \* id + (id + id) - id + (id + id) \* 5$                                          | Reducir T -> F      |
| 42  | $E - T \*         | id + (id + id) - id + (id + id) \* 5$                                             | Desplazar           |
| 43  | $E - T \* id      | + (id + id) - id + (id + id) \* 5$                                                | Reducir F -> id     |
| 44  | $E - T \* F       | + (id + id) - id + (id + id) \* 5$                                                | Reducir T -> T \* F |
| 45  | $E - T            | + (id + id) - id + (id + id) \* 5$                                                | Reducir E -> E - T  |
| 46  | $E                | + (id + id) - id + (id + id) \* 5$                                                | Desplazar           |
| 47  | $E +              | (id + id) - id + (id + id) \* 5$                                                  | Desplazar           |
| 48  | $E + (            | id + id) - id + (id + id) \* 5$                                                   | Desplazar           |
| 49  | $E + (id          | + id) - id + (id + id) \* 5$                                                      | Desplazar           |
| 50  | $E + (F           | + id) - id + (id + id) \* 5$                                                      | Reducir F -> id     |
| 51  | $E + (T           | + id) - id + (id + id) \* 5$                                                      | Reducir T -> F      |
| 52  | $E + (E           | + id) - id + (id + id) \* 5$                                                      | Reducir E -> T      |
| 53  | $E + (E +         | id) - id + (id + id) \* 5$                                                        | Desplazar           |
| 54  | $E + (E + id      | ) - id + (id + id) \* 5$                                                          | Desplazar           |
| 55  | $E + (E + F       | ) - id + (id + id) \* 5$                                                          | Reducir F -> id     |
| 56  | $E + (E + T       | ) - id + (id + id) \* 5$                                                          | Reducir T -> F      |
| 57  | $E + (E           | ) - id + (id + id) \* 5$                                                          | Reducir E -> E + T  |
| 58  | $E + (E)          | - id + (id + id) \* 5$                                                            | Desplazar           |
| 59  | $E + F            | - id + (id + id) \* 5$                                                            | Reducir F -> (E)    |
| 60  | $E + T            | - id + (id + id) \* 5$                                                            | Reducir T -> F      |
| 61  | $E                | - id + (id + id) \* 5$                                                            | Reducir E -> E + T  |
| 62  | $E -              | id + (id + id) \* 5$                                                              | Desplazar           |
| 63  | $E - id           | + (id + id) \* 5$                                                                 | Desplazar           |
| 64  | $E - F            | + (id + id) \* 5$                                                                 | Reducir F -> id     |
| 65  | $E - T            | + (id + id) \* 5$                                                                 | Reducir T -> F      |
| 66  | $E                | + (id + id) \* 5$                                                                 | Reducir E -> E - T  |
| 67  | $E +              | (id + id) \* 5$                                                                   | Desplazar           |
| 68  | $E + (            | id + id) \* 5$                                                                    | Desplazar           |
| 69  | $E + (id          | + id) \* 5$                                                                       | Reducir F -> id     |
| 70  | $E + (F           | + id) \* 5$                                                                       | Reducir T -> F      |
| 71  | $E + (T           | + id) \* 5$                                                                       | Reducir E -> T      |
| 72  | $E + (E           | + id) \* 5$                                                                       | Desplazar           |
| 73  | $E + (E +         | id) \* 5$                                                                         | Desplazar           |
| 74  | $E + (E + id      | ) \* 5$                                                                           | Reducir F -> id     |
| 75  | $E + (E + F       | ) \* 5$                                                                           | Reducir T -> F      |
| 76  | $E + (E + T       | ) \* 5$                                                                           | Reducir E -> E + T  |
| 77  | $E + (E           | ) \* 5$                                                                           | Desplazar           |
| 78  | $E + (E)          | \* 5$                                                                             | Desplazar           |
| 79  | $E + F            | \* 5$                                                                             | Reducir F -> (E)    |
| 80  | $E + T            | \* 5$                                                                             | Reducir T -> F      |
| 81  | $E + T \*         | 5$                                                                                | Desplazar           |
| 82  | $E + T \* 5       | $                                                                                 | Reducir F -> num    |
| 83  | $E + T \* F       | $                                                                                 | Reducir T -> T \* F |
| 84  | $E + T            | $                                                                                 | Reducir E -> E + T  |
| 85  | $E                | $                                                                                 | Reducir E' -> E     |
| 86  | $E'               | $                                                                                 | Aceptar             |

Ejercicio #2

| #   | Pila                | Cadena                                                                            | Acciones            |
| --- | ------------------- | --------------------------------------------------------------------------------- | ------------------- |
| 1   | $                   | (5 + 16 \* 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$ | Desplazar           |
| 2   | $(                  | 5 + 16 \* 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$  | Desplazar           |
| 3   | $(5                 | + 16 \* 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$    | Desplazar           |
| 4   | $(F                 | + 16 \* 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$    | Reducir F -> num    |
| 5   | $(T                 | + 16 \* 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$    | Reducir T -> F      |
| 6   | $(E                 | + 16 \* 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$    | Reducir E -> T      |
| 7   | $(E +               | 16 \* 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$      | Desplazar           |
| 8   | $(E + 16            | \* 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$         | Reducir F -> num    |
| 9   | $(E + F             | \* 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$         | Reducir T -> F      |
| 10  | $(E + T             | \* 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$         | Desplazar           |
| 11  | $(E + T \*          | 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$            | Desplazar           |
| 12  | $(E + T \* 3        | 3) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$            | Desplazar           |
| 13  | $(E + T \* F        | ) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$             | Reducir F -> num    |
| 14  | $(E + T             | ) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$             | Reducir T -> T \* F |
| 15  | $(E                 | ) / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$             | Reducir E -> E + T  |
| 16  | $(E)                | / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$               | Desplazar           |
| 17  | $F                  | / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$               | Reducir F -> (E)    |
| 18  | $T                  | / (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$               | Reducir T -> F      |
| 19  | $T /                | (10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                 | Desplazar           |
| 20  | $T / (              | 10 / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                  | Desplazar           |
| 21  | $T / (10            | / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                     | Desplazar           |
| 22  | $T / (F             | / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                     | Reducir F -> num    |
| 23  | $T / (T             | / 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                     | Reducir T -> F      |
| 24  | $T / (T /           | 2 + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                       | Desplazar           |
| 25  | $T / (T / 2         | + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                         | Desplazar           |
| 26  | $T / (T / F         | + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                         | Reducir F -> num    |
| 27  | $T / (T             | + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                         | Reducir T -> T / F  |
| 28  | $T / (E             | + 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                         | Reducir E -> T      |
| 29  | $T / (E +           | 1) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                           | Desplazar           |
| 30  | $T / (E + 1         | ) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                            | Desplazar           |
| 31  | $T / (E + F         | ) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                            | Reducir F -> num    |
| 32  | $T / (E + T         | ) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                            | Reducir T -> F      |
| 33  | $T / (E             | ) + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                            | Reducir E -> E + T  |
| 34  | $T / (E)            | + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                              | Desplazar           |
| 35  | $T / F              | + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                              | Reducir F -> (E)    |
| 36  | $T                  | + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                              | Reducir T -> T / F  |
| 37  | $E                  | + 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                              | Reducir E -> T      |
| 38  | $E +                | 5 / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                | Desplazar           |
| 39  | $E + 5              | / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                  | Desplazar           |
| 40  | $E + F              | / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                  | Reducir F -> num    |
| 41  | $E + T              | / (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                  | Reducir T -> F      |
| 42  | $E + T /            | (4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                    | Desplazar           |
| 43  | $E + T / (          | 4 - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                     | Desplazar           |
| 44  | $E + T / (4         | - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                       | Desplazar           |
| 45  | $E + T / (F         | - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                       | Reducir F -> num    |
| 46  | $E + T / (T         | - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                       | Reducir T -> F      |
| 47  | $E + T / (E         | - 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                       | Reducir E -> T      |
| 48  | $E + T / (E -       | 6 + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                         | Desplazar           |
| 49  | $E + T / (E - 6     | + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                           | Desplazar           |
| 50  | $E + T / (E - F     | + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                           | Reducir F -> num    |
| 51  | $E + T / (E - T     | + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                           | Reducir T -> F      |
| 52  | $E + T / (E         | + 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                           | Reducir E -> E - T  |
| 53  | $E + T / (E +       | 18 / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                             | Desplazar           |
| 54  | $E + T / (E + 18    | / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                                | Desplazar           |
| 55  | $E + T / (E + F     | / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                                | Reducir F -> num    |
| 56  | $E + T / (E + T     | / 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                                | Reducir T -> F      |
| 57  | $E + T / (E + T /   | 2) + (25 - 3) / 7 + 18 \* 6 - 2$                                                  | Desplazar           |
| 58  | $E + T / (E + T / 2 | ) + (25 - 3) / 7 + 18 \* 6 - 2$                                                   | Desplazar           |
| 59  | $E + T / (E + T / F | ) + (25 - 3) / 7 + 18 \* 6 - 2$                                                   | Reducir F -> num    |
| 60  | $E + T / (E + T     | ) + (25 - 3) / 7 + 18 \* 6 - 2$                                                   | Reducir T -> T / F  |
| 61  | $E + T / (E         | ) + (25 - 3) / 7 + 18 \* 6 - 2$                                                   | Reducir E -> E + T  |
| 62  | $E + T / (E)        | + (25 - 3) / 7 + 18 \* 6 - 2$                                                     | Desplazar           |
| 63  | $E + T / F          | + (25 - 3) / 7 + 18 \* 6 - 2$                                                     | Reducir F -> (E)    |
| 64  | $E + T              | + (25 - 3) / 7 + 18 \* 6 - 2$                                                     | Reducir T -> T / F  |
| 65  | $E                  | + (25 - 3) / 7 + 18 \* 6 - 2$                                                     | Reducir E -> E + T  |
| 66  | $E +                | (25 - 3) / 7 + 18 \* 6 - 2$                                                       | Desplazar           |
| 67  | $E + (              | 25 - 3) / 7 + 18 \* 6 - 2$                                                        | Desplazar           |
| 68  | $E + (25            | - 3) / 7 + 18 \* 6 - 2$                                                           | Desplazar           |
| 69  | $E + (F             | - 3) / 7 + 18 \* 6 - 2$                                                           | Reducir F -> num    |
| 70  | $E + (T             | - 3) / 7 + 18 \* 6 - 2$                                                           | Reducir T -> F      |
| 71  | $E + (E             | - 3) / 7 + 18 \* 6 - 2$                                                           | Reducir E -> T      |
| 72  | $E + (E -           | 3) / 7 + 18 \* 6 - 2$                                                             | Desplazar           |
| 73  | $E + (E - 3         | ) / 7 + 18 \* 6 - 2$                                                              | Desplazar           |
| 74  | $E + (E - F         | ) / 7 + 18 \* 6 - 2$                                                              | Reducir F -> num    |
| 75  | $E + (E - T         | ) / 7 + 18 \* 6 - 2$                                                              | Reducir T -> F      |
| 76  | $E + (E             | ) / 7 + 18 \* 6 - 2$                                                              | Reducir E -> E - T  |
| 77  | $E + (E)            | / 7 + 18 \* 6 - 2$                                                                | Desplazar           |
| 78  | $E + F              | / 7 + 18 \* 6 - 2$                                                                | Reducir F -> (E)    |
| 79  | $E + T              | / 7 + 18 \* 6 - 2$                                                                | Reducir T -> F      |
| 80  | $E + T /            | 7 + 18 \* 6 - 2$                                                                  | Desplazar           |
| 81  | $E + T / 7          | + 18 \* 6 - 2$                                                                    | Desplazar           |
| 82  | $E + T / F          | + 18 \* 6 - 2$                                                                    | Reducir F -> num    |
| 83  | $E + T              | + 18 \* 6 - 2$                                                                    | Reducir T -> T / F  |
| 84  | $E                  | + 18 \* 6 - 2$                                                                    | Reducir E -> E + T  |
| 85  | $E +                | 18 \* 6 - 2$                                                                      | Desplazar           |
| 86  | $E + 18             | \* 6 - 2$                                                                         | Desplazar           |
| 87  | $E + F              | \* 6 - 2$                                                                         | Reducir F -> num    |
| 88  | $E + T              | \* 6 - 2$                                                                         | Reducir T -> F      |
| 89  | $E + T \*           | 6 - 2$                                                                            | Desplazar           |
| 90  | $E + T \* 6         | - 2$                                                                              | Desplazar           |
| 91  | $E + T \* F         | - 2$                                                                              | Reducir F -> num    |
| 92  | $E + T              | - 2$                                                                              | Reducir T -> T \* F |
| 93  | $E                  | - 2$                                                                              | Reducir E -> E + T  |
| 94  | $E -                | 2$                                                                                | Desplazar           |
| 95  | $E - 2              | $                                                                                 | Desplazar           |
| 96  | $E - F              | $                                                                                 | Reducir F -> num    |
| 97  | $E - T              | $                                                                                 | Reducir T -> F      |
| 98  | $E                  | $                                                                                 | Reducir E -> E - T  |
| 99  | $E'                 | $                                                                                 | Reducir E' -> E     |
