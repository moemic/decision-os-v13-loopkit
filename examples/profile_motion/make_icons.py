"""Original, small, high-contrast demo icons; users may supply any PNG instead."""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).parent
S = 4


def save(name, draw_icon):
    im = Image.new("RGBA", (64*S, 64*S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    draw_icon(d)
    im.resize((64, 64), Image.Resampling.LANCZOS).save(ROOT / name)


def cat(d):
    # Deliberately large crown and ears: recognizable after README scaling.
    d.polygon([(12*S, 25*S), (13*S, 4*S), (26*S, 17*S), (38*S, 17*S), (51*S, 4*S), (52*S, 25*S)], fill="#070b18", outline="#bac7db", width=2*S)
    d.ellipse((7*S, 18*S, 57*S, 62*S), fill="#070b18", outline="#bac7db", width=2*S)
    d.polygon([(16*S, 12*S), (21*S, 4*S), (28*S, 12*S), (34*S, 3*S), (41*S, 12*S), (47*S, 5*S), (46*S, 23*S), (17*S, 23*S)], fill="#ffd672", outline="#805523")
    d.rectangle((17*S, 20*S, 46*S, 24*S), fill="#ecaa42")
    d.ellipse((29*S, 13*S, 35*S, 19*S), fill="#9056d4")
    d.ellipse((20*S, 37*S, 27*S, 42*S), fill="#68e8ef")
    d.ellipse((38*S, 37*S, 45*S, 42*S), fill="#68e8ef")
    d.polygon([(30*S, 46*S), (34*S, 46*S), (32*S, 49*S)], fill="#f5a4bd")
    for y, x2 in [(49, 15), (53, 13)]:
        d.line((26*S, y*S, x2*S, (y-2)*S), fill="#c6c7d4", width=S)
        d.line((38*S, y*S, (64-x2)*S, (y-2)*S), fill="#c6c7d4", width=S)


def fox(d):
    d.polygon([(5*S, 7*S), (19*S, 20*S), (32*S, 18*S), (45*S, 20*S), (59*S, 7*S), (54*S, 45*S), (43*S, 60*S), (21*S, 60*S), (10*S, 45*S)], fill="#f08152", outline="#582d39", width=2*S)
    d.polygon([(13*S, 14*S), (20*S, 26*S), (17*S, 33*S)], fill="#ffdbbd")
    d.polygon([(51*S, 14*S), (44*S, 26*S), (47*S, 33*S)], fill="#ffdbbd")
    d.polygon([(9*S, 40*S), (28*S, 47*S), (32*S, 54*S), (36*S, 47*S), (55*S, 40*S), (43*S, 60*S), (21*S, 60*S)], fill="#fff1dd")
    d.ellipse((20*S, 36*S, 26*S, 41*S), fill="#25203b")
    d.ellipse((38*S, 36*S, 44*S, 41*S), fill="#25203b")
    d.polygon([(28*S, 48*S), (36*S, 48*S), (32*S, 53*S)], fill="#392739")


if __name__ == "__main__":
    save("crowned_cat.png", cat)
    save("fox.png", fox)
