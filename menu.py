"""今日の献立を menu.csv からランダムに選んで表示する tkinter アプリです。"""

import csv
import random
from pathlib import Path

MENU_CSV = Path(__file__).with_name("menu.csv")
DEFAULT_TEXTS = ("メイン", "サイドディッシュ", "おまけ", "")
MAX_ITEMS = 3
NONE_TEXT = "なし！"
TOO_MANY_TEXT = "そんなに作れないからだめ！"
EMPTY_TEXT = "献立が登録されていません。"


def load_menus(path=MENU_CSV):
    """CSV の各行を献立として読み込みます。空の項目と空行は無視します。"""
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = [[item.strip() for item in row if item.strip()] for row in csv.reader(f)]
    return [row for row in rows if row]


def menu_texts(items):
    """献立 1 件を、画面の 4 つのラベルに表示する文字列に変換します。"""
    if len(items) > MAX_ITEMS:
        return ("", "", "", TOO_MANY_TEXT)
    return (*items, *[NONE_TEXT] * (MAX_ITEMS - len(items)), "")


def pick_texts(menus, choice=random.choice):
    """献立を 1 件選び、ラベルに表示する文字列を返します。"""
    if not menus:
        return ("", "", "", EMPTY_TEXT)
    return menu_texts(choice(menus))


def main():
    # tkinter は画面表示にだけ使います。ここで読み込むことで、
    # 上の関数は tkinter がない環境でもテストできます。
    import tkinter as tk

    menus = load_menus()
    root = tk.Tk()
    root.title("Today's Menu")
    root.geometry("500x500")
    frame = tk.Frame(root)
    frame.pack()

    texts = [tk.StringVar(value=text) for text in DEFAULT_TEXTS]

    def decide_menu():
        for var, text in zip(texts, pick_texts(menus), strict=True):
            var.set(text)

    tk.Label(frame, text="今日のめにゅーは何かな？").pack()
    tk.Button(frame, text="Click me", command=decide_menu).pack()
    for var in texts:
        tk.Label(frame, textvariable=var).pack()
    root.mainloop()


if __name__ == "__main__":
    main()
