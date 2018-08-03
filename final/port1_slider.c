/* 

Compilar com a flag -lsoc
Informar apenas o numero da porta Digital de acordo com o Shield 
(de D1 a D4)

*/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "libsoc_gpio.h"
#include "libsoc_debug.h"

int get_id (int porta);		// retorna o gpio_id de acordo com a porta 

int main ()
{
  gpio *gpio_entrada;
  
  gpio_entrada = libsoc_gpio_request (get_id (1), LS_GPIO_SHARED);
  libsoc_gpio_set_direction (gpio_entrada, INPUT);
  
  if (libsoc_gpio_get_level (gpio_entrada) == HIGH)
    printf("1");
  else if (libsoc_gpio_get_level (gpio_entrada) == LOW)
    printf("0");
  else{
    printf ("-1");
  }

  libsoc_gpio_free (gpio_entrada);
  return 0;
}

int get_id (int porta)
{
  switch (porta)
    {
    case 1:
      return 36;
    case 2:
      return 13;
    case 3:
      return 115;
    case 4:
      return 24;
    default:
      return 0;
    }
  return 0;
}
