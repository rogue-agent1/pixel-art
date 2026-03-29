#!/usr/bin/env python3
"""pixel_art - ASCII art text renderer."""
import sys, argparse, json

FONT = {"A":["  #  ","# # #","#####","#   #","#   #"],"B":["#### ","#   #","#### ","#   #","#### "],"C":[" ####","#    ","#    ","#    "," ####"],"D":["#### ","#   #","#   #","#   #","#### "],"E":["#####","#    ","###  ","#    ","#####"],"F":["#####","#    ","###  ","#    ","#    "],"G":[" ####","#    ","# ###","#   #"," ####"],"H":["#   #","#   #","#####","#   #","#   #"],"I":["#####","  #  ","  #  ","  #  ","#####"],"L":["#    ","#    ","#    ","#    ","#####"],"M":["#   #","## ##","# # #","#   #","#   #"],"N":["#   #","##  #","# # #","#  ##","#   #"],"O":[" ### ","#   #","#   #","#   #"," ### "],"P":["#### ","#   #","#### ","#    ","#    "],"R":["#### ","#   #","#### ","# #  ","#  ##"],"S":[" ####","#    "," ### ","    #","#### "],"T":["#####","  #  ","  #  ","  #  ","  #  "],"U":["#   #","#   #","#   #","#   #"," ### "],"W":["#   #","#   #","# # #","## ##","#   #"],"X":["#   #"," # # ","  #  "," # # ","#   #"],"Y":["#   #"," # # ","  #  ","  #  ","  #  "],"Z":["#####","   # ","  #  "," #   ","#####"]," ":["     ","     ","     ","     ","     "]}

def render(text, char="#", space=" "):
    text = text.upper()
    lines = [""] * 5
    for ch in text:
        glyph = FONT.get(ch, FONT.get(" "))
        for i in range(5):
            lines[i] += glyph[i].replace("#", char).replace(" ", space) + space
    return "
".join(lines)

def main():
    p = argparse.ArgumentParser(description="ASCII art text")
    p.add_argument("text")
    p.add_argument("--char", default="#")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    art = render(args.text, args.char)
    if args.json:
        print(json.dumps({"text": args.text, "width": len(art.splitlines()[0]), "height": 5, "art": art}))
    else:
        print(art)

if __name__ == "__main__": main()
