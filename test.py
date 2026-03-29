from pixel_art import create, set_pixel, fill_rect, draw_line, to_ppm, scale
img = create(8, 8, (0,0,0))
set_pixel(img, 0, 0, (255,0,0))
assert img[0][0] == (255,0,0)
fill_rect(img, 2, 2, 3, 3, (0,255,0))
assert img[3][3] == (0,255,0)
ppm = to_ppm(img)
assert ppm.startswith(b"P6")
s = scale(img, 2)
assert len(s) == 16 and len(s[0]) == 16
print("Pixel art tests passed")