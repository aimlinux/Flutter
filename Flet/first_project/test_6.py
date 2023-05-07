import flet as ft
from flet import Theme
#from flet import Element, render

import os 

import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox 

import time
from time import sleep
    

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "80000"


def main(page: ft.Page):
    # add/update controls on Page
    
    
    r = ft.Row(wrap=True, scroll="always", expand=True)
    page.add(r)
    
    for i in range(5000):
        r.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                width=100, 
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_50,
                border=ft.border.all(1, ft.colors.AMBER_300),
                border_radius=ft.border_radius.all(5),
            )
        )
        page.update()
    
    

ft.app(target=main, view=ft.WEB_BROWSER)
#ft.app(target=main)