from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import print_formatted_text

def print_menu():
    print_formatted_text(HTML(
        '''
<ansiblue>Menú:</ansiblue>
1. Nuevo
2. Editar
3. Eliminar
<ansigreen>Selecciona una opción:</ansigreen>
        '''
    ))

def mainMenu():
    session = PromptSession()
    
    while True:
        print_menu()
        try:
            input_text = session.prompt('> ')
            if input_text in ['1','2','3']:
                return input_text
            else:
                print_formatted_text(HTML('<ansired>Opción no válida, por favor intente de nuevo.</ansired>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<ansiyellow>\nInterrupción detectada. Saliendo...</ansiyellow>'))
            exit()

def deleteRecordMenu():
    session = PromptSession()
    
    while True:
        print_formatted_text(HTML(
        '''
<ansiblue>Que tipo de operacion quiere ejecutar:</ansiblue>
1. Eliminar por ids
2. Eliminar por dominio
3. Volver
<ansigreen>Selecciona una opción:</ansigreen>'''
    ))
        try:
            input_text = session.prompt('> ')
            if input_text in ['1','2','3']:
                return input_text
            else:
                print_formatted_text(HTML('<ansired>Opción no válida, por favor intente de nuevo.</ansired>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<ansiyellow>\nInterrupción detectada. Saliendo...</ansiyellow>'))
            exit()
