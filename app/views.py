from flask import jsonify, request
from app.models import Usuario
from app.models import Registro
from app.models import coctel
from app.models import ingrediente



#devuelve datos en formato json




def getUsuario():
    usuarios = Usuario.get_all()
    list_usr=[Usuario.serialize(usuario) for usuario in usuarios]
    return jsonify(list_usr)

     
def Registrarse(data):
    
    Usuario = data['usuario']
    Passw = data['passw']
    Nick = data['nick']
    Correo = data['correo']
    resultado = Registro.Registrar(Usuario, Passw, Nick, Correo)
    if resultado.Resultado== True:
        return jsonify({'resultado':'0','message':resultado.Mensaje}),201
    else:
        return jsonify({'resultado':'-1','message':resultado.Mensaje}),201

def GetFavoritos():
    data = request.json
    IDusr = data['IdUsuario']
    favoritos= coctel.getFavoritos(IDusr)
    list_favsr=[coctel.serialize(favorito) for favorito in favoritos]
    return jsonify(list_favsr)

def AddFavorito():
    data = request.json
    IDusr = data['IdUsuario']
    IDcoctel = data['IdCoctel']
    coctel.AgrFavorito(IDusr,IDcoctel)
    return jsonify({"resultado":"0","message":"Favorito agregado con exito"})

def UpdateCorreo():
    data = request.json
    IDusr = data['IdUsuario']
    usuario =data['Usuario']
    Correo = data['Correo']
    result = Usuario.UpdUsuario(IDusr, usuario, Correo)
    if result.Resultado==True:
        return jsonify({"resultado":0,"mensaje":result.Mensaje})
    else:
        return jsonify({"resultado":-1,"mensaje":result.Mensaje})

def DelFavorito():
    data = request.json
    IDusr = data['IdUsuario']
    Coctel =data['IdCoctel']
    coctel.DeleteFavorito(IDusr, Coctel)
    return jsonify({"resultado":"0","message":"Favorito eliminado con exito"})

def GetCocteles():
    listCoct = coctel.getCocteles()
    list_coct=[coctel.serialize(coctel) for coctel in listCoct]
    return jsonify(list_coct)


def iniciarSesion():
    data = request.json
    usuario = data['usuario']
    passw = data['passw']
    resultado = Usuario.IniciarSesion(usuario,passw)
    if len(resultado) == 0:
        #Sesion no iniciada
        return jsonify( {"resultado":"-1", "message":"Error en usuario o contraseña", "id":"-1"})
    else:
        return jsonify (Usuario.serialize(resultado[0], usuario))
    
def getIngredientes():
    data = request.json
    idCoctel = data['idCoctel']
    lista=ingrediente.getIngredientesCoctel(idCoctel)
    lista_P=[ingrediente.serialize() for ingr in lista]
    return jsonify(lista_P)
