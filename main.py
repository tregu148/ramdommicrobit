def on_button_pressed_a():
    global aaa
    aaa = aaa + 1
    if aaa > 4:
        aaa = 0
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global bbb
    bbb = bbb + 1
    if bbb > 4:
        bbb = 0
    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

bbb = 0
aaa = 0
aaa = 0
bbb = 0

def on_forever():
    pass
basic.forever(on_forever)

def on_every_interval():
    led.plot(aaa, bbb)
loops.every_interval(100, on_every_interval)
