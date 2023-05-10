import flet as ft
from flet import IconButton, Page, icons
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import time 
from time import sleep
import random as rand
import sys
import logging


#log設定ファイルからlog設定を読み込み
#logging.config.fileConfig('logging.conf')

#logの出力名を設定
logger = logging.getLogger('Log')
#logLevelを設定
logger.setLevel(20)
#logをコンソール出力するための設定
sh = logging.StreamHandler()
logger.addHandler(sh)
#logのファイル出力先設定
fh = logging.FileHandler('C:/Users/kxiyt/Documents/GitHub/Flutter/Flet/Quiz_app/python/log/main.log')
logger.addHandler(fh)

#全てのフォーマットオプションとその役割
# %(asctime)s	実行時刻
# %(filename)s	ファイル名
# %(funcName)s	行番号
# %(levelname)s	ログの定義
# %(lineno)d	ログレベル名
# %(message)s	ログメッセージ
# %(module)s	モジュール名
# %(name)s	関数名
# %(process)d	プロセスID
# %(thread)d	スレッドID
formatter = logging.Formatter('%(asctime)s : %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)



root = tk.Tk()
screen_width:int = root.winfo_screenwidth()
screen_height:int = root.winfo_screenheight()
screen_area = screen_height * screen_width
root.destroy()




res = messagebox.askquestion("QuizApp", "アプリケーションを起動しますか？")
print("OpenApp : ", res)
logger.log(100, f"OpenApp : {res}")


if res == "yes":
    logger.log(100, "QuizApp START")
    
elif res == "no":
    logger.log(100, "QuizApp EXIT")
    #pythonプログラムを終了させる
    sys.exit()
    



def main(page: Page):
    page.title = "aim"
    #top : 上端、  center : 中央、  bottom : 下端
    page.vertical_alignment = "center"
    
    
    page.add(
        ft.Container(
            width = screen_width,
            height=screen_height,
            bgcolor=ft.colors.AMBER_900,
        )    
    )

    
    tf = ft.Text(
        value="Quiz",
        width=1000,
        height=1000,
        bgcolor=ft.colors.CYAN_100,
    )
    
    title_containter = ft.Container(    
        width=1000, 
        height=1000, 
        bgcolor=ft.colors.CYAN_ACCENT_200,
    )
    page.add(title_containter)
    
    
    def animation():
        c1 = ft.colors.PINK_500
        c2 = ft.colors.PINK_500
        c3 = ft.colors.PINK_200
        c4 = ft.colors.PINK_200
        
        
        #文字列のパーツの配置情報を表すリスト
        #各パーツは（left, top, bgcolor）の形式で定義されている
        # left: パーツの左端の位置を表す整数値です。単位はピクセルです。
        # top: パーツの上端の位置を表す整数値です。単位はピクセルです。
        # bgcolor: パーツの背景色を指定する変数です。
        parts = [
            # Q
            (0, 0, c1),
            (0, 1, c1),
            (0, 2, c1),
            (0, 3, c1),
            (1, 0, c1),
            (1, 3, c1),
            (2, 0, c1),
            (2, 3, c1),
            (3, 0, c1),
            (3, 1, c1),
            (3, 2, c1),
            (3, 3, c1),
            (4, )
            # U
            (4, 0, c2),
            (4, 1, c2),
            (4, 2, c2),
            (4, 3, c2),
            (4, 4, c2),
            (5, 4, c2),
            (6, 4, c2),
            # I
            (8, 0, c3),
            (9, 0, c3),
            (10, 0, c3),
            (8, 1, c3),
            (8, 2, c3),
            (9, 2, c3),
            (10, 2, c3),
            (8, 3, c3),
            (8, 4, c3),
            (9, 4, c3),
            (10, 4, c3),
            # Z
            (12, 0, c4),
            (13, 0, c4),
            (14, 0, c4),
            (13, 1, c4),
            (13, 2, c4),
            (13, 3, c4),
            (13, 4, c4),    
        ]
        
        width = 10
        height = 10
        duration = 2000
    
        anime_cvs = ft.Stack(
            #Stackオブジェクトのインスタンス化
            #width : スタックコンテナの幅を指定
            #height : スタックコンテナの高さを指定
            #animate_scale : スタック内のコントロールのスケーリングアニメーションの期間を指定
            #animate_opacity : スタック内のコントロールの不透明度アニメーションの期間を指定
            width = width,
            height = height,
            animate_scale = duration,
            animate_opacity = duration,
        )
    
    


if __name__ == "__main__":
    #ft.app(target=main, view=ft.WEB_BROWSER)
    ft.app(target=main)
    #root.mainloop()s