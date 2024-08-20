from .models import *

# get tipo_usuario

def get_tipo_usuario(request):
    return TipoUsuario.objects.all()

# crear tipo usuario

def crea_tipo_usuario(nombre):
    try:
        tipo = TipoUsuario(tipo_usuario=nombre)
        tipo.save()
        return tipo
    except Exception as e:
        return e

# Tipo_usuario

def tipo_usuario(id):
    try:
        return TipoUsuario.objects.get(id_tipo_usuario=id)
    except Exception as e:
        return e
    
# actualizar tipo_usuario

def actualiza_tipo_usuario(id, nombre):
    try:
        tipo_usuario = (id)
        tipo_usuario.nombre = nombre
        tipo_usuario.save()
        return tipo_usuario
    except Exception as e:
        return e
    
# Eliminar tipo usuario

def elimina_tipo_usuario(id):
    try:
        tipo_usuario = (id)
        tipo_usuario.delete()
        return "Tipo usuario eliminado correctamente"
    except Exception as e:
        return e