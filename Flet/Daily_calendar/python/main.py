import flet as ft
import flet.version
from flet import IconButton, Page, icons
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pyautogui as pg
import time 
from time import sleep
import random as rand
import sys
import logging
import atexit


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
#fh = logging.FileHandler('C:/Users/kxiyt/Documents/GitHub/Flutter/Flet/Daily_callendar/python/log/main.log')
fh = logging.FileHandler('C:/Users/1k8ai/Documents/GitHub/Flutter/Flet/Daily_calendar/python/log/main.log')
#fh = logging.FileHandler('/home/j21070/ドキュメント/GitHub/Flutter/Flet/Daily_calendar/python/log/main.log')
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







#pysimpleguiを使った画面の高さ・幅
scr_w,scr_h= pg.size()
print("screen_height : " + str(scr_h) + "px")
print("screen_width : " + str(scr_w) + "px")
scr_area = scr_h * scr_w


#プログラムが終了したときに呼び出される関数
@atexit.register
def exit_handler():
    logger.log(100, "QuizApp __END__")


usr_name = "mia"


def main(page: Page):
    page.title = "aim"
    page.theme_mode = ft.ThemeMode.LIGHT
    #top : 上端、  center : 中央、  bottom : 下端
    page.vertical_alignment = "center"
    
    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    
    
    
    appbar_color = "#ef7389"
    main_bg_color = "#ef7380"
    
    
    page.appbar = ft.AppBar(
        leading=ft.Container(padding=5, content=ft.Text(value="")),
        leading_width=40, 
        title=ft.Text(
            value="~~ Daily Calender ~~",
            color="#ee1919", 
            bgcolor=appbar_color
        ),
        center_title=True, 
        bgcolor=appbar_color, 
        actions=[
            ft.Container(
                padding=10, 
                content=ft.ElevatedButton(
                    f"Hello {usr_name}",
                    color="#ee1919",
                    bgcolor="#191970",
                    #on_click=my_status_clicked,
                )
            )
        ]
        
    )
    
    
    def my_status_clicked(e):
        page.add(ft.Text("title"))


    
    
    page.controls.append(
        
        ft.Container(
            width=int(scr_w) * 1,
            height=int(scr_h) * 1,
            bgcolor=main_bg_color
            #gradient=ft.LinearGradient,
        )
    )
    page.update()
    
    
if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
    #ft.app(target=main)
    