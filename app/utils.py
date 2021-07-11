"""
    proceso de mutación del modelo genérico
    esta funcion recibe un modelo (hace referencia una tabla en la base de datos), 
    datos (es un diccionario), un id(opcional), 
    y un commit que por defecto esta en true.
    Si la funcion recibe un id, este se usara para encontrar un registro por 
    medio del  ORM que coincida con el mismo, luego intenta borrar el id dentro
    del diccionario data, pero si no lo consigue activa la excepcion la cual
    pasa, luego en el for asigna el valor encontrado a lista de objetos.
    En caso de no enviar el id se crea el item con los datos enviados en el
    diccionario data, luego si el commit esta en true lo guarda en la base de
    datos el item y por ultimo lo retorna.
    Esta funcion se usa en el caso de que se necesite crear varios
    registros en un modelo o cambiar el valor de unos atributos que existen
    en las tablas
"""


def generic_model_mutation_process(model, data, id=None, commit=True):
    if id:
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)

    if commit:
        item.save()

    return item
