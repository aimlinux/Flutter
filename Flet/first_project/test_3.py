import flet as ft
from flet import Theme
#from flet import Element, render
import time
from time import sleep

def main(page: ft.Page):
    # add/update controls on Page
    
    
    #Themeの変更をしたかった
    '''
    light_theme = Theme(
        background_color = "#ffffff",
        text_color = "aqua",
        #他のオプションも追加できる
    )
    
    element = Element("div", text="HelloWorld!")
    
    element.set_theme(light_theme)
    
    html = render(element)
    print(html)
    '''
    
    
    
    first_name = ft.TextField(label="First Name", autofocus=True)
    last_name = ft.TextField(label="Lase Name", autofocus=False)
    greetings = ft.Column()
    
    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value} ! "))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()
        
        
    page.add(
        first_name,
        last_name, 
        ft.ElevatedButton("Say Hello!", on_click=btn_click),
        greetings,
    )

    
    sleep(1)
    
    
    #ユーザー入力の取得
    btn = ft.ElevatedButton("Click mie!")
    page.add(btn)
    
    
    


ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)