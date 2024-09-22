from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import print_formatted_text


def prepareMenu(opciones):
    menu = f'<ansiblue>Menú:</ansiblue>\n'
    for i,item in enumerate(opciones):
        menu += f'\n{i+1}. {item}'
    menu += f'\n<ansigreen>Selecciona una opción:</ansigreen>'
    return menu


def mainMenu():
    session = PromptSession()
    opciones = ['Nuevo','Editar','Eliminar']
    menu = prepareMenu(opciones)
    
    while True:
        print_formatted_text(HTML(menu))
        try:
            input_text = session.prompt('> ')
            if input_text in (str(i) for i in range(1, len(opciones) + 1)):
                return opciones[int(input_text) - 1]
            else:
                print_formatted_text(HTML('<ansired>Opción no válida, por favor intente de nuevo.</ansired>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<ansiyellow>\nInterrupción detectada. Saliendo...</ansiyellow>'))
            exit()

def deleteRecordMenu():
    session = PromptSession()
    session = PromptSession()
    opciones = ['Eliminar por ids','Eliminar por dominio','Volver']
    menu = prepareMenu(opciones)
    while True:
        print_formatted_text(HTML(menu))
        try:
            input_text = session.prompt('> ')
            if input_text in (str(i) for i in range(1, len(opciones) + 1)):
                return opciones[int(input_text) - 1]
            else:
                print_formatted_text(HTML('<ansired>Opción no válida, por favor intente de nuevo.</ansired>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<ansiyellow>\nInterrupción detectada. Saliendo...</ansiyellow>'))
            exit()


def selectDomain(domain):
    session = PromptSession()
    operations = ['>','>=','=','!=','in','not in','Terminar']    
    menu = f'<ansiblue>Agregar operaciones al dominio: {domain}</ansiblue>'
    for i,operation in enumerate(operations):
        menu += f'\n{i+1}. {operation}'
    while True:
        print_formatted_text(HTML(menu))
        try:
            input_text = session.prompt('> ')
            if input_text in ['1','2','3','4','5','6','7']:
                
                return operations[int(input_text)-1]
            else:
                print_formatted_text(HTML('<ansired>Opción no válida, por favor intente de nuevo.</ansired>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<ansiyellow>\nInterrupción detectada. Saliendo...</ansiyellow>'))
            exit()
