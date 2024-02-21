let aaa = 0
let bbb = 0
loops.everyInterval(1000, function () {
    led.unplot(aaa, bbb)
    aaa += randint(0, 2) - 1
    bbb += randint(0, 2) - 1
    if (aaa > 4) {
        aaa = 4
    } else {
        if (aaa < 0) {
            aaa = 0
        } else {
        	
        }
    }
    if (bbb > 4) {
        bbb = 4
    } else {
        if (bbb < 0) {
            bbb = 0
        } else {
        	
        }
    }
    led.plot(aaa, bbb)
})
basic.forever(function () {
	
})
