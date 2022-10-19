def zhasni_diodu():
    pins.digital_write_pin(DigitalPin.P0, 0)
def nastav_diodu(param: number):
    pins.digital_write_pin(DigitalPin.P0, param)
def rozsvit_diodu():
    pins.digital_write_pin(DigitalPin.P0, 1)

def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 1)
    basic.pause(500)
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.pause(200)
basic.forever(on_forever)
