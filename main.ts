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
        } else if (barva == GREEN) {
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
        if (prerus == 1) {
            break;
        }
    }
}
input.onButtonPressed(Button.A, function () {
    zmen_pauzu(1)
})
input.onButtonPressed(Button.AB, function () {
    prerus = 0
    blikej(GREEN)
})
function nastav_diodu (param: number) {
    pins.digitalWritePin(DigitalPin.P0, param)
}
input.onButtonPressed(Button.B, function () {
    zmen_pauzu(0)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    prerus = 1
})
function prepni_diodu (barva2: number) {
    if (barva2 == RED) {
        if (red_is_on == 1) {
            red_is_on = 0
        } else {
            red_is_on = 1
        }
        pins.digitalWritePin(DigitalPin.P0, blue_is_on)
    } else if (barva2 == GREEN) {
        if (green_is_on == 1) {
            green_is_on = 0
        } else {
            green_is_on = 1
        }
        pins.digitalWritePin(DigitalPin.P1, green_is_on)
    } else if (barva2 == BLUE) {
        if (blue_is_on == 1) {
            blue_is_on = 0
        } else {
            blue_is_on = 1
        }
        pins.digitalWritePin(DigitalPin.P2, blue_is_on)
    }
}
function rozsvit_diodu () {
    pins.digitalWritePin(DigitalPin.P0, 1)
}
function zmen_pauzu (prodluz: number) {
    if (pauza <= 900 && prodluz == 1 || pauza >= 200 && prodluz == 0) {
        if (prodluz == 1) {
            pauza += 100
        } else {
            pauza += -100
        }
    }
}
let prerus = 0
let pauza = 0
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
pauza = 500
prerus = 0
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    basic.pause(pauza)
    pins.digitalWritePin(DigitalPin.P0, 0)
    basic.pause(pauza)
})
