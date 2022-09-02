1) Construtir una ER que permite generar un identificador en C

  a | b | c | ... | z | A | B | C | ... | Z (( a | b | c | ... | z | A | B | C | ... | Z ) | ( 0 | 1 | 2 | 3 | ... | 9 ) | _ ) *

2) Construir ER para recorrer números como: 8, -15, 2000, 15834, 2.83, -4.16

  ( 0 | 1 | ... | 9 )( 0 | 1 | ... | 9 ) * | - ( 0 | 1 | ... | 9 )( 0 | 1 | ... | 9 ) * |
  ( 0 | 1 | ... | 9 )( 0 | 1 | ... | 9 ) * . ( 0 | 1 | ... | 9 )( 0 | 1 | ... | 9 ) * | 
  - ( 0 | 1 | ... | 9 )( 0 | 1 | ... | 9 ) * . ( 0 | 1 | ... | 9 )( 0 | 1 | ... | 9 ) *

3) Construir una ER que permita generar número de telefono celular en colombia

  3 ( 1 | 2 | 3 | 4 | 5 )( 0 | 1 | 2 | ... | 9 ) + { 8 }
