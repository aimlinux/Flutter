import flet as ft
from flet import Theme
#from flet import Element, render

import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox 

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
    
    page.add(
        ft.Container(
            width=1000,
            height=100,
            bgcolor=ft.colors.BROWN_900,
        )
    )
    
    
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

    page.add(
        ft.Container(
            width=1000,
            height=100,
            bgcolor=ft.colors.CYAN_50,
        )
    )

    
    
    sleep(1)
    
    
    #ユーザー入力の取得
    
    #btn = ft.ElevatedButton("Click mie!")
    #page.add(btn)
    

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            #page.clean()
            page.add(ft.Text(f"Hello, {name}!"))
            
    txt_name = ft.TextField(label="Your name")
    
    page.add(
        txt_name,
        ft.ElevatedButton("Say Hello!", on_click=btn_click))
    
            
    
    sleep(1)
    
    
    #チェックボックスコントロール
    def checkbox_changed(e):
        if todo_check.value == True:
            output_text.value = (
                f"mia"
            )
            #messagebox.showwarning("title", "mia", icon="info")
        elif todo_check.value == False:
            output_text.value = (
                f"aim"
            )
            #messagebox.showwarning("title", "aim", icon="info")
        else:
            output_text.value = (
                f"error"
            )
            
        
        page.update()
        
    output_text = ft.Text()
    todo_check = ft.Checkbox(label="Todo: Learn how to use ski", value=False, on_change=checkbox_changed)
    page.add(
        todo_check,
        output_text
    )



    sleep(1)
    
    
    #submit...
    def sumbit_clicked(e):
        output_text_2.value = f"Dropdown value is : {color_dropdown.value}"
        page.update()
        
    
    output_text_2 = ft.Text("")
    submit_btn = ft.ElevatedButton(text="Submit", on_click=sumbit_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("mia"),
            ft.dropdown.Option("mia"),
            ft.dropdown.Option("mia"),
        ],
    )
    page.add(
        color_dropdown,
        submit_btn,
        output_text_2,
    )



ft.app(target=main, view=ft.WEB_BROWSER)
#ft.app(target=main)