from app.database import getDB
class ingrediente:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre=nombre

    def serialize(self):
        return self.nombre
    
    @staticmethod
    def getIngredientesCoctel(idCoctel):
        db = getDB()
        cursor = db.cursor()
        cursor.execute("select id, nombre from ingredientes where id in (select ingrediente from ingredientesCoctel where coctel = " + str(idCoctel) +");")
        rows = cursor.fetchall()
        ingreds=[]
        for row in rows:
            nuevo_ingr=ingrediente(row[0],row[1])
            ingreds.append(nuevo_ingr)
        cursor.close()
        return ingreds
    
    def getAllIngredientes():
        db = getDB()
        cursor = db.cursor()
        cursor.execute("select id, nombre from ingredientesCoctel;")
        rows = cursor.fetchall()
        ingreds=[]
        for row in rows:
            nuevo_ingr=Usuario(row[0],row[1])
            ingreds.append(nuevo_ingr)
        cursor.close()
        return ingreds

class tipo:
    def __init__(self, id, nombre):

        self.id = id
        self.nombre = nombre

    def serialize(self):
        return self.nombre
        
    
    @staticmethod

    def getTipo(id):
        db = getDB()
        cursor = db.cursor()
        cursor.execute("select tipo from tipos where id = " + str(id) +";")
        rows = cursor.fetchall()
        ntipo=tipo("0","")
        for row in rows:
            nuevo=tipo(id, row[0])
            ntipo = nuevo
        cursor.close()
        return ntipo
    
class ingredientePrincipal:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    def serialize(self):
        return self.nombre
    
    @staticmethod

    def getIngPrinc(id):
        db = getDB()
        cursor = db.cursor()
        cursor.execute("select nombre from ingredientepri where id = " + str(id) +";")
        rows = cursor.fetchall()
        ningr=ingredientePrincipal("0","")
        for row in rows:
            nuevo=ingredientePrincipal(id, row[0])
            ningr = nuevo
        cursor.close()
        return ningr
    
class coctel:
    #ID	Usuario	Nombre	Preparacion	DeAutor	FechaCreacion	Imagen
    def __init__(self, id, usuario, nombre, preparacion, deautor, fechacreacion, imagen, principal, tipoCoctel):
        self.id = id
        self.usuario=usuario
        self.nombre=nombre
        self.preparacion=preparacion
        self.deautor=deautor
        self.fechacreacion=fechacreacion
        self.imagen=imagen
        self.principal = principal #ingredientePrincipal.getIngPrinc(principal)
        self.tipo= tipoCoctel #tipo.getTipo(tipoCoctel)
        

    def setIngredientes(self):
        self.ingredientes=ingrediente.getIngredientesCoctel(self.id)
    def setIngredientePrinc(self):
        self.principal=ingredientePrincipal.getIngPrinc(self.principal)
    def setTipo(self):
        self.tipo=tipo.getTipo(self.tipo)
    
    @staticmethod
   
    def serialize(self):
        listIngred=[ingrediente.serialize() for ingrediente in self.ingredientes]
        coctel = {
            'id' : self.id,
            'nombre':self.nombre,
            'preparacion':self.preparacion,
            'deAutor':self.deautor,
            'fechaCreacion' : self.fechacreacion,
            'imagen': self.imagen,
            'tipo': tipo.serialize(self.tipo),
            'ingrediente': ingredientePrincipal.serialize(self.principal),
            'ingredientes':listIngred,
            }
        return coctel
    
    def getCocteles():
        db = getDB()
        cursor = db.cursor()
        cursor.execute("select id, idUsuario, Nombre, Preparacion, deAutor, FechaCreacion, imagen, tipo, ingrediente from cocteles")
        rows = cursor.fetchall()
        ncoctel=[]
        for row in rows:


            nuevo=coctel(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[8],row[7])
            nuevo.setIngredientes()
            nuevo.setIngredientePrinc()
            nuevo.setTipo()
            ncoctel.append(nuevo)
        cursor.close()
        return ncoctel
    
    
        
        

    
    def Guardar(self):
        db = getDB()
        cursor = db.cursor()
      #  nID= str(Usuario.AddUsuario())
        query=""
        if self.id==0:
            #Insertar
            query = "insert into cocteles (usuario, nombre, preparacion, deautor, fechacreacion, imagen) values (" + self.Usuario + ", " +  self.nombre + ", " + self.preparacion + ", " + self.deautor + ", " + self.imagen + ");"
        else:
        #Actualizar
            query = "update cocteles set (usuario = " + self.usuario + ", nombre = '" + self.nombre + "', preparacion = '" + self.preparacion + "', deautor = " + self.deautor +", imagen = '" + self.imagen + "' where id = " + self.id + ";"
        cursor.execute(query)
        db.commit()

    
    
    @staticmethod
    def getFavoritos(idUsuario):
        db = getDB()
        cursor = db.cursor()
        query="select id, idUsuario, Nombre, Preparacion, deAutor, FechaCreacion, imagen, tipo, ingrediente from cocteles where id in (Select Coctel from favoritos where Usuario = " + str(idUsuario) + ");"
        cursor.execute(query)
        rows = cursor.fetchall()
        favoritos=[]
        for row in rows:
            nuevo=coctel(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[8],row[7])
            nuevo.setIngredientes()
            nuevo.setIngredientePrinc()
            nuevo.setTipo()
            favoritos.append(nuevo)
        cursor.close()
        return favoritos
    def getIdFavorito(idUsuario, idCoctel):
        db = getDB()
        cursor = db.cursor()
        query="select id from favoritos where usuario = "+ str(idUsuario) + " and coctel = " + str(idCoctel) + ";"
        cursor.execute(query)
        rows = cursor.fetchone()
        idC = rows[0]
        db.close()
        return idC
    
    def AgrFavorito(idUsuario, idCoctel):
        db = getDB()
        cursor = db.cursor()
        query="insert into favoritos(usuario, coctel) values("+ str(idUsuario) + ", " + str(idCoctel) +");"
        cursor.execute(query)
        db.commit()
        return
    
    def DeleteFavorito(idUsuario, idCoctel):
        db = getDB()
        cursor = db.cursor()
        query="delete from favoritos where Usuario = " + str(idUsuario) + " and Coctel = " + str(idCoctel) + ";"
        cursor.execute(query)
        db.commit()
        return
    
