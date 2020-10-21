from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

#Tabla de Solicitudes
class Solicitud(db.Model):
    __tablename__ = 'solicitudes'
    id = db.Column(db.Integer, primary_key=True) 
    nombre_empleado = db.Column(db.String(100), nullable=False)
    sucursal  = db.Column(db.String(30))
    proveedor = db.Column(db.String(70))
    insumo_nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))
    marca = db.Column(db.String(70))
    cantidad_solicitada = db.Column(db.Integer)
    cantidad_recibida = db.Column(db.Integer)
    precio_unidad = db.Column(db.Float(precision=10)) 
    estado_solicitud = db.Column(db.String(50))
    total = db.Column(db.Float())
    observacion = db.Column(db.String(100))
    fecha_emision = db.Column(db.DateTime, default= datetime.datetime.now)


    def __init__(self, nombre_empleado, sucursal, proveedor, insumo_nombre,descripcion, marca, cantidad_solicitada,cantidad_recibida, precio_unidad, estado_solicitud,total, observacion):
            self.nombre_empleado = nombre_empleado
            self.sucursal = sucursal
            self.proveedor = proveedor
            self.insumo_nombre = insumo_nombre
            self.descripcion = descripcion
            self.marca = marca
            self.cantidad_solicitada = cantidad_solicitada
            self.cantidad_recibida = cantidad_recibida
            self.precio_unidad = precio_unidad
            self.estado_solicitud = estado_solicitud
            self.total = total
            self.observacion = observacion
            
    



