###
###Revisar uso de mayusculas
###Agregar input // crear funcion por separado
###Calcular edad
###Codigo de metodos en las clases
###
###
import datetime
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir="C:\instantclient_21_10")
connstr='STEFANO_MAINO/123456@54.213.164.78'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.arraysize=50

###
###Revisar uso de mayusculas
###
administradores = {}
vendedores= {}


class Persona:
    id_Persona = ""
    nombre = ""
    apellido = ""
    fecha_nacimiento = ""
    rut = ""
    telefono = ""
    direccion = ""

    def __init__(self,id_Persona,nombre,apellido,fecha_nacimiento,rut,telefono,direccion):
        self.id_Persona= id_Persona
        self.nombre= nombre
        self.apellido= apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.rut= rut
        self.telefono = telefono
        self.direccion = direccion
###    
    def registrar(self,id_Persona,nombre,apellido,fecha_nacimiento,rut,telefono,direccion):
        self.id_Persona= id_Persona
        self.nombre= nombre
        self.apellido= apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.rut= rut
        self.telefono = telefono
        self.direccion = direccion
        pass
    
    def calcular_edad(self,fecha_nacimiento):
        fecha_actual = datetime
        edad = fecha_actual - fecha_nacimiento
        return edad

class Colaborador(Persona):
    id_Colaborador = ""
    cargo = ""
    def __init__(self, id_Persona, id_Colaborador, nombre, apellido, fecha_nacimiento, rut, telefono, direccion, cargo):
        super().__init__(id_Persona, nombre, apellido, fecha_nacimiento, rut, telefono, direccion)
        self.id_Colaborador = id_Colaborador
        self.cargo = cargo
              
###        
    def autorizar_acceso(self,cargo):
        self.cargo= cargo
        pass

class Cliente(Persona):
    id_Cliente = ""
    
    def __init__(self, id_Persona, id_Cliente ,nombre, apellido, fecha_nacimiento, rut,telefono, direccion):
        super().__init__(id_Persona, nombre, apellido, fecha_nacimiento, rut, telefono, direccion)
        self.id_Cliente = id_Cliente
        

###    
    def registrarCliente(self, id_Cliente):
        self.id_Cliente = id_Cliente
        pass

class Proveedor:
    id_Proveedor = ""
    razon_social = ""
    rut_empresa = ""
    def __init__(self,id_Proveedor,razon_social,rut_empresa):
        self.id_Proveedor= id_Proveedor
        self.razon_social= razon_social
        self.rut_empresa= rut_empresa
        
    ###
    def registrarProveedor(self, id_Proveedor, razon_social, rut_empresa):
        self.id_Proveedor = id_Proveedor
        self.razon_social= razon_social
        self.rut_empresa = rut_empresa
        pass

class Usuario(Colaborador):
    id_Usuario = ""
    nombre_usuario = ""
    contrasena = ""

    def __init__(self, id_Usuario, nombre_usuario, contrasena, id_Persona, id_Colaborador, nombre, apellido, fecha_nacimiento, rut, telefono, direccion, cargo):
        super().__init__(id_Persona, id_Colaborador, nombre, apellido, fecha_nacimiento, rut, telefono, direccion, cargo)
        self.id_Usuario = id_Usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
###    
    def registrarUsuario(self, id_Usuario, nombre_Usuario, contrasena):
        self.id_Usuario= id_Usuario
        self.nombre_usuario= nombre_Usuario
        self.contrasena= contrasena
        pass

##
## Input de datos // lo pasaremos a una funcion separada
nuevoColaborador = Colaborador(
    id_Usuario = input("id_Usuario")
    id_Colaborador=input("id_Colaborador: "),
    nombre_usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    nombre=input("Nombre: "),
    apellido=input("Apellido: "),
    fecha_nacimiento=input("Fecha_nacimiento: "),
    rut=input("Rut: "),
    telefono=input("Telefono :"),
    direccion=input("Direccion: "),
    cargo=input("Cargo :")
)
print(nuevoColaborador.__dict__)  
##

class Producto:
    id_Producto = ""
    talla = ""
    modelo = ""
    material = ""
    codigo = ""
    cantidad = ""
    precio = ""
    def __init__(self, id_Producto, talla, modelo, material, codigo, cantidad,precio):
        self.id_Producto = id_Producto
        self.talla = talla
        self.modelo = modelo
        self.material = material
        self.codigo = codigo
        self.cantidad = cantidad
        self.precio =precio
###
    def registrarProdcuto(self, id_Producto, talla, modelo, material ,codigo ,cantidad ,precio):
        self.id_Producto = id_Producto
        self.talla = talla
        self.modelo = modelo
        self.material = material
        self.codigo = codigo
        self.cantidad = cantidad
        self.precio =precio
        pass

class Boleta:
    id_Boleta = ""
    nombre_cliente = ""
    producto = ""
    codigo = ""
    def __init__(self,id_Boleta,nombre_cliente,producto,codigo):
        self.id_Boleta= id_Boleta
        self.nombre_cliente= nombre_cliente
        self.producto= producto
        self.codigo= codigo
###
    def registrarBoleta(self, id_Boleta,nombre_cliente,producto,codigo):
        self.id_Boleta= id_Boleta
        self.nombre_cliente= nombre_cliente
        self.producto= producto
        self.codigo= codigo
        pass

