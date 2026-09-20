"""Deterministic, script-free README GIFs; never writes to GitHub's graph."""
import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import random
import subprocess
from PIL import Image, ImageColor, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).parent
W, H = 580, 164
STEP, X0, Y0 = 17, 40, 33
HEADING = "Technical Boundary Audit & Repair for AI Systems"


def font(size, bold=False):
    try:
        return ImageFont.truetype("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf", size)
    except OSError:
        return ImageFont.load_default(size=size)


def color(hex_value):
    rgb = ImageColor.getrgb(hex_value)
    if len(rgb) != 3:
        raise ValueError("Use opaque #RRGGBB colors")
    return rgb


def blend(a, b, ratio):
    return tuple(round(x * (1-ratio) + y * ratio) for x, y in zip(a, b))


def capture(username, output, start, end):
    """Optional one-time public contribution snapshot through authenticated gh."""
    query = ("query { user(login: " + json.dumps(username) + ") { "
             "contributionsCollection(from: " + json.dumps(start + "T00:00:00Z") + ", to: "
             + json.dumps(end + "T23:59:59Z") + ") { contributionCalendar { weeks { "
             "contributionDays { date contributionCount } } } } } }")
    result = subprocess.run(["gh", "api", "graphql", "-f", "query=" + query],
                            check=True, capture_output=True, text=True)
    weeks = json.loads(result.stdout)["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    days = [dict(date=day["date"], count=day["contributionCount"])
            for week in weeks for day in week["contributionDays"]]
    payload = {"username": username, "source": "GitHub GraphQL contributionsCollection snapshot",
               "observed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "days": days}
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def sample(username, output):
    """Explicitly synthetic activity for testing customization, never real data."""
    from datetime import date, timedelta
    start = date(2026, 3, 8)
    days = [dict(date=(start+timedelta(days=i)).isoformat(),
                 count=(i*7 % 13 if i % 4 else 0)) for i in range(196)]
    payload = {"username": username, "source": "SYNTHETIC example, not a GitHub contribution claim",
               "observed_at": "synthetic", "days": days}
    output.write_text(json.dumps(payload, indent=2) + "\n")


def activity_grid(data):
    entries = {d["date"]: d["count"] for d in data["days"]}
    if len(entries) != len(data["days"]) or any(type(v) is not int or v < 0 for v in entries.values()):
        raise ValueError("Activity dates must be unique, with nonnegative integer counts")
    # Input is a dated snapshot. Explicitly render only its final 28 calendar weeks.
    dates = sorted(entries)
    if not dates:
        raise ValueError("No activity days")
    from datetime import date, timedelta
    end = date.fromisoformat(dates[-1])
    sunday = end - timedelta(days=(end.weekday()+1) % 7)
    first = sunday - timedelta(weeks=27)
    return [[entries.get((first + timedelta(weeks=col, days=row)).isoformat(), 0)
             for row in range(7)] for col in range(28)]


def base_frame(username, data, accent):
    bg = (17, 23, 37)
    im = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((1, 1, W-2, H-2), radius=16, outline=(59, 72, 95), width=2)
    d.text((X0, 9), "@" + username, fill=(232, 239, 249), font=font(15, True))
    d.text((W-112, 11), "ACTIVITY", fill=(170, 185, 203), font=font(11, True))
    grid = activity_grid(data)
    shades = [(39, 49, 68), blend((45, 56, 73), accent, .29),
              blend((45, 56, 73), accent, .48), blend((45, 56, 73), accent, .72), accent]
    for col in range(28):
        for row in range(7):
            n = grid[col][row]
            level = 0 if n == 0 else 1 if n < 3 else 2 if n < 6 else 3 if n < 10 else 4
            x, y = X0 + col*STEP, Y0 + row*STEP
            d.rounded_rectangle((x, y, x+12, y+12), radius=3, fill=shades[level])
    d.text((X0, 148), data.get("observed_at", "sample")[:10] + " snapshot  ·  glow = illustration, counts unchanged",
           fill=(161, 178, 199), font=font(10))
    return im, grid


def target_points(grid, seed):
    active = [(c, r) for c in range(2, 27) for r in range(1, 6) if grid[c][r] > 0]
    if not active:
        active = [(8, 3), (21, 4)]
    rng = random.Random(seed)
    first = rng.choice(active[:max(1, len(active)//2)])
    second = rng.choice(active[max(1, len(active)//2):] or active)
    return [first, second]


def position(target, t):
    # Two visits: approach, touch/glow, pause; common motion for any icon.
    anchors = [(0, (10, 3)), (13, target[0]), (20, target[0]),
               (31, target[0]), (45, target[1]), (53, target[1]), (65, target[1])]
    for (f0, p0), (f1, p1) in zip(anchors, anchors[1:]):
        if t <= f1:
            s = (t-f0)/(f1-f0)
            s = s*s*(3-2*s)
            return (p0[0]*(1-s)+p1[0]*s, p0[1]*(1-s)+p1[1]*s)
    return target[1]


def frames(config, data, seed):
    accent, glow = color(config["accent"]), color(config["glow"])
    base, grid = base_frame(config["username"], data, accent)
    targets = target_points(grid, seed)
    icon = Image.open(ROOT / config["icon"]).convert("RGBA")
    icon.thumbnail((51, 51), Image.Resampling.LANCZOS)
    for t in range(66):
        im = base.copy()
        d = ImageDraw.Draw(im, "RGBA")
        for visit, (start, end) in enumerate(((17, 27), (50, 60))):
            if start <= t <= end:
                c, r = targets[visit]
                x, y = X0 + c*STEP+6, Y0 + r*STEP+6
                power = max(0, 1-abs(t-(start+end)/2)/((end-start)/2))
                d.ellipse((x-14, y-14, x+14, y+14), fill=(*glow, int(35*power)))
                d.rounded_rectangle((x-6, y-6, x+6, y+6), radius=3,
                                    fill=(*glow, int(125*power)))
        col, row = position(targets, t)
        walking = t < 16 or 31 < t < 49
        hop = abs(math.sin(t*math.pi/5))*7 if walking else 0
        # During touch, the icon leans toward the cell. During pause, it rests.
        tilt = -9 if 17 <= t <= 25 or 50 <= t <= 58 else (3*math.sin(t*.7) if walking else 0)
        sprite = icon.rotate(tilt, Image.Resampling.BICUBIC, expand=True)
        x = int(X0 + col*STEP - sprite.width/2)
        y = int(Y0 + row*STEP - sprite.height - 1 - hop)
        im.paste(sprite, (x, y), sprite)
        yield im


def heading_frames(mobile=False):
    w, h = (440, 86) if mobile else (850, 62)
    bg = (17, 23, 37)
    purple, cyan = (151, 107, 226), (79, 220, 230)
    title_font = font(22 if mobile else 29, True)
    for t in range(40):
        im = Image.new("RGB", (w, h), bg)
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((1, 1, w-2, h-2), radius=12, outline=(61, 69, 92), width=1)
        for x in range(20, w-20, 3):
            phase = (x/w - t/40) % 1
            lum = math.exp(-((phase-.45)/.17)**2)
            c = blend(purple, cyan, x/w)
            c = blend(bg, c, .22 + .65*lum)
            d.line((x, h-8, x+3, h-8), fill=c, width=3)
        if mobile:
            d.text((19, 10), "Technical Boundary Audit", fill=(238, 243, 252), font=title_font)
            d.text((19, 41), "& Repair for AI Systems", fill=(238, 243, 252), font=title_font)
        else:
            d.text((25, 10), HEADING, fill=(238, 243, 252), font=title_font)
        yield im


def gif(images, dest, duration):
    # One global fixed palette suppresses per-frame palette flicker.
    images = list(images)
    palette = images[0].quantize(colors=128)
    frames_p = [im.quantize(palette=palette) for im in images]
    frames_p[0].save(dest, save_all=True, append_images=frames_p[1:], duration=duration,
                     loop=0, disposal=2, optimize=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, help="JSON with username, icon, accent, glow")
    parser.add_argument("--activity", type=Path, help="Frozen dated JSON activity input")
    parser.add_argument("--seed", type=int, default=216)
    parser.add_argument("--out", type=Path, help="Output activity GIF")
    parser.add_argument("--heading-out", type=Path, help="Output heading GIF")
    parser.add_argument("--heading-mobile-out", type=Path, help="Output two-line narrow-screen heading GIF")
    parser.add_argument("--capture", type=Path, help="Capture dated GraphQL snapshot to path, then stop")
    parser.add_argument("--username", help="Username for --capture")
    parser.add_argument("--sample", type=Path, help="Write synthetic activity for --username, then stop")
    parser.add_argument("--from-date", default="2026-03-08")
    parser.add_argument("--to-date", default="2026-09-20")
    args = parser.parse_args()
    if args.capture:
        if not args.username:
            parser.error("--capture needs --username")
        capture(args.username, args.capture, args.from_date, args.to_date)
        return
    if args.sample:
        if not args.username:
            parser.error("--sample needs --username")
        sample(args.username, args.sample)
        return
    if args.heading_out:
        gif(heading_frames(), args.heading_out, 125)
    if args.heading_mobile_out:
        gif(heading_frames(mobile=True), args.heading_mobile_out, 125)
    if args.out:
        if not args.config or not args.activity:
            parser.error("--out needs --config and --activity")
        config = json.loads(args.config.read_text())
        data = json.loads(args.activity.read_text())
        if data["username"] != config["username"]:
            parser.error("activity username does not match config")
        gif(frames(config, data, args.seed), args.out, 90)


if __name__ == "__main__":
    main()
