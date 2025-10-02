# MicroPython MAX7219 8x8 LED matrix driver
# Works with Raspberry Pi Pico using SPI

from micropython import const
import framebuf

_DIGIT0 = const(1)
_DECODEMODE = const(9)
_INTENSITY = const(10)
_SCANLIMIT = const(11)
_SHUTDOWN = const(12)
_DISPLAYTEST = const(15)

class Matrix8x8(framebuf.FrameBuffer):
    def __init__(self, spi, cs, num):
        self.spi = spi
        self.cs = cs
        self.cs.init(cs.OUT, value=1)
        self.num = num
        self.buffer = bytearray(8 * num)
        super().__init__(self.buffer, 8 * num, 8, framebuf.MONO_HLSB)
        self.init()

    def _write(self, command, data):
        self.cs(0)
        for m in range(self.num):
            self.spi.write(bytearray([command, data]))
        self.cs(1)

    def init(self):
        for cmd, data in (
            (_SHUTDOWN, 0),
            (_DISPLAYTEST, 0),
            (_SCANLIMIT, 7),
            (_DECODEMODE, 0),
            (_SHUTDOWN, 1),
        ):
            self._write(cmd, data)
        self.fill(0)
        self.show()

    def brightness(self, val=7):
        if not 0 <= val <= 15:
            raise ValueError("Brightness must be 0-15")
        self._write(_INTENSITY, val)

    def show(self):
        for y in range(8):
            self.cs(0)
            for m in range(self.num):
                self.spi.write(bytearray([_DIGIT0 + y, self.buffer[y * self.num + m]]))
            self.cs(1)
