1) Utilizar DR para identificadores en C

  letra -> [a-z A-Z]
  digito -> [0-9]
  id -> letra(letra| digito | _ ) *

2) Utilizar DR para generar número como: 8, -3, 2.45, -6.8, 15E2, 1.8E-3, 45E2.6

  digito -> [ 0-9 ]
  digitos -> digito+
  num -> (-)? digitos ( . digitos )? ( E (-)? digitos(.digitos)? )?

EJERCICIO:

Construir definiciones regulares para generar correos electonicos bien escritos

 letras -> [ a - z A - Z ]
 digito -> [ 0 - 9 ]
 correo -> letras ( letras | digito | _ | . )* @ letras+ . (letras) + { 3 } . ( letras + { 2 } ) ?
