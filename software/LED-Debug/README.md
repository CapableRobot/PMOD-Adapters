## LED Debug Migen Code

The `led-pmod.py` file here is a small driver for the LED Debug PMOD board.

| ![Top Render](../../images/CRBFH0_top.png?raw=true) | ![Bottom Render](../../images/CRBFH0_bottom.png?raw=true) |
| :-------------: | :-------------: |
| **Top Rendering**    | **Bottom Rendering** |

This PCB allows a single PMOD to control 64 LEDs via a 4:16 address decoder and 4 mask control signals.  It was originally designed by H.Poetzl as part of the [Apertus project](https://www.apertus.org/pmod-debug) and they provide example [VHDL code](https://github.com/apertus-open-source-cinema/alpha-software/blob/master/axi3_hdmi/pmod_debug.vhd) showing how to address the LEDs.

The python-based Migen code to address the LEDs is very simple

```python
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
```

This shows a few unique features to Migen (in comparison to Verilog or VHDL):

- The appropriate pins are requested from the passed-in platform object.
- Signals are automatically initialized to 0, so no reset logic or signal is needed.
- Generated logic is easy to change at build time.  Here, the clock divider changes when the package is simulated.

Also included in the code here are two examples of using this 'driver'.

#### Chasing

```python
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
```

This code starts at zero, every `maxperiod` ticks lights the next LED.  Once all leds are lit, every `maxperiod` ticks the LED which has been on the longest is turned off.

| <iframe src="https://player.vimeo.com/video/309325726?autoplay=1&loop=1&autopause=0" width="400" height="400" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> |
| :-------------: |
| ICE Breaker running Chasing Demo  |

| ![Simulation of chasing](led-chaser.png?raw=true) |
| :-------------: |
| Simulation of chasing |

#### Counting

```python
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
```

This code starts at zero, every `maxperiod` ticks increases the displayed value by 1.

| ![Simulation of counting](led-counter.png?raw=true) |
| :-------------: |
| Simulation of counting |
