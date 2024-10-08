#Odoo xmlrpc
import odoorpc
#Load .env
from dotenv import load_dotenv
import os

from cli_addons import autocomplete
from cli_addons import menu
from cli_addons import prompt

from xml_calls import operations

load_dotenv()

URL = os.getenv('URL')
DB = os.getenv('DB')
ACCOUNT = os.getenv('ACCOUNT')
PASSWORD = os.getenv('PASSWORD')
PORT = os.getenv('PORT')


def create_record(odoo,model_fields,model):
    model_fields_names = ['exit']
    fields = []
    for key in model_fields:
        if(model_fields[key]['required'] == True):
            fields.append(key)
            continue
        model_fields_names.append(key)
    while(True):
        field = autocomplete.autocompletePrompt(model_fields_names,f'Campos a insertar {", ".join(fields)}\nIngrese los campos que quiere agregar (para salir ingrese exit):', 'No se encontro ese modelo, vuelve a intentar')
        if(field == 'exit'):
            break
        model_fields_names.remove(field)
        fields.append(field)
    data = {}
    for field in fields:
        data[field] =  prompt.simplePrompt(f'Ingrese el valor de la propiedad: {field}: ')
    new_id = operations.createRecord(odoo,model,data)
    print(f'Se creo un nuevo registro {model} con id: {new_id}')
        
def prepareDomain(fields):
    domain = []
    while(True):
        operation = menu.selectDomain(domain)
        if operation == 'Terminar':
            break
        field = autocomplete.autocompletePrompt(fields,f'Ingrese el campo a agregar:', 'No se encontro ese modelo, vuelve a intentar')
        if operation in ['in','not in']:
            value = prompt.prepareArray()
        else:
            value = prompt.simplePrompt('Ingrese el valor: ')
        domain.append((field,operation,value))
    return domain

def prepareData(fields):
    fields['exit'] = True
    fields['Exit'] = True
    data = {}
    while(True):
        field = autocomplete.autocompletePrompt(fields,f'Ingrese el campo a actualizar {data} (exit para continuar):', 'No se encontro ese modelo, vuelve a intentar')
        if field in ['exit','Exit']:
            break
        value = prompt.simplePrompt('Ingrese el valor: ')
        data[field] = value
    return data    
    
def delete_records(odoo,model_fields,model):
    operation = menu.deleteRecordMenu()
    if(operation == 'Eliminar por ids'):
        #Eliminar por ids
        ids = []
        while(True):
            res = prompt.simplePrompt(f'Ingrese la id, para continuar ingrese EXIT: ')
            if (res in ['exit','EXIT']):
                break
            try:
                int(res)
                ids.append(res)
            except:
                print('¡Ingrese un numero valido!')
        if(prompt.confirmation(f'Eliminar {model} con las ids {(", ".join(ids))}')):
            if operations.deleteRecordByIds(odoo,model,ids):
                prompt.printhtml("<ansigreen>Eliminado con exito</ansigreen>")
        return
    if(operation == 'Eliminar por dominio'):
        domain = prepareDomain(model_fields)
        if operations.deleteRecordByDomain(odoo,model,domain):
            prompt.printhtml("<ansigreen>Eliminado con exito</ansigreen>")
        return
    #Si la operacion no esta entre esas dos, volver al menu principal
    return

def update_records(odoo,model_fields,model):
    print('Debe crear un dominio de registros a actualizar')
    domain = prepareDomain(model_fields)
    data = prepareData(model_fields)
    if operations.editRecordByDomain(odoo,model,domain,data):
        prompt.printhtml("<ansigreen>Editado con exito</ansigreen>")


def main():
    odoo = odoorpc.ODOO(URL, port=PORT)
    odoo.login(DB, ACCOUNT,PASSWORD)
    
    while(True):
        #se selecciona la operacion que se quiere hacer
        operation = menu.mainMenu()
        #se selecciona el modelo sobre el cual hacerlo
        model = autocomplete.autocompletePrompt([item['model'] for item in operations.getAllModels(odoo)],'Seleccione su modelo:', 'No se encontro ese modelo, vuelve a intentar')
        model_fields = operations.getAllFields(odoo,model)
        if operation == 'Nuevo':
            create_record(odoo,model_fields,model)
        if operation == 'Editar':
            update_records(odoo,model_fields,model)
        if operation == 'Eliminar':
            delete_records(odoo,model_fields,model)
        # TODO llamar metodos de los modelos
    

if __name__ == '__main__':
    main()