#pip install pyfiglet

from pyfiglet import Figlet

def render(text,style):
    f = Figlet(font=style)
    print('\n'*10)
    print(f.renderText(text))

render('Hello World', 'isometric1')
