import flet as ft

def main(page: ft.Page):
    page.title = "test_05.06"
    
    #コントロールのインスタンスを生成
    t = ft.Text(value="HelloWorld", color="#ffffff")
    
    #ページにコントロールを追加
    page.controls.append(t)
    #ページを更新
    page.update()
    
ft.app(target=main)