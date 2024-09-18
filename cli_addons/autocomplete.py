from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.shortcuts import print_formatted_text
from prompt_toolkit.formatted_text import HTML

class CustomCompleter(Completer):
    def __init__(self, options):
        self.options = options

    def get_completions(self, document, complete_event):
        # Obtener el texto actual del documento
        text = document.text_before_cursor
        
        # Generar las sugerencias de autocompletado
        for option in self.options:
            if option.startswith(text):
                yield Completion(option, start_position=-len(text))

def autocompletePrompt(posibilities, message, notfoundmessage):
    # Crear un completer personalizado con las posibilidades de autocompletado
    command_completer = CustomCompleter(posibilities)
    
    # Crear una sesión de prompt_toolkit
    session = PromptSession(completer=command_completer)
    
    while True:
        # Usar la sesión para obtener la entrada del usuario
        user_input = session.prompt(message)
        
        # Procesar el comando ingresado
        if user_input in posibilities:
            return user_input
        else:
            print_formatted_text(HTML(f'<ansired>{notfoundmessage} {user_input}</ansired>'))
    

