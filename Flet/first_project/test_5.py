import flet as ft
from flet import Theme
#from flet import Element, render

import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox 

import time
from time import sleep


'''
def main(page: ft.Page):
    for i in range(5000):
        page.controls.append(ft.Text(f"Line {i}"))
    page.scroll = "always"
    page.update()
'''

def main(page: ft.Page):
    lv = ft.ListView(expand=True, spacing=10)
    for i in range(5000):
        lv.controls.append(ft.Text(f"Line {i}"))
    page.add(lv)

    

ft.app(target=main, view=ft.WEB_BROWSER)
#ft.app(target=main)