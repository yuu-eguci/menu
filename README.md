# menu

今日の献立をランダムに表示する、tkinter 製の小さなデスクトップアプリです。
[nekotohito/menu](https://github.com/nekotohito/menu) のフォークです。

「Click me」ボタンを押すと、`menu.csv` から献立を 1 件選び、メイン・サイドディッシュ・おまけを表示します。

## 必要なもの

- Python 3.11 以上（tkinter が使えるもの）

## クイックスタート

```sh
python3 menu.py
```

`menu.csv` は `menu.py` と同じディレクトリから読み込むため、どのディレクトリから起動しても動作します。

## 献立の書き方

`menu.csv` は UTF-8（BOM 付きも可）で保存し、1 行に 1 件の献立をカンマ区切りで書きます。

```csv
チャーハン,餃子,玉子スープ
サンドイッチ,コーヒー
ペペロンチーノ
```

- 1 品目がメイン、2 品目がサイドディッシュ、3 品目がおまけとして表示されます。
- 品数が 3 品より少ない場合、足りない欄には「なし！」と表示されます。
- 品数が 4 品以上の場合は「そんなに作れないからだめ！」と表示されます。
- 空行は無視されます。献立が 1 件もない場合は、その旨を表示します。

## リンターとテスト

リンターには [Ruff](https://docs.astral.sh/ruff/) を、テストには標準ライブラリの `unittest` を使います。テストは tkinter がない環境でも実行できます。

```sh
python3 -m pip install -r requirements-dev.txt
ruff check .
ruff format --check .
python3 -m unittest -v
```

GitHub Actions でも、master へのプッシュとプルリクエストのたびに同じリンターと、Python 3.11 と 3.15 のテストを実行します。
