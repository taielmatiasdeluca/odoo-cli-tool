from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.shortcuts import print_formatted_text
from prompt_toolkit.formatted_text import HTML

def simplePrompt(message):
    session = PromptSession()
    return session.prompt(message)

def confirmation(message):
    session = PromptSession()
    res = session.prompt(f'¿Estas seguro de {message}? Coloque SI para continuar: ')   
    if res.strip() in ['SI','si','Si','sI']:
        return True
    return False

def printhtml(html):
    print_formatted_text(HTML(html))
    
def prepareArray():
    array = []
    session = PromptSession()
    while(True):
        res = session.prompt(f'Ingrese un valor para agrarlo a {array} (exit para continuar):')
        if res in ['exit','Exit']:
            return array
        array.append(res)
    