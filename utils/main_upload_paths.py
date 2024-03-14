def systems_ilustration_upload(instance, filename):
    system_name = instance.name
    system_name = str(system_name).lower()
    path = f'systems/{system_name}/cover/{filename}'
    
    return path