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
        # self.setvar()     # buttoncommandに組み込んだから不要。
        self.create_widgets()

    # ウィジェットを作っていくよ。
    def create_widgets(self):
        tk.Label(self, text='今日のめにゅーは何かな？').pack()
        tk.Button(self, text='Click me', command=self.decide_menu).pack()
        
        # labelのデフォの設定。
        # tk.StringVarはメモ帳だから、全部用意しないとだめ？
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
        self.num = rd.randint(0, len(self.menulist)-1)
        if len(self.menulist[self.num]) == 3:
            self.menutext_1.set(self.menulist[self.num][0])
            self.menutext_2.set(self.menulist[self.num][1])
            self.menutext_3.set(self.menulist[self.num][2])
            self.menutext_4.set('')
        elif len(self.menulist[self.num]) == 2:
            self.menutext_1.set(self.menulist[self.num][0])
            self.menutext_2.set(self.menulist[self.num][1])
            self.menutext_3.set('なし！')
            self.menutext_4.set('')            
        elif len(self.menulist[self.num]) == 1:
            self.menutext_1.set(self.menulist[self.num][0])
            self.menutext_2.set('なし！')
            self.menutext_3.set('なし！')
            self.menutext_4.set('')
        else:
            self.menutext_1.set('')
            self.menutext_2.set('')
            self.menutext_3.set('')
            self.menutext_4.set('そんなに作れないからだめ！')

        # self.menutext_1.set(self.menulist[self.num][0])
        # self.menutext_2.set(self.menulist[self.num][1])
        # self.menutext_3.set(self.menulist[self.num][2])

    # csvファイル読み込んでリストにするよ。
    def menuinput(self):
        with open('menu.csv', encoding='utf-8') as f:
            self.menulist = list(csv.reader(f))
        # print(self.menulist)

    # ランダムな数字つくるよ。
    # 何回も変更したいから、buttonコマンドにくみこんだよ。
    # def setvar(self):
    #     self.num = rd.randint(0, len(self.menulist)-1)


root = tk.Tk()
app = app_menu(master=root)
app.mainloop()
