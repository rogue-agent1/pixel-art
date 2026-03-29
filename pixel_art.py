#!/usr/bin/env python3
"""Pixel art generator outputting PPM format."""

class Canvas:
    def __init__(self, width, height, bg=(0,0,0)):
        self.width = width
        self.height = height
        self.pixels = [[bg for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color

    def get_pixel(self, x, y):
        return self.pixels[y][x]

    def fill_rect(self, x, y, w, h, color):
        for dy in range(h):
            for dx in range(w):
                self.set_pixel(x+dx, y+dy, color)

    def draw_line(self, x0, y0, x1, y1, color):
        dx, dy = abs(x1-x0), abs(y1-y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        while True:
            self.set_pixel(x0, y0, color)
            if x0 == x1 and y0 == y1: break
            e2 = 2 * err
            if e2 > -dy: err -= dy; x0 += sx
            if e2 < dx: err += dx; y0 += sy

    def to_ppm(self) -> bytes:
        header = f"P6\n{self.width} {self.height}\n255\n".encode()
        data = bytearray()
        for row in self.pixels:
            for r, g, b in row:
                data.extend([r, g, b])
        return header + bytes(data)

    def save(self, path):
        with open(path, "wb") as f:
            f.write(self.to_ppm())

if __name__ == "__main__":
    c = Canvas(16, 16, (30, 30, 30))
    c.fill_rect(4, 4, 8, 8, (255, 0, 0))
    c.draw_line(0, 0, 15, 15, (0, 255, 0))
    c.save("pixel_art.ppm")
    print("Saved pixel_art.ppm")

def test():
    c = Canvas(8, 8, (0, 0, 0))
    assert c.get_pixel(0, 0) == (0, 0, 0)
    c.set_pixel(3, 3, (255, 0, 0))
    assert c.get_pixel(3, 3) == (255, 0, 0)
    # Out of bounds
    c.set_pixel(-1, -1, (255, 255, 255))
    c.set_pixel(100, 100, (255, 255, 255))
    # Fill rect
    c.fill_rect(0, 0, 2, 2, (0, 255, 0))
    assert c.get_pixel(0, 0) == (0, 255, 0)
    assert c.get_pixel(1, 1) == (0, 255, 0)
    # PPM
    ppm = c.to_ppm()
    assert ppm.startswith(b"P6\n8 8\n255\n")
    assert len(ppm) == len("P6\n8 8\n255\n") + 8*8*3
    # Line
    c.draw_line(0, 0, 7, 7, (255, 255, 255))
    assert c.get_pixel(4, 4) == (255, 255, 255)
    print("  pixel_art: ALL TESTS PASSED")
