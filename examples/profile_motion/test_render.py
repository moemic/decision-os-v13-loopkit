import json
import unittest
from pathlib import Path
from PIL import Image
import render
import make_layout

ROOT = Path(__file__).parent


class RenderTest(unittest.TestCase):
    def test_data_is_not_changed_and_seed_replays_frames(self):
        config = json.loads((ROOT / "cat.json").read_text())
        input_path = ROOT / "shin_activity_2026-09-20.json"
        before = input_path.read_bytes()
        data = json.loads(before)
        first = list(render.frames(config, data, 216))
        second = list(render.frames(config, data, 216))
        self.assertEqual(len(first), 104)
        self.assertEqual([im.tobytes() for im in first], [im.tobytes() for im in second])
        self.assertNotEqual(first[0].tobytes(), first[33].tobytes())
        self.assertEqual(first[0].tobytes(), first[-1].tobytes())
        self.assertEqual({im.getpixel((4, 4)) for im in first}, {(17, 23, 37)})
        self.assertEqual(input_path.read_bytes(), before)
        self.assertTrue(any(day["count"] > 0 for day in data["days"]))

    def test_shock_launch_and_staggered_return_preserve_each_cell(self):
        data = json.loads((ROOT / "shin_activity_2026-09-20.json").read_text())
        grid = render.activity_grid(data)
        stop = render.shock_stop(grid, 216)
        plan = render.shock_plan(grid, 216, stop)
        self.assertEqual(len(plan), 196)
        self.assertEqual([cell["count"] for cell in plan],
                         [grid[col][row] for col in range(28) for row in range(7)])
        self.assertGreater(len({cell["return_start"] for cell in plan}), 10)
        self.assertGreater(len({cell["return_end"] for cell in plan}), 15)
        for t in (0, 87, 94, 95):
            self.assertTrue(all(render.cell_position(cell, t) == (cell["x"], cell["y"])
                                for cell in plan))
        burst = [(render.cell_position(cell, 36)[0]-cell["x"],
                  render.cell_position(cell, 36)[1]-cell["y"]) for cell in plan]
        self.assertGreater(sum(dx > 0 for dx, _ in burst), 25)
        self.assertGreater(sum(dx < 0 for dx, _ in burst), 25)
        self.assertGreater(sum(dy > 0 for _, dy in burst), 25)
        self.assertGreater(sum(dy < 0 for _, dy in burst), 25)
        home_at_72 = sum(render.cell_position(cell, 72) == (cell["x"], cell["y"])
                         for cell in plan)
        self.assertGreater(home_at_72, 0)
        self.assertLess(home_at_72, len(plan))

    def test_alternate_icon_colors_and_gif_frames(self):
        cat = json.loads((ROOT / "cat.json").read_text())
        fox = json.loads((ROOT / "fox.json").read_text())
        self.assertNotEqual(cat["icon"], fox["icon"])
        self.assertNotEqual(cat["accent"], fox["accent"])
        self.assertNotEqual(cat["glow"], fox["glow"])
        self.assertIn("sleep_icon", cat)
        self.assertIn("wake_icon", cat)
        self.assertNotIn("sleep_icon", fox)
        self.assertNotIn("wake_icon", fox)
        self.assertNotEqual((ROOT / cat["sleep_icon"]).read_bytes(),
                            (ROOT / cat["icon"]).read_bytes())
        data = json.loads((ROOT / "example_activity.json").read_text())
        self.assertIn("SYNTHETIC", data["source"])
        self.assertEqual(fox["username"], data["username"])
        frames = list(render.frames(fox, data, 216))
        self.assertNotEqual(frames[0].tobytes(), frames[20].tobytes())
        for name, n in (("crowned_cat.gif", 104), ("fox.gif", 104),
                        ("crowned_cat_touch.gif", 66), ("heading.gif", 40),
                        ("heading_mobile.gif", 40)):
            with Image.open(ROOT / name) as gif:
                # GIF encoding can coalesce visually identical adjacent frames.
                self.assertGreaterEqual(gif.n_frames, n-10)
                self.assertLessEqual(gif.n_frames, n)
                self.assertEqual(gif.info["loop"], 0)

    def test_layout_keeps_body(self):
        preview = (ROOT / "profile_layout_preview.md").read_text()
        self.assertTrue(preview.startswith(make_layout.HEADING))
        self.assertIn(make_layout.PORTFOLIO_ABSOLUTE, preview)
        self.assertNotIn(make_layout.PORTFOLIO_RELATIVE, preview)
        source = (preview.replace(make_layout.HEADING, make_layout.TITLE, 1)
                  .replace(make_layout.CREATURE, "", 1)
                  .replace(make_layout.PORTFOLIO_ABSOLUTE,
                           make_layout.PORTFOLIO_RELATIVE, 1))
        self.assertEqual(make_layout.build(source), preview)
        self.assertIn("**32 direct upstream merges across 28 independent public repositories**", source)
        self.assertIn("siriusa.paper@gmail.com", source)


if __name__ == "__main__":
    unittest.main()
