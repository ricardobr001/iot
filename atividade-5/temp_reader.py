"""Temperature sensor module."""
########################################################
# Topicos Avancados em Redes de Computadores - Grupo 9
#######################################################
#
#                                                        
# ROBSON MIRIM DO CARMO
# Atividade 5 -> Le Temperatura               
#######################################################
import spidev
from libsoc import gpio
from time import sleep

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 10000
spi.mode = 0b00
spi.bits_per_word = 8
channel_select = [0x01, 0xA0, 0x00]


def get():
    """Get temperature."""
    gpio_cs = gpio.GPIO(18, gpio.DIRECTION_OUTPUT)
    gpio_cs.set_high()
    with gpio.request_gpios([gpio_cs]):
        gpio_cs.set_low()
        rx = spi.xfer(channel_select)
        gpio_cs.set_high()
        adc_value = (rx[1] << 8) & 0b1100000000
        adc_value = adc_value | (rx[2] & 0xff)

    return adc_value

if __name__ == '__main__':
    print("ADC Value: %d" % get())

