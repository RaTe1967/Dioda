def zhasni_diodu():
    pins.digital_write_pin(DigitalPin.P0, 0)
def blikej(barva: number):
    while True:
        if barva == RED:
            pins.digital_write_pin(DigitalPin.P0, 1)
            basic.pause(500)
            pins.digital_write_pin(DigitalPin.P0, 0)
            basic.pause(200)
        elif barva == GREEN:
            pins.digital_write_pin(DigitalPin.P1, 1)
            basic.pause(500)
            pins.digital_write_pin(DigitalPin.P1, 0)
            basic.pause(200)
        else:
            pins.digital_write_pin(DigitalPin.P2, 1)
            basic.pause(500)
            pins.digital_write_pin(DigitalPin.P2, 0)
            basic.pause(200)
        if prerus == 1:
            break

def on_button_pressed_a():
    zmen_pauzu(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global prerus
    prerus = 0
    blikej(GREEN)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def nastav_diodu(param: number):
    pins.digital_write_pin(DigitalPin.P0, param)

def on_button_pressed_b():
    zmen_pauzu(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global prerus
    prerus = 1
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def prepni_diodu(barva2: number):
    global red_is_on, green_is_on, blue_is_on
    if barva2 == RED:
        if red_is_on == 1:
            red_is_on = 0
        else:
            red_is_on = 1
        pins.digital_write_pin(DigitalPin.P0, blue_is_on)
    elif barva2 == GREEN:
        if green_is_on == 1:
            green_is_on = 0
        else:
            green_is_on = 1
        pins.digital_write_pin(DigitalPin.P1, green_is_on)
    elif barva2 == BLUE:
        if blue_is_on == 1:
            blue_is_on = 0
        else:
            blue_is_on = 1
        pins.digital_write_pin(DigitalPin.P2, blue_is_on)
def rozsvit_diodu():
    pins.digital_write_pin(DigitalPin.P0, 1)
def zmen_pauzu(prodluz: number):
    global pauza
    if pauza <= 900 and prodluz == 1 or pauza >= 200 and prodluz == 0:
        if prodluz == 1:
            pauza += 100
        else:
            pauza += -100
prerus = 0
pauza = 0
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
pauza = 500
prerus = 0

def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 1)
    basic.pause(pauza)
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.pause(pauza)
basic.forever(on_forever)
