def zhasni_diodu():
    pins.digital_write_pin(DigitalPin.P0, 0)
def blikej(barva: number):
    while True:
        if barva == RED:
            pins.digital_write_pin(DigitalPin.P0, 1)
            basic.pause(500)
            pins.digital_write_pin(DigitalPin.P0, 0)
            basic.pause(200)
        else:
            if barva == GREEN:
                pins.digital_write_pin(DigitalPin.P1, 1)
                basic.pause(500)
                pins.digital_write_pin(DigitalPin.P1, 0)
                basic.pause(200)
            else:
                pins.digital_write_pin(DigitalPin.P2, 1)
                basic.pause(500)
                pins.digital_write_pin(DigitalPin.P2, 0)
                basic.pause(200)

def on_button_pressed_a():
    blikej(GREEN)
input.on_button_pressed(Button.A, on_button_pressed_a)

def nastav_diodu(param: number):
    pins.digital_write_pin(DigitalPin.P0, param)

def on_button_pressed_b():
    prepni_diodu(BLUE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def prepni_diodu(barva2: number):
    global red_is_on, green_is_on, blue_is_on
    if barva2 == RED:
        if red_is_on == 1:
            red_is_on = 0
        else:
            red_is_on = 1
        pins.digital_write_pin(DigitalPin.P0, blue_is_on)
    else:
        if barva2 == GREEN:
            if green_is_on == 1:
                green_is_on = 0
            else:
                green_is_on = 1
            pins.digital_write_pin(DigitalPin.P1, green_is_on)
        else:
            if barva2 == BLUE:
                if blue_is_on == 1:
                    blue_is_on = 0
                else:
                    blue_is_on = 1
                pins.digital_write_pin(DigitalPin.P2, blue_is_on)
def rozsvit_diodu():
    pins.digital_write_pin(DigitalPin.P0, 1)
green_is_on = 0
blue_is_on = 0
red_is_on = 0
BLUE = 0
GREEN = 0
RED = 0
RED = 0
GREEN = 1
BLUE = 2
red_is_on = 0
blue_is_on = 0
green_is_on = 0

def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 1)
    basic.pause(500)
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.pause(200)
basic.forever(on_forever)
