

def getAllModels(odoo):
    model = 'ir.model' 
    domain = [('model', '!=', 'ir.model')] 
    ids = odoo.env[model].search(domain)
    records = odoo.env[model].read(ids, ['model'])  
    return records

def getAllFields(odoo,model_name):
    model = odoo.env[model_name]    
    fields_info = model.fields_get()
    fields_details = {}
    for field_name, field_info in fields_info.items():
        # Extrae la información de los campos
        fields_details[field_name] = {
            'type': field_info.get('type'),
            'required': field_info.get('required', False),
            'readonly': field_info.get('readonly', False),
            'string': field_info.get('string'),
            'help': field_info.get('help'),
            'selection': field_info.get('selection', []),  # Si el campo es de tipo 'selection'
        }
    return fields_details

def createRecord(odoo,model_name,data):
    return odoo.env[model_name].create(data)

def deleteRecordByIds(odoo,model_name,ids):
    records =  odoo.env[model_name].read(ids)
    return odoo.env[model_name].unlink(records)

def deleteRecordByDomain(odoo,model_name,domain):
    records =  odoo.env[model_name].search(domain)
    return odoo.env[model_name].unlink(records)

def editRecordByDomain(odoo,model_name,domain,data):
    records =  odoo.env[model_name].search(domain)
    return odoo.env[model_name].write(records,data)
    
