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

int main (int argc, char *argv[]){
  gpio *gpio_saida;
  gpio_saida = libsoc_gpio_request(get_id(4), LS_GPIO_SHARED);
  libsoc_gpio_set_direction (gpio_saida, OUTPUT);

  if (strcmp(argv[1], "1") == 0){
    libsoc_gpio_set_level (gpio_saida, HIGH);
    printf("On\n");
  }
  else if (strcmp(argv[1], "0") == 0){
    libsoc_gpio_set_level (gpio_saida, LOW);
    printf("Off\n");
  } else {
    printf("Erro\n");
  }

  libsoc_gpio_free (gpio_saida);
  return 0;
}

int get_id (int porta){
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
