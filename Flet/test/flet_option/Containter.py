import flet 

container = flet.Container()

options = container.__dict__.keys()
for option in options:
    print(option)