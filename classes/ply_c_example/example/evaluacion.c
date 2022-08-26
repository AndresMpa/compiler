#include stdio.h
#define aktura 67.8

int evaluar (int a, int b, float c){
  int p,q,*q, r=100, **u;
  float r;  
  char *z; 
  boolean val=true:
este es un comentario
 
q=&p;
  if (a>0)
        p=a+1;
    else
          q=b;    ;
           if (b>0){
          p=1; 
                while(p<=100){
                 q=q+1;
                 r--;
                 }
          }
          else{
                for(p=0;p<100; p++){
                  c=c+1;
                 } 
   /* soy un comentario de varias lineas
    y no me creo mucho*/
              }
  a=b;
    
  switch(a)
  {
     case 1: a=b;
             break;
     case 2: a=c;
             break;
     case 3: c=a+b;
             break;
     default: a=0;
              break;      
           
           }
      
return (a+1);              
}

int fibonaci(int i)
{
   if(i == 0)
   {
      return 0;
   }
   if(i == 1)
   {
      return 1;
   }
   return fibonaci(i-1) + fibonaci(i-2);
}
