"""Tilt sensor module."""
########################################################
# Topicos Avancados em Redes de Computadores - Grupo 9
#######################################################
#
#                                                        
# CAIO HENRIQUE GIACOMELLI
# RAFAEL PEREIRA ALONSO
# RICARDO MENDES LEAL JUNIOR 
# ROBSON MIRIM DO CARMO

# Atividade 5 -> Verifica Tilt Conectado.desconectado
#######################################################
from libsoc_zero.GPIO import Tilt

tilt = Tilt('GPIO-C')


def get():
    """Get tilt."""
    if tilt.is_tilted():
        return 1
    else:
        return 0


if __name__ == '__main__':
    print("Tilted: %d" % get())

