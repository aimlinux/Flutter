import flet
from flet import Text

# Textコントロールのデフォルトオプションを表示する
default_options = Text().__dict__
for option in default_options:
    print(option)