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
        self.assertEqual(len(first), 66)
        self.assertEqual([im.tobytes() for im in first], [im.tobytes() for im in second])
        self.assertNotEqual(first[0].tobytes(), first[20].tobytes())
        self.assertEqual(input_path.read_bytes(), before)
        self.assertTrue(any(day["count"] > 0 for day in data["days"]))

    def test_alternate_icon_colors_and_gif_frames(self):
        cat = json.loads((ROOT / "cat.json").read_text())
        fox = json.loads((ROOT / "fox.json").read_text())
        self.assertNotEqual(cat["icon"], fox["icon"])
        self.assertNotEqual(cat["accent"], fox["accent"])
        self.assertNotEqual(cat["glow"], fox["glow"])
        data = json.loads((ROOT / "example_activity.json").read_text())
        self.assertIn("SYNTHETIC", data["source"])
        self.assertEqual(fox["username"], data["username"])
        frames = list(render.frames(fox, data, 216))
        self.assertNotEqual(frames[0].tobytes(), frames[20].tobytes())
        for name, n in (("crowned_cat.gif", 66), ("fox.gif", 66), ("heading.gif", 40), ("heading_mobile.gif", 40)):
            with Image.open(ROOT / name) as gif:
                # GIF encoding can coalesce visually identical adjacent frames.
                self.assertGreaterEqual(gif.n_frames, n-10)
                self.assertLessEqual(gif.n_frames, n)
                self.assertEqual(gif.info["loop"], 0)

    def test_layout_keeps_body(self):
        preview = (ROOT / "profile_layout_preview.md").read_text()
        self.assertTrue(preview.startswith(make_layout.HEADING))
        source = preview.replace(make_layout.HEADING, make_layout.TITLE, 1).replace(make_layout.CREATURE, "", 1)
        self.assertEqual(make_layout.build(source), preview)
        self.assertIn("**32 direct upstream merges across 28 independent public repositories**", source)
        self.assertIn("siriusa.paper@gmail.com", source)


if __name__ == "__main__":
    unittest.main()
