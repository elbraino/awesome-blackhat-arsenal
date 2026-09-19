"""Tests for scripts/validate.py.  Run:  python3 -m unittest scripts/test_validate.py"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate  # noqa: E402
from normalize import canonical_dump, slug  # noqa: E402

GOOD = {
    "Tool Name": "Example Tool",
    "Description": "An example tool that does something genuinely useful for security researchers everywhere.",
    "Github URL": "https://github.com/example/tool",
    "Tracks": ["Web AppSec"],
    "Speakers": ["Jane Doe"],
    "Year": "2026",
    "Location": "USA",
}


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.event_dir = os.path.join(self.tmp.name, "tools", "USA", "2026")
        os.makedirs(self.event_dir)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, data, raw=None):
        path = os.path.join(self.event_dir, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(raw if raw is not None else canonical_dump(data))
        return path

    def check(self, data, name="example-tool.json", raw=None):
        for f in os.listdir(self.event_dir):
            os.remove(os.path.join(self.event_dir, f))
        self.write(name, data, raw)
        _count, report = validate.run([self.event_dir])
        return report

    def errors(self, report):
        return [msg for _p, msg in report.errors if not _p.endswith("AutoReadme.py")]

    def test_good_file_passes(self):
        r = self.check(GOOD)
        self.assertEqual(self.errors(r), [])
        self.assertEqual(r.warnings, [])

    def test_invalid_json(self):
        r = self.check(None, raw="{not json")
        self.assertTrue(any("invalid JSON" in m for m in self.errors(r)))

    def test_missing_and_unknown_keys(self):
        d = dict(GOOD); del d["Speakers"]; d["Author"] = "x"
        msgs = self.errors(self.check(d))
        self.assertTrue(any("missing required key 'Speakers'" in m for m in msgs))
        self.assertTrue(any("unknown key 'Author'" in m for m in msgs))

    def test_event_key_is_rejected(self):
        with_event = {**GOOD, "Event": "BH-US-26"}
        msgs = self.errors(self.check(with_event, raw=json.dumps(with_event, indent=2) + "\n"))
        self.assertTrue(any("unknown key 'Event'" in m for m in msgs))

    def test_non_canonical_form_is_error(self):
        msgs = self.errors(self.check(GOOD, raw=json.dumps(GOOD, indent=4)))
        self.assertTrue(any("not in canonical form" in m for m in msgs), msgs)
        msgs = self.errors(self.check(GOOD, raw=json.dumps(GOOD, indent=2, ensure_ascii=False)))  # no trailing newline
        self.assertTrue(any("not in canonical form" in m for m in msgs), msgs)

    def test_filename_must_be_slug_of_name(self):
        msgs = self.errors(self.check(GOOD, name="Example Tool.json"))
        self.assertTrue(any("filename should be example-tool.json" in m for m in msgs), msgs)
        self.assertEqual(self.errors(self.check(GOOD, name="example-tool-2.json")), [])  # collision suffix ok

    def test_slug(self):
        self.assertEqual(slug(".NET Unpacking: When Frida Gets the JIT out of It"), "net-unpacking-when-frida-gets-the-jit-out-of-it")
        self.assertEqual(slug("Squatm3gator: 360° Cybersquatting"), "squatm3gator-360-cybersquatting")
        self.assertEqual(slug("!!!"), "tool")
        self.assertLessEqual(len(slug("word-" * 40)), 80)

    def test_unknown_track_is_error(self):
        msgs = self.errors(self.check({**GOOD, "Tracks": ["Malware"]}))
        self.assertTrue(any("unknown track 'Malware'" in m for m in msgs))

    def test_empty_tracks_is_warning_only(self):
        r = self.check({**GOOD, "Tracks": []})
        self.assertEqual(self.errors(r), [])
        self.assertTrue(any("'Tracks' is empty" in m for _p, m in r.warnings))

    def test_null_speakers_is_error(self):
        msgs = self.errors(self.check({**GOOD, "Speakers": None}))
        self.assertTrue(any("'Speakers' must be a list" in m for m in msgs))

    def test_url_rules(self):
        cases = {
            "http://github.com/a/b": "must start with https://",
            "https://github.com/a/b/": "trailing slash",
            "https://github.com/a/b;": "not a valid GitHub repo URL",
            "https://github.com/a?tab=repositories": "not a valid GitHub repo URL",
            " https://github.com/a/b": "surrounding whitespace",
        }
        for url, expected in cases.items():
            with self.subTest(url=url):
                msgs = self.errors(self.check({**GOOD, "Github URL": url}))
                self.assertTrue(any(expected in m for m in msgs), f"{url!r}: {msgs}")

    def test_url_warnings(self):
        for url, expected in {
            "https://github.com/objective-see": "user/org page",
            "https://github.com/a/b/blob/main/x.py": "inside a repo",
            "https://play.secdim.com/": "not on github.com",
        }.items():
            with self.subTest(url=url):
                r = self.check({**GOOD, "Github URL": url})
                self.assertEqual(self.errors(r), [])
                self.assertTrue(any(expected in m for _p, m in r.warnings), f"{url!r}: {r.warnings}")

    def test_empty_url_is_allowed(self):
        self.assertEqual(self.errors(self.check({**GOOD, "Github URL": ""})), [])

    def test_year_and_location_must_match_folder(self):
        msgs = self.errors(self.check({**GOOD, "Year": "2025", "Location": "Asia"}))
        self.assertTrue(any("'Year' '2025' does not match folder '2026'" in m for m in msgs))
        self.assertTrue(any("'Location' 'Asia' does not match folder 'USA'" in m for m in msgs))

    def test_null_location_is_error(self):
        msgs = self.errors(self.check({**GOOD, "Location": None}))
        self.assertTrue(any("'Location' must be a non-empty string" in m for m in msgs))

    def test_description_thresholds(self):
        self.assertTrue(any("too short" in m for m in self.errors(self.check({**GOOD, "Description": "tiny"}))))
        r = self.check({**GOOD, "Description": "x" * 50})
        self.assertEqual(self.errors(r), [])
        self.assertTrue(any("is short" in m for _p, m in r.warnings))
        self.assertTrue(any("'Description' must be a non-empty" in m
                            for m in self.errors(self.check({**GOOD, "Description": None}))))

    def test_duplicate_tool_name_in_same_event(self):
        self.write("example-tool.json", GOOD)
        self.write("example-tool-2.json", {**GOOD, "Tool Name": "example tool"})
        _c, r = validate.run([self.event_dir])
        self.assertTrue(any("duplicate 'Tool Name'" in m for m in self.errors(r)))

    def test_category_map_matches_canonical_tracks(self):
        self.assertEqual(validate.category_map_keys_from_autoreadme(), validate.CANONICAL_TRACKS)


if __name__ == "__main__":
    unittest.main()