class Detalle_Boleta(Boleta):
    id_Detalle_B = ""
    cantidad= ""
    precio = ""
    def __init__(self, id_Boleta, id_Detalle_B, nombre, producto, codigo):
        super().__init__(id_Boleta, nombre, producto, codigo)
        self.id_Detalle_B = id_Detalle_B
###
    def registrarDetalle(self,id_Detalle_B, fecha, cantidad, precio):
        self.id_Detalle_B= id_Detalle_B
        self.fecha= fecha
        self.cantidad= cantidad
        self.precio= precio
        pass

class Factura:
    id_Factura = ""
    id_Proveedor= ""
    razon_social = ""
    nombre_colaborador = ""
    fecha = ""
    codigo = ""
    giro = ""
    cantidad = ""
    
    def __init__(self, id_Factura, id_Proveedor,razon_social, nombre_colaborador, fecha, codigo, giro, cantidad):
        self.id_Factura= id_Factura
        self.id_Proveedor= id_Proveedor
        self.razon_social= razon_social
        self.nombre_colaborador= nombre_colaborador
        self.fecha= fecha
        self.codigo= codigo
        self.giro= giro
        self.cantidad= cantidad
###    
    def registrarFactura(self, id_Factura, id_Proveedor, razon_social, fecha ,codigo ,giro ,cantidad):
        self.id_Factura= id_Factura
        self.id_Proveedor= id_Proveedor
        self.razon_social= razon_social
        self.fecha= fecha
        self.codigo= codigo
        self.giro= giro
        self.cantidad= cantidad
        pass


class Detalle_Factura(Factura):
    id_Detalle_F = ""
    codigo = ""
    giro = ""


    def __init__(self, id_Detalle_F,id_Factura, razon_social, nombre_colaborador, fecha, codigo, cantidad, giro):
        super().__init__(id_Factura, razon_social, nombre_colaborador, fecha, codigo, giro, cantidad)
        self.id_Detalle_F= id_Detalle_F
        self.nombre_colaborador= nombre_colaborador
        self.fecha= fecha
        self.codigo= codigo
        self.giro= giro
###    
    def registrarDetalle(self, id_Detalle_F, fecha, giro, cantidad):
        self.id_Detalle_F= id_Detalle_F
        self.fecha= fecha
        self.giro= giro
        self.cantidad= cantidad
        pass

class Insumo:
    id_Insumo = ""
    nombre = ""
    tipo = ""
    cantidad = ""
    descripcion = ""
    en_Bodega= ""
    def __init__(self,id_Insumo,nombre,tipo,cantidad,descripcion, en_Bodega):
        self.id_Insumo= id_Insumo
        self.nombre= nombre
        self.tipo= tipo
        self.cantidad= cantidad
        self.descripcion= descripcion
        self.en_Bodega= en_Bodega
###
    def validarInsumo(self, id_Insumo, nombre, tipo,cantidad, descripcion, en_Bodega):
        self.id_Insumo= id_Insumo
        self.nombre= nombre
        self.tipo= tipo
        self.cantidad= cantidad
        self.descripcion= descripcion
        self.en_Bodega= en_Bodega
###
        pass

class Herramienta:
    id_Herramienta = ""
    nombre = ""
    tipo = ""
    cantidad = ""
    descripcion = ""
    def __init__(self,id_Herramienta,nombre,tipo,cantidad,descripcion):
        self.id_Herramienta= id_Herramienta
        self.nombre= nombre
        self.tipo= tipo
        self.cantidad= cantidad
        self.descripcion= descripcion
###
    def registrarHerramienta(self, id_Herramienta, nombre, cantidad, descripcion ,tipo):
        self.id_Herramienta= id_Herramienta
        self.nombre= nombre
        self.tipo= tipo
        self.cantidad= cantidad
        self.descripcion= descripcion
        pass


class Maquinaria:
    id_Maquinaria = ""
    nombre = ""
    tipo = ""
    cantidad = ""
    descripcion = ""
    def __init__(self,id_Maquinaria,nombre,tipo,cantidad,descripcion):
        self.id_Maquinaria= id_Maquinaria
        self.nombre= nombre
        self.tipo= tipo
        self.cantidad= cantidad
        self.descripcion= descripcion
###   
    def registrarMaquinaria(self, id_Maquinaria, nombre, cantidad, descripcion ,tipo):
        self.id_Maquinaria= id_Maquinaria
        self.nombre= nombre
        self.tipo= tipo
        self.cantidad= cantidad
        self.descripcion= descripcion
        pass
    def Alocar(self,id_Maquinaria, nombre, tipo, descripcion, cantidad, en_Bodega):
        self.id_Maquinaria= id_Maquinaria
        self.nombre= nombre
        self.tipo= tipo
        self.cantidad= cantidad
        self.descripcion= descripcion
        self.en_Bodega= en_Bodega
        pass

###

###
###
###

admins='SELECT NOMBRE_USUARIO, CONTRASENA FROM USUARIO WHERE ID_CARGO = 14'
curs.execute(admins)
result = conn.commit()

for column1, column2 in curs.fetchall():
    administradores.update({column1:column2})


vendedor='SELECT NOMBRE_USUARIO, CONTRASENA FROM USUARIO WHERE ID_CARGO = 17'
curs.execute(vendedor)
result = conn.commit()

for column1, column2 in curs.fetchall():
    vendedores.update({column1:column2})
###
###
###

#