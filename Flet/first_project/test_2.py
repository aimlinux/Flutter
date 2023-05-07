import flet as ft
import time

def main(page: ft.Page):
    # add/update controls on Page



    for i in range(10):
        t = ft.Text(f"Line {i}")
        page.controls.append(t)
        if i > 9:
            page.controls.pop(0)
        else: 
            pass
        page.update()
    
    
    
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
    




ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)