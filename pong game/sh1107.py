import framebuf

class SH1107:
    def __init__(self, width, height, i2c, addr=0x3C):
        self.width = width
        self.height = height
        self.i2c = i2c
        self.addr = addr
        self.pages = height // 8
        self.buffer = bytearray(self.width * self.pages)
        self.fb = framebuf.FrameBuffer(
            self.buffer, self.width, self.height, framebuf.MONO_VLSB
        )
        self.init_display()

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, bytearray([0x00, cmd]))

    def write_data(self, data):
        self.i2c.writeto(self.addr, b'\x40' + data)

    def init_display(self):
        cmds = [
            0xAE,             # Display OFF
            0xDC, 0x00,       # Display start line
            0x81, 0x2F,       # Contrast
            0x20, 0xA0,       # Segment remap
            0xC0,             # COM scan direction
            0xA6,             # Normal display
            0xA8, 0x7F,       # Multiplex ratio = 128
            0xD3, 0x00,       # Display offset
            0xD5, 0x51,       # Clock
            0xD9, 0x22,       # Precharge
            0xDB, 0x35,       # VCOM
            0xAF              # Display ON
        ]
        for c in cmds:
            self.write_cmd(c)
        self.fill(0)
        self.show()

    def show(self):
        for page in range(self.pages):
            self.write_cmd(0xB0 + page)
            self.write_cmd(0x02)
            self.write_cmd(0x10)
            start = self.width * page
            end = start + self.width
            self.write_data(self.buffer[start:end])

    # FrameBuffer helpers
    def fill(self, c): self.fb.fill(c)
    def text(self, s, x, y, c=1): self.fb.text(s, x, y, c)
    def pixel(self, x, y, c=1): self.fb.pixel(x, y, c)
    def rect(self, x, y, w, h, c=1): self.fb.rect(x, y, w, h, c)
    def fill_rect(self, x, y, w, h, c=1): self.fb.fill_rect(x, y, w, h, c)
