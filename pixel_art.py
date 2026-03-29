import argparse, json

PALETTE = {
    "0": " ", "1": "░", "2": "▒", "3": "▓", "4": "█",
    "r": "\033[31m█\033[0m", "g": "\033[32m█\033[0m",
    "b": "\033[34m█\033[0m", "y": "\033[33m█\033[0m",
    "c": "\033[36m█\033[0m", "m": "\033[35m█\033[0m",
    "w": "\033[37m█\033[0m",
}

def render(data, scale=1):
    for row in data:
        line = ""
        for pixel in row:
            char = PALETTE.get(str(pixel), str(pixel))
            line += char * scale
        for _ in range(scale):
            print(line)

def make_sprite(name):
    sprites = {
        "heart": [
            "0rr0rr0",
            "rrrrrrr",
            "rrrrrrr",
            "0rrrrr0",
            "00rrr00",
            "000r000",
        ],
        "smiley": [
            "0yyyy0",
            "y0yy0y",
            "yyyyyy",
            "y0000y",
            "yy00yy",
            "0yyyy0",
        ],
        "mushroom": [
            "00rrr00",
            "0rrrrr0",
            "rr4rr4r",
            "rrrrrrr",
            "0w4w4w0",
            "00www00",
            "00www00",
        ],
    }
    return sprites.get(name, sprites["heart"])

def main():
    p = argparse.ArgumentParser(description="Pixel art renderer")
    p.add_argument("--sprite", choices=["heart", "smiley", "mushroom"], default="heart")
    p.add_argument("--scale", type=int, default=2)
    p.add_argument("--file", help="JSON pixel data file")
    p.add_argument("--list-palette", action="store_true")
    args = p.parse_args()
    if args.list_palette:
        for k, v in PALETTE.items(): print(f"  {k} -> {v}")
        return
    if args.file:
        data = json.load(open(args.file))
    else:
        data = make_sprite(args.sprite)
    render(data, args.scale)

if __name__ == "__main__":
    main()
