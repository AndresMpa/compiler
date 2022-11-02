# Taller

Completar los siguientes ejercicios

### 1) Sea la gramática

S -> (S) S | e

- AFD LR(0) correspondiente a esta gramática
- Muestre las acciones de análisis sintáctico para la entrada: ((())(()()))

![Punto_1_AFD_LR(0)](<./Taller_P1_AFD_LR(0).png>)

| #   | Pila                       | Cadena        | Acciones          |
| --- | -------------------------- | ------------- | ----------------- |
| 1   | $0                         | ((())(()()))$ | Desplazar         |
| 2   | $0(2                       | (())(()()))$  | Desplazar         |
| 3   | $0(2(2                     | ())(()()))$   | Desplazar         |
| 4   | $0(2(2(2                   | ))(()()))$    | Reducir S -> e    |
| 5   | $0(2(2(2S3                 | ))(()()))$    | Desplazar         |
| 6   | $0(2(2(2S3)                | )(()()))$     | Reducir S -> e    |
| 7   | $0(2(2(2S3)S5              | )(()()))$     | Reducir S -> (S)S |
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
