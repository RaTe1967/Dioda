function zhasni_diodu () {
    pins.digitalWritePin(DigitalPin.P0, 0)
}
function blikej (barva: number) {
    while (true) {
        if (barva == RED) {
            pins.digitalWritePin(DigitalPin.P0, 1)
            basic.pause(500)
            pins.digitalWritePin(DigitalPin.P0, 0)
            basic.pause(200)
        } else {
            if (barva == GREEN) {
                pins.digitalWritePin(DigitalPin.P1, 1)
                basic.pause(500)
                pins.digitalWritePin(DigitalPin.P1, 0)
                basic.pause(200)
            } else {
                pins.digitalWritePin(DigitalPin.P2, 1)
                basic.pause(500)
                pins.digitalWritePin(DigitalPin.P2, 0)
                basic.pause(200)
            }
        }
    }
}
input.onButtonPressed(Button.A, function () {
    blikej(GREEN)
})
function nastav_diodu (param: number) {
    pins.digitalWritePin(DigitalPin.P0, param)
}
input.onButtonPressed(Button.B, function () {
    prepni_diodu(BLUE)
})
function prepni_diodu (barva: number) {
    if (barva == RED) {
        if (red_is_on == 1) {
            red_is_on = 0
        } else {
            red_is_on = 1
        }
        pins.digitalWritePin(DigitalPin.P0, blue_is_on)
    } else {
        if (barva == GREEN) {
            if (green_is_on == 1) {
                green_is_on = 0
            } else {
                green_is_on = 1
            }
            pins.digitalWritePin(DigitalPin.P1, green_is_on)
        } else {
            if (barva == BLUE) {
                if (blue_is_on == 1) {
                    blue_is_on = 0
                } else {
                    blue_is_on = 1
                }
                pins.digitalWritePin(DigitalPin.P2, blue_is_on)
            }
        }
    }
}
function rozsvit_diodu () {
    pins.digitalWritePin(DigitalPin.P0, 1)
}
let green_is_on = 0
let blue_is_on = 0
let red_is_on = 0
let BLUE = 0
let GREEN = 0
let RED = 0
RED = 0
GREEN = 1
BLUE = 2
red_is_on = 0
blue_is_on = 0
green_is_on = 0
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    basic.pause(500)
    pins.digitalWritePin(DigitalPin.P0, 0)
    basic.pause(200)
})
