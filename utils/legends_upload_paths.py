def race_ilustration_upload(instance, filename):
    race_name = instance.name
    path = f'systems/legends/races/{race_name}/{filename}'
    
    return path


def specialization_ilustration_upload(instance, filename):
    specialization_name = instance.name
    path = f'systems/legends/specializations/{specialization_name}/{filename}'
    
    return path


def item_ilustration_upload(instance, filename):
    item_name = instance.name
    path = f'systems/legends/items/{item_name}/{filename}'
    
    return path


def character_ilustration_upload(instance, filename):
    character_name = instance.name
    path = f'systems/legends/characters/{character_name}/{filename}'
    
    return path


def weapon_ilustration_upload(instance, filename):
    weapon_name = instance.name
    path = f'systems/legends/weapons/{weapon_name}/{filename}'
    
    return path