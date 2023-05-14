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


#グローバル変数の宣言
main_page_view = False




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
#fh = logging.FileHandler('C:/Users/1k8ai/Documents/GitHub/Flutter/Flet/Quiz_app/python/log/main.log')
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




#tkinterでのメッセージボックス表示
res = messagebox.askquestion("QuizApp", "アプリケーションを起動しますか？")
print("OpenApp : ", res)
logger.log(100, f"OpenApp : {res}")


if res == "yes":
    logger.log(100, "QuizApp Start")
    
elif res == "no":
    logger.log(100, "QuizApp Exit")
    #pythonプログラムを終了させる
    sys.exit()
    

#tkinterでの名前入力ダイアログ（ログイン画面が完成するまでの間）
result = tk.simpledialog.askstring("Input Dialog", "Please enter your name : ")
usr_name = result

if not usr_name:
    usr_name = "000"
else:
    pass



def main(page: Page):
    page.title = "aim"
    page.theme_mode = ft.ThemeMode.LIGHT
    #top : 上端、  center : 中央、  bottom : 下端
    page.vertical_alignment = "center"
    
    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    
    
    appbar_color = "#ef7389"
    main_bg_color = "#e0ffff"
    main_bg_color_2 = "#20b2aa"
    
    
    
    page.bgcolor = main_bg_color
    page.padding = 40
    #ページのスクロールオプション
    # None(デフォルト) - 行はスクロール不可能であり、その内容がオーバーフローする可能性があります。
    # AUTO- スクロールが有効になり、スクロールが発生した場合にのみスクロール バーが表示されます。
    # ADAPTIVE- スクロールが有効になり、アプリを Web またはデスクトップとして実行するとスクロール バーが常に表示されます。
    # ALWAYS- スクロールが有効になり、スクロール バーが常に表示されます。
    # HIDDEN- スクロールは有効ですが、スクロール バーは常に非表示になります。
    page.scroll = "AUTO"
    
    
    # def main_page_view_clicked(e):
    #     global main_page_view
    #     main_page_view = True
    #スタート画面で確認ボタンが押されたとき
    def main_page_view_clicked(e):
        
        time.sleep(0.5)
        
        #スタート画面を消す
        start_container.visible = False
        page.update()
        
    
        
        labels = ft.Container(
            content=ft.TextField(
                label="答えを入力してください",
                value="",
                max_length=100,
                multiline=True,
                autofocus=False,
                password="",
                prefix="",
                expand=True,
                keyboard_type="text",
                prefix_icon="",
                color="#00bfff"
            ),
            bgcolor="#d8bfd8",
            padding=10,
            margin=10,
            alignment=ft.alignment.center,
            ink=True,
        )
        #if main_page_view == True:
        page.add(labels)
        
        main_container = ft.Container(
            width=int(scr_w) * 1.3,
            height=int(scr_h) * 1.3,
            bgcolor="#d8bfd8",
            content=ft.Text(
                "答えを入力してください",
                text_align="center", 
                bgcolor="#ffffff",
            ),
            border_radius=50,
        )   
        page.add(main_container)
        
        
        
        
    #usr_nameの入力された値のvalue
    global val_name
    val_name = 'aimlinux'
        
    #スタート画面の設定
    start_container = ft.Container(
        
        ft.Column(
            
            [
                ft.Text(
                    #f" おはよう{usr_name}!! ",
                    "                       ~~~ テキスト入力画面 ~~~",
                    size=30,
                    color=appbar_color,
                ),
                ft.Text("", height=30),
                
                ft.Text(
                    "・ユーザーネイム(必須)",
                    size=18,
                    ),
                ft.TextField(
                    label="例：高専太郎",
                    bgcolor=main_bg_color,
                    keyboard_type="NAME",
                    value=val_name
                    ),
                ft.Text("", height=10),
                
                ft.Text(
                    "・パスワード",
                    size=18,
                    ),
                ft.TextField(
                    label="Password",
                    bgcolor=main_bg_color,
                    password=True,
                    can_reveal_password=True,
                    keyboard_type="TEXT",
                    ),
                ft.Text("", height=10),
                
                ft.Text(
                    "・Fletについて何かあれば",
                    size=18,
                    ),
                ft.TextField(
                    label="例：とても面白いですね！！",
                    bgcolor=main_bg_color,
                    multiline=True,
                    max_length=100,
                    min_lines=1, 
                    max_lines=5,
                    keyboard_type="TEXT",
                    ),
                ft.Text("", height=10),
                
                # ft.Text(
                #     "・ff",
                #     size=18,
                #     ),
                # ft.TextField(
                #     label="例：とても面白いですね！！",
                #     bgcolor=main_bg_color,
                #     border="underline",
                #     border_color="red",
                #     border_width=1,
                #     hint_text="Enter text here",
                #     icon=ft.icons.FORMAT_SIZE,
                #     prefix_icon=ft.icons.COLOR_LENS,
                #     prefix_text="",
                #     suffix_text="",
                #     helper_text="※自由にご記入ください", 
                #     counter_text="0 symbols typed",
                #     cursor_color="red",
                #     ),
                # ft.Text("", height=25),
                
                # ft.Text(
                #     "・ユーザーネイム(必須)",
                #     size=18,
                #     ),
                # ft.TextField(
                #     label="例：高専太郎",
                #     bgcolor=main_bg_color,
                #     password=True,
                #     can_reveal_password=True,
                #     focused_bgcolor="lightblue",
                #     focused_border_color="lightblue",
                #     focused_border_width=1,
                #     focused_color="red",
                #     keyboard_type="URL",
                #     selection_color="",
                #     ),
                # ft.Text("", height=10),
                
                ft.ElevatedButton(
                    text="確定する", 
                    width=90,
                    height=50,
                    color="#000000",
                    bgcolor=appbar_color,
                    on_click=main_page_view_clicked
                    ),
            ],
        height=scr_h * 0.75,
        width=scr_w * 1.0,
        alignment="top"
        ),
        bgcolor=main_bg_color_2,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#7fffd4", "#ee82ee"],
        ),
        padding=30, 
        border_radius=50,
        #alignment="center"
    )
    
    
    print(val_name)
    logger.log(100, f"Starts with {usr_name}.")
    page.add(start_container)
    page.update()
    
    
    
    
    
    #ハンバーガーメニューが押されたときの処理
    def menu_clicked(event):
        logger.log(50, "MenuButton clicked")
    
    #名前変更が押されたとき
    def change_name_clicked(event):
        messagebox.showerror("title", "名前が変更されました")
        global usr_name
        usr_name = "999"
        page.update()
    
    #戻るが押されたとき
    def return_name_clicked(event):
        messagebox.showinfo("title", "戻りましょうね")
    
    #MyStatusが押されたときの処理
    def my_status_clicked(event):
        logger.log(50, "MyStatusButton clicked")
        
        #AlertDialogの表示
        dig = ft.AlertDialog(
            title=ft.Text(
                f"Hi {usr_name} !", 
                color="aqua", 
                #bgcolor="",
                size=20,
                
                ),
            title_padding=10,
            content=ft.TextField(label="名前変更", ),
            actions=[
                ft.ElevatedButton(text="変更する", on_click=change_name_clicked),
                ft.ElevatedButton(text="戻る", on_click=return_name_clicked)
            ]
        )
        page.dialog = dig
        dig.open = True   
        page.update()
                
    
    
    #設定ボタンが押されたときの処理
    def settings_clicked(event):
        logger.log(50, "SettingsButton clicked")
        
        dig_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text()
        )
        page.dialog = dig_modal
        dig_modal.open = True   
        page.update()
    
    
    
    
    #アプリケーションバー
    page.appbar = ft.AppBar(
        #leading=ft.Container(padding=5, content=ft.Text(value="")),
        leading=
            ft.IconButton(
                icon="menu",
                on_click=menu_clicked,
                width=100
                ), 
            #ft.IconButton(icon="search"),
        leading_width=60, 
        title=ft.Text(
            value="Quiz",
            color="#afeeee", 
        ),
        center_title=True, 
        bgcolor=appbar_color, 
        actions=[
            ft.Container(
                padding=10, 
                content=ft.ElevatedButton(
                    f"Hello {usr_name}",
                    color="#ee1919",
                    bgcolor="#afeeee",
                    #on_click=my_status_clicked,
                    on_click=my_status_clicked,
                )
            ), 
            ft.IconButton(
                icon="settings", 
                on_click=settings_clicked,
                ),
        ],
        elevation=2,
    )
    
    page.add
    
    
    
    
    
    
    
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
    ft.app(target=main, view=ft.WEB_BROWSER)
    #ft.app(target=main)
    
    
