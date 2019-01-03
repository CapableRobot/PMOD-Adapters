from migen import *
from migen.build.generic_platform import *
from migen.build.platforms import icebreaker

class ClockDiv(Module):
    def __init__(self, divbitwidth, divout, divtick):
        divcounter = Signal(divbitwidth+1)
        # count every clock tick
        self.sync += divcounter.eq(divcounter + 1)
        # output 50% duty cycle clock output
        self.comb += divout.eq(divcounter[divbitwidth])
        # output a one clock wide strobe
        divcounter_inv = Signal(divbitwidth)
        self.comb += divcounter_inv.eq(~divcounter[0:divbitwidth])
        self.comb += divtick.eq(divcounter_inv == 0)

class LedPmod(Module):
    def __init__(self, platform, value):
        
        clock = Signal()
        clock_strobe  = Signal()

        addr = Signal(4)
        mask = Signal(4)

        if platform == 'sim':
            div = 1
        else:
            div = 8

            for i in range(4):
                ledpmod_mask = platform.request("ledpmod_mask")
                ledpmod_addr = platform.request("ledpmod_addr")

                self.comb += ledpmod_mask.eq(mask.part(i,1))
                self.comb += ledpmod_addr.eq(addr.part(i,1))

        self.submodules.clk_div = ClockDiv(div, clock, clock_strobe)

        self.comb += mask.eq(Cat(
                        ~value.part(addr     ,1),
                        ~value.part(addr + 16,1),
                        ~value.part(addr + 32,1),
                        ~value.part(addr + 48,1)
                    ))

        self.sync += If(clock_strobe,
                            addr.eq(addr + 1),
                        )

class LedPmodCounter(Module):
    def __init__(self, platform, maxperiod):
        value = Signal(64)

        counter = Signal(max=maxperiod+1)
        period = Signal(max=maxperiod+1)

        self.submodules.leds = LedPmod(platform, value)
        
        self.comb += period.eq(maxperiod)
        self.sync += If(counter == 0,
                            value.eq(value + 1),
                            counter.eq(period),
                        ).Else(
                            counter.eq(counter - 1),
                        )

class LedPmodChaser(Module):
    
    def __init__(self, platform, maxperiod):
        NUM_LEDS = 64

        value = Signal(NUM_LEDS,reset=1)
        index = Signal(max=NUM_LEDS)

        counter = Signal(max=maxperiod+1)
        period = Signal(max=maxperiod+1)

        # Used to trigger the bit flip via the index.
        # without this signal, the active bit/LED will change
        # on every system clock (making it dimmer).
        strobe = Signal()

        self.submodules.leds = LedPmod(platform, value)
        
        self.comb += period.eq(maxperiod)
        self.sync += If(counter == 0,
                            index.eq(index + 1),
                            strobe.eq(1),
                            counter.eq(period),
                        ).Else(
                            counter.eq(counter - 1),
                        )

        for i in range(NUM_LEDS): 
            self.sync += If(index == i, If(strobe,
                            strobe.eq(0),
                            value[i].eq(~value[i]),
                        ))

def _test(dut):
    for i in range(1000):
        yield

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "sim":
            
            if sys.argv[2] == "counter":
                dut = LedPmodCounter('sim', 80)
            elif sys.argv[2] == "chaser":
                dut = LedPmodChaser('sim', 80)
            else:
                print("Don't know how to simulate that.  Options: [counter, chaser]")
                sys.exit(0)

            dut.clock_domains.cd_sys = ClockDomain("sys")
            run_simulation(dut, _test(dut), vcd_name="led_pmod.vcd")
    else:
        platform = icebreaker.Platform()

        platform.add_extension([
            ("ledpmod_addr", 0, Pins("PMOD1A:7")),
            ("ledpmod_addr", 1, Pins("PMOD1A:6")),
            ("ledpmod_addr", 2, Pins("PMOD1A:5")),
            ("ledpmod_addr", 3, Pins("PMOD1A:4")),
            ("ledpmod_mask", 0, Pins("PMOD1A:0")),
            ("ledpmod_mask", 1, Pins("PMOD1A:1")),
            ("ledpmod_mask", 2, Pins("PMOD1A:3")), # These are backwards on the LED board
            ("ledpmod_mask", 3, Pins("PMOD1A:2")), # These are backwards on the LED board
        ])

        
        if len(sys.argv) > 1 and sys.argv[1] == "counter":
            blinker = LedPmodCounter(platform, 500)
        else:
            blinker = LedPmodChaser(platform, 100000)

        platform.build(blinker)
        platform.create_programmer().flash(0, 'build/top.bin')