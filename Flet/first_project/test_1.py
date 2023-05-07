import flet as ft
import time

def main(page: ft.Page):
    # add/update controls on Page
    
    t = ft.Text(value="HelloWorld", color="#ffffff")
    page.controls.append(t)
    page.update()
    time.sleep(1)
    
    
    '''
    for i in range(5):
        a = 5 - i
        t.value = f"Step {a}"
        page.update()
        time.sleep(1)
    '''
        
        
    t = ft.Row(controls=[
        ft.Text("A"), 
        ft.Text("B"), 
        ft.Text("C"), 
        ft.TextButton("Mia"),
        ft.ElevatedButton(text="Say my name!!!!")
    ])
    page.controls.append(t)
    page.update()
    time.sleep(1)
    
    
    
    t = ft.Column(controls=[
        ft.TextField(label="yourname"),
        ft.TextField(label="passward")
    ])
    page.controls.append(t)
    page.update()
    
    
    '''
    for i in range(10):
        t = ft.Text(f"Line {i}")
        page.controls.append(t)
        if i > 4:
            page.controls.pop(0)
        else: 
            pass
        page.update()
    '''
    
    
    
        
        
    pass



#ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)