#!/usr/bin/env python3
"""Pixel art generator (PPM format). Zero dependencies."""
import sys

def create(width, height, bg=(0,0,0)):
    return [[bg for _ in range(width)] for _ in range(height)]

def set_pixel(img, x, y, color):
    if 0 <= y < len(img) and 0 <= x < len(img[0]):
        img[y][x] = color

def fill_rect(img, x, y, w, h, color):
    for dy in range(h):
        for dx in range(w):
            set_pixel(img, x+dx, y+dy, color)

def draw_line(img, x0, y0, x1, y1, color):
    dx, dy = abs(x1-x0), abs(y1-y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        set_pixel(img, x0, y0, color)
        if x0 == x1 and y0 == y1: break
        e2 = 2 * err
        if e2 > -dy: err -= dy; x0 += sx
        if e2 < dx: err += dx; y0 += sy

def draw_circle(img, cx, cy, r, color):
    x, y, d = 0, r, 3 - 2*r
    while x <= y:
        for px, py in [(cx+x,cy+y),(cx-x,cy+y),(cx+x,cy-y),(cx-x,cy-y),
                        (cx+y,cy+x),(cx-y,cy+x),(cx+y,cy-x),(cx-y,cy-x)]:
            set_pixel(img, px, py, color)
        if d < 0: d += 4*x + 6
        else: d += 4*(x-y) + 10; y -= 1
        x += 1

def to_ppm(img):
    h, w = len(img), len(img[0])
    header = f"P6\n{w} {h}\n255\n"
    pixels = bytes(c for row in img for px in row for c in px)
    return header.encode() + pixels

def scale(img, factor):
    return [[img[y][x] for x in range(len(img[0])) for _ in range(factor)]
            for y in range(len(img)) for _ in range(factor)]

if __name__ == "__main__":
    img = create(16, 16, (30,30,30))
    fill_rect(img, 4, 4, 8, 8, (255,0,0))
    draw_circle(img, 8, 8, 6, (0,255,0))
    draw_line(img, 0, 0, 15, 15, (255,255,0))
    scaled = scale(img, 8)
    with open("output.ppm", "wb") as f:
        f.write(to_ppm(scaled))
    print("Wrote output.ppm (128x128)")