class Usuario:
    #ID	Usuario	Nombre	Preparacion	DeAutor	FechaCreacion	Imagen
    def __init__(self, id,  nick, correo, nivelus, fecharegistro):
        self.id = id
        self.nick=nick
        self.correo=correo
        self.nivelus=nivelus
        self.fecharegistro=fecharegistro

    @staticmethod

    def get_all():
        db = getDB()
        cursor = db.cursor()
        cursor.execute("select id, nick, correo, nivelus, fecharegistro from usuarios")
        rows = cursor.fetchall()
        nusuario=[]
        for row in rows:
            nuevo_usr=Usuario(row[0],row[1],row[2],row[3],row[4])
            nusuario.append(nuevo_usr)
        cursor.close()
        return nusuario
        
    def serialize(self, usuario):
        return{
            'resultado': "0",
            'usuario' : usuario,
            'id' : self.id,
            'nick':self.nick,
            'correo':self.correo,
            'nivelus':self.nivelus,
            'fecharegistro':self.fecharegistro,
        }
    
    def IniciarSesion(usuario, passw):
        db = getDB()
        cursor = db.cursor()
        cursor.execute("select id, nick, correo, nivelus, fecharegistro from usuarios where usuario = '" + usuario + "' and pass = '" + passw + "'")
        rows = cursor.fetchall()
        nusuario=[]
        for row in rows:
            nuevo_usr=Usuario(row[0],row[1],row[2],row[3],row[4])
            nusuario.append(nuevo_usr)
        cursor.close()
        return nusuario
        
    def ExisteUsuario(usr, Passw):
        usr = Usuario.IniciarSesion(usr,Passw)
        if len(usr) > 0:
           return True
            #resultado OK
        else:
           return False
            #resultadoError

    def ExisteCorreo(Correo):
        db = getDB()
        cursor = db.cursor()
        cursor.execute("select id from usuarios where Correo = '" + Correo + "' order by id DESC LIMIT 1")
        rows = cursor.fetchall()
        Cantidad=0

        for row in rows:
            Cantidad= int(row[0])

        if Cantidad > 0:
           return True
            #resultado OK
        else:
           return False
            #resultadoError        
    def ExisteNick(Nick):
        db = getDB()
        cursor = db.cursor()
        cursor.execute("select id from usuarios where Nick = '" + Nick + "' order by id DESC LIMIT 1")
        rows = cursor.fetchall()
        Cantidad=0

        for row in rows:
            Cantidad= int(row[0])

        if Cantidad > 0:
           return True
            #resultado OK
        else:
           return False
            #resultadoError
    def UpdUsuario(idUsr, usuario, Correo):
        result = Registro()
        usre= Usuario.ExisteCorreo(Correo)
        if usre==True:
           result.MResultado(False, "Correo Existente", usuario)
           return result

        db = getDB()
        cursor = db.cursor()
        cursor.execute("update usuarios set correo = '" + Correo +"' where id = " + str(idUsr) + ";")
        db.commit()
        result.Mensaje ="Actualizado correctamente"
        result.Resultado = True
        result.Usuario = usuario
        return result
    
class Registro:
    def __init__(self):
        pass
    def MResultado(self, resultado, mensaje, usuario):
        self.Resultado = resultado
        self.Mensaje = mensaje
        self.Usuario = usuario
        
    @staticmethod
    

    def Registrar(usuario, Passw, Nick, Correo):
        result = Registro()
        # ----> Verificaciones previas <-----
        usre = Usuario.ExisteUsuario(usuario, Passw)
        if usre==True:
           result.MResultado(False, "Usuario Existente", usuario)
           return result
        usre = Usuario.ExisteCorreo(Correo)
        if usre==True:
           result.MResultado(False, "Correo Existente", usuario)
           return result
        usre = Usuario.ExisteNick(Nick)
        if usre==True:
           result.MResultado(False, "Alias Existente", usuario)
           return result
        
        db = getDB()
        cursor = db.cursor()
        query=""
        query = "insert into Usuarios(Usuario, Pass, Nick, Correo) values ('"+ usuario +"','"+ Passw + "','"+ Nick +"','" + Correo + "');"#, (usuario, Passw, Nick, Correo)
                
        # """ insert into Usuarios(Usuario, Pass, Nick, Correo)
                #values ( %s, %s, %s, %s);""", (usuario, Passw, Nick, Correo)
        cursor.execute(query)
        db.commit()
    
        usre = Usuario.ExisteUsuario(usuario, Passw)

        if usre==True:
           result.MResultado(True, "Registro Satisfactorio!", usuario)
        else:
            result.MResultado(False, "Registro Error o usuario existente", usuario)

        return result

