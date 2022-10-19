def nastav_diodu(číslo: number):
    pass
def zhasni_diodu2():
    pins.digital_write_pin(DigitalPin.P0, 0)
def rozsvit_diodu():
    pins.digital_write_pin(DigitalPin.P0, 1)

def on_forever():
    pass
basic.forever(on_forever)
