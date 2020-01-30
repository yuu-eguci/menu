import tkinter as tk
import random as rd
import csv

# 献立アプリをつくる。
# frame >> button, label1(今日のめにゅーは？), label2(ランダムめにゅーの表示)

class app_menu(tk.Frame):
    def __init__(self, master=None):
        # master=Noneにすると、全体が親ウィジェットのことになる。
        super().__init__(master)
        self.pack()
        self.master.title("Today's Menu")
        self.master.geometry('500x500')

        self.menuinput()
        self.create_widgets()

    # ウィジェットを作っていくよ。
    def create_widgets(self):
        tk.Label(self, text='今日のめにゅーは何かな？').pack()
        tk.Button(self, text='Click me', command=self.decide_menu).pack()

        # labelのデフォの設定。
        # tk.StringVarはメモ帳だから、全部用意しないとだめ？
        # HACK: ↑用意しないとだめ。 for を使って行数を減らすことはできると思います。
        self.menutext_1 = tk.StringVar()
        self.menutext_1.set('メイン')
        self.menutext_2 = tk.StringVar()
        self.menutext_2.set('サイドディッシュ')
        self.menutext_3 = tk.StringVar()
        self.menutext_3.set('おまけ')
        self.menutext_4 = tk.StringVar()
        self.menutext_4.set('')
        # labelつくっていくよ
        tk.Label(self, textvariable=self.menutext_1).pack()
        tk.Label(self, textvariable=self.menutext_2).pack()
        tk.Label(self, textvariable=self.menutext_3).pack()
        tk.Label(self, textvariable=self.menutext_4).pack()

    def decide_menu(self):
        num = rd.randint(0, len(self.menulist)-1)
        menulist_len = len(self.menulist[num])

        # HACK: menulist を「デフォルトでは"なし!"か""」を返す、っていう風に作ればとても短くなるかも。
        if menulist_len == 3:
            self.menutext_1.set(self.menulist[num][0])
            self.menutext_2.set(self.menulist[num][1])
            self.menutext_3.set(self.menulist[num][2])
            self.menutext_4.set('')
        elif menulist_len == 2:
            self.menutext_1.set(self.menulist[num][0])
            self.menutext_2.set(self.menulist[num][1])
            self.menutext_3.set('なし！')
            self.menutext_4.set('')
        elif menulist_len == 1:
            self.menutext_1.set(self.menulist[num][0])
            self.menutext_2.set('なし！')
            self.menutext_3.set('なし！')
            self.menutext_4.set('')
        else:
            self.menutext_1.set('')
            self.menutext_2.set('')
            self.menutext_3.set('')
            self.menutext_4.set('そんなに作れないからだめ！')

    # csvファイル読み込んでリストにするよ。
    def menuinput(self):
        with open('menu.csv', encoding='utf-8') as f:
            self.menulist = list(csv.reader(f))


root = tk.Tk()
app = app_menu(master=root)
app.mainloop()
