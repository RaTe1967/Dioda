function zhasni_diodu () {
    pins.digitalWritePin(DigitalPin.P0, 0)
}
function nastav_diodu (param: number) {
    pins.digitalWritePin(DigitalPin.P0, param)
}
function rozsvit_diodu () {
    pins.digitalWritePin(DigitalPin.P0, 1)
}
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    basic.pause(500)
    pins.digitalWritePin(DigitalPin.P0, 0)
    basic.pause(200)
})
