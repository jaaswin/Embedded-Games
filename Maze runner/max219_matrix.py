# max7219_matrix.py
from machine import SPI, Pin
import time

# registers
_NOOP = 0x00
_DIG0 = 0x01
_DECODE = 0x09
_INTENSITY = 0x0A
_SCAN_LIMIT = 0x0B
_SHUTDOWN = 0x0C
_DISPLAY_TEST = 0x0F

class MAX7219:
    def __init__(self, spi, cs_pin, n=1):
        self.spi = spi
        self.cs = Pin(cs_pin, Pin.OUT)
        self.n = n
        self.init()

    def _write(self, register, data):
        # for cascaded modules, send (reg, data) pairs n times. Here we support identical for all modules.
        buf = bytearray()
        for _ in range(self.n):
            buf.append(register)
            buf.append(data)
        self.cs.value(0)
        self.spi.write(buf)
        self.cs.value(1)

    def init(self):
        self._write(_SHUTDOWN, 0x01)     # normal operation
        self._write(_DISPLAY_TEST, 0x00) # no test
        self._write(_SCAN_LIMIT, 0x07)   # display all 8 digits
        self._write(_DECODE, 0x00)       # no decode (matrix)
        self.set_intensity(6)
        self.clear()

    def set_intensity(self, intensity):
        if intensity < 0: intensity = 0
        if intensity > 15: intensity = 15
        self._write(_INTENSITY, intensity)

    def clear(self):
        for row in range(8):
            self._write(_DIG0 + row, 0x00)

    def pixel(self, x, y, on):
        # Note: to avoid keeping a whole display buffer in this small driver,
        # we maintain an internal buffer (8 bytes).
        if not hasattr(self, '_buf'):
            self._buf = [0]*8
        if 0 <= x < 8 and 0 <= y < 8:
            mask = 1 << x
            if on:
                self._buf[y] |= mask
            else:
                self._buf[y] &= ~mask
            # MAX7219 rows: digit1->row0 ... digit8->row7
            self._write(_DIG0 + y, self._buf[y])

    def draw_buffer(self, buf8):
        # buf8: list of 8 bytes where bit0 = column 0, bit7 = column7 (x)
        for row in range(8):
            self._buf = buf8[:]  # keep for pixel operations too
            self._write(_DIG0 + row, buf8[row])
