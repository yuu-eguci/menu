import tempfile
import unittest
from pathlib import Path

import menu


class LoadMenusTest(unittest.TestCase):
    def write_csv(self, text):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "menu.csv"
        path.write_text(text, encoding="utf-8")
        return path

    def test_reads_rows_and_skips_blank_lines(self):
        path = self.write_csv("カレー,サラダ\n\n , \nうどん\n")

        self.assertEqual(menu.load_menus(path), [["カレー", "サラダ"], ["うどん"]])

    def test_ignores_utf8_bom(self):
        path = self.write_csv("\ufeffカレー\n")

        self.assertEqual(menu.load_menus(path), [["カレー"]])

    def test_default_path_is_next_to_script(self):
        self.assertEqual(menu.MENU_CSV, Path(menu.__file__).with_name("menu.csv"))
        self.assertTrue(menu.load_menus())


class MenuTextsTest(unittest.TestCase):
    def test_three_items(self):
        self.assertEqual(menu.menu_texts(["A", "B", "C"]), ("A", "B", "C", ""))

    def test_missing_items_are_shown_as_none(self):
        self.assertEqual(menu.menu_texts(["A"]), ("A", "なし！", "なし！", ""))

    def test_too_many_items(self):
        self.assertEqual(
            menu.menu_texts(["A", "B", "C", "D"]),
            ("", "", "", "そんなに作れないからだめ！"),
        )


class PickTextsTest(unittest.TestCase):
    def test_uses_given_choice(self):
        menus = [["A"], ["B", "C"]]

        self.assertEqual(
            menu.pick_texts(menus, choice=lambda items: items[1]),
            ("B", "C", "なし！", ""),
        )

    def test_no_menus(self):
        self.assertEqual(
            menu.pick_texts([]), ("", "", "", "献立が登録されていません。")
        )


if __name__ == "__main__":
    unittest.main()
