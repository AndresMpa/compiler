# Acá va una imagen

| Tabla  | Letra | Digito |
| -------| ------| -------|
| q1     | q2    | -      |
| q2     | q2    | q2     |

digito -> [ 0 - 9 ]
digitos -> digito+
num -> (-)? digitos ( . digitos )? ( E (-)? digitos ( . digitos )? )?

EJERCICIO:

Construir una expresión regular, con definiciones y su automata, para generar horas en el formato, H:M
donde H sea 01 a 12 y M de 00 a 59

  hour -> 0 [ 1 - 9 ]+ | 1 [ 1 - 2 ]+
  minutes -> [ 0 - 5 ] [ 0 - 9 ]

  time -> hour : minutes
