import flet as ft
import flet.version
from flet import IconButton, Page, icons
from flet import BorderSide
from flet import RoundedRectangleBorder
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
from selenium import webdriver
from selenium.webdriver.chrome import service


#グローバル変数の宣言
main_page_view = False



#log設定ファイルからlog設定を読み込み
#logging.config.fileConfig('logging.conf')

#logの出力名を設定
logger = logging.getLogger('Log')
#logLevelを設定
logger.setLevel(100)
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
    usr_name = "ppp"
else:
    pass



def main(page: Page):
    page.title = "aim"
    page.theme_mode = ft.ThemeMode.LIGHT
    #top : 上端、  center : 中央、  bottom : 下端
    page.vertical_alignment = "center"
    #テキストなどオブジェクトを中央に
    #page.horizontal_alignment = "center"
    #page.overlay = 
    page.on_scroll_interval = 10
    
    page.padding = 40
    #ページのスクロールオプション
    # None(デフォルト) - 行はスクロール不可能であり、その内容がオーバーフローする可能性があります。
    # AUTO- スクロールが有効になり、スクロールが発生した場合にのみスクロール バーが表示されます。
    # ADAPTIVE- スクロールが有効になり、アプリを Web またはデスクトップとして実行するとスクロール バーが常に表示されます。
    # ALWAYS- スクロールが有効になり、スクロール バーが常に表示されます。
    # HIDDEN- スクロールは有効ですが、スクロール バーは常に非表示になります。
    page.scroll = "AUTO"
    
    
    
    appbar_color = "#ef7389"
    main_bg_color = "#e0ffff"
    main_bg_color_2 = "#20b2aa"
    
    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    
    page.bgcolor = main_bg_color
    
    
    
    
    # def main_page_view_clicked(e):
    #     global main_page_view
    #     main_page_view = True
    #スタート画面で確認ボタンが押されたとき
    def main_page_view_clicked(event):
        
        time.sleep(0.5)
        
        #スタート画面を消す
        a.visible = False
        b.visible = False
        c.visible = False
        d.visible = False
        name.visible = False
        f.visible = False
        g.visible = False
        password.visible = False
        i.visible = False
        j.visible = False
        contents.visible = False
        l.visible = False
        m.visible = False
        
        
        #NAME_VALUE
        if not name.value:
            name.value = "NoName"
            NAME_VALUE:str = name.value
            logger.log(100, "Starts with NoName.")
        else:
            NAME_VALUE:str = name.value
            logger.log(30, "Starts with " + NAME_VALUE)
            
        #PASSWORD_VALUEs
        if not password.value:
            password.value = "NoPassword"
            PASSWORD_VALUE:str = password.value
            logger.log(100, "Starts with NoPassword.")
        else:
            PASSWORD_VALUE:str = password.value
            logger.log(30, "Starts with " + PASSWORD_VALUE)
        
        #CONTENTS_VALUE
        if not contents.value:
            contents.value = "NoContents"
            CONTENTS_VALUE:str = password.value
        else:
            CONTENTS_VALUE:str = contents.value
            logger.log(30, "Starts with " + CONTENTS_VALUE)
        
        
        
        logger.log(100, f"[ NAME : " + str(NAME_VALUE) + " ]  [ PASSWORD_VALUE : " + str(PASSWORD_VALUE) + " ]  [ CONTENTS : " + str(CONTENTS_VALUE) + " ]")
        
        
        
        space_A = ft.Text("", height=10)
        
        Button_A = ft.ElevatedButton(
            width=300,
            height=80,
            text="初級", 
            scale=1,
            tooltip="簡単だよ!!",
            icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, 
            icon_color="purple",
            #bgcolor="#e000ff",
            #color="#ffffff",
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                    ft.MaterialState.FOCUSED: ft.colors.BLUE,
                    ft.MaterialState.DEFAULT: ft.colors.BLACK,
                },
                bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200, "": ft.colors.YELLOW},
                padding={ft.MaterialState.HOVERED: 20},
                overlay_color=ft.colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: BorderSide(1, ft.colors.BLUE),
                    ft.MaterialState.HOVERED: BorderSide(2, ft.colors.BLUE),
                },
                shape={
                    ft.MaterialState.HOVERED: RoundedRectangleBorder(radius=20),
                    ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=20),
                },
            ),
        )
        
        space_B = ft.Text("", height=20)
        
        Button_B = ft.ElevatedButton(
            width=300,
            height=80,
            text="中級",
            scale=1,
            tooltip="そこそこ難しいよ!!",
            icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, 
            icon_color="purple", 
            #bgcolor="#e000ff",
            #color="#ffffff",
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                    ft.MaterialState.FOCUSED: ft.colors.BLUE,
                    ft.MaterialState.DEFAULT: ft.colors.BLACK,
                },
                bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200, "": ft.colors.YELLOW},
                padding={ft.MaterialState.HOVERED: 20},
                overlay_color=ft.colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: BorderSide(1, ft.colors.BLUE),
                    ft.MaterialState.HOVERED: BorderSide(2, ft.colors.BLUE),
                },
                shape={
                    ft.MaterialState.HOVERED: RoundedRectangleBorder(radius=20),
                    ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),
                },
            ),
        )
        
        space_C = ft.Text("", height=20)
        
        Button_C = ft.ElevatedButton(
            width=300,
            height=80,
            text="上級",
            scale=1,
            tooltip="とっても難しいよ!!",
            icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, 
            icon_color="purple",
            #bgcolor="#e000ff",
            #color="#ffffff",
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                    ft.MaterialState.FOCUSED: ft.colors.BLUE,
                    ft.MaterialState.DEFAULT: ft.colors.BLACK,
                },
                bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200, "": ft.colors.YELLOW},
                padding={ft.MaterialState.HOVERED: 20},
                overlay_color=ft.colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: BorderSide(1, ft.colors.BLUE),
                    ft.MaterialState.HOVERED: BorderSide(2, ft.colors.BLUE),
                },
                shape={
                    ft.MaterialState.HOVERED: RoundedRectangleBorder(radius=20),
                    ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=2),
                },
            ),
        )        
        
        page.add(space_A, Button_A, space_B, Button_B, space_C, Button_C)
        
        # labels = ft.Container(
            
            
            
        #     bgcolor="#d8bfd8",
        #     gradient=ft.LinearGradient(
        #         begin=ft.alignment.top_center,
        #         end=ft.alignment.bottom_center,
        #         colors=["#7fffd4", "#ee82ee"],
        #     ),
        #     padding=10,
        #     margin=10,
        #     alignment=ft.alignment.center,
        #     ink=True,
        # )
        # page.add(labels)
        
        main_container = ft.Container(
            width=int(scr_w) * 1.3,
            height=int(scr_h) * 0.2,
            bgcolor="#d8bfd8",
            content=ft.Text(
                "     ・説明 :\n初級 : \n中級 : \n上級 : \n",
                text_align="center"
            ),
            border_radius=50,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#7fffd4", "#ee82ee"],
            ),
        )   
        page.add(main_container)
        
        
        
    
    
    
    #ハンバーガーメニューが押されたときの処理
    def menu_clicked(event):
        logger.log(50, "MenuButton clicked")
    
    
    
    
    #名前変更が押されたとき
    def change_name_clicked(event):
        messagebox.showerror("title", "名前が変更されました")
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
                f"Name : {name.value} \nPassword : {password.value} \nContents : {contents.value}", 
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
    
    
    
    #スタート画面の設定
    # start_container = ft.Container(
    #     height=scr_h * 0.75,
    #     width=scr_w * 1.0,
    #     #alignment="top",
    #     bgcolor=main_bg_color_2,
    #     gradient=ft.LinearGradient(
    #         begin=ft.alignment.top_center,
    #         end=ft.alignment.bottom_center,
    #         colors=["#7fffd4", "#ee82ee"],
    #     ),
    #     padding=30, 
    #     border_radius=50,
    #     #alignment="center"
    # )
    
    
    
    
    
    global e
    
    a = ft.Text("", height=50)
    b = ft.Text(
        "~~~ テキスト入力画面 ~~~",
        size=30,
        color=appbar_color,
    )
    c = ft.Text("", height=30)
    d = ft.Text(
        "・ユーザーネイム(必須)",
        size=18,
        )
    name = ft.TextField(
        label="例：高専太郎",
        bgcolor=main_bg_color,
        keyboard_type="NAME",
        value=""
        )
    f = ft.Text("", height=30)
    g = ft.Text(
        "・パスワード",
        size=18,
        )
    password = ft.TextField(
        label="Password",
        bgcolor=main_bg_color,
        password=True,
        can_reveal_password=True,
        keyboard_type="TEXT",
        )
    i = ft.Text("", height=30)
    j = ft.Text(
        "・Fletについて何かあれば",
        size=18,
        )
    contents = ft.TextField(
        label="例：とても面白いですね！！",
        bgcolor=main_bg_color,
        multiline=True,
        max_length=100,
        min_lines=1, 
        max_lines=5,
        keyboard_type="TEXT",
        )
    l = ft.Text("", height=20)
    #rascreenjindra
    m = ft.ElevatedButton(
        text="確定する", 
        width=90,
        height=50,
        color="#000000",
        bgcolor=appbar_color,
        on_click=main_page_view_clicked
        )
    
    #page.add(start_container)
    page.add(a, b, c, d, name, f, g, password, i, j, contents, l, m)
    
    
    
    
    #アプリケーションバー
    page.appbar = ft.AppBar(
        #leading=ft.Container(padding=5, content=ft.Text(value="Quiz")),
        leading=
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="item1"),
                    ft.PopupMenuItem(icon=ft.icons.POWER_INPUT, text="Check power"),
                    ft.PopupMenuItem(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.HOURGLASS_TOP_OUTLINED),
                                ft.Text("App Exit"),
                            ]
                        ),
                        on_click=lambda _: messagebox.showinfo("title", "アプリケーションを終了しますか？"),
                    ),
                    ft.PopupMenuItem(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.HOURGLASS_TOP_OUTLINED),
                                ft.Text("App Exit"),
                            ]
                        ),
                        on_click=lambda _: messagebox.showinfo("title", "アプリケーションを終了しますか？"),
                    ),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=menu_clicked,
                    ),
                ],
                width=100
                ), 
            #ft.IconButton(icon="search"),
        leading_width=60, 
        title=ft.Text(
            value="Quiz!!",
            color="#afeeee", 
        ),
        center_title=True, 
        bgcolor=appbar_color, 
        actions=[
            ft.Container(
                padding=10, 
                content=ft.ElevatedButton(
                    f"Your Status",
                    color="#ee1919",
                    bgcolor="#afeeee",
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
    
    
    
